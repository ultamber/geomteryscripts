import matplotlib.pyplot as plt
import numpy as np
import random

# Λειτουργία που βρίσκει τον προσανατολισμό τριών σημείων
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return -1

# Αυξητικός αλγόριθμος για το κυρτό περίβλημα
def incremental_convex_hull(points):
    points = sorted(points)
    upper_hull = []
    lower_hull = []
    
    for p in points:
        while len(upper_hull) >= 2 and orientation(upper_hull[-2], upper_hull[-1], p) != -1:
            upper_hull.pop()
        upper_hull.append(p)
    
    for p in reversed(points):
        while len(lower_hull) >= 2 and orientation(lower_hull[-2], lower_hull[-1], p) != -1:
            lower_hull.pop()
        lower_hull.append(p)
    
    del upper_hull[-1]
    del lower_hull[-1]
    
    return upper_hull + lower_hull

# Δημιουργία τυχαίων σημείων στο επίπεδο
random.seed(42)
points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(100)]

# Υπολογισμός του κυρτού περιβλήματος
hull_points = incremental_convex_hull(points)

# Οπτικοποίηση
plt.scatter(*zip(*points))
plt.plot(*zip(*(hull_points + [hull_points[0]])), 'r')
plt.show()
