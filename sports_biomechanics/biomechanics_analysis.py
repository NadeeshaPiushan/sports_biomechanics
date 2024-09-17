import numpy as np

def calculate_joint_angle(landmark1, landmark2, landmark3):
    """
    Calculate the angle between three landmarks using the cosine rule.
    """
    # Get the vectors between the landmarks.
    vector1 = np.array(landmark1) - np.array(landmark2)
    vector2 = np.array(landmark3) - np.array(landmark2)

    # Calculate the dot product and magnitudes.
    dot_product = np.dot(vector1, vector2)
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)

    # Calculate the angle in radians and convert to degrees.
    angle = np.arccos(dot_product / (magnitude1 * magnitude2))
    return np.degrees(angle)

def analyze_pose_data(pose_data):
    """
    Analyze pose landmarks to extract biomechanical data like joint angles.
    """
    biomechanical_data = []
    
    for frame_data in pose_data:
        frame = frame_data['frame']
        landmarks = frame_data['landmarks']
        
        # Calculate joint angles (example: elbow joint).
        if 'landmark_11' in landmarks and 'landmark_13' in landmarks and 'landmark_15' in landmarks:
            elbow_angle = calculate_joint_angle(
                landmarks['landmark_11'],  # Shoulder
                landmarks['landmark_13'],  # Elbow
                landmarks['landmark_15']   # Wrist
            )
            
            # Store biomechanical data.
            biomechanical_data.append({
                'frame': frame,
                'elbow_angle': elbow_angle
            })
    
    return biomechanical_data

