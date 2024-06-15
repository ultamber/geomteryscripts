from scipy.spatial import ConvexHull

# Δημιουργία τυχαίων σημείων στον χώρο R3
points_3d = np.random.rand(85, 3)

# Υπολογισμός του κυρτού περιβλήματος
hull = ConvexHull(points_3d)

# Οπτικοποίηση
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(points_3d[:,0], points_3d[:,1], points_3d[:,2])
for simplex in hull.simplices:
    ax.plot(points_3d[simplex, 0], points_3d[simplex, 1], points_3d[simplex, 2], 'r-')

plt.show()
