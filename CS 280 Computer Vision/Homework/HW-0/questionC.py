import numpy as np
from scipy.linalg import eig

def computeRotationMatrix(s, phi):
    s = s / np.linalg.norm(s)
    s1, s2, s3 = s
    I = np.eye(3)

    s_hat = np.array([
        [0, -s3, s2],
        [s3, 0, -s1],
        [-s2, s1, 0]
    ])
    
    # Rodriguez
    R = I + np.sin(phi) * s_hat + (1 - np.cos(phi)) * np.dot(s_hat, s_hat)
    return R


s = np.array([1, 1, 1])
phi = np.pi / 4 

# Compute orthogonal matrix
R = computeRotationMatrix(s, phi)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = eig(R)

# Verify cos(phi) = 1/2 * (trace(R) - 1)
cos_phi = 0.5 * (np.trace(R) - 1)

# Test points before and after rotation
points = np.array([
    [1, 0, 0],  # Along x-axis
    [0, 1, 0],  # Along y-axis
    [0, 0, 1],  # Along z-axis
    [1, 1, 1],  # Along the rotation axis
    [1, -1, 0], # Diagonal in xy-plane
    [0, 1, -1], # Diagonal in yz-plane
    [-1, 0, 1], # Diagonal in xz-plane
    [1, 2, 3],  # Arbitrary point
    [-2, -1, 0] # Arbitrary point
])
rotated_points = np.dot(R, points.T).T

# Results
print("Rotation Matrix R:")
print(R,'\n')
print("Eigenvalues:")
print(eigenvalues,'\n')
print("Eigenvectors:")
print(eigenvectors,'\n')
print(f"1/2(trace(R)-1): {cos_phi}, cos(phi): {np.cos(phi)} \n")
print("Points before rotation:")
print(points, '\n')
print("Points after rotation:")
print(rotated_points)
