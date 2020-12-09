def getSum(data):
    return sum(data)
  
def getMean(data):
    return getSum(data)/len(data)

def getMax(data):
    maxV=data[0]
    for i in data[1:]:
        if i>maxV:
            maxV=i
    return maxV

def getMin(data):
    minV=data[0]
    for i in data[1:]:
        if i<minV:
            minV=i
    return minV

def getTwoSum(n2,n1=1):
    if n2<n1:
        n2,n1=n1,n2
    return (n1+n2)*(n2+1-n1)//2
