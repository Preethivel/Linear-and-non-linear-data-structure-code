def titleToNumber(self, columnTitle: str) -> int:
  r=0
  for ch in columnTitle:
    r=r*26+(ord(ch)-ord('A')+1)
  return r
