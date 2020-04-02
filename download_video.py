import os
import pytube
from pytube import YouTube

print("Enter YT video URL:")
url = input()
yt = YouTube(url)

#list only MP4 (for Transcribe! compatibility) otherwise use:
#all_streams = yt.streams.all()
#Also only show only progressive streams (both audio and video in single file)
#for now - that will limit video to 720p - for best quality download one needs
#to utilize DASH (Dynamic Adaptive Streaming over HTTP) technology - download
#audio and video separately then merge them via FFMPEG.
#For future consider audio only download and file extension defaulting to MP3.
s = 1
all_streams = yt.streams.filter(file_extension='mp4',progressive=True).all()
for st in all_streams:
    file_name = st.default_filename
    print(file_name)
    (codec_video, codec_audio) = st.parse_codecs()
    if codec_video is None:
        codec_video = 'None'
    if codec_audio is None:
        codec_audio = 'None'
    print(str(s)+". "+file_name+" [video codec: "+codec_video+" ,audio codec: "+codec_audio+"]")
    s += 1

if(len(all_streams) == 1):
    stream = all_streams[0]
else:
    print("Enter the number of video:")
    n = int(input())
    stream = all_streams[n-1]

stream.download()
print(stream.default_filename + "\nHas been downloaded")