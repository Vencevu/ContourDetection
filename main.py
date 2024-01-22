import numpy as np
from stl import mesh

obj = mesh.Mesh.from_file('data/mesh.stl')

points = np.around(np.unique(obj.vectors.reshape([int(obj.vectors.size/3), 3]), axis=0),2)
print(points.tolist())
