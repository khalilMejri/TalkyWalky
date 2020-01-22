import time
from interface import *
from sender import SenderBroker
from receiver import ReceiverBroker


# TODO memory leak
def on_closing():
    # check if saving
    # if not:
    # listener.discard_channel()
    root.destroy()
    app.disconnect_from_server()

# start application
#sender = SenderBroker()
#listener = ReceiverBroker()

#sender.connect(exchange="room 1")
#listener.connect(exchange="room 1")

app = ChatInterface(root)
# connect
# app.connect_to_server('JOE')

# do what u want

# app.select_room('room1')
#app.send_msg_to_room('room1', 'hello man!')

# start consuming
# app.async_consumer()

app.default_format()


# listener.async_consumer(app.on_message_recieved)

root.protocol('WM_DELETE_WINDOW', on_closing)  # root is your root window

root.mainloop()
