import os
from datetime import datetime
from pathlib import Path
from time import time

from apscheduler.schedulers.background import BackgroundScheduler
from PySide6.QtCore import QObject, Signal
from PySide6.QtQml import QQmlApplicationEngine
from vlc import MediaPlayer


class Notifier(QObject):
    # signal to pass to QML to show a notification. parameters: title, text, duration, noti_type
    mainsign = Signal(str, str, int)

    INFO = 0
    WARNING = 1
    ERROR = 2

    def __init__(self, engine: QQmlApplicationEngine):
        '''
        Custom notifier, built for the NjHub project.
        Features:
        - Cool
        - Schedule for notifications, send multiple notifications and they will appear one after the other

        Todo:
        - View notification history
        - Different notification types (info, warning, error) with different colors
        - Notification scheduling (show notification at a specific time)

        :param engine: QQmlApplicationEngine of the QGuiApplication instance.
        '''

        super(Notifier, self).__init__()

        # history of all notifications already shown
        # format: (title: str, text: str, notification_type: int, timestamp: int)
        self.history = []
        # timestamp of the end of the latest notification
        self.latest = 0

        # path to the the parent directory ('NotificationManager/') - the base path of the project
        self.basepath = Path(__file__).resolve().parent

        # initialize vlc media player for the notification sound
        self.sound = MediaPlayer(str(self.basepath / 's1.mp3'))

        # initialize and start the scheduler
        self.scheduler = BackgroundScheduler(timezone='Europe/Rome')
        self.scheduler.start()

        # load the ui and connect the signals
        engine.load(os.fspath(self.basepath / 'main.qml'))
        # engine.rootContext().setContextProperty('notifier_backend', self)
        self.root = engine.rootObjects()[-1]
        self.mainsign.connect(self.root.notify)

    def notify(self, title: str, text: str, duration: int = 3000, noti_type: int = 0, sound: bool = True, schedule: bool = True):
        '''
        Show a cool notification.
        If already showing a notification, it will be scheduled and shown when possible.

        :param str title: the title of the notification
        :param str text: the content/body of the notification
        :param int duration: the duration in milliseconds of the notification
        :param int noti_type: the type of the notification (0: INFO, 1: WARNING, 2: ERROR)
        :param bool sound: if the notification should play a sound
        :param bool schedule: if the notification should be scheduled or run immediately. Best if left as True as it could cause animation problems.
        '''

        timestamp = time()

        if schedule:
            # if the notification request is sent before the latest notification ended, schedule it
            if self.latest > timestamp:
                # add the notification to the scheduler - 1 second after "latest" (the end of the last notification), setting 'schedule' to False to avoid recursion and give permission to run immediately
                self.scheduler.add_job(self.notify, 'date', run_date=datetime.fromtimestamp(self.latest+1), args=(title, text, duration, noti_type, sound, False))
                # set the new value of "latest" as the value it had previously + the duration of the notification + 1 for the end animation
                self.latest += duration/1000 + 1
                # this function will be called again at the sheduled time with the priority to show the notification, so we return here
                return None

            else:
                # if the notification is run immediately (not scheduled), the latest timestamp is this one
                self.latest = timestamp + duration/1000 + 1

        # play the notification sound if requested
        if sound:
            # reset the media player (returns to the beginning of the media) and plays the sound
            self.sound.stop()
            self.sound.play()

        # send the signal to the qml ui to show the notification
        self.mainsign.emit(title, text, duration)

        # add the useful data of the notification to the history
        self.history.append((title, text, noti_type, int(timestamp)))


if __name__ == '__main__':
    from PySide6.QtGui import QGuiApplication
    app = QGuiApplication([])
    engine = QQmlApplicationEngine()

    n = Notifier(engine)

    for i in range(5):
        n.notify(f'Notifica {i+1}!', 'Testo della notifica di esempio')

    '''
    def test():
        while True:
            title = input('Title: ')
            text = input('Text: ')
            n.notify(title, text)
    from threading import Thread
    Thread(target=test, daemon=True).start()
    '''

    exit(app.exec())
