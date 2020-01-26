import random
import math

def generateRandomData():
    lst=[]
    for i in range(500):
        lst.append((random.randint(-5,10),random.randint(-5,10)))
    return lst

def euclideanDistance(point1,point2):
    dist=math.sqrt(((point2[0]-point1[0])**2)+((point2[1]-point1[1])**2))
    return dist

def assignCluster(data):
    for i in data:
        dist1=euclideanDistance(centeroid1,i)
        dist2=euclideanDistance(centeroid2,i)
        if dist1<dist2:
            cluster1.append(i)
        else:
            cluster2.append(i)

def meanCluster(lst):
    x=0
    y=0
    for i in lst:
        x+=i[0]
        y+=i[1]
    newPoint=(x/len(lst),y/len(lst))
    return newPoint
    
data=generateRandomData()
centeroid1=(-2,4)
centeroid2=(5,6)
cluster1=[]
cluster2=[]
assignCluster(data)
meanC1=meanCluster(cluster1)
meanC2=meanCluster(cluster2)
while meanC1!=centeroid1 or meanC2!=centeroid2:
    centeroid1=meanC1
    centeroid2=meanC2
    cluster1,cluster2=[],[]
    assignCluster(data)
    meanC1=meanCluster(cluster1)
    meanC2=meanCluster(cluster2)
print(centeroid1)
print(centeroid2)
print (len(cluster1))
print (len(cluster2))
print (cluster1)
print (cluster2)


    
    
