from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl

MIDDLE_MOOD = "assets/middle_mood.mp3"

class MediaPlayer(QMediaPlayer):
    def __init__(self) -> None:
        QMediaPlayer.__init__(self)
        self.url = QUrl.fromLocalFile(MIDDLE_MOOD)
        self.content = QMediaContent(self.url)
        self.setMedia(self.content)
        self.setVolume(25)

    # Play Pause Function
    def togglePlay(self):
        if self.state() == 0 or self.state() == 2:
            self.play()
            return "Pause Music"

        elif self.state() == 1:
            self.pause()
            return "Play Music"

    # Change Volume Function
    def changeVolumeBy(self, volume):
        self.setVolume(self.volume() + volume)
