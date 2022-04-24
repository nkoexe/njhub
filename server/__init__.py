from socket import socket
from threading import Thread
from time import time
import locale

from compleanni import get_birthdays

MY_ID = '0'

devices = {
    '0': 'me',
    '1': 'Computer',
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
online = {}

locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')


# Todo: send_file function

def send(sock, msg: str, bytes: bool = False):
    '''
    Send a string message to a device.

    :param socket sock: the socket of the device
    :param str msg: the string message to send
    :param bool bytes: if the string is already encoded
    '''

    if not bytes:
        msg = msg.encode()

    sock.send(str(len(msg)).zfill(6).encode() + msg)


def recieve(sock) -> str:
    '''
    Recieve a string message from a device.

    :param socket sock: the socket of the device
    :return: the string message
    :rtype: str
    '''
    pass


def build(msg: str or bytes, zfill: int = 4, bytes: bool = False) -> bytes:
    '''
    Builds the component of a message.
    returns the length of the message + the encoded message

    :param str msg: the string to encode
    :param int zfill: the number of zeroes to add to the length of the message (the first part)
    :param bool bytes: if the string is already encoded
    :return: length + encoded message
    :rtype: str
    '''

    l = str(len(msg)).zfill(zfill).encode()

    if not bytes:
        msg = msg.encode()

    return l + msg


def send_notification(device_id: str, title: str, text: str, duration: int = 3000, noti_type: int = 0):
    '''
    Send a notification to a device.

    :param str device_id: the id of the device
    :param str title: the title of the notification
    :param str text: the text of the notification
    :param int duration: the duration of the notification
    :param int noti_type: the type of the notification (0: info, 1: warning, 2: error)
    '''

    if device_id not in online:
        return None

    head = MY_ID + device_id + str(int(time())) + '1'
    body = build(title) + build(text) + str(duration).zfill(6).encode() + str(noti_type).encode()
    send(online[device_id], head.encode() + body, True)


def handle_cli(sock):
    '''
    Main loop for handling a device.

    :param socket sock: the socket of the device
    '''

    # recieve the device id and set it as online
    device_id = sock.recv(1).decode()
    online[device_id] = sock

    for i in compleanni:
        name, date, age, remaining = i

        if remaining == 2:
            when = 'dopodomani!'
        elif remaining == 1:
            when = 'domani'
        if remaining == 0:
            when = 'oggi'
        else:
            when = f'tra {remaining} giorni'

        # * hashtag to remove leading zero in datetime is only on windows, on unix replace with hyphen
        send_notification(device_id,
                          f'Compleanno di {name.split()[0]}!',
                          f'{name} compie {age} anni il {date:%#d} {date:%B}',
                          7000)


if __name__ == '__main__':
    # create and initialize the socket
    sock = socket(2, 1)
    sock.bind(('0.0.0.0', 12357))
    sock.listen()

    compleanni = get_birthdays(50)

    # accept connections and handle them in new threads
    while True:
        cli, addr = sock.accept()

        Thread(target=handle_cli, args=(cli,)).start()
