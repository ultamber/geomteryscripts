def merge_hulls(left, right):
    # Merge logic for left and right hulls
    return left + right

def divide_and_conquer(points):
    if len(points) <= 3:
        return sorted(points)
    
    mid = len(points) // 2
    left_hull = divide_and_conquer(points[:mid])
    right_hull = divide_and_conquer(points[mid:])
    
    return merge_hulls(left_hull, right_hull)

# Υπολογισμός του κυρτού περιβλήματος με τον αλγόριθμο Διαίρει και Βασίλευε
points = sorted(points)
hull_points = divide_and_conquer(points)

# Οπτικοποίηση
plt.scatter(*zip(*points))
plt.plot(*zip(*(hull_points + [hull_points[0]])), 'r')
plt.show()
