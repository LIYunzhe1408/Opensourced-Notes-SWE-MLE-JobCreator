import numpy as np
from questionC import computeRotationMatrix

def computeAxisAndAngle(R):
    skew_symmetric = R - R.T
    
    sin_phi = np.linalg.norm(skew_symmetric) / 2
    cos_phi = (np.trace(R) - 1) / 2
    
    phi = np.arctan2(sin_phi, cos_phi)
    
    # Extract the axis of rotation
    s = np.array([
        skew_symmetric[2, 1],
        skew_symmetric[0, 2],
        skew_symmetric[1, 0]
    ]) 

    # Normalize
    s = s / (2 * sin_phi)  
    return s, phi


phi = np.pi / 4
s = np.array([1, 1, 1]) / np.sqrt(3)
R = computeRotationMatrix(s, phi) 
recovered_s, recovered_phi = computeAxisAndAngle(R)

print("Original Axis of Rotation (s):", s)
print("Recovered Axis of Rotation (s):", recovered_s)
print("Original Rotation Angle (phi):", phi)
print("Recovered Rotation Angle (phi):", recovered_phi)


