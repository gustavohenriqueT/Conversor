import yt_dlp
import os

def downloadytb(url, output_path):
    try:

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        

        info_dict = yt_dlp.YoutubeDL().extract_info(url, download=False)
        title = info_dict.get('title', None)
        mp3file = os.path.join(output_path, f"{title}.mp3")
        
        return mp3file
    except Exception as e:
        print(f"Erro ao converter o vídeo: {e}")
        return None

def main():
    youtube_url = input("Insira o link do vídeo do YouTube: ")
    output_directory = 'c:/Users/Gustavo/Desktop/ConversorGerso'
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    mp3path = downloadytb(youtube_url, output_directory)
    
    if mp3path:
        print(f'MP3 salvo em: {mp3path}')
    else:
        print('Falha na conversão.')

if __name__ == "__main__":
    main()
