from Downloader.Classes import download_class

# Create an object of the Downloader class
file = download_class.Downloader()


if __name__ == "__main__":
    # Set the attributes of the object
    file.url = "https://www.youtube.com/watch?v=1BXJewS5CT0"
    file.encoder = "mp4"
    file.output_path = "D:\WORK\Projects\Downloader"
    file.res = "1080p"
    
    # Call the download method
    file.download()