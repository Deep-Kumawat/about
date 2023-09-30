from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi


class Transcript:
    videoId = ""
    youtube = None
    transcript = ""
    output_file = "transcript.txt"
    

    def __init__(self, url) -> None:
        self.youtube = YouTube(url)
        self.videoId = self.youtube.video_id
        self.transcript = self.getTranscript()
        self.saveTranscript()
        self.getTranscriptStringVariable()

    def getVideoId(self, url):
        return self.youtube.video_id
    
    def getTranscript(self):
        return YouTubeTranscriptApi.get_transcript(self.videoId)
    
    def getTranscriptStringVariable(self):
        # Copying the transcript from transcript.txt to inputText
        with open("transcript.txt", 'r') as transcriptTextFile:
            self.transcript += transcriptTextFile.read().replace('\n', '')
        return self.transcript

    def saveTranscript(self):
        with open(self.output_file, 'w', encoding='utf-8') as f:
            for entry in self.transcript:
                text = entry['text']
                f.write(text + '\n')

