

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

![YouTube Downloader EXE Preview](https://private-user-images.githubusercontent.com/108033300/361132292-f70b8647-7a30-471e-b0b1-bbfd4dd33070.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjQ0OTQwMDQsIm5iZiI6MTcyNDQ5MzcwNCwicGF0aCI6Ii8xMDgwMzMzMDAvMzYxMTMyMjkyLWY3MGI4NjQ3LTdhMzAtNDcxZS1iMGIxLWJiZmQ0ZGQzMzA3MC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgyNFQxMDAxNDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iZTM3MTNlNWFkZjdmZjFmMWU2NjU1OTIwNjNhMjg3NzM5MjhhMTQ2MzRmZWMwMWE1NzgzZTRlOGM5ODljNGY4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.SZEOePO-9SOqvLGUUr2TpF7CQQhksJlljPApmaoLOBE)
![YouTube Downloader EXE Preview 2](https://private-user-images.githubusercontent.com/108033300/361132323-25f655e4-ad46-45e9-8c19-452e54c12fd2.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjQ0OTQwMDQsIm5iZiI6MTcyNDQ5MzcwNCwicGF0aCI6Ii8xMDgwMzMzMDAvMzYxMTMyMzIzLTI1ZjY1NWU0LWFkNDYtNDVlOS04YzE5LTQ1MmU1NGMxMmZkMi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgyNFQxMDAxNDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02MzZkNjViZjRhNTI1MmZjNjllMDY5ZmVmZTc0ZjA5ZjVkMThjNDFmYmMxNzJiMDQyMjFiOWExMWQyYjc1NWUzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9._a5Jl6B4ChhDHIZ3lVi3SPA3_Q0efD7w0CfL1-4nEvo)

## Download

Click the link below to download the latest version of the YouTube Downloader EXE:

[Download YouTube Downloader EXE](https://github.com/ExyXyz/YT-Downloader/releases/tag/release)

## Dependency: pytubefix

This project utilizes the `pytubefix` library for handling YouTube downloads. You can find more about this library and its usage here:

- [pytubefix GitHub Repository](https://github.com/JuanBindez/pytubefix)

---

*Developed by [Ekushi](https://github.com/ExyXyz).*
