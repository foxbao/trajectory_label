import cv2
import numpy as np
import matplotlib.pyplot as plt

def generate_sample_data():
    # Generate 25 random point pairs for demonstration
    np.random.seed(42)
    points_src = np.random.rand(25, 2) * 100  # Source points
    homography_matrix = np.array([[2, 0.5, 30], [0.1, 1.5, 20], [0.001, 0.002, 1]])  # Homography matrix
    points_dst = cv2.perspectiveTransform(points_src.reshape(-1, 1, 2), homography_matrix)[:, 0, :]

    return points_src, points_dst

def homography_transform(points_src, points_dst):
    # Find homography matrix using OpenCV
    homography_matrix, _ = cv2.findHomography(points_src, points_dst)

    return homography_matrix

def apply_homography_transform(points_src, homography_matrix):
    # Apply homography transformation
    points_transformed = cv2.perspectiveTransform(points_src.reshape(-1, 1, 2), homography_matrix)[:, 0, :]

    return points_transformed

def main():
    # Generate sample data
    points_src, points_dst = generate_sample_data()

    # Find homography matrix
    homography_matrix = homography_transform(points_src, points_dst)

    # Apply homography transformation to the source points
    points_transformed = apply_homography_transform(points_src, homography_matrix)

    # Display the results
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.scatter(points_src[:, 0], points_src[:, 1], c='r', marker='o', label='Source Points')
    plt.scatter(points_dst[:, 0], points_dst[:, 1], c='b', marker='x', label='Destination Points')
    plt.title('Original Points')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.scatter(points_src[:, 0], points_src[:, 1], c='r', marker='o', label='Source Points')
    plt.scatter(points_transformed[:, 0], points_transformed[:, 1], c='g', marker='s', label='Transformed Points')
    plt.title('Homography Transformed Points')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
