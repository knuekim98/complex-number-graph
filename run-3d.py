import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import mpl_toolkits
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import math
import cmath

# equation input
inp = input('put equation by list of coefficient(e.g. 2,1,2): ')
inp.replace(' ', '')
c = list(map(float, inp.split(',')))
eq = np.poly1d(c, False)

# ReX, ImX 축 설정
x1 = np.arange(-2,1,0.05)
x2 = np.arange(-2,2,0.05)

# grid
ReX, ImX = np.meshgrid(x1, x2)

# 연산
Y = ReX + ImX*1j
Y = np.polyval(eq, Y)

# 실수, 허수부 추출
ReY = Y.real
ImY = Y.imag
SizeY = np.sqrt(ReY**2 + ImY**2)

# graph mapping
fig = plt.figure()
ax = fig.gca(projection='3d') # 3d axes
surf = ax.plot_surface(ReX, ImX, SizeY, # 2d ndarray
                       rstride=2, # row step size
                       cstride=2, # column step size
                       cmap='inferno',
                       linewidth=1, # wireframe line width
                       antialiased=True)

# title
ax.set_title('Complex Number graph')
ax.set_xlabel('Re(x)')
ax.set_ylabel('Im(x)')
ax.set_zlabel('SizeY')

# colorbar
norm = colors.Normalize(vmin=SizeY.min(), vmax=SizeY.max())
sm = cm.ScalarMappable(cmap=surf.cmap, norm=norm)
sm.set_array([])
plt.colorbar(sm)

# elevation, angle
ax.view_init(elev=30,azim=70)

# distance
ax.dist=8

plt.show()