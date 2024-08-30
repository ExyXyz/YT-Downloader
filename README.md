

# YouTube Downloader EXE

This standalone executable allows you to download videos or audio from YouTube with optional subtitles. The simple command-line interface guides you through the process of selecting the format (audio or video), choosing from available resolutions, and downloading subtitles if needed.

## Features

- **Standalone EXE**: No need to install Python or any libraries. (Except ffmpeg)
- **Ffmpeg Installer**: Automatically install ffmpeg if you haven't install it.
- **Download Video or Audio**: Choose between video with the highest available resolution or audio in MP3 format.
- **Subtitle Support**: Download subtitles in your preferred language.
- **Resolution Selection**: Pick from the available video resolutions.
- **Automatic Merging**: Video and audio streams are automatically merged using `ffmpeg`.
- **Continuous Usage**: The EXE remains open for you to download multiple videos in a session.

## Usage

1. **Download the EXE**: [Download YouTube Downloader EXE](https://github.com/ExyXyz/YT-Downloader/releases).
2. **Run the EXE**: Double-click the file to launch the command prompt interface.
3. **Follow the Prompts**:
   - Enter the YouTube link.
   - Select whether you want to download audio or video.
   - Choose your desired resolution.
   - Optionally, specify a subtitle language.

## Example

Here's what the interface looks like:

```plaintext
=============================================
Link: 
=============================================
1 For Audio
2 For Video
Type the number here: 
=============================================
Subtitle Lang-ID (Just let it empty if you don't want to download anything): 
=============================================
Resolutions Available:
1 : 1080p60
2 : 1080p
3 : 720p60
4 : 720p
5 : 480p
6 : 360p
7 : 240p
Type the number here: 
=============================================
Download complete! The file is saved as <video-title>.mp4
=============================================
Do you want to download another video? (y/n):
```

## Screenshot Preview

![Screenshot 2024-08-24 170002](https://github.com/user-attachments/assets/02e393ec-52c5-4a4c-bf9d-3a6c8e09e9a5)

![Screenshot 2024-08-24 170059](https://github.com/user-attachments/assets/48217236-3930-432e-80d0-4fc1538627ec)



## Download

Click the link below to download the latest version of the YouTube Downloader EXE:

[Download YouTube Downloader EXE](https://github.com/ExyXyz/YT-Downloader/releases/tag/release)

## Dependency: pytubefix

This project utilizes the `pytubefix` library for handling YouTube downloads. You can find more about this library and its usage here:

- [pytubefix GitHub Repository](https://github.com/JuanBindez/pytubefix)

---

*Developed by [Ekushi](https://github.com/ExyXyz).*
