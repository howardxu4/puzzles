import sys

def getmatrix(m):
  """get a MxM array
  """ 
  m += 1
  return[[0 for i in range(m)] for j in range(m)]

def loop(cc, max, method, sub=None):
  """loop upper right triangle call
  """
  max += 1
  for i in range(2,max):
    for j in range(i, max):
      method(cc, i, j, max, sub)

def allproduct(cc, i, j, max, sub):
  cc[i][j] = i*j

def allsum(cc, i, j, max, sub):
  cc[i][j] = i+j

def cnvtnum(cc, i, j, max, sub):
  cc[i][j] = len(sub[str(cc[i][j])])
  
def dictpair(cc, i, j, max, sub):
  """dict pair list
  """
  if not sub.get(str(cc[i][j]), False):
    t = []
    for m in range(2, max):
      for n in range(m,max):
        if cc[m][n] == cc[i][j]:
          t.append((m, n))
    sub[str(cc[i][j])] = t
    
def nrdp(ds, NDP):
  """no reverse dis-product
  """
  cnt = 0
  for v in ds:
    if NDP[v[0]][v[1]] > 1:
      cnt += 1
  return cnt

def snrdp(dp, DS, NDP, F=True):
  """dis-sum of nrdp
  """
  cnt = 0
  for v in dp:
    sds = DS[str(v[0]+v[1])]
    n = nrdp(sds, NDP)
    if F:
      if nrdp(sds, NDP) > 1:
        cnt += 1
    else:
      if nrdp(sds, NDP) == 1:
        cnt += 1
  return cnt

def getnorm(dp, DS, NDP):
  """get-norm
  """
  cnt = 0
  for v in dp:
    sds = DS[str(v[0]+v[1])]
    if len(sds) == nrdp(sds, NDP):
      cnt += 1
  return cnt

def noknowknow(m, n, DS, DP, NDP):
  """1st kind guessing
  """
  if not NDP[m][n]>1:
    return False
  ds = DS[str(m+n)]
  if not len(ds)>1:
    return False
  if nrdp(ds, NDP) != 1:
    return False
  dp = DP[str(m*n)]
  return snrdp(dp, DS, NDP) == 1

def nonoknowknow(m, n, DS, DP, NDP):
  """2nd kind guessing
  """
  if not NDP[m][n]>1:
    return False
  ds = DS[str(m+n)]
  if nrdp(ds, NDP) <= 1:
    return False
  dp = DP[str(m*n)]
  if snrdp(dp, DS, NDP) != 1:
    return False
  cnt = 0
  for v in ds:
    sdp = DP[str(v[0]*v[1])]
    if snrdp(sdp, DS, NDP, False) == 1:
      cnt += 1
  return cnt == 1

def sunpangnumber(m, n, DS, DP, NDP):
  """sun pang number (1~(>61))
  """
  ds = DS[str(m+n)]
  if len(ds) != nrdp(ds, NDP):
    return False
  dp = DP[str(m*n)]
  if getnorm(dp, DS, NDP) != 1:
    return False
  cnt = 0
  for v in ds:
    sdp = DP[str(v[0]*v[1])]
    if getnorm(sdp, DS, NDP) == 1:
      cnt += 1
  return cnt == 1

def main():
  """MAIN (defalt 99, can accept parameter to change)
  """
  D=99
  if len(sys.argv) > 1:
    try:
      D = int(sys.argv[1])
    except:
      pass
  print "m, n in (1 ~ " + str(D) + ") A: m*n B: m+n "
  A = getmatrix(D)
  # SUM table
  loop(A, D, allsum)
  # SUM dict 
  DS = {}
  loop(A, D, dictpair, DS)
  # PRODUCT table
  loop(A, D, allproduct)
  # PRODUCT dict
  DP = {}
  loop(A, D, dictpair, DP)
  # number of DP
  loop(A, D, cnvtnum, DP)

  print "No-Know-Know: [A->B: No] B->A: No, A: Know, B: Know"
  for m in range(2, D):
    for n in range(m, D):
      if noknowknow(m, n, DS, DP, A):
        print m, n, ":", m+n, m*n

  print "No-No-Know-Know: B->A: No, A->B: No, A: Know, B: Know"
  for m in range(2, D):
    for n in range(m, D):
      if nonoknowknow(m, n, DS, DP, A):
        print m, n, ":", m+n, m*n

  print "Sun-Pang-Number: P->S: No both, S: Know, P: Know"
  for m in range(2, D):
    for n in range(m, D):
      if sunpangnumber(m, n, DS, DP, A):
        print m, n, ":", m+n, m*n

if __name__ == "__main__":
  main()
