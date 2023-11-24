import numpy as np

def transform_to_pixel_coordinates(pos_cam, intriMatrix):
    # Convert 3D point to homogeneous coordinates
    pos_homogeneous = np.append(pos_cam, 1)
    pos_homogeneous=pos_cam
    # pos_homogeneous=pos_cam/pos_cam[2]
    # Perform the transformation
    pixel_coordinates_homogeneous = np.dot(intriMatrix, pos_homogeneous)

    # Convert back to Cartesian coordinates
    pixel_coordinates = pixel_coordinates_homogeneous[:2] / pixel_coordinates_homogeneous[2]

    return pixel_coordinates

# Example usage:
# Define the 3D position point in camera coordinates
pos_cam = np.array([2, 3, 5])

# Define the intrinsic matrix
intriMatrix = np.array([[800, 0, 0],
                        [0, 800, 0],
                        [0, 0, 1]])

# Transform the 3D point to pixel coordinates
pixel_coordinates = transform_to_pixel_coordinates(pos_cam, intriMatrix)

# Display the result
print("3D Point in Camera Coordinates:", pos_cam)
print("Intrinsic Matrix:")
print(intriMatrix)
print("Pixel Coordinates:", pixel_coordinates)
