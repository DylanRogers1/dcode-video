from moviepy import editor

class VideoEditor:
	def __init__(self, video_file_path):
		self.clip = editor.VideoFileClip(video_file_path)
	def display()