'''
Created on Jun 26, 2015

@author: puneeth
'''

'''
Created on Jun 25, 2015

@author: puneeth
'''

import socket

HOST, PORT = '127.0.0.1', 8080

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((HOST, PORT))
serverSocket.listen(5)

connectionSocket, addr = serverSocket.accept()
try:
    request = connectionSocket.recv(1024)
    print(request)
    
    filename = request.split()[1]
    print(filename[1:])
    
    try:
        f = open(filename[1:], 'r')
        outputdata = f.readlines()
               
        http_response = """\
HTTP/1.1 200 OK

"""                            
        connectionSocket.sendall(http_response)
        
        for i in range(0, len(outputdata)):
            connectionSocket.sendall(outputdata[i])
            
        connectionSocket.close()
    
    except IOError:
        http_response = """\
HTTP/1.1 404

<HTML>
<BODY>
File Not Found
</BODY>
</HTML>
"""
        connectionSocket.sendall(http_response)
        connectionSocket.close()

except IOError:
    http_response = """\
                    HTTP/1.1 4040 Not Found
                    """
    connectionSocket.sendall(http_response)
    connectionSocket.close()
        
print('Serving on %s ' % PORT)
while True:
    print('Ready to serve...')
    
    connectionSocket, addr = serverSocket.accept()
    
    try:
        request = connectionSocket.recv(1024)
        print(request)
         
        filename = request.split()[1]
        print(filename[1:])
         
        try:
            f = open(filename[1:], 'r')
            outputdata = f.readlines()
                    
            http_response = """\
HTTP/1.1 200 OK
 
"""                            
            connectionSocket.sendall(http_response)
             
            for i in range(0, len(outputdata)):
                connectionSocket.sendall(outputdata[i])
                 
            connectionSocket.close()
         
        except IOError:
            http_response = """\
HTTP/1.1 404
 
<HTML>
<BODY>
    File Not Found
</BODY>
</HTML>
"""
            connectionSocket.sendall(http_response)
            connectionSocket.close()
 
    except IOError:
        http_response = """\
                        HTTP/1.1 4040 Not Found
                        """
        connectionSocket.sendall(http_response)
        connectionSocket.close()
     
serverSocket.close()