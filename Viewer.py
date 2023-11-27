import matplotlib.pyplot as plt

class Viewer:
    def __init__(self) -> None:
        pass

    def visualize_enu_points_2d(self,enu_points):
        # Extract E and N coordinates from the list of points
        eastings, northings = zip(*enu_points)
        # Create a 2D scatter plot
        plt.scatter(eastings, northings, c='r', marker='o')

        # Set axis labels
        plt.xlabel('Eastings (m)')
        plt.ylabel('Northings (m)')

        # Set plot title
        plt.title('ENU Coordinates Visualization (2D)')

        # Display a grid for better visualization
        plt.grid(True)

        # Show the plot
        plt.show()

def main():
    # Example usage:
    enu_points = [(10, 20), (15, 25), (20, 30)]  # Replace with your ENU coordinates
    viewer=Viewer()
    viewer.visualize_enu_points_2d(enu_points)

if __name__ == "__main__":
    main()