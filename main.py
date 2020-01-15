import time
from interface import *
from sender import SenderBroker
from receiver import ReceiverBroker


# TODO memory leak
def on_closing():
    # check if saving
    # if not:
    listener.discard_channel()
    root.destroy()


# start application
sender = SenderBroker()
listener = ReceiverBroker()

sender.connect(exchange="room 1")
listener.connect(exchange="room 1")

app = ChatInterface(root, sender_broker=sender, receiver_broker=listener)
app.default_format()

listener.async_consumer(app.on_message_recieved)

root.protocol('WM_DELETE_WINDOW', on_closing)  # root is your root window

root.mainloop()