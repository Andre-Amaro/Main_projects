from Downloader.Classes import download_class

# Create an object of the Downloader class
file = download_class.Downloader()


if __name__ == "__main__":
    # Set the attributes of the object
    file.url = "Youtube video URL"
    file.encoder = "mp4"
    file.output_path = "file save path"
    file.res = "1080p"
    
    # Call the download method
    file.download()
