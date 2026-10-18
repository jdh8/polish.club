#!/bin/sh
# Apply a polish.club style.css or suit font commit to the sibling bridge books
set -e
cd "$(dirname "$0")"
for d in blueberry-precision bridge-tutorial cranberry-moscito muscat-walsh watermelon-dutch wbridge5.book; do
	git format-patch -1 --binary --stdout "${1:-HEAD}" -- style.css theme/fonts suits.py | git -C "../$d" apply -3
done
