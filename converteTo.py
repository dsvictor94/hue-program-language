import sys

def toHue(brainfuck):
  brainfuck = "".join(b for b in brainfuck if b in "><+-.,[]")
  code = ""
  for c in brainfuck:
    if c == ">":
      code+= "h "
    elif c == "<":
      code+= "hu "
    elif c == "+":
      code+="hue "
    elif c == "-":
      code+="hueh " 
    elif c == ".":
      code+="huehu "
    elif c == ",":
      code+="huehue "
    elif c == "[":
      code+="huehueh "
    elif c == "]":
      code+="huehuehu "
  return code

def toBrainfuck(hue):
  hue = ''.join(c for c in hue if c in "hue ").split()
  code = ""
  for c in hue:
    if c == "h":
      code+= ">"
    elif c == "hu":
      code+= "<"
    elif c == "hue":
      code+="+"
    elif c == "hueh":
      code+="-" 
    elif c == "huehu":
      code+="."
    elif c == "huehue":
      code+=","
    elif c == "huehueh":
      code+="["
    elif c == "huehuehu":
      code+="]"
  return code

if __name__ == "__main__":
  if len(sys.argv) == 3: 
     f = open(sys.argv[1], "r")
     if sys.argv[2] == "hue":
       print toHue(f.read())
     elif sys.argv[2] == "brainfuck":
       print toBrainfuck(f.read())
     f.close()
  else: print "Usage:", sys.argv[0], "filename", "brainfuck|hue"