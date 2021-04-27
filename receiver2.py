# pip install stomp.py
# run: docker run -p 61613:61613 -p 8161:8161 rmohr/activemq
# broker (admin - password) 61613 is stomp port
# activemq admin: http://localhost:8161/admin/ (admin - admin)
# run this script: python main.py This is a test


import time
import sys

import stomp

class MyListener2(stomp.ConnectionListener):
    def on_error(self, frame):
        print('received an error "%s"' % frame.body, flush=True)

    def on_message(self, frame):
        print('received a message "%s"' % frame.body, flush=True)

print("listening on receiver2", flush=True)
conn = stomp.Connection([('localhost', 61613)])
conn.set_listener('', MyListener2())
conn.connect('admin', 'password', wait=True)
conn.subscribe(destination='/topic/test', id=1, ack='auto')

time.sleep(200)
conn.disconnect()
