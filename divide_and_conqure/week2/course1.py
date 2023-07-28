# Karatsuba Multiplication
from math import log, ceil

count = 0 
def kara_mult(a,b):

  a,b = str(a),str(b)

  x = len(a)
  y = len(b)

  if not(log(x,2).is_integer()):
    x = pow(2,ceil(log(x,2)))
  if not(log(y,2).is_integer()):
    y = pow(2,ceil(log(y,2)))
  
  x = y = max(x,y)
  a = '0'*(x-len(a))+a
  b = '0'*(y-len(b))+b
    
  if x+y ==2:
    return int(a)*int(b)
    
  x_by_2 = round(x/2) if x > 1 else 1
  m = a[:x_by_2] if x > 1 else '0'
  n = a[x_by_2:] if x > 1 else a

  y_by_2 = round(y/2) if y > 1 else 1
  o = b[:y_by_2] if y > 1 else '0'
  p = b[y_by_2:] if y > 1 else b

  mo = kara_mult(m,o)
  np = kara_mult(n,p)
  intrim = ((pow(10,x_by_2)))*((kara_mult(str(int(m)+int(n)),str(int(o)+int(p))))-(mo+np))
  res = ((pow(10,x))*mo) + intrim + np
  return res


# if __name__ == "__main__":
#     a = '3141592653589793238462643383279502884197169399375105820974944592'#input("a : ")
#     b = '2718281828459045235360287471352662497757247093699959574966967627' #input("b : ")
#     res = kara_mult(a,b)
#     print("Result : ",res)
#     print("Count : ",count)


# ==================================== WEEK 2 ====================================

# BUBBLE sort algorithm
count = 0
def bubble(a):
  for _ in range(len(a)):
    for i in range(len(a)-1):
      global count; count+=1
      if a[i]>a[i+1]:
        a[i],a[i+1] = a[i+1],a[i]
  return a

# MERGE sort algorithm
def merge(a,b):
  opt = []
  i=j=0
  for _ in range(len(list(a))+len(b)):
    if i == len(a):
      opt.append(b[j]);j+=1
    elif j == len(b):
      opt.append(a[i]);i+=1
    elif a[i] < b[j]:
      opt.append(a[i]);i+=1
    else:
      opt.append(b[j]);j+=1
  return opt

def merge_sort_algo(a):
  if len(a) == 1:
    return a
  else:
    n = len(a)
    n_by_2 = n//2
    return merge(merge_sort_algo(a[:n_by_2]),merge_sort_algo(a[n_by_2:]))

# INVERSION : basic implementation(this works like bubble sort) with the time complexity of O(n^2)
inversion_cnt = 0
inversion_basic_pairs = []
def inversion_basic(a):
  global inversion_cnt,inversion_basic_pairs
  for i in range(len(a)-1):
    for j in range(i+1,len(a)):
      if a[i]>a[j]:
        # print(f"({a[i]},{a[j]})")
        inversion_basic_pairs.append((a[i],a[j]))
        inversion_cnt+=1

# INVERSION : merge sort implementaion(we will use merge sort logic to find the inversions) with the time complexity of O(nlogn)
inversion_count = 0
inversion_merge_pairs = []
def merge_with_inversion(a,b):
  global inversion_count,inversion_merge_pairs
  opt = []
  i=j=0
  for _ in range(len(list(a))+len(b)):
    if i == len(a):
      opt.append(b[j]);j+=1
    elif j == len(b):
      opt.append(a[i]);i+=1
    elif a[i] < b[j]:
      opt.append(a[i]);i+=1
    else:
      # inversion logic
      if a[i]==b[j]:
        opt.append(a[i])
        i+=1
        continue
      opt.append(b[j])
      inversion_count+=len(a)-i
      # for m in range(i,len(a)):
      #   print(f"({a[m]},{b[j]})")
      #   inversion_merge_pairs.append((a[m],b[j]))
      j+=1
  return opt

def merge_sort_algo_inversion(a):
  if len(a) == 1:
    return a
  else:
    n = len(a)
    n_by_2 = n//2
    opt =  merge_with_inversion(
      merge_sort_algo_inversion(a[:n_by_2]),
      merge_sort_algo_inversion(a[n_by_2:])
    )
    return opt

# basic matrix multiplication
import numpy as np
def mat_mult(x,y):
  x = list(x)
  y = list(y)
  opt = 0
  for i in range(len(x)):
    opt += x[i]*y[i]
  return opt
def matrix_multiplication_basic(a,b):
  m,n = a.shape
  o,p = b.shape
  if n!= o:
    print("a,b cannot be multiplied.")
  else:
    opt = np.array([None for _ in range(m*p)]).reshape(m,p)
  for i in range(m):
    for j in range(p):
      opt[i,j] = mat_mult(a[i,:],b[:,j])
  return opt


def eucl_dist(a,b):
  return np.sqrt(pow((a[0]-b[0]),2)+pow((a[1]-b[1]),2))

def closest_pair(P):
  n = len(closest_pair)
  if n==1:
    return P[0]
  else:
    n_by_2 = n//2

    
# binary search
count=0
def bin_search(lst,k):
  global count; count+=1; print(count)
  n = len(lst)
  n_by_2 = n//2
  if len(lst)<=1:
    return lst[0]
  else:
    if lst[n_by_2]==k:
      return lst[n_by_2]
    elif k<lst[n_by_2]:
      return bin_search(lst[:n_by_2],k)
    else:
      return bin_search(lst[n_by_2+1:],k)

# Quick sort
def quick_sort_sorting(arr,piv):
  if piv != 0:
    arr[0],arr[piv] = arr[piv],arr[0]
  i=1
  j=2
  for _ in range(1,len(arr)-1):
    if arr[j] < arr[0]:
      arr[i],arr[j] = arr[j],arr[i]
      i+=1
      j+=1
    else:
      j+=1
  arr[0],arr[i-1] = arr[i-1],arr[0]
  
  return arr

def quick_sort(arr):
  n = len(arr)
  if n == 1:
    return arr
  arr = quick_sort_sorting(arr,0)
  print(arr)




if __name__ == "__main__":

  # print(bubble([5,4,3,2,1]))

  # print(merge_sort_algo([8,7,6,5,4,3,2]))

  # inversion_basic([4,3,2,1])
  
  # file = open('IntegerArray.txt','r')
  # IntergerArray = [int(i) for i in file]
  # inversion_basic(IntergerArray);print("number of inversions(basic) : ", inversion_cnt)
  # merge_sort_algo_inversion(IntergerArray);print("number of inversions(merge) : ", inversion_count)

  # basic matrix mutliplication has a time complexity of n^3
  # a = np.arange(1,5).reshape(2,2)
  # b = np.arange(1,5).reshape(2,2)
  # matrix_multiplication_basic(a,b)
  #TODO: strassens matrix multiplication

  # P = [(-1,-2),(-1,1),(0,2),(1.2,1.2),(0,3),(-1.5,-1.5)]

  # print(bin_search(list(range(20000)),2))


  quick_sort([3,7,6,5,4,3,2,1])



