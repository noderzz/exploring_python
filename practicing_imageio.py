"""
I was unable to get this to work with the audio version and was repeatedly getting this error:

ValueError: Could not find a backend to open `./audio/ev.mp3`` with iomode `r?`.
"""

import imageio
import os

frame_filenames = []
files = os.listdir("./frames")
files = [f for f in files if os.path.isfile(os.path.join("./frames", f))]

# Define the path and filename of the audio file
audio_file = "./audio/ev.mp3"

# Create a list of the file names of the frames.
for filename in os.listdir("."):
    frame_filenames = [f"frames/frame_{i:02d}.png" for i in range(1, len(files))]

# Define the output file name and path for the video
output_file = "video/test_video.mp4"

# Create an imageio writer object for the output file
writer = imageio.get_writer(output_file, fps=30)

# Loop over the frame filenames and add each frame to the writer object
for filename in frame_filenames:
    frame = imageio.imread(filename)
    writer.append_data(frame)

# Load the audio file using imageio
audio = imageio.get_reader(audio_file, plugin='ffmpeg')

# Add the audio track to the video writer
writer.add_audio(audio)

# Close the writer to finalize the video file
writer.close()
