string = input("enter numbers by space")
a = input("enter number to be searched")
x = int(a)
list = string.split(" ")
arr = []
for i in list :
    arr.append(int(i))
def binarysearch(arr,l,r,x) :
    while (l <= r):
        mid = l + (r -1)//2;
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else :
            r = mid - 1
    return -1
result = binarysearch(arr,0,len(arr)-1,x)
if result != -1:
   print("element is present at index",result)
else:
   print("element is not present in array")
       
         
