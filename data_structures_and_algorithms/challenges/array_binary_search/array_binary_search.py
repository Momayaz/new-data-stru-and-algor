def BinarySearch(Lis,val):
  try:
    test_length = 0
    while True:
        try:
            Lis[test_length]
        except IndexError:
            break
        else:
            test_length += 1
            continue
    len_of_Lis = test_length

    index_of_Lis=len_of_Lis-1

    mid= len_of_Lis // 2


    if len_of_Lis == 0:
      return "the list is empty"
    else:
      while Lis[mid] != val:
        if val > Lis[index_of_Lis]:
          return -1
        else:
          if val == Lis[mid]:
            return mid

          else:
            if val < Lis[mid]:
              mid = mid // 2

            elif val > Lis[mid]:
              mid =index_of_Lis-mid

    return mid
  except Exception as errorr:
    print('I think you did not stick to the specified inputs wich is ("list","num")')
  
if __name__=="__main__":
    print(BinarySearch([4,8,15,16,23,42], 'ssss'))
    print(BinarySearch([11,22,33,44,55,66,77], 90))