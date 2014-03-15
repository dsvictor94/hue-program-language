"""
  hue program language
  based: 
     Brainfuck <http://en.wikipedia.org/wiki/Brainfuck>
     Python-Brainfuck <https://github.com/pocmo/Python-Brainfuck>
     
  implemented to answer: <https://www.facebook.com/photo.php?fbid=645866465460967>
"""

import sys
import getch

def run(code):
  code = ''.join(c for c in code if c in "hue ").split()
  map = buildmap(code)
  
  cells, ptr, pox = [0], 0, 0
  
  while pox < len(code):
    c = code[pox]
    
    if c == "h":
      ptr+=1
      if ptr == len(cells): cells.append(0)
    elif c == "hu":
      ptr = max(0, ptr-1)
    elif c == "hue":
      cells[ptr] = (cells[ptr]+1) % 256
    elif c == "hueh":
      cells[ptr] = (cells[ptr]-1) % 256
    elif c == "huehu":
      sys.stdout.write(chr(cells[ptr]))
    elif c == "huehue":
      cells[ptr] = ord(getch.getch())
    elif c == "huehueh" and cells[ptr]==0:
      pox = map[pox]
    elif c == "huehuehu" and cells[ptr]!=0:
      pox = map[pox]
    
    
    pox+=1


def buildmap(code):
  tmp, map = [], {}
  for pox, c in enumerate(code):
    if c == "huehueh": tmp.append(pox)
    if c == "huehuehu":
      start = tmp.pop()
      map[start] = pox
      map[pox] = start
  return map
  
if __name__ == "__main__":
  if len(sys.argv) == 2: 
     f = open(sys.argv[1], "r")
     run(f.read())
     f.close()
  else: print "Usage:", sys.argv[0], "filename"