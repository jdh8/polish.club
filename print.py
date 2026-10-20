#!/usr/bin/env python3
"""Typeset the book as a PDF: SUMMARY.md order -> one Markdown file -> pandoc -> lualatex.

Needs pandoc, lualatex with lua-ul and luacolor, rsvg-convert, Libertinus (fontconfig) and Noto Serif CJK TC.
Output: book/polish-club.pdf; intermediates in build/.
"""
import datetime, html, pathlib, posixpath, re, shutil, subprocess, tomllib

SRC, OUT = pathlib.Path('src'), pathlib.Path('build')
OUT.mkdir(parents=True, exist_ok=True)

def fid(path):  # '1C/1D.md' -> 'f-1c-1d'
    return 'f-' + re.sub(r'[^a-z0-9]+', '-', path[:-3].lower())

def slug(s):  # mdbook heading ids
    return ''.join(c if c.isalnum() or c in '_-.' else '-' if c.isspace() else '' for c in s.lower())

# SUMMARY.md -> [(depth, title, path)] with depth -1 for prefix chapters, None path for parts
toc = []
for line in (SRC / 'SUMMARY.md').read_text().splitlines():
    if m := re.match(r'( *)- \[(.*)\]\((.*)\)', line):
        toc.append((len(m[1]) // 2, m[2], m[3]))
    elif m := re.match(r'\[(.*)\]\((.*)\)', line):
        toc.append((-1, m[1], m[2]))
    elif (m := re.match(r'# (.*)', line)) and m[1] != 'Summary':
        toc.append((None, m[1], None))
files = {p for _, _, p in toc if p}

def convert(depth, title, path):
    d = posixpath.dirname(path)
    me = fid(path)

    def resolve(target):
        if target.startswith('#'):
            return f'#{me}--{target[1:]}'
        if re.match(r'[a-z]+:', target):
            return target
        p, _, anchor = target.partition('#')
        p = posixpath.normpath(posixpath.join(d, p))
        if p in files:
            return f'#{fid(p)}--{anchor}' if anchor else f'#{fid(p)}'
        return str(SRC / p) if (SRC / p).exists() else target

    text = (SRC / path).read_text().replace('︎', '').replace('️', '')
    text = re.sub(r'<code>(.*?)</code>', lambda m: '`' + html.unescape(m[1]) + '`', text, flags=re.S)
    text = re.sub(r'<figure>\s*<img src="([^"]+)"[^>]*>\s*<figcaption>(.*?)</figcaption>\s*</figure>',
                  lambda m: '![%s](%s)' % (' '.join(re.sub(r'<a href="([^"]+)">\s*(.*?)\s*</a>', r'[\2](\1)', m[2], flags=re.S).split()), m[1]),
                  text, flags=re.S)
    text = re.sub(r'\]\(([^)\s]+)\)', lambda m: f']({resolve(m[1])})', text)
    text = re.sub(r'^(\[[^\]]+\]:\s*)(\S+)', lambda m: m[1] + resolve(m[2]), text, flags=re.M)

    out, seen = [], {}
    for line in text.splitlines():
        if m := re.match(r'(#+) (.*?)(?: \{#([^}]+)\})?$', line):  # keep mdbook custom ids verbatim
            level = len(m[1]) + max(depth, 0) + 1
            if len(m[1]) == 1:
                line = f'{"#" * level} {title} {{#{me}{" .unnumbered" if depth < 0 else ""}}}'
            else:
                anchor = m[3] or slug(m[2])
                seen[anchor] = seen.get(anchor, -1) + 1  # mdbook suffixes repeats with -1, -2, ...
                line = f'{"#" * level} {m[2]} {{#{me}--{anchor}{"-%d" % seen[anchor] if seen[anchor] else ""}}}'
        out.append(line)
    return '\n'.join(out) + '\n\n'

doc = [f'''---
title: Strawberry Polish Club
author: Chen-Pang He
date: {datetime.date.today():%B %Y}
documentclass: scrbook
classoption: [11pt, oneside, numbers=noendperiod]
papersize: a4
toc: true
toc-depth: 2
numbersections: true
secnumdepth: 2
indent: true
colorlinks: true
linkcolor: MidnightBlue
urlcolor: MidnightBlue
---
''']
started = False
for depth, title, path in toc:
    if depth is None or (depth == 0 and not started):
        if not started:
            doc.append('```{=latex}\n\\mainmatter\\setcounter{secnumdepth}{2}\n```\n')
            started = True
        doc.append(f'# {title}\n\n' if depth is None else '# One-level openings\n\n')
    if path:
        doc.append(convert(depth, title, path))

abbr = tomllib.loads(pathlib.Path('book.toml').read_text())['preprocessor']['abbr']['list']
abbr['(R)'] = 'relay'
doc.append('```{=latex}\n\\backmatter\n```\n\n# Abbreviations {.unnumbered}\n\n| | |\n|-|-|\n')
doc += [f'| {k} | {v} |\n' for k, v in sorted(abbr.items(), key=lambda kv: kv[0].lower())]
(OUT / 'book.md').write_text(''.join(doc))

(OUT / 'preamble.tex').write_text(r'''
\directlua{luaotfload.add_fallback("cjk", {"Noto Serif CJK TC:mode=harf;script=hani;"})}
\setmainfont{Libertinus Serif}[RawFeature={fallback=cjk}]
\setsansfont{Libertinus Sans}[RawFeature={fallback=cjk}]
% Code spans: no monospace in print; Libertinus Sans on the website's light gray, breakable across lines
\usepackage{luacolor,lua-ul}
\definecolor{codebg}{HTML}{ECECEC}
\renewcommand\texttt[1]{{\sffamily\highLight[codebg]{\kern.15em #1\kern.15em}}}
\definecolor{suitred}{HTML}{BB2222}
% Red hearts and diamonds everywhere, except inside links (\plainsuittrue), as on the website
\newif\ifplainsuit \protected\def\plainsuiton{\plainsuittrue}  % robust for captions
\let\♥=♥ \let\♦=♦  % one-char control symbols survive hyperref bookmark strings
\catcode`♥=\active \catcode`♦=\active
\def♥{\texorpdfstring{\ifplainsuit\♥\else\textcolor{suitred}{\♥}\fi}{\♥}}
\def♦{\texorpdfstring{\ifplainsuit\♦\else\textcolor{suitred}{\♦}\fi}{\♦}}
% Page reference after an internal link, omitted when the target is on this page
\usepackage{refcount}
\newcommand\pref[1]{\ifnum\getpagerefnumber{#1}=\value{page}\else~(p.\,\pageref{#1})\fi}
% Front matter: swallow pandoc's \mainmatter so Introduction and Author stay in it
\let\realmainmatter\mainmatter
\renewcommand\mainmatter{\global\let\mainmatter\realmainmatter}
\renewcommand\arraystretch{1.15}
\setcounter{secnumdepth}{-2}  % no section numbers in the front matter; restored at \mainmatter
\usepackage{graphicx}
\subject{\includegraphics[height=3cm]{favicon.pdf}}
'''.replace('favicon.pdf', str(OUT / 'favicon.pdf')))  # TeX Live 2023 does not search the output directory

subprocess.run(['rsvg-convert', '-f', 'pdf', '-o', OUT / 'favicon.pdf', 'theme/favicon.svg'], check=True)
subprocess.run(['pandoc', OUT / 'book.md', '-o', OUT / 'polish-club.tex', '-s', '--top-level-division=part',
                '--columns=10000', '--lua-filter=print.lua', '-H', OUT / 'preamble.tex'], check=True)
for _ in range(3):
    if subprocess.run(['lualatex', '-interaction=batchmode', '-halt-on-error', '-output-directory', OUT, OUT / 'polish-club.tex'],
                      stdout=subprocess.DEVNULL).returncode:
        log = (OUT / 'polish-club.log').read_text(errors='replace').splitlines()
        raise SystemExit('\n'.join(log[-40:]))
pathlib.Path('book').mkdir(exist_ok=True)
shutil.copy(OUT / 'polish-club.pdf', 'book/polish-club.pdf')
print('book/polish-club.pdf')
