def jarvis_march(points):
    n = len(points)
    if n < 3:
        return points
    
    leftmost_point = min(points)
    hull = []
    p = leftmost_point
    
    while True:
        hull.append(p)
        q = points[0]
        for r in points:
            if orientation(p, q, r) == -1:
                q = r
        p = q
        if p == leftmost_point:
            break
    
    return hull

# Υπολογισμός του κυρτού περιβλήματος με τον αλγόριθμο του περιτυλίγματος
hull_points = jarvis_march(points)

# Οπτικοποίηση
plt.scatter(*zip(*points))
plt.plot(*zip(*(hull_points + [hull_points[0]])), 'r')
plt.show()
