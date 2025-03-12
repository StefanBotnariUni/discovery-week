import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1)

# Camera capture
cap = cv2.VideoCapture(1)

# Thresholds for yaw and pitch (in degrees)
YAW_THRESHOLD = 15  # Adjust based on sensitivity
PITCH_THRESHOLD = 10  # Adjust based on sensitivity
DEAD_ZONE = 5  # Range within which the head is considered "straight"

def get_head_direction():
    success, image = cap.read()
    if not success:
        return "Straight"

    # Convert image to RGB and process
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            h, w, _ = image.shape
            landmarks = face_landmarks.landmark

            # Extract key facial landmarks
            nose_tip = landmarks[1]
            chin = landmarks[152]
            left_eye = landmarks[33]
            right_eye = landmarks[263]
            left_mouth = landmarks[61]
            right_mouth = landmarks[291]

            # Convert to pixel coordinates
            image_points = np.array([
                (int(nose_tip.x * w), int(nose_tip.y * h)),
                (int(chin.x * w), int(chin.y * h)),
                (int(left_eye.x * w), int(left_eye.y * h)),
                (int(right_eye.x * w), int(right_eye.y * h)),
                (int(left_mouth.x * w), int(left_mouth.y * h)),
                (int(right_mouth.x * w), int(right_mouth.y * h))
            ], dtype="double")

            # 3D model reference points (same as before)
            model_points = np.array([
                (0.0, 0.0, 0.0),
                (0.0, -330.0, -65.0),
                (-225.0, 170.0, -135.0),
                (225.0, 170.0, -135.0),
                (-150.0, -150.0, -125.0),
                (150.0, -150.0, -125.0)
            ])

            # Camera matrix approximation
            focal_length = w
            camera_matrix = np.array([
                [focal_length, 0, w / 2],
                [0, focal_length, h / 2],
                [0, 0, 1]
            ], dtype="double")

            # Solve PnP to get head pose
            _, rotation_vector, _ = cv2.solvePnP(
                model_points, image_points, camera_matrix, None
            )

            # Convert rotation vector to matrix
            rotation_matrix, _ = cv2.Rodrigues(rotation_vector)

            # Calculate Euler angles (improved calculation)
            pitch = np.degrees(np.arcsin(-rotation_matrix[2, 0]))
            yaw = np.degrees(np.arctan2(rotation_matrix[1, 0], rotation_matrix[0, 0]))
            roll = np.degrees(np.arctan2(rotation_matrix[2, 1], rotation_matrix[2, 2]))

            # Determine direction
            direction = []

            # Check Yaw (Left/Right)
            if yaw > YAW_THRESHOLD:
                direction.append("Right")
            elif yaw < -YAW_THRESHOLD:
                direction.append("Left")

            # Check Pitch (Up/Down)
            if pitch > PITCH_THRESHOLD:
                direction.append("Up")
            elif pitch < -PITCH_THRESHOLD:
                direction.append("Down")

            # If no significant movement, mark as "Straight"
            if not direction and abs(yaw) < DEAD_ZONE and abs(pitch) < DEAD_ZONE:
                direction = ["Straight"]
            elif not direction:
                direction = ["Straight"]  # Minor movement within dead zone

            return direction

    return "Straight"

# Main loop for testing
while True:
    direction = get_head_direction()
    print(f"Direction: {direction}")
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()