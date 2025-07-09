import os

os.system('ffmpeg -r 20 -s 1920x1080 -i ./images/pendulum_2/%06d.png -vcodec libx264 -crf 25 ./pendulum.mp4')