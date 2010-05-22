##########################################################
# Minimum
##########################################################

def Minimum(A):
    return min(A)
#    j=0
#    for i in range(1,len(A)):
#        if A[i]<A[j]:
#            j=i
#    return  A[j]

##########################################################
# Maximum
##########################################################

def Maximum(A):
    return max(A)
#    j=0
#    for i in range(1,len(A)):
#        if A[i]>A[j]:
#            j=i
#    return  A[j]





##########################################################
# InsertionSort
##########################################################
def InsertionSort(A):
    for i in range(1,len(A)):
        j=i-1
        while(j>=0):
            if A[j]>A[j+1]:
                (A[j], A[j+1]) = (A[j+1], A[j]) 
                j=j-1
            else:
                break
            pass
            

##########################################################
# MergeSort
##########################################################
def Merge(A,p,q,r):
    B=[]
    i=p
    j=q
    while True:
        if A[i]<=A[j]:
            B.append(A[i])
            i=i+1
        else:
            B.append(A[j])
            j=j+1
        if i==q:
            while j<r:
                B.append(A[j])
                j=j+1
            break
        if j==r:
            while i<q:
                B.append(A[i])
                i=i+1
            break
    A[p:r]=B

        
def MergeSort(A, p=0, r=-1):
    if r is -1:
        r=len(A)
    if p<r-1:
        q=int((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q,r)
        Merge(A,p,q,r)
        
        
##########################################################
# MergeSortDP
##########################################################
def MergeSortDP(A):
    blocksize=1
    listsize=len(A)
    while blocksize<listsize:
        for p in range(0, listsize, 2*blocksize):
            q=p+blocksize
            r=min(q+blocksize, listsize)
            if r>q:
                Merge(A,p,q,r)
        blocksize=2*blocksize




##########################################################
# QuickSort
##########################################################
def Partition(A,i,j):
    x=A[i]
    h=i
    for k in range(i+1,j):
        if A[k]<x:
            h=h+1
            A[h],A[k]=A[k],A[h]
    A[h],A[i]=A[i],A[h]    
    return h
        
def QuickSort(A,p=0,r=-1):
    if r is -1:
        r=len(A)
    if p<r-1:
        q=Partition(A,p,r)
        QuickSort(A,p,q)
        QuickSort(A,q+1,r)


##########################################################
# RandomizedQuickSort
##########################################################
def RandomizedPartition(A,p,r):
    i=randint(p,r-1)
    (A[p],A[i])=(A[i],A[p])
    return Partition(A,p,r)


def RandomizedQuickSort(A,p=0,r=-1):
    if r is -1:
        r=len(A)
    if p<r-1:
        q=RandomizedPartition(A,p,r)
        RandomizedQuickSort(A,p,q)
        RandomizedQuickSort(A,q+1,r)


##########################################################
# CountingSort
##########################################################
def CountingSortSmall(A):
    if Minimum(A)<0:
        raise 'CountingSort List Unbound'
    n=len(A)
    C=[]
    k=Maximum(A)+1
    for j in range(k):
        C.append(0)
    for j in range(n):
        C[A[j]]=C[A[j]]+1
    i=0        
    for j in range(k):
        while C[j]>0:
            A[i]=j
            C[j]=C[j]-1
            i=i+1

def CountingSort(A):
    if Minimum(A)<0:
        raise 'CountingSort List Unbound'
    B=[]
    C=[]
    k=Maximum(A)+1
    for j in range(k):
        C.append(0)
    for j in range(len(A)):
        B.append(0)
        C[A[j]]=C[A[j]]+1
    for i in range(1,k):
        C[i]=C[i]+C[i-1]
    j=len(A)-1
    while j>=0:
        B[C[A[j]]-1]=A[j]
        C[A[j]]=C[A[j]]-1
        j=j-1
    return B



