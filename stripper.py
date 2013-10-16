#!/usr/bin/python

import sys
import os

def remove_whitespace(filename):
  f = open(filename, "r")
  tmpfile = "/tmp/out" + str(os.getpid())

  g = open(tmpfile, "w")

  while True:
    line = f.readline()
    if line == '':
      break

    g.write(line.rstrip() + "\n")

  f.close()
  g.close()

  os.rename(tmpfile, filename)

for i in sys.argv[1:]:
  remove_whitespace(i)
