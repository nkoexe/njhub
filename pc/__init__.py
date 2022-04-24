from socket import socket
from threading import Thread

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from NotificationManager import Notifier


MY_ID = '1'
SERVER_ADDR = ('127.0.0.1', 12357)

devices = {
    '0': 'Server',
    '1': 'me',
    '2': 'Smartphone',
    '3': 'Smartwatch',
    'A': 'Dina',
    'B': 'Lucine',
    'C': 'Smartsocket',
    'D': 'Tapparella1',
    'E': 'Tapparella2',
    'F': 'Tapparella3',
    'G': 'Tapparella4',
    'H': 'Tapparella5',
    'I': 'Tapparella6',
    'J': 'Bobby'
}


# send a notification
def notify(from_id, body):
    '''
    Build and send a notification to the notification manager.

    :param str from_id: the id of the device that sent the message
    :param str body: the unique body/content of the message
    '''

    # subdivide the body into its components - see /docs/Dati.md
    title_len = int(body[:4])
    title = body[4:title_len+4]
    text_len = int(body[title_len+4:title_len+8])
    text = body[title_len+8:title_len+text_len+8]
    duration = int(body[title_len+text_len+8:title_len+text_len+14])
    noti_type = int(body[title_len+text_len+14])

    # send the notification
    notifier.notify(title, text, duration, noti_type)


def handle_message(msg: str):
    '''
    Handle a recieved message.

    :param str msg: the string message to handle
    '''

    # subdivide the message into its components
    from_id, to_id, timestamp, actiontype, body = msg[0], msg[1], msg[2:12], msg[12], msg[13:]

    # * NOTIFICATION
    if actiontype == '1':
        assert to_id == MY_ID
        notify(from_id, body)


def main():
    '''
    Main loop for handling the connection.
    '''

    # connect to the server
    sock.connect(SERVER_ADDR)

    # send my device id
    sock.send(MY_ID.encode())

    # main loop for receiving messages
    while True:
        # recieve the length of the message, then the message
        msg_len = int(sock.recv(6))
        msg = sock.recv(msg_len).decode()

        # handle the recieved message (new thread ??) (naw probably not)
        handle_message(msg)


if __name__ == '__main__':
    # create qt application and the socket
    app = QGuiApplication([])
    engine = QQmlApplicationEngine()
    sock = socket(2, 1)

    # initialize services
    notifier = Notifier(engine)
    # * assistant = Assistant(engine)

    # start the main loop for the connection in a separate thread
    Thread(target=main, daemon=True).start()

    # run the application
    app.exec()
