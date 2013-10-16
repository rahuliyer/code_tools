#!/usr/bin/python

import sys
import os

def add_license(filename):
  l = open("license.txt", "r")
  license = l.read()

  f = open(filename, "r")
  tmpfile = "/tmp/out" + str(os.getpid())

  g = open(tmpfile, "w")

  g.write(license + "\n")

  while True:
    line = f.readline()
    if line == '':
      break

    g.write(line.rstrip() + "\n")

  f.close()
  g.close()

  os.rename(tmpfile, filename)

for i in sys.argv[1:]:
  add_license(i)
