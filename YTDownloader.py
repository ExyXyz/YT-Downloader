import os
import subprocess
import sys
from pytubefix import YouTube
from pytubefix.cli import on_progress

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("FFmpeg is not installed. Installing FFmpeg...")
        install_ffmpeg()
    except FileNotFoundError:
        print("FFmpeg is not installed. Installing FFmpeg...")
        install_ffmpeg()

def install_ffmpeg():
    if sys.platform.startswith("win"):
        print("Windows detected. Installing FFmpeg using winget...")
        try:
            subprocess.run(["winget", "install", "ffmpeg"], check=True)
            print("FFmpeg installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install FFmpeg: {e}")
            sys.exit(1)
    else:
        print("Unsupported operating system for automated FFmpeg installation.")
        sys.exit(1)

def get_resolution_choice(streams):
    print("Resolutions Available:")
    resolution_map = {}
    for idx, stream in enumerate(streams):
        resolution = stream.resolution or stream.abr
        if resolution and resolution not in resolution_map.values():
            print(f"{idx + 1} : {resolution}")
            resolution_map[idx + 1] = resolution
    choice = int(input("Type the number here: "))
    return resolution_map.get(choice, None)

def download_subtitle(yt, title):
    print("=============================================")
    subtitle_lang = input("Subtitle Lang-ID (Just let it empty if you don't want to download anything): ")
    if subtitle_lang:
        caption = yt.captions.get_by_language_code(subtitle_lang)
        if caption:
            caption.save_captions(f"{title}_captions.txt")
            print(f"Subtitles saved as {title}_captions.txt")
        else:
            print(f"No subtitles found for language code '{subtitle_lang}'.")
    else:
        print("No subtitles will be downloaded.")
    print("=============================================")

def download_audio(yt, title):
    print("=============================================")
    audio_stream = yt.streams.get_audio_only()
    audio_file = f'{title}.mp3'

    try:
        audio_stream.download(filename=audio_file)
        print(f"Audio downloaded successfully as {audio_file}")
    except Exception as e:
        print(f"Failed to download audio: {e}")

def download_video(yt, title):
    video_streams = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc()
    selected_resolution = get_resolution_choice(video_streams)

    if selected_resolution:
        video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True, resolution=selected_resolution).first()
    else:
        video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()

    audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()

    video_file = f'{title}_video.mp4'
    audio_file = f'{title}_audio.mp4'

    try:
        video_stream.download(filename=video_file)
        print(f"Video downloaded successfully as {video_file}")
    except Exception as e:
        print(f"Failed to download video: {e}")
        return

    try:
        audio_stream.download(filename=audio_file)
        print(f"Audio downloaded successfully as {audio_file}")
    except Exception as e:
        print(f"Failed to download audio: {e}")
        return

    if not os.path.exists(video_file) or not os.path.exists(audio_file):
        print("One or both of the files are missing. Ensure that downloads were successful.")
        return

    output_file = f'{title}.mp4'
    ffmpeg_command = f'ffmpeg -i "{video_file}" -i "{audio_file}" -c copy "{output_file}"'
    ffmpeg_result = os.system(ffmpeg_command)

    if ffmpeg_result != 0:
        print("Failed to combine video and audio using ffmpeg.")
        return

    os.remove(video_file)
    os.remove(audio_file)
    print(f"Video and audio merged successfully into {output_file}")
    print("=============================================")

def main():
    check_ffmpeg()
    while True:
        print("=============================================")
        url = input("Link: ")
        if not url:
            print("No link provided, exiting.")
            break

        yt = YouTube(url, on_progress_callback=on_progress)
        title = yt.title.replace(" ", "_").replace("/", "_")
        print(f"Title: {yt.title}")
        print("=============================================")

        choice = input("1 For Audio\n2 For Video\nType the number here: ")

        if choice == "1":
            download_audio(yt, title)
        elif choice == "2":
            download_subtitle(yt, title)
            download_video(yt, title)
        else:
            print("Invalid choice. Please select either 1 for Audio or 2 for Video.")
            continue

        repeat = input("Do you want to download another video? (y/n): ")
        if repeat.lower() != 'y':
            break

if __name__ == "__main__":
    main()
