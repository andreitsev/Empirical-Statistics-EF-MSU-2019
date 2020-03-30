import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


N = 200
granz_x = (-2, 2)
granz_y = (-2, 2)
granz_z = (-20, 15)
x = np.array(np.random.uniform(-2, 2, size=N).tolist())
y = np.array(np.random.uniform(-2, 2, size=N).tolist())
z = 3*x - 5*y
def z_func(x, y): 
    return 3*x - 5*y
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='3d')
point_x, point_y = -1, 1.5
point = np.array([point_x, point_y, 3*point_x - 5*point_y]) 

def draw_3dpoint(point, ax, draw_coords=True, color='orange'):
    ax.scatter(point[0], point[1], point[2], color=color, s=60)
    begin = [point[0], granz_y[1], granz_z[0]]
    end = [point[0], point[1], granz_z[0]]
    ax.quiver(begin[0], begin[1], begin[2], end[0] - begin[0], end[1] - begin[1], end[2] - begin[2], 
              color = 'red', alpha = .8, lw = 1, arrow_length_ratio=0.0, ls='--')
    begin = [granz_x[1], point[1], granz_z[0]]
    end = [point[0], point[1], granz_z[0]]
    ax.quiver(begin[0], begin[1], begin[2], end[0] - begin[0], end[1] - begin[1], end[2] - begin[2], 
              color = 'red', alpha = .8, lw = 1, arrow_length_ratio=0.0, ls='--')
    begin = [point[0], point[1], granz_z[0]]
    end = [point[0], point[1], point[2]]
    ax.quiver(begin[0], begin[1], begin[2], end[0] - begin[0], end[1] - begin[1], end[2] - begin[2], 
              color = 'red', alpha = .8, lw = 1, arrow_length_ratio=0.0, ls='--')
    if draw_coords:
        ax.text(point[0]+0.05, point[1]+0.05, point[2]-0.05, f'({np.round(point[0], decimals=2)}, {np.round(point[1], decimals=2)}, {np.round(point[2], decimals=2)})', size=15)

def draw_lincomb(vec1, vec2, ax, alpha1=1, alpha2=2, color='orange'):
    begin = [0, 0, 0]
    ax.quiver(begin[0], begin[1], begin[2], vec1[0] - begin[0], vec1[1] - begin[1], vec1[2] - begin[2], 
              color = 'black', alpha = .8, lw = 2, arrow_length_ratio=0.1, ls='-')
    ax.quiver(begin[0], begin[1], begin[2], vec2[0] - begin[0], vec2[1] - begin[1], vec2[2] - begin[2], 
              color = 'black', alpha = .8, lw = 2, arrow_length_ratio=0.1, ls='-')

    ax.quiver(begin[0], begin[1], begin[2], alpha1*vec1[0] - begin[0], alpha1*vec1[1] - begin[1], 
              alpha1*vec1[2] - begin[2], color = 'red', alpha = .8, lw = 1, arrow_length_ratio=0.05, ls='--')
    ax.quiver(begin[0], begin[1], begin[2], alpha2*vec2[0] - begin[0], alpha2*vec2[1] - begin[1], 
              alpha2*vec2[2] - begin[2], color = 'red', alpha = .8, lw = 1, arrow_length_ratio=0.05, ls='--')

    begin = alpha2*vec2
    end = alpha1*vec1 + alpha2*vec2
    ax.quiver(begin[0], begin[1], begin[2], end[0] - begin[0], end[1] - begin[1], 
              end[2] - begin[2], color = 'red', alpha = .8, lw = 1, arrow_length_ratio=0.05, ls='--')

    begin = alpha1*vec1
    end = alpha1*vec1 + alpha2*vec2
    ax.quiver(begin[0], begin[1], begin[2], end[0] - begin[0], end[1] - begin[1], 
              end[2] - begin[2], color = 'red', alpha = .8, lw = 1, arrow_length_ratio=0.05, ls='--')
    draw_3dpoint(alpha1*vec1, ax=ax, draw_coords=False)
    draw_3dpoint(alpha2*vec2, ax=ax, draw_coords=False)
    draw_3dpoint(alpha1*vec1 + alpha2*vec2, ax=ax, draw_coords=True, color=color)

