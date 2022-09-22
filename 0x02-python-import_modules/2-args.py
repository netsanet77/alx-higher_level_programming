#!/usr/bin/python3
import sys
argv = sys.argv
length = len(argv) - 1
if length == 1:
    print(f"{length} argument:")
elif length == 0:
    print(f"{length} arguments.")
else:
    print(f"{length} arguments:")
for i in range(1, length + 1):
    print(f"{i}: {argv[i]}")
