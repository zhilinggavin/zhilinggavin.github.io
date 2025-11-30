from moviepy.video.io.VideoFileClip import VideoFileClip

def convert_mp4_to_gif(input_path, output_path, resize_factor=0.5):
    # Load the video file
    clip = VideoFileClip(input_path)
    
    # Resize the clip to reduce the size of the GIF
    clip = clip.resized(resize_factor)
    
    # Write the GIF file
    clip.write_gif(output_path, fps=10)


if __name__ == "__main__":
    input_path = "video1.mp4"  # Replace with your input MP4 file path
    output_path = "video1.gif"      # Replace with your desired output GIF file path
    convert_mp4_to_gif(input_path, output_path)