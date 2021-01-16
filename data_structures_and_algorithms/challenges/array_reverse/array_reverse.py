# if you want to test it type this command "pytest tests/challenges/test_array_reverse.py"

# soluation number 1
def reverse_array1(lis):
  return lis[::-1]


# soluation number 2
def reverse_array2(lis):
  lis.reverse()
  return lis


# soluation number 3
def reverse_array3(lis):
  lis =lis[::-1]
  return lis


# soluation number 4
def reverse_array4(Lis):
  newLis=[]
  lenOfLis= len(Lis)
  while lenOfLis :
    newLis.append(Lis[lenOfLis-1])
    lenOfLis-=1
  return newLis


# soluation number 5 
def reverse_array5(Lis):
  length = 0
  while True:
      try:
          Lis[length]
      except IndexError:
          break
      else:
          length += 1
          continue
  new=0
  end=length-1
# to add new array with spesific numer of index

  newLis=[int]*(length)
  while (end >= 0):
    newLis[new]=Lis[end]
    new+=1
    end-=1

  return newLis


# "******/note/******"
#if you going to test it  then test it one by one :)

# inp=[1, 22, 333 , 4444, 55555]
# print(reverse_array1(inp))
# print(reverse_array2(inp))
# print(reverse_array3(inp))
# print(reverse_array4(inp))
# print(reverse_array5(inp))

