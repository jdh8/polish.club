-- pandoc filter for print.py: <br>, link page refs, table column widths
local LINE = 80  -- ponytail: characters per text line at 11pt, tuned by eye

function RawInline(el)
  if el.format == 'html' and el.text:match('^<br') then return pandoc.LineBreak() end
end

function Link(el)
  if el.target:sub(1, 1) ~= '#' then return el end
  return {el, pandoc.RawInline('latex', '\\pref{' .. el.target:sub(2) .. '}')}
end

-- Longest line of a cell, in characters; header auctions break at <br>
local function width(blocks)
  local best, cur = 0, 0
  for _, b in ipairs(blocks) do
    for _, x in ipairs(b.content or {}) do
      if x.t == 'LineBreak' then best, cur = math.max(best, cur), 0
      else cur = cur + (utf8.len(pandoc.utils.stringify(x)) or 0) end
    end
    best, cur = math.max(best, cur), 0
  end
  return best
end

-- Column widths from content.  Narrow tables without line breaks keep natural
-- widths; otherwise (pandoc would split line-broken tables evenly) each column
-- gets its longest line, and the last column absorbs any overflow by wrapping.
function Table(t)
  local n, max, broken = #t.colspecs, {}, false
  for i = 1, n do max[i] = 0 end
  local function scan(rows)
    for _, r in ipairs(rows) do
      for i, c in ipairs(r.cells) do
        if i <= n then max[i] = math.max(max[i], width(c.contents)) end
        pandoc.Div(c.contents):walk{LineBreak = function() broken = true end}
      end
    end
  end
  scan(t.head.rows)
  for _, body in ipairs(t.bodies) do scan(body.body) end
  local total = 0
  for i = 1, n do total = total + max[i] + 3 end
  if total <= LINE and not broken then return nil end
  local used = 0
  for i = 1, n - 1 do
    t.colspecs[i] = {t.colspecs[i][1], (max[i] + 3) / LINE}
    used = used + (max[i] + 3) / LINE
  end
  local want = (max[n] + 3) / LINE
  if used + want <= 1 then
    t.colspecs[n] = {t.colspecs[n][1], want}
  elseif 1 - used >= 0.25 then
    t.colspecs[n] = {t.colspecs[n][1], 1 - used}
  else  -- the last column alone cannot absorb the overflow: shrink all proportionally
    for i = 1, n do t.colspecs[i] = {t.colspecs[i][1], (max[i] + 3) / total} end
  end
  return t
end

-- Unnumbered chapters (front and back matter) via KOMA's \addchap, which also sets the running head
function Header(el)
  if el.level == 2 and el.classes:includes('unnumbered') then
    local title = pandoc.write(pandoc.Pandoc({pandoc.Plain(el.content)}), 'latex'):gsub('\n$', '')
    return pandoc.RawBlock('latex', '\\addchap{' .. title .. '}\\label{' .. el.identifier .. '}')
  end
end
