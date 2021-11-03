'''
array rotation
o/p for 3 =[4, 5, 6, 7, 1, 2, 3]
'''
def rotation_by_concatenation(list1,d):
    list2 = list1[d:] + list1[:d]
    print(list2)

def rotatebyone(list1,d,n):    
    for i in range(0,d):
        temp = list1[0]
        for i in range(0,n-1):
            list1[i]=list1[i+1]
        list1[n-1]=temp
    print(list1)
     
list1 = [1,2,3,4,5,6,7]
rotation_by_concatenation(list1, 3)
rotatebyone(list1, 3, len(list1))
list1 = [1,2,3,4,5,6,7]
#reversal recursive
def swap(list1,m,n):
    temp1=list1[m]
    list1[m]=list1[n]
    list1[n]=temp1
def rev(list1,i,j):
    while(i<j):
        swap(list1,i,j)
        i=i+1
        j=j-1 
rev(list1,0,2)
rev(list1,3,len(list1)-1) 
rev(list1,0,len(list1)-1)
print("list 1 is ")
print(list1)  

sample_list=[1,2,3,4,5,6,7]
'''Input:  arr[] = {1, 2, 3, 4, 5}
Output: arr[] = {5, 1, 2, 3, 4}'''
def by_one(sample_list1):
    print(len(sample_list1))
    temp= sample_list1[len(sample_list1)-1]
    for i in range(0,len(sample_list1)-1):
        sample_list1[i]=sample_list1[i+1]
    sample_list1[len(sample_list1)-1]=temp
    print(sample_list1)
by_one(sample_list)


'''
Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3};
         key = 3
Output : Found at index 8'''
list1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
low =0
high=8
print("lllllllllllllllllllllllllllllllllllllllll")
def findpivote(list1,low,high):
    if high < low:
        return -1
    if high == low:
        return low
    (mid) = int((low+high)/2)
    print(mid)
    if list1[mid]>list1[mid+1]:
        return mid
    if list1[mid-1]>list1[mid]:
        return (mid-1)
    if list1[low]>=list1[mid]:
        return findpivote(list1,low,mid-1)
    
    return findpivote(list1,mid+1,high)

def bin_search(list1,low,high,key):
    if high < low:
        return -1
    mid = int((low+high)/2)
    if (key==list1[mid]):
        return mid
    if (key<list1[mid]):
        return bin_search(list1,low,mid-1,key)
    else:
        return bin_search(list1,mid+1,high,key)

def pivot_return (list1,p,key,low,high):      
    if list1[0] <= key:
        return bin_search(list1, 0, p-1, key);
    return bin_search(list1, p + 1, high, key);
#driver
p = findpivote(list1,0,8)
print(p)
        
i =pivot_return (list1,p,8,0,8)   
print("index Value is"+str(i))


'''
Input: arr[] = {11, 15, 26, 38, 9, 10}, x = 35
Output: true
There is a pair (26, 9) with sum 35
.'''

list1=[11, 15, 26, 38, 9, 10]
def findpivot(list1,low,high):
    #Binary search O(logn)
    if (low>high):
        return -1
    if high == low:
        return low
    mid=int((low+high)/2)
    if (list1[mid]<list1[mid-1]):
        return (mid-1)
    if(list1[mid]>list1[mid+1]):
        return (mid)
    if (list1[mid]<=list1[low]):
        return (findpivot(list1,low,mid-1))
    return(findpivot(list1,mid+1,high))

p=findpivot(list1,0,5)
print(p)
n=len(list1)
def sum(list1,p,gsum):
    l = (p+1)%n
    r =p%n
    while(l!=r):
        if (list1[l]+list1[r]==gsum):
            return True
        # If current pair sum is less,
        # move to the higher sum
        if(list1[l]+list1[r]<gsum):
            
            l=(l+1)%n
        else:             
            # Move to the lower sum side
            #rotate it from 3,2,1,0,5,4
            r = (n + r - 1) % n
            print(r)
    return False
val = sum(list1,p,14)       
print(val)

