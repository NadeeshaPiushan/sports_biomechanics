import cv2
import mediapipe as mp
import pandas as pd

# Initialize MediaPipe Pose.
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Initialize drawing utility.
mp_drawing = mp.solutions.drawing_utils

def process_video(video_path, output_video_path, output_data_path):
    # Open the video file.
    cap = cv2.VideoCapture(video_path)

    # Get video properties.
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Initialize video writer for output.
    out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))
    
    # List to store pose data.
    pose_data = []

    # Process video frame by frame.
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert the frame to RGB as MediaPipe expects RGB input.
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Perform pose estimation.
        results = pose.process(rgb_frame)

        # Draw pose landmarks and connections.
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )
            
            # Extract landmark data and store in pose_data.
            landmarks = results.pose_landmarks.landmark
            frame_data = {
                'frame': int(cap.get(cv2.CAP_PROP_POS_FRAMES)),
                'landmarks': {f'landmark_{i}': (lm.x, lm.y, lm.z) for i, lm in enumerate(landmarks)}
            }
            pose_data.append(frame_data)
        
        # Write the processed frame to the output video.
        out.write(frame)

        # Display the video (optional).
        cv2.imshow('Pose Estimation', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources.
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # Save pose data to a CSV file.
    df = pd.DataFrame(pose_data)
    df.to_csv(output_data_path, index=False)


