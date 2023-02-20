import imageio

# Create a list of the file names of the frames.
frame_filenames = [f"frames/frame_{i:02d}.png" for i in range(1, 23)]
# Define the output file name and path for the video
output_file = "video/test_video.mp4"

# Create an imageio writer object for the output file
writer = imageio.get_writer(output_file, fps=30)

# Loop over the frame filenames and add each frame to the writer object
for filename in frame_filenames:
    frame = imageio.imread(filename)
    writer.append_data(frame)

# Close the writer to finalize the video file
writer.close()
