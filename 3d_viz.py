import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.cm as cm

# ===== إعداد الستايل =====
plt.style.use('dark_background')

fig = plt.figure(figsize=(18, 12))
fig.suptitle('تصورات 3D بمكتبة Matplotlib', fontsize=16, color='#B87333', y=0.98)

# ===== 1. سطح موجي 3D =====
ax1 = fig.add_subplot(231, projection='3d')
X = np.linspace(-5, 5, 60)
Y = np.linspace(-5, 5, 60)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

surf = ax1.plot_surface(X, Y, Z, cmap='copper', alpha=0.9, linewidth=0)
ax1.set_title('سطح موجي', color='#EFE6DC', pad=10)
ax1.set_xlabel('X', color='#B87333')
ax1.set_ylabel('Y', color='#B87333')
ax1.set_zlabel('Z', color='#B87333')
ax1.tick_params(colors='gray', labelsize=7)
fig.colorbar(surf, ax=ax1, shrink=0.5, aspect=10)

# ===== 2. مبعثر 3D =====
ax2 = fig.add_subplot(232, projection='3d')
n = 200
x = np.random.randn(n)
y = np.random.randn(n)
z = np.random.randn(n)
colors = np.sqrt(x**2 + y**2 + z**2)

sc = ax2.scatter(x, y, z, c=colors, cmap='YlOrBr', s=40, alpha=0.8)
ax2.set_title('مخطط مبعثر 3D', color='#EFE6DC', pad=10)
ax2.set_xlabel('X', color='#B87333')
ax2.set_ylabel('Y', color='#B87333')
ax2.set_zlabel('Z', color='#B87333')
ax2.tick_params(colors='gray', labelsize=7)
fig.colorbar(sc, ax=ax2, shrink=0.5, aspect=10)

# ===== 3. أعمدة 3D =====
ax3 = fig.add_subplot(233, projection='3d')
categories = ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو']
products = ['منتج A', 'منتج B', 'منتج C']
data = np.array([
    [120, 85, 200, 150, 180, 220],
    [90,  110, 130, 170, 140, 190],
    [60,  75,  95,  110, 125, 160],
])

colors_bar = ['#6B4F3A', '#B87333', '#EFE6DC']
xpos = np.arange(len(categories))
for i, (row, color) in enumerate(zip(data, colors_bar)):
    ax3.bar(xpos, row, zs=i, zdir='y', color=color, alpha=0.85, width=0.6)

ax3.set_title('مبيعات المنتجات', color='#EFE6DC', pad=10)
ax3.set_xticks(xpos)
ax3.set_xticklabels(categories, rotation=30, fontsize=7, color='gray')
ax3.set_yticks([0, 1, 2])
ax3.set_yticklabels(products, fontsize=7, color='gray')
ax3.set_zlabel('المبيعات', color='#B87333', fontsize=8)
ax3.tick_params(colors='gray', labelsize=7)

# ===== 4. سطح كوني 3D =====
ax4 = fig.add_subplot(234, projection='3d')
u = np.linspace(0, 2 * np.pi, 60)
v = np.linspace(0, np.pi, 60)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

ax4.plot_surface(x, y, z, cmap='copper', alpha=0.85, linewidth=0)
ax4.set_title('كرة ثلاثية الأبعاد', color='#EFE6DC', pad=10)
ax4.tick_params(colors='gray', labelsize=7)

# ===== 5. منحنى 3D =====
ax5 = fig.add_subplot(235, projection='3d')
t = np.linspace(0, 4 * np.pi, 300)
x = np.sin(t) * (1 + 0.5 * np.cos(8*t))
y = np.cos(t) * (1 + 0.5 * np.cos(8*t))
z = t / (4 * np.pi)

points = np.array([x, y, z]).T.reshape(-1, 1, 3)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
colors_line = cm.copper(np.linspace(0, 1, len(segments)))

for seg, col in zip(segments, colors_line):
    ax5.plot(seg[:, 0], seg[:, 1], seg[:, 2], color=col, linewidth=1.5)

ax5.set_title('منحنى لولبي', color='#EFE6DC', pad=10)
ax5.tick_params(colors='gray', labelsize=7)

# ===== 6. سطح متموج =====
ax6 = fig.add_subplot(236, projection='3d')
X2 = np.linspace(-3, 3, 50)
Y2 = np.linspace(-3, 3, 50)
X2, Y2 = np.meshgrid(X2, Y2)
Z2 = X2 * np.exp(-X2**2 - Y2**2)

ax6.plot_surface(X2, Y2, Z2, cmap='YlOrBr', alpha=0.9, linewidth=0)
ax6.contourf(X2, Y2, Z2, zdir='z', offset=Z2.min()-0.2, cmap='copper', alpha=0.4)
ax6.set_title('سطح متموج مع ظل', color='#EFE6DC', pad=10)
ax6.tick_params(colors='gray', labelsize=7)

plt.tight_layout(pad=2)
plt.savefig('/mnt/user-data/outputs/3d_visualizations.png', dpi=150, bbox_inches='tight',
            facecolor='#1a0f0a', edgecolor='none')
print("✅ تم الحفظ!")
