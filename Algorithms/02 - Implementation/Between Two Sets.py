#python 3
#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    l1=len(a)
    l2=len(b)
    temp=[]
    tt=[]
    t=[]
    for i in range(a[l1-1],b[0]+1):
        temp.append(i)
    for i in range(0,l1):
        for j in range(0,len(temp)):
            if(temp[j]%a[i]==0):
                tt.append(temp[j])
        temp[:]=[]
        temp=tt[0:len(tt)]
        tt[:]=[]
    tem=temp[0:len(temp)]
    i=0
    while(i<len(tem)):
        for j in range(0,l2):
            if(b[j]%tem[i]==0):
                t.append(tem[i])
            else:
                tem.remove(tem[i])
                i=i-1
        i=i+1
    h=len(tem)
    return h

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()