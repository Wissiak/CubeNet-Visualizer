import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

os.makedirs("dataset/train/images", exist_ok=True)
os.makedirs("dataset/train/labels", exist_ok=True)
os.makedirs("dataset/val/images", exist_ok=True)
os.makedirs("dataset/val/labels", exist_ok=True)

# points in world coordinates
pts1_w = np.array([
    [0, 4, 0.1], # 0
    [0, 3, 0.1], # 1
    [1, 3, 0.1], # 2
    [1, 0, 0.1], # 3
    [2, 0, 0.1], # 4
    [2, 1, 0.1], # 5
    [3, 1, 0.1], # 6
    [3, 2, 0.1], # 7
    [2, 2, 0.1], # 8
    [2, 4, 0.1], # 9
])
pts2_w = np.array([
    [0, 4, 0.1], # 0
    [0, 3, 0.1], # 1
    [1, 3, 0.1], # 2
    [1, 0, 0.1], # 3
    [2, 0, 0.1], # 4
    [2, 2, 0.1], # 5
    [3, 2, 0.1], # 6
    [3, 3, 0.1], # 7
    [2, 3, 0.1], # 8
    [2, 4, 0.1], # 9
])
pts3_w = np.array([
    [0, 4, 0.1], # 0
    [0, 3, 0.1], # 1
    [1, 3, 0.1], # 2
    [1, 0, 0.1], # 3
    [3, 0, 0.1], # 4
    [3, 1, 0.1], # 5
    [2, 1, 0.1], # 6
    [2, 4, 0.1], # 7
])
pts4_w = np.array([
    [0, 4, 0.1], # 0
    [0, 3, 0.1], # 1
    [1, 3, 0.1], # 2
    [1, 1, 0.1], # 3
    [2, 1, 0.1], # 4
    [2, 0, 0.1], # 5
    [3, 0, 0.1], # 6
    [3, 2, 0.1], # 7
    [2, 2, 0.1], # 8
    [2, 4, 0.1], # 9
])
pts5_w = np.array([
    [0, 4, 0.1], # 0
    [0, 3, 0.1], # 1
    [1, 3, 0.1], # 2
    [1, 0, 0.1], # 3
    [2, 0, 0.1], # 4
    [2, 3, 0.1], # 5
    [3, 3, 0.1], # 6
    [3, 4, 0.1], # 7
])
pts6_w = np.array([
    [1, 4, 0.1], # 0
    [1, 2, 0.1], # 1
    [0, 2, 0.1], # 2
    [0, 1, 0.1], # 3
    [1, 1, 0.1], # 4
    [1, 0, 0.1], # 5
    [2, 0, 0.1], # 6
    [2, 2, 0.1], # 7
    [3, 2, 0.1], # 8
    [3, 3, 0.1], # 9
    [2, 3, 0.1], # 10
    [2, 4, 0.1], # 11
])
pts7_w = np.array([
    [0, 0, 0.1], # 0
    [2, 0, 0.1], # 1
    [2, 1, 0.1], # 2
    [3, 1, 0.1], # 3
    [3, 2, 0.1], # 4
    [4, 2, 0.1], # 5
    [4, 3, 0.1], # 6
    [2, 3, 0.1], # 7
    [2, 2, 0.1], # 8
    [1, 2, 0.1], # 9
    [1, 1, 0.1], # 10
    [0, 1, 0.1], # 11
])
pts8_w = np.array([
    [1, 4, 0.1], # 0
    [1, 3, 0.1], # 1
    [0, 3, 0.1], # 2
    [0, 2, 0.1], # 3
    [1, 2, 0.1], # 4
    [1, 0, 0.1], # 5
    [2, 0, 0.1], # 6
    [2, 2, 0.1], # 7
    [3, 2, 0.1], # 8
    [3, 3, 0.1], # 9
    [2, 3, 0.1], # 10
    [2, 4, 0.1], # 11
])
pts9_w = np.array([
    [0, 3, 0.1], # 0
    [0, 2, 0.1], # 1
    [1, 2, 0.1], # 2
    [1, 0, 0.1], # 3
    [2, 0, 0.1], # 4
    [2, 2, 0.1], # 5
    [3, 2, 0.1], # 6
    [3, 4, 0.1], # 7
    [2, 4, 0.1], # 8
    [2, 3, 0.1], # 9
])
pts10_w = np.array([
    [0, 2, 0.1], # 0
    [0, 0, 0.1], # 1
    [1, 0, 0.1], # 2
    [1, 1, 0.1], # 3
    [2, 1, 0.1], # 4
    [2, 2, 0.1], # 5
    [3, 2, 0.1], # 6
    [3, 3, 0.1], # 7
    [2, 3, 0.1], # 8
    [2, 4, 0.1], # 9
    [1, 4, 0.1], # 9
    [1, 2, 0.1], # 10
])
pts11_w = np.array([
    [0, 3, 0.1], # 0
    [0, 0, 0.1], # 1
    [1, 0, 0.1], # 2
    [1, 2, 0.1], # 3
    [2, 2, 0.1], # 4
    [2, 5, 0.1], # 5
    [1, 5, 0.1], # 6
    [1, 3, 0.1], # 7
])


