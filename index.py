# Import everything needed to edit video clips
import moviepy.editor as mpy
from moviepy.video.fx.all import crop
from moviepy.video.fx.all import resize

# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clip = mpy.VideoFileClip("myHolidays.mp4").subclip(50, 60)
(w, h) = clip.size
# Reduce the audio volume (volume x 0.8)
clip = clip.volumex(0.8)

if(w == 1280):
    clip_resized = crop(clip, width=480, height=720,
                        x_center=w/2, y_center=h/2)


# Generate a text clip. You can customize the font, color, etc.

txt = "\n".join([
    "'A long time ago, in a faraway galaxy,",
    "there lived a prince and a princess",
    "there lived a prince and a princess",
    "there lived a prince and a princess",
    "there lived a prince and a princess",
    "there lived a prince and a princess'",
    "Author Name"
])


# Add blanks
txt = 10*"\n" + txt + 10*"\n"

txt_clip = mpy.TextClip(txt, fontsize=20, font='Times New Roman', align='center',
                        color='white').set_duration(10).set_pos('center')

txt_col = txt_clip.on_color(
    size=(1280, 250), pos=('center'), color=(0, 0, 0), col_opacity=0.6).set_pos('center')

# piano = (VideoFileClip("../../videos/douceamb.mp4",audio=False).
#          subclip(30,50).
#          resize((w/3,h/3)).    # one third of the total screen
#          margin( 6,color=(255,255,255)).  #white margin
#          margin( bottom=20, right=20, opacity=0). # transparent
#          set_pos(('right','bottom')) )

newclip = mpy.ImageClip("myHouse.jpg")
im_clip = resize(newclip, 0.2, method='bilinear')

# Overlay the text clip on the first video clip
video = mpy.CompositeVideoClip([clip_resized, txt_col, im_clip])

# Write the result to a file (many options available !)
video.set_duration(10).write_videofile("myHolidays_edited.mp4")
