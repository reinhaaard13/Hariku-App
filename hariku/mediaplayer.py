from hariku.moodselect import Mood
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl
import time

HIGH_MOOD = "assets/high_mood.mp3"
MIDDLE_MOOD = "assets/middle_mood.mp3"
LOW_MOOD = "assets/low_mood.mp3"

class MediaPlayer(QMediaPlayer):
    def __init__(self) -> None:
        QMediaPlayer.__init__(self)
        self.content = {
            'high': QMediaContent(QUrl.fromLocalFile(HIGH_MOOD)),
            'middle': QMediaContent(QUrl.fromLocalFile(MIDDLE_MOOD)),
            'low': QMediaContent(QUrl.fromLocalFile(LOW_MOOD))
        }
        self.setMedia(self.content['middle'])
        self.setVolume(25)
        self.mood = Mood()

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

    def fadeOut(self):
        while self.volume() > 0:
            self.changeVolumeBy(-4)
            time.sleep(0.2)
        self.stop()

    def fadeIn(self, volume):
        self.play()
        while self.volume() < volume:
            self.changeVolumeBy(4)
            time.sleep(0.2)

    def changeSong(self,mood):
        if self.media() == self.content[mood]:
            return

        media_status = self.state()

        # If media player if stopped or paused
        if media_status == 0 or media_status == 2:
            self.setMedia(self.content[mood])
        # Else if media player is playing the music
        elif media_status == 1:
            self.fadeOut()
            self.setMedia(self.content[mood])
            self.fadeIn(25)


    def reviewMood(self, text):
        score = self.mood.score
        new_score = self.mood.count_mood(text)
        if score != new_score:
            if new_score > 2:
                self.changeSong('high')
                print('Mood Refreshed!')
            elif new_score < -2:
                self.changeSong('low')
                print('Mood Refreshed!')
            else:
                self.changeSong('middle')
                print('Mood Refreshed!')
        else:
            return