from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

hide_grid = True
show_3d = False
images_per_class = 500
my_dpi = 96

f = 80  # Focal length
cx, cy = 320, 320  # Center of projection

def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

def find_line_params(p1, p2):
    """Calculates the slope (m) and y-intercept (c) of the line passing through points p1 and p2."""
    if p2[0] - p1[0] == 0:  # To handle vertical lines
        return None, p1[0]  # Returning None for slope indicates a vertical line, and x-value for the intercept
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = p1[1] - m * p1[0]
    return m, c

def line_intersection(m1, c1, m2, c2):
    """Finds the intersection point of two lines given their slopes (m1, m2) and y-intercepts (c1, c2)."""
    if m1 is None:  # First line is vertical
        if m2 is None:  # Both lines are vertical
            return None
        x = c1
        y = m2 * x + c2
        return np.array([x, y])
    if m2 is None:  # Second line is vertical
        x = c2
        y = m1 * x + c1
        return np.array([x, y])
    if m1 == m2:  # Parallel lines
        return None  # No intersection
    x = (c2 - c1) / (m1 - m2)
    y = m1 * x + c1
    return np.array([x, y])

def find_extreme_points(pts, find_max=True):
    curr_val = -1
    curr_idx = -1
    for i in range(-1, len(pts)-1):
        pt0 = pts[i]
        pt1 = pts[i+1]
        sum = pt0 + pt1
        if find_max:
            if sum > curr_val:
                curr_val = sum
                curr_idx = i
        else:
            if sum < curr_val or curr_val == -1:
                curr_val = sum
                curr_idx = i
    return curr_idx, curr_idx + 1


def oriented_bounding_box(pts):

    idx0, idx1 = find_extreme_points(pts[:,0], find_max=True)
    top_points = [pts[idx0], pts[idx1]]
    idx0, idx1 = find_extreme_points(pts[:,0], find_max=False)
    bottom_points = [pts[idx0], pts[idx1]]

    idx0, idx1 = find_extreme_points(pts[:,1], find_max=True)
    right_points = [pts[idx0], pts[idx1]]
    idx0, idx1 = find_extreme_points(pts[:,1], find_max=False)
    left_points = [pts[idx0], pts[idx1]]

    #return left_points[0], right_points[0], right_points[1], left_points[1]

    bottom_line_params = find_line_params(bottom_points[0], bottom_points[1])
    top_line_params = find_line_params(top_points[0], top_points[1])
    right_line_params = find_line_params(right_points[0], right_points[1])
    left_line_params = find_line_params(left_points[0], left_points[1])

    # Calculate intersections (example for bottom and right vectors)
    intersection_br = line_intersection(*bottom_line_params, *right_line_params)
    intersection_tr = line_intersection(*top_line_params, *right_line_params)
    intersection_tl = line_intersection(*top_line_params, *left_line_params)
    intersection_bl = line_intersection(*bottom_line_params, *left_line_params)

    if intersection_bl is None or intersection_br is None or intersection_tr is None or intersection_tl is None:
        return None, None, None, None
    
    if np.allclose(intersection_bl, intersection_br) or np.allclose(intersection_br, intersection_tr) or np.allclose(intersection_tr, intersection_tl) or np.allclose(intersection_tl, intersection_bl):
        return None, None, None, None

    return intersection_br, intersection_tr, intersection_tl, intersection_bl


