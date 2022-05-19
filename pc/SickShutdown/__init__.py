import os
from pathlib import Path

from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtQml import QQmlApplicationEngine


class ShutdownUI(QObject):
    mainsign = Signal()

    def __init__(self, engine: QQmlApplicationEngine):
        super(ShutdownUI, self).__init__()
        self.backend = self.Backend(self)

        engine.load(os.fspath(Path(__file__).resolve().parent / 'main.qml'))
        self.root = engine.rootObjects()[-1]
        engine.rootContext().setContextProperty('shutdownbackend', self.backend)
        self.mainsign.connect(self.root.main)

    def show(self):
        self.mainsign.emit()

    def doBeforeShutdown(self): pass
    def doBeforeReboot(self): pass
    def doBeforeSleep(self): pass

    class Backend(QObject):
        def __init__(self, parent):
            super(type(self), self).__init__()
            self.parent = parent

        @Slot()
        def shutdown(self):
            self.parent.doBeforeShutdown()
            print('shutdown')

        @Slot()
        def reboot(self):
            self.parent.doBeforeReboot()
            print('reboot')

        @Slot()
        def sleep(self):
            self.parent.doBeforeSleep()
            print('sleep')


if __name__ == '__main__':
    from PySide6.QtGui import QGuiApplication
    app = QGuiApplication([])
    engine = QQmlApplicationEngine()

    s = ShutdownUI(engine)
    s.show()

    exit(app.exec())
