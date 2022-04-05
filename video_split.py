import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


class ClipLargeVideos:
    __path = None

    def __init__(self):
        self.__path = os.path.abspath("")
        # Replace the filename below.
        required_video_file = self.__path+"/airshow.mp4"
        target_path = self.__path+"/video_clips/"
        time_input_file_path = self.__path+"/times.txt"
        target_file_name = ['0thFrame', '1800thFrame']

        with open(time_input_file_path) as f:
            times = f.readlines()

        times = [t.strip() for t in times]
        
        for time in times:
            starttime = int(time.split("-")[0])
            endtime = int(time.split("-")[1])
            ffmpeg_extract_subclip(required_video_file, starttime, endtime,
                                   targetname=target_path + str(target_file_name[times.index(time)]) + ".mp4")


if __name__ == '__main__':
    ClipLargeVideos()
