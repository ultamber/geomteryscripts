def distance(point1, point2, point):
    return abs((point[1] - point1[1]) * (point2[0] - point1[0]) - (point2[1] - point1[1]) * (point[0] - point1[0]))

def quickhull_rec(points, point1, point2):
    if not points:
        return []
    
    max_point = max(points, key=lambda point: distance(point1, point2, point))
    points_left = [p for p in points if orientation(point1, max_point, p) == -1]
    points_right = [p for p in points if orientation(max_point, point2, p) == -1]
    
    return quickhull_rec(points_left, point1, max_point) + [max_point] + quickhull_rec(points_right, max_point, point2)

def quickhull(points):
    leftmost_point = min(points)
    rightmost_point = max(points)
    points_left = [p for p in points if orientation(leftmost_point, rightmost_point, p) == -1]
    points_right = [p for p in points if orientation(rightmost_point, leftmost_point, p) == -1]
    
    return [leftmost_point] + quickhull_rec(points_left, leftmost_point, rightmost_point) + [rightmost_point] + quickhull_rec(points_right, rightmost_point, leftmost_point)

# Υπολογισμός του κυρτού περιβλήματος με τον αλγόριθμο QuickHull
hull_points = quickhull(points)

# Οπτικοποίηση
plt.scatter(*zip(*points))
plt.plot(*zip(*(hull_points + [hull_points[0]])), 'r')
plt.show()
