#!/usr/bin/python

import sys
import os

def remove_whitespace(filename):
  f = open(filename, "r")
  tmpfile = "/tmp/out" + str(os.getpid())

  g = open(tmpfile, "w")

  num_empty_lines = 0
  while True:
    line = f.readline()
    if line == '':
      break

    line = line.rstrip()
    if line == '':
      num_empty_lines += 1
    else:
      for i in range(0, num_empty_lines):
        g.write("\n")

      num_empty_lines = 0
      g.write(line + "\n")

  f.close()
  g.close()

  os.rename(tmpfile, filename)

for i in sys.argv[1:]:
  remove_whitespace(i)
