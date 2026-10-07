def linearsearch(a,el):
  for i in range(len(a)):
    if a[i]==el:
      print(f'(el) is found at (i) index')
      return i
  return -1

a=[12,2,44,23,14,65,14]
print(linearsearch(a,14))
