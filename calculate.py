#!/usr/bin/env python
'''
  calculates stats over a column

  usage:
    python calculate.py [field delimiter] < data

  output:
    count: number of rows
    mean
    median
    min
    max
    sd
    repeats: list of repeated values in column 1
'''
import sys

import numpy as np

if len(sys.argv) > 2:
  field = int(sys.argv[1])
  delimiter = sys.argv[2]
else:
  field = 2
  delimiter = '|'

print "calculating on field {0} with delimiter {1}".format(field, delimiter)

r = []
names = set()
repeats = set()
for line in sys.stdin:
  fields = line.strip().split(delimiter)
  if len(fields) > field:
    try:
      value = float(fields[field])
      r.append(value)
      if fields[0] in names:
        repeats.add(fields[0])
      else:
        names.add(fields[0])
    except ValueError:
      print "skipped {0}".format(line.strip())
      pass

if len(r) > 0:
  print "count: {0}\nmean: {1:.2f}\nmedian: {6:.2f}\nmin: {2:.2f}\nmax: {3:.2f}\nsd: {4:.2f}\nrepeats: {5}".format( len(r), np.mean(r), min(r), max(r), np.std(r), ','.join(list(repeats)), np.median(r) )
else:
  print "no records"
