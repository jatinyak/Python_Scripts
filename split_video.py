from moviepy import VideoFileClip

def split_video_at_middle(input_path):
    # Load the video file
    with VideoFileClip(input_path) as clip:
        duration = clip.duration
        midpoint = duration / 2
        
        print(f"Total duration: {duration:.2f}s | Splitting at: {midpoint:.2f}s")
        
        # In MoviePy 2.x, use .subclipped()
        first_half = clip.subclipped(0, midpoint)
        print("Writing first half...")
        first_half.write_videofile("part1_start.mp4", codec="libx264")
        
        second_half = clip.subclipped(midpoint, duration)
        print("Writing second half...")
        second_half.write_videofile("part2_end.mp4", codec="libx264")

    print("Video split successfully!")

# Usage
split_video_at_middle('/Users/jatin.s/Library/CloudStorage/OneDrive-SAPFioneer/FS-PE Documents/Recordings/02) Introduction - part 2.mp4')