# pip install stomp.py
# http://jasonrbriggs.github.io/stomp.py/api.html#establishing-a-connection
# run: docker run -p 61613:61613 -p 8161:8161 rmohr/activemq
# broker (admin - password) 61613 is stomp port
# activemq admin: http://localhost:8161/admin/ (admin - admin)
# run this script: python main.py This is a test

# this main.py is the publisher of a topic
# run the 2 receiver.pys first for a good demo


import time
import sys

import stomp


class MyListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print('received an error "%s"' % frame.body)

    def on_message(self, frame):
        print('received a message "%s"' % frame.body)


conn = stomp.Connection([('localhost', 61613)])
conn.set_listener('', MyListener())
conn.connect('admin', 'password', wait=True, headers = {'client-id': 'main'})
conn.subscribe(destination='/topic/test', id=1, ack='auto')
conn.send(body=' '.join(sys.argv[1:]), destination='/topic/test')
time.sleep(2)
conn.disconnect()

