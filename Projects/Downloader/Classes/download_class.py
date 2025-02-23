from pytubefix import YouTube
from moviepy import VideoFileClip, AudioFileClip

class Downloader(object):
    
    def __init__(self):
        # initialize the class
        self.url = None
        self.encoder = None
        self.output_path = None
        self.res = None
     
    def download(self):
        # get the video
        yt = YouTube(self.url)
        
        # download the video or audio
        if self.encoder != "mp4":
            audio = yt.streams.get_audio_only()
            audio.download(output_path=self.output_path)
        else:
            # get video and audio streams
            video = yt.streams.filter(adaptive= True,
                                      file_extension=self.encoder,
                                      ).order_by("resolution").desc().first()
            audio = yt.streams.get_audio_only()
            
            # download video and audio
            video.download(output_path=self.output_path)
            audio.download(output_path=self.output_path, filename=f"{video.title}.m4a")
            
            # get audio and video clips ready for merging
            final_audio = AudioFileClip(f"{self.output_path}/{video.title}.m4a")
            final_video = VideoFileClip(f"{self.output_path}/{video.title}.{self.encoder}")
            
            # merge audio and video and save it on designated path
            final_product = final_video.with_audio(final_audio)
            final_product.write_videofile(f"{self.output_path}/{video.title}_final.mp4", 
                                            audio_codec="aac", 
                                            preset = "ultrafast")

            


        
        

    