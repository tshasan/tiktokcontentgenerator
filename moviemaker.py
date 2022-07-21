from moviepy.editor import *
from moviepy.video.fx.all import crop
import mutagen
import os
from pydub import AudioSegment


class MovieMaker:
    def __init__(self, instanceid):
        cwd = os.getcwd()
        print('audio load')
        print(cwd)
        audio = AudioSegment.from_file("{0}/data/audio/{1}titletext.mp3".format(cwd, instanceid))
        audio1 = AudioSegment.from_file("{0}/data/audio/{1}bodytext.mp3".format(cwd, instanceid))
        audiolength = audio.duration_seconds + audio1.duration_seconds
        print('audio found')
        print(audio.duration_seconds)
        print(audio1.duration_seconds)
        print(audiolength)

        video = VideoFileClip(cwd + "/data/backroundvideo/minecraft2.mp4").subclip(0, audiolength)
        value = video.size
        video1 = crop(video, x_center=(int(value[0]) / 2), y_center=(int(value[1]) / 2),
                      width=((int(value[1])) * 9 / 16), height=(int(value[1])))
        print(value)
        print('videocrop done')

        video2 = (ImageClip(cwd + "/data/images/" + instanceid + "title.png")
                  .set_start(0)
                  .set_duration(audio.duration_seconds)
                  .set_position(("center", 100)))

        video3 = (ImageClip(cwd + "/data/images/" + instanceid + "text.png")
                  .set_start(audio.duration_seconds)
                  .set_duration(audio1.duration_seconds)
                  .set_position(("center", 100)))
        videofinal = CompositeVideoClip([video1, video2, video3])
        print('image overlay done')
        audiotitle = AudioFileClip(cwd + "/data/audio/" + instanceid + "titletext.mp3").set_duration(
            audio.duration_seconds)
        audiotext = AudioFileClip(cwd + "/data/audio/" + instanceid + "bodytext.mp3")
        new_audioclip = CompositeAudioClip(
            [videofinal.audio, audiotitle.set_start(0),audiotext.set_start(int(audio.duration_seconds+1))])
        new_audioclip.set_fps(48000)
        videofinal = videofinal.set_audio(new_audioclip)
        print('audio sync done ')
        videofinal.write_videofile(cwd+'/data/results/'+instanceid + "video.mp4",fps=30, codec='MPEG', audio=True, audio_codec='aac')
# videofinal.write_videofile(cwd + '/data/results/' + instanceid + ".mp4", fps=30, codec='libx264', audio=True,
                                   # audio_codec='aac',ffmpeg_params=['-video_format','mac','-crf','18','-preset','veryslow' ]