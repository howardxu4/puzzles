import sys

def printout(aa, m):
  print "From 2 - {}".format(m)
  m += 1
  for i in range(m):
    for j in range(m):
      if aa[i][j]:
        print i, j, aa[i][j]

def getmatrix(m):
   m += 1
   return[[0 for i in range(m)] for j in range(m)]

def loop(aa, max, method, sub=None):
  max += 1
  for i in range(2,max):
    for j in range(i, max):
      method(aa, i, j, max, sub)

def allproducts(aa, i, j, max, sub):
  aa[i][j] = i*j

def identicalsum(aa, i, j, m, n):
  return aa[m][n] and i+j==m+n

def identicalproduct(aa, i, j, m, n):
  return aa[m][n] == aa[i][j]

def filterunique(aa, i, j, max, sub):
  if aa[i][j]:
    f = 1
    for m in range(2,max):
      if f:
        for n in range(m, max):
          if f:
            if aa[i][j] == aa[m][n] and i!=m and j!=n:
              f = 0
    if f:
      aa[i][j] = 0

def filterall(aa, i, j, max, sub):
  if aa[i][j]:
    f = 0
    for m in range(i, max):
      k = j+1 if i==m else m
      for n in range(k, max):
        if sub(aa, i, j, m, n):
          aa[m][n] = 0
          f = 1
    if f:
      aa[i][j] = 0

def main():
  m=99
  n = len(sys.argv)
  if n > 1:
    try:
      m = int(sys.argv[1])
    except:
      pass 
  aa = getmatrix(m)
  loop(aa, m, allproducts)
  if n > 3:
    printout(aa, m)
  loop(aa, m, filterunique)
  if n > 2:
    printout(aa, m)
  loop(aa, m, filterall, identicalsum)
  if n > 2:
    printout(aa, m)
  loop(aa, m, filterall, identicalproduct)
  printout(aa, m)

if __name__ == "__main__":
  main()  