for j, points in enumerate([pts1_w, pts2_w, pts3_w, pts4_w, pts5_w, pts6_w, pts7_w, pts8_w, pts9_w, pts10_w, pts11_w]):
    generated_images = 0
    while generated_images < images_per_class:
        if show_3d:
            fig = plt.figure(figsize=(640/my_dpi, 640/my_dpi), dpi=my_dpi)
            ax = Axes3D(fig, auto_add_to_figure=False)
            if hide_grid:
                ax.grid(False)
                plt.axis('off') 
                ax.set_xticks([])
                ax.set_yticks([])
                ax.set_zticks([])
                # make the panes transparent
                ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
                ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
                ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
                # make the grid lines transparent
                ax.xaxis._axinfo["grid"]['color'] =  (1,1,1,0)
                ax.yaxis._axinfo["grid"]['color'] =  (1,1,1,0)
                ax.zaxis._axinfo["grid"]['color'] =  (1,1,1,0)
                ax.set_axis_off()
            else:
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_zlabel('z')
            ax.set_xlim(-10, 10)
            ax.set_ylim(-10, 10)
            ax.set_zlim(-10, 10)
            fig.add_axes(ax)


        # https://eecs.qmul.ac.uk/~gslabaugh/publications/euler.pdf
        theta = np.deg2rad(np.random.randint(0, 360))
        R_y = np.array([[np.cos(theta), 0, np.cos(theta)],
                        [0, 1, 0],
                        [-np.sin(theta), 0, np.cos(theta)]])
        
        phi = np.deg2rad(np.random.randint(0, 30))
        R_z = np.array([[np.cos(phi), -np.sin(phi), 0],
                        [np.sin(phi), np.cos(phi), 0],
                        [0, 0, 1]])

        psi = np.deg2rad(np.random.randint(0, 30))
        R_x = np.array([[1, 0, 0],
                        [0, np.cos(psi), -np.sin(psi)],
                        [0, np.sin(psi), np.cos(psi)]])


        pts_r = R_z @ points.T
        pts_r = R_y @ pts_r
        #pts_r = R_x @ pts_r
        pts_r = pts_r.T

        t_x = np.random.randint(-8, 8)
        t_y = np.random.randint(-8, 8)
        t_z = np.random.randint(-8, 8)
        pts_r[:,0] += t_x
        pts_r[:,1] += t_y
        pts_r[:,2] += t_z

        x = pts_r[:,0]
        y = pts_r[:,1]
        z = pts_r[:,2]
        color = np.random.rand(3,)
        if show_3d:
            verts = [list(zip(x,y,z))]
            ax.add_collection3d(Poly3DCollection(verts, facecolors=color))

        if z.max() - z.min() > 1.8:
            # larger values yield weird projections
            continue
        points_2d = np.zeros((pts_r.shape[0], 2))
        points_2d[:, 0] = (x * f / z) + cx
        points_2d[:, 1] = (y * f / z) + cy

        if PolyArea(points_2d[:,0], points_2d[:,1]) < 2000 or not all(points_2d[:,0] > 0) or not all(points_2d[:,0] < 640) or not all(points_2d[:,1] > 0) or not all(points_2d[:,1] < 640):
            # area must be large enough to be visible
            # all points must be within the image
            continue


        fig, ax = plt.subplots(figsize=(640/my_dpi, 640/my_dpi), dpi=my_dpi, frameon=True)
        polygon = Polygon(points_2d)
        p = PatchCollection([polygon], color=color, edgecolor='black', linewidth=1)
        ax.add_collection(p)
        ax.set_axis_off()
        br, tr, tl, bl = oriented_bounding_box(points_2d)
        if br is None or tr is None or tl is None or bl is None or all(br < 0) or all(tr < 0) or all(tl < 0) or all(bl < 0) or all(br > 640) or all(tr > 640) or all(tl > 640) or all(bl > 640):
            continue
        bbox = np.array([br, tr, tl, bl, br])
        print("-------------------")
        print(f"Class {j+1}, image {generated_images+1}")
        ax.plot(bbox[:,0], bbox[:,1], 'r-')
        plt.xlim(0, 640)
        plt.ylim(0, 640)
        plt.grid(False)
        #plt.show()
        generated_images += 1


        #plt.pause(0.01)
        plt.savefig(f"dataset/train/images/{j+1}-{generated_images}.png", dpi=my_dpi)
        plt.close()

        text = f"{j+1} {br[0]} {br[1]} {tr[0]} {tr[1]} {tl[0]} {tl[1]} {bl[0]} {bl[1]}"
        with open(f"dataset/train/labels/{j+1}-{generated_images}.txt", "w") as file:
            file.write(text)
