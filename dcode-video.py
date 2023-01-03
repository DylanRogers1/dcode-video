from moviepy import editor

clip = editor.VideoFileClip("test/video.mp4").subclip(0, 10)

txt = editor.TextClip("Christmas at Center Parcs", fontsize=100, color="white")
txt = txt.set_position("center")
txt = txt.set_duration(5)

video = editor.CompositeVideoClip([clip, txt])
video.write_videofile("test/newvideo.mp4")