'''
Created on Oct 29, 2021

@author: 707578
'''
'''
1)outer forloop is for number of rows/lines
2) inner forloop is for column in a row
3) print statement inside inner loop
'''
for row in range(0,4):
    for col in range(0,row+1):
        print("akshay", end="")
    print("\n")
    
print("pattern 2")
for row in range(0,5):
    for col in range(0,5-row):
        print("akshay", end="\t")
    print("\n")
    
print("patter3\n")

for row in range(1,5):
    for col in range(1,col+1):
        print(col,end="")
    print("\n")


print("patter4\n")
n=5
for row in range(1,2*n):
    if(row<6):
        col=row+1;
    else:
        col=(2*n-row)+1
    for j in range(1,col):
        print("*",end=" ")
    print("\n")
    
print("pattern5\n")
'''
        *   

      *   *   

    *   *   *   

  *   *   *   *   

*   *   *   *   *   

  *   *   *   *   

    *   *   *   

      *   *   

        *   
'''


row=5
for i in range(1,2*row):
    #for 1 to 5
    if(i<row):
        col=i;
    #for 6 to 10
    else:
        col=(2*row-i)
    #for spaces
    spaces=row-col
    for s in range(1,spaces+1):
        print(" ",end=" ")
    for j in range(1, col+1):
        print("* ",end="  ")
    print("\r")
    

print("pattern 6")
n=5
import math   
for row in range(1,n+1):
    spaces=n-i
    for s in range(1,spaces+1):
        print(" ",end = " ")
#     for j in range(1,((2*i)-1)+1):
    col=row
    while(col>=1):
        print(col, end=" ")
        col=col-1
    for ko in range(2,row+1):
        print(ko ,end=" ")

    print("\n")      
'''
4 4 4 4 4 4 4 4 4 

4 3 3 3 3 3 3 3 4 

4 3 2 2 2 2 2 3 4 

4 3 2 1 1 1 2 3 4 

4 3 2 1 0 1 2 3 4 

4 3 2 1 1 1 2 3 4 

4 3 2 2 2 2 2 3 4 

4 3 3 3 3 3 3 3 4 

4 4 4 4 4 4 4 4 4 

'''
print("pattern 7\n")
n=4
N=2*n
for row in range(0,2*n+1):
    for col in range(0,2*n+1):
        
        min_val=min(row,col,N-(col),N-(row))
        min_val=n - min_val
        print(min_val,end=" ")
    print("\n")
    
    
            

    