import yt_dlp
import gradio as gr
import os

def download_video(url):
    if not url:
        return "Barah-e-karam koi valid YouTube link dein."
    
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            return f"Video kamyabi se download ho gayi hai: {filename}"
    except Exception as e:
        return f"Error aa gaya: {str(e)}"

# Gradio ka interface
demo = gr.Interface(
    fn=download_video,
    inputs=gr.Textbox(label="YouTube Video Link Yahan Paste Karein"),
    outputs=gr.Text(label="Download Status"),
    title="Tipu Video Downloader",
    description="Yahan YouTube ya kisi bhi platform ka link daal kar video download karein."
)

if __name__ == "__main__":
    demo.launch()