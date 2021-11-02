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