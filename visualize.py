import matplotlib.animation as animation

fig, ax = plt.subplots()
scat = ax.scatter(*zip(*points))

line, = ax.plot([], [], 'r')

def update_quickhull(frame):
    leftmost_point = min(points)
    rightmost_point = max(points)
    hull = [leftmost_point]
    points_left = [p for p in points if orientation(leftmost_point, rightmost_point, p) == -1]
    points_right = [p for p in points if orientation(rightmost_point, leftmost_point, p) == -1]
    
    left_hull = quickhull_rec(points_left, leftmost_point, rightmost_point)
    right_hull = quickhull_rec(points_right, rightmost_point, leftmost_point)
    
    hull += left_hull + [rightmost_point] + right_hull
    hull.append(leftmost_point)
    
    line.set_data(zip(*hull))
    return line,

ani = animation.FuncAnimation(fig, update_quickhull, frames=range(1), interval=1000, blit=True)
plt.show()
