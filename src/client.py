'''
Created on Jun 27, 2015

@author: Puneeth Umesh Bharawdaj
@id: 100 110 6478

References:
http://www.tutorialspoint.com/python/python_command_line_arguments.htm
http://codereview.stackexchange.com/questions/52701/proxy-using-socket-doubts-on-multithreading-and-connection-closing
https://docs.python.org/3.1/howto/sockets.html
http://ilab.cs.byu.edu/python/threadingmodule.html
http://ruslanspivak.com/lsbaws-part1/
http://learnpythonthehardway.org/book/ex15.html
http://www.december.com/html/tutor/hello.html
http://www.tutorialspoint.com/python/python_multithreading.htm

'''

import argparse
import socket
import errno
from socket import error as socket_error

client_log = 'log/client_log.txt'

def main(host, port, folder, filename):
#     SERVER_ADDRESS = 'localhost', port
    SERVER_ADDRESS = host, port 
    REQUEST = b"""\
GET """ + folder + filename + """ HTTP/1.1
Host: localhost:""" + str(port)

    try:
#         print REQUEST
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(SERVER_ADDRESS)
        sock.sendall(REQUEST)
        data = sock.recv(1024)
        sock.close()
        # print 'Received', repr(data)
#         print 'Data from server %s' % data
        
        log = open(client_log, 'a')
        log.write(data)
        log.write('\n-------------------------------------------------\n')
        log.close()
    
    except socket_error as serr:
        if serr.errno == errno.ECONNREFUSED:
            print('Server not online')
            log = open(client_log, 'a')
            log.write('Server not online')
            log.write('\n-------------------------------------------------\n')
            log.close()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Client for HttpServer.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        '--host',
        type=str,
        default='localhost',
        help='Server name or IPf')
    parser.add_argument(
        '--port',
        type=int,
        default=8080,
        help='Port on the server.'
    )
    parser.add_argument(
        '--folder',
        type=str,
        default='',
        help='Folder on the server')
    parser.add_argument(
        '--filename',
        type=str,
        default='',
        help='File on the server.'
    )
    args = parser.parse_args()
#     print args
    len_folder = len(args.folder)
    len_filename = len(args.filename)
    
    if len_folder == 0 and len_filename == 0:
        main(args.host, args.port, '/', '')
    if len_folder == 0 and len_filename > 0:
        main(args.host, args.port, args.folder, "/" + args.filename)
    if len_folder > 0 and len_filename == 0:
        main(args.host, args.port, "/" + args.folder, args.filename)
    if len(args.folder) > 0 and len(args.filename) > 0:
        main(args.host, args.port, "/" + args.folder, "/" + args.filename)