def draw_plane(granz_x, granz_y, granz_z, z_func, ax):
    begin, end = [granz_x[1]-0.5, granz_y[0], z_func(granz_x[1]-0.5, granz_y[0])], \
    [granz_x[1]-0.5, granz_y[1], z_func(granz_x[1]-0.5, granz_y[1])]
    ax.quiver(begin[0], begin[1], begin[2], end[0] - begin[0], end[1] - begin[1], 
                  end[2] - begin[2], color = 'black', alpha = .8, lw = 1, arrow_length_ratio=0, ls='-')

    begin, end = [granz_x[0]-0.5, granz_y[0], z_func(granz_x[0]-0.5, granz_y[0])], \
    [granz_x[0]-0.5, granz_y[1], z_func(granz_x[0]-0.5, granz_y[1])]
    ax.quiver(begin[0], begin[1], begin[2], end[0] - begin[0], end[1] - begin[1], 
                  end[2] - begin[2], color = 'black', alpha = .8, lw = 1, arrow_length_ratio=0, ls='-')

    begin, end = [granz_x[1]-0.5, granz_y[0], z_func(granz_x[1]-0.5, granz_y[0])], \
    [granz_x[0]-0.5, granz_y[0], z_func(granz_x[0]-0.5, granz_y[0])]
    ax.quiver(begin[0], begin[1], begin[2], end[0] - begin[0], end[1] - begin[1], 
                  end[2] - begin[2], color = 'black', alpha = .8, lw = 1, arrow_length_ratio=0, ls='-')

    begin, end = [granz_x[1]-0.5, granz_y[1], z_func(granz_x[1]-0.5, granz_y[1])], \
    [granz_x[0]-0.5, granz_y[1], z_func(granz_x[0]-0.5, granz_y[1])]
    ax.quiver(begin[0], begin[1], begin[2], end[0] - begin[0], end[1] - begin[1], 
                  end[2] - begin[2], color = 'black', alpha = .8, lw = 1, arrow_length_ratio=0, ls='-')


   
def draw_final_plot():
    N = 200
    granz_x = (-2, 2)
    granz_y = (-2, 2)
    granz_z = (-20, 15)
    x = np.array(np.random.uniform(-2, 2, size=N).tolist())
    y = np.array(np.random.uniform(-2, 2, size=N).tolist())
    z = 3*x - 5*y
    def z_func(x, y): 
        return 3*x - 5*y
    fig = plt.figure(figsize=(12, 12))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, color='blue')
    point_x, point_y = -1, 1.5
    point = np.array([point_x, point_y, 3*point_x - 5*point_y]) 
    draw_3dpoint(point=point, ax=ax, color='black')
    draw_3dpoint(point=[0, 0, 0], ax=ax, draw_coords=False, color='red')

    # Рисуем базис плоскости
    vec1 = np.array([0, 1, -5])
    vec2 = np.array([-1, 0, -3])
    vec1 = 2*vec1/np.linalg.norm(vec1)
    vec2 = 2*vec2/np.linalg.norm(vec2)
    V = np.c_[vec1, vec2]
    alpha1, alpha2 = np.linalg.inv(V.T@V)@V.T@point
    draw_lincomb(vec1=vec1, vec2=vec2, ax=ax, alpha1=alpha1, alpha2=alpha2)

    # Рисуем плоскость
    draw_plane(granz_x=granz_x, granz_y=granz_y, granz_z=granz_z, z_func=z_func, ax=ax)

    ax.view_init(30, 40)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_xlim(granz_x[0], granz_x[1])
    ax.set_ylim(granz_y[0], granz_y[1])
    ax.set_zlim(granz_z[0], granz_z[1]);
    
