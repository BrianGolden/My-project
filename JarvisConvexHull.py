def isLeft(a,b,c):
    # From point a Is ca left of bc
    vec1 = [b[0]-a[0],b[1]-a[1]]
    vec2 = [c[0]-a[0],c[1]-a[1]]
    crossProduct = vec1[0]*vec2[1] - vec1[1]*vec2[0]
    lenv1 = (vec1[0])**2 + (vec1[1])**2
    lenv2 = (vec2[0])**2 + (vec2[1])**2
    if crossProduct == 0:
        return [lenv1,lenv2]
    else:
        return crossProduct

    '''
    if crossProduct > 0:
        return 'l'
    elif crossProduct < 0:
        return 'r'
    else:
        if lenv1 > lenv2:
            return b 
        else:
            return a 
    '''
# O(n^2)
# No sort find the next most left point
def JarvisConvexHull(graph):
    currentPoint = graph[0]
    n = len(graph)
    convexPoint = []
    for i in range(0,n):

        for j in range(0,n-1):
            a = isLeft(currentPoint,graph[j],graph[j-1])
            if a > 0 :
                nextPoint = graph[j-1]
            elif a < 0 :
                nextPoint = graph[j]
            else:



            # elif isinstance(isLeft(currentPoint,graph[i],graph[i-1]),list ):
            #     nextPoint = isLeft(currentPoint,graph[i],graph[i-1]) 
        currentPoint = nextPoint
        convexPoint.append(currentPoint)
    
    return convexPoint

tab = [[-3,2],[1,2],[8,4],[2,4],[7,6],[2,-6],[8,-8],[-1,-8] ]

res = JarvisConvexHull(tab)
print(res)


