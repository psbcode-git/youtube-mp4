import os
from pytube import YouTube


def download_video(url, save_path='.'):
    try:
        # Creating YouTube object
        yt = YouTube(url)

        # Getting the best available stream (resolution/format)
        stream = yt.streams.get_highest_resolution()

        # Downloading the video
        print(f'Downloading {yt.title}...')
        stream.download(output_path=save_path)
        print(f'{yt.title} has been successfully downloaded.')
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Asking user for YouTube URL and path to save the video
    url = input("Enter the YouTube URL: ")
    save_path = input("Enter the directory path to save the video (leave empty for current directory): ")

    # If save_path is empty, use the current directory
    save_path = save_path or '.'

    # Making sure the save path exists
    if not os.path.exists(save_path):
        print("The specified path does not exist.")
    else:
        # Download the video
        download_video(url, save_path)

