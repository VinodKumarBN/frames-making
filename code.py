import cv2
import os

video_path = 'downloaded-file.mp4'  # Replace with your video file name
output_folder = 'frames'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cap = cv2.VideoCapture(video_path)
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_filename = os.path.join(output_folder, f'frame_{frame_count:03d}.jpg')
    cv2.imwrite(frame_filename, frame)
    frame_count += 1

cap.release()
print(f" {frame_count} frames saved to '{output_folder}' folder.")
