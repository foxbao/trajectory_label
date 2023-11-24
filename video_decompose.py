import cv2
import os
from datetime import datetime, timedelta

def decompose_video(video_path, output_folder, initial_timestamp_str):
    # Convert the initial timestamp string to a datetime object
    initial_timestamp = datetime.strptime(initial_timestamp_str, "%Y%m%d%H%M%S")

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Get the frames per second (fps) of the video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Iterate over each frame and save it with the renamed timestamp
    for i in range(total_frames):
        # Read the frame
        ret, frame = cap.read()

        if not ret:
            break  # Break the loop if there are no more frames

        # Calculate the elapsed time from the initial timestamp
        elapsed_time = timedelta(seconds=i / fps)
        current_timestamp = initial_timestamp + elapsed_time

        # Format the timestamp as a string
        timestamp_str = current_timestamp.strftime("%Y%m%d%H%M%S%f")[:-3]  # Remove microseconds

        # Save the frame as an image file with timestamp
        frame_filename = os.path.join(output_folder, f"{timestamp_str}.jpg")
        cv2.imwrite(frame_filename, frame)

    # Release the video capture object
    cap.release()

    print(f"Decomposed video into {total_frames} frames. Images saved in {output_folder}.")

if __name__ == "__main__":
    # Specify the path to the video file
    video_path = "video_data/video.mp4"

    # Specify the output folder for images
    output_folder = "output_images"

    # Specify the initial timestamp string (format: %Y%m%d%H%M%S)
    initial_timestamp_str = "20230101120000"  # Example: January 1, 2023, 12:00:00

    # Decompose the video into images with timestamps
    decompose_video(video_path, output_folder, initial_timestamp_str)
