def insertShiftArray(Lis2,val):
  Lis = Lis2.copy()
  Lis.sort()
  testLength = 0
  while True:
      try:
          Lis[testLength]
      except IndexError:
          break
      else:
          testLength += 1
          continue
  lenOfLis = testLength
  print(lenOfLis)
  i=0
  valee='valee'
  
  # to add new array with spesific numer of index
  newLis=[valee]*(lenOfLis+1)
  print(newLis)
  while i<lenOfLis:
    if Lis[i]<val:
      newLis[i]=Lis[i]
    elif Lis[i]>val:
      newLis[i+1]=Lis[i]
      if newLis[i] == valee:
        newLis[i]= val
    elif Lis[i]>val:
      newLis[i]==val

    i+=1
  
  return newLis

print(insertShiftArray([2,4,6,8], 5))
print(insertShiftArray([4,8,15,23,42], 16))