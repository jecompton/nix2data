## tab2json.py
## Takes typical space-separated tabular output typical of many *nix utilities
## and returns json

def parse_line(line):
  return line.strip().split()
