class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for point in points:
            # Calculate distance to origo
            distance = math.sqrt(pow(point[0] - 0, 2) + pow(point[1]-0,2))
            print(point, distance)
            point.append(distance)
        
        points.sort(key=lambda x : x[2])
        res = []
        for i in range(k):
            res.append([points[i][0],points[i][1]])

        return res
        
