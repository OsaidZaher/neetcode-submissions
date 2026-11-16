'''

you are a array of points where points[i] = [xi, yi] 

these values repesents the coordinates on an axis 

we are also given an integer k

we are to return the k closest coordinates to (0,0)

this is the formula to to get the coordinates: sqrt((x1 - x2)^2 + (y1 - y2)^2))

--
points = [[0,2],[2,0],[2,2]], k = 2

take the two values in each element in the array points [0,2]
add them together you get 2
assign 2 as the value to [0:2] key hashMap = {[0:2]:2, [2:0]:2, [2:2]:4}

we make a new array res 
add the keys and value as pairs/ add the keys in ascending order based on the value of said keys res = [2,2,4] or [[[0:2],2], [[2:0],2], [[2:2]:4]]

return :k keys 

'''


class Solution:
    def kClosest(self, points, k):
        hashMap = {}
        res = []

        for point in points:
            pointKey = tuple(point)
            pointValue = point[0] ** 2 + point[1] ** 2
            hashMap[pointKey] = pointValue

        for point in points:
            pointKey = tuple(point)
            res.append([point, hashMap[pointKey]])

        res.sort(key=lambda item: item[1])

        return [item[0] for item in res[:k]]