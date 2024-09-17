from pose_estimation import process_video
from biomechanics_analysis import analyze_pose_data
import pandas as pd

def main(video_path, output_video_path, output_data_path, biomechanical_data_path):
    # Step 1: Process video and extract pose landmarks.
    process_video(video_path, output_video_path, output_data_path)

    # Step 2: Load the pose data from CSV.
    pose_data = pd.read_csv(output_data_path)

    # Step 3: Perform biomechanical analysis (e.g., joint angles).
    biomechanical_data = analyze_pose_data(pose_data)

    # Step 4: Save biomechanical data to CSV.
    biomechanical_df = pd.DataFrame(biomechanical_data)
    biomechanical_df.to_csv(biomechanical_data_path, index=False)

if __name__ == "__main__":
    video_path = "input_video.mp4"
    output_video_path = "output_video_with_landmarks.mp4"
    output_data_path = "pose_landmarks.csv"
    biomechanical_data_path = "biomechanical_data.csv"
    
    main(video_path, output_video_path, output_data_path, biomechanical_data_path)

