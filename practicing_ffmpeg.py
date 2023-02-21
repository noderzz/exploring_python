import os
import subprocess

# Set the paths to the input image frames, audio file, and output video file
input_path = "./frames"
audio_path = "./audio/ev.mp3"
output_file = "./video/test_video.mp4"

# Set the frame rate for the output video
frame_rate = 30

# Use FFmpeg to create the video from the image frames and audio
cmd = (f"ffmpeg -y -framerate {frame_rate} -i {input_path}/frame_%02d.png "
       f"-i {audio_path} -c:v libx264 -preset veryfast -crf 18 -c:a copy {output_file}")

subprocess.call(cmd, shell=True)

# Check if the output file was created
if os.path.isfile(output_file):
    print(f"Video file '{output_file}' created successfully!")
else:
    print(f"Error: Failed to create video file '{output_file}'")
