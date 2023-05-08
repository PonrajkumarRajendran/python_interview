def solution(h,li):
  mydict={}
  for i in range(1,31):
    mydict["row%s" %i] = []
  i=1
  x=0
  def proper(i,x):
      if i <= 2 or x == 0:
        mydict["row1"].append(i)
        x +=1
      else:
        mydict["row%s" %x].append(i)
        if len(mydict["row%s" %x])%2 != 0:
            x=0
        else:
            x=x+1
      return x

  while i<2**h:
    x = proper(i,x)
    i +=1
  
  
  output = []
  root = (2**h)-1
  m = 0
  for s in li:
    if s == root:
      output.append(-1)
    else:
      n=1
      while n <= h:
        if mydict["row%s" %n].count(s) != 0:
          m=n
        n +=1
      g=m+1
      f=s+1
      while mydict["row%s" %g].count(f) ==0:
        f += 1
      output.append(f)
      
  print output
solution(3, [7, 3, 5, 1])