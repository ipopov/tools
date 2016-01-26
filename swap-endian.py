#!/usr/bin/python
#
# Usage:
#   pipe a stream of uint64s on stdin
#   get a stream of uint64s with reversed endianness on stdout

import sys

kLen = 8

buf = ""

while True:
  s = sys.stdin.read(kLen-len(buf))
  if not s:
    sys.stdout.write(buf.ljust(kLen, '\0')[::-1])
    break
  buf += s
  if len(buf) == kLen:
    sys.stdout.write(buf[::-1])
    buf = ""
