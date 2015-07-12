'''
Created on Jun 25, 2015

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

import socket
import thread
import argparse

server_log = 'log/server_log.txt'

def server_function(sock, addr):
    try:      
        request = sock.recv(1024)
#         print type(request)
#         print request
        
        log = open(server_log, 'a')
        log.write(request)
        log.write('\n------------------------------\n')
        log.close()
            
        filename = request.split()[1]
#         print'filename', filename[1:], len(filename)
                        
        try:
            if len(filename) == 1:
#                 http_response = """\
# HTTP/1.1 200 OK
# 
# <html>
#     <head>
#         <title>
#             HttpServer Project Home
#         </title>
#     </head>
#     <body>
#         <center>
#             Hello World!! <br>
#             Welcome to HttpServer Project
#         </center>
#     </body>
# </html>
# """
                f = open('helloworld.html', 'r')
                outputdata = f.readlines()
                
                http_response = """\
HTTP/1.1 200 OK

"""
                for i in range(0, len(outputdata)):
                    http_response = http_response + outputdata[i]
                                
                sock.sendall(http_response)
                sock.close()
            
            if len(filename) > 1:
                f = open(filename[1:], 'r')
                outputdata = f.readlines()
                
                http_response = """\
HTTP/1.1 200 OK

"""                            
#                 sock.sendall(http_response)
                
#                 for i in range(0, len(outputdata)):
#                     print outputdata[i]
#                     sock.sendall(outputdata[i])
    
                for i in range(0, len(outputdata)):
                    http_response = http_response + outputdata[i]
                    
                
                f.close()
                sock.sendall(http_response)
                sock.close()
        
        except IOError:
            http_response = """\
HTTP/1.1 404 Not Found

<html>
    <head>
        <title>
            HttpServer Project Home
        </title>
    </head>
    <body>
        <center>
            404 File Not Found
        </center>
    </body>
</html>
"""
            sock.sendall(http_response)
            sock.close()

    except IOError:
        http_response = """\
HTTP/1.1 404 Not Found

<html>
    <head>
        <title>
            HttpServer Project Home
        </title>
    </head>
    <body>
        <center>
            404 Server Not Found
        </center>
    </body>
</html>
"""
        sock.sendall(http_response)
        sock.close()

def main(port):
    HOST = '127.0.0.1'
#     try:
#         PORT = int(raw_input("Enter port number"))
#     except ValueError:
#         PORT = 8080
        
    PORT = port
    
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(5)
    
    print('Serving on %s ' % PORT)
    print('Press Ctrl+C to exit')
    while True:
        try:
            print('\nReady to serve...')
            
            sock, addr = serverSocket.accept()
            
            thread.start_new_thread(server_function, (sock, addr))
        except KeyboardInterrupt:
            print('Closing and exiting server')
            exit()
         
    serverSocket.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Client for HttpServer.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        '--port',
        type=int,
        default=8080,
        help='Port on the server.'
    )
    args = parser.parse_args()
    main(args.port)