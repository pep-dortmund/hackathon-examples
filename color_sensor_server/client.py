import zmq
from argparse import ArgumentParser
from pprint import pprint

parser = ArgumentParser()
parser.add_argument('host')
parser.add_argument('-p', '--port', type=int, default=5000)

context = zmq.Context()
socket = context.socket(zmq.REQ)


def main():
    args = parser.parse_args()

    socket.connect('tcp://{}:{}'.format(args.host, args.port))

    commands = ['raw', 'color', 'reflected', 'ambient', 'all', 'quit']
    print('Select one of {}'.format(commands))

    while True:
        answer = input('Command: ')
        if answer not in commands:
            print('Invalid input.')
            print('Select one of {}'.format(commands))

        elif answer == 'quit':
            break

        socket.send_string(answer)
        pprint(socket.recv_pyobj())


if __name__ == '__main__':
    main()
