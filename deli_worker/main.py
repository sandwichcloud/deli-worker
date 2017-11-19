import sys

from ingredients_tasks.celary import Messaging


def main():
    messaging = Messaging('127.0.0.1', 5672, 'sandwich', 'hunter2', '/')
    messaging.connect()
    messaging.app.main = 'deli_worker'
    sys.argv.extend(['worker', '-l', 'info', '-Ofair'])
    messaging.start(argv=None)


if __name__ == '__main__':
    main()
