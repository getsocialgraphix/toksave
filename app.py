from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/download')
def download_video():
    url = request.args.get('url')
    # yt-dlp fetches the video without watermark
    ydl_opts = {'format': 'best', 'outtmpl': 'video.mp4'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    # send_file forces the browser to trigger a direct download
    return send_file('video.mp4', as_attachment=True, download_name='tiktok_video.mp4')

if __name__ == '__main__':
    app.run()