import matplotlib.pyplot as plt
import numpy as np
import os

for i in range(1, 12):
    os.makedirs(f"dataset/{i}", exist_ok = True) 

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
images_per_class = 200
my_dpi = 96

for j, points in enumerate([pts1_w, pts2_w, pts3_w, pts4_w, pts5_w, pts6_w, pts7_w, pts8_w, pts9_w, pts10_w, pts11_w]):
    for i in range(images_per_class):
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
        phi = np.deg2rad(np.random.randint(0, 360))
        R_z = np.array([[np.cos(phi), -np.sin(phi), 0],
                        [np.sin(phi), np.cos(phi), 0],
                        [0, 0, 1]])

        if j != 10:
            theta = np.deg2rad(np.random.randint(-30, 30))
            R_y = np.array([[np.cos(theta), 0, np.cos(theta)],
                            [0, 1, 0],
                            [-np.sin(theta), 0, np.cos(theta)]])

            psi = np.deg2rad(np.random.randint(0, 30))
            R_x = np.array([[1, 0, 0],
                            [0, np.cos(psi), -np.sin(psi)],
                            [0, np.sin(psi), np.cos(psi)]])
        else:
            R_y = np.eye(3)
            R_x = np.eye(3)


        pts1_r = R_z @ points.T
        pts1_r = R_y @ pts1_r
        pts1_r = R_x @ pts1_r
        pts1_r = pts1_r.T

        t_x = np.random.randint(-8, 8)
        t_y = np.random.randint(-8, 8)
        t_z = np.random.randint(-8, 8)
        pts1_r[:,0] += t_x
        pts1_r[:,1] += t_y
        pts1_r[:,2] += t_z

        x = pts1_r[:,0]
        y = pts1_r[:,1]
        z = pts1_r[:,2]
        verts = [list(zip(x,y,z))]
        color = np.random.rand(3,)
        ax.add_collection3d(Poly3DCollection(verts, facecolors=color))

        plt.savefig(f"dataset/{j+1}/{i}.png", dpi=my_dpi)
        plt.close()
