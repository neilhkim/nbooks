"""Build the public copy of the app for GitHub Pages.

    python tools/build_public.py

Reads  nbooks.html        (your private copy, with the built-in book list — never committed)
Writes docs/nbooks.html   (same app with the built-in book list and categories removed)

The public copy starts empty; your books come from your secret Gist once you connect sync.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'nbooks.html')
OUT = os.path.join(ROOT, 'docs', 'nbooks.html')

s = open(SRC, encoding='utf-8').read()

def empty_array(name):
    global s
    start = s.index('const %s=[' % name)
    end = s.index('];', start) + 2
    s = s[:start] + 'const %s=[];' % name + s[end:]

empty_array('SEED_CATS')
empty_array('SEED')
s = s.replace('/* ===== Starting data: [title, author, year(0=unknown), categories] ===== */',
              '/* Public build: no built-in data. The library loads from the secret Gist via sync. */')

# safety check: nothing from the private list may remain
priv = open(SRC, encoding='utf-8').read()
seed = priv[priv.index('const SEED=['):priv.index('];', priv.index('const SEED=['))]
titles = re.findall(r'^\["((?:[^"\\]|\\.)+)"', seed[len('const SEED=['):], re.M)
leaks = [t for t in titles if len(t) > 12 and t in s]
if leaks:
    sys.exit('Refusing to write: private titles still present, e.g. %r' % leaks[:3])

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8', newline='\n').write(s)
print('wrote %s (%d KB, %d private titles checked)' % (os.path.relpath(OUT, ROOT), len(s.encode()) // 1024, len(titles)))
