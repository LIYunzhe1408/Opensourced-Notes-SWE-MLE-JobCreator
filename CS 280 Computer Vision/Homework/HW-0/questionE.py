import numpy as np

def findBestTransformation(u, v):
    u_mean, v_mean = np.mean(u, axis=0), np.mean(v, axis=0)
    u_centered, v_centered = u - u_mean, v - v_mean
    
    covariance_matrix = np.dot(u_centered.T, v_centered)
    
    U, S, Vt = np.linalg.svd(covariance_matrix)
    
    R = np.dot(Vt.T, U.T)
    t = v_mean - np.dot(R, u_mean)
    return R, t

# Test
u = np.array([[-3, 0], [1, 1], [1, 0], [1, -1]])
v = np.array([[0, 3], [1, 0], [0, 0], [-1, 0]])

R, t = findBestTransformation(u, v)


print("Optimal Rotation Matrix (R):")
print(R, '\n')
print("Optimal Translation Vector (t):")
print(t, '\n')

# Verify the transformation
u_transformed = np.dot(u, R.T) + t
print("Transformed Points:")
print(u_transformed, '\n')
print("Target Points:")
print(v)
