import time
from interface import *
from sender import SenderBroker
from receiver import ReceiverBroker


class Chatroom():

    # TODO memory leak
    def on_closing(self):
        # check if saving
        # if not:
        # listener.discard_channel()
        self.root.destroy()
        self.app.disconnect_from_server()

    def run(self, user):
        self.root = Tk()
        self.root.title("Talky Walky")
        self.root.geometry(default_window_size)
        self.root.minsize(360, 200)

        # start application
        #sender = SenderBroker()
        #listener = ReceiverBroker()

        #sender.connect(exchange="room 1")
        #listener.connect(exchange="room 1")

        self.app = ChatInterface(self.root, fullname=user)
        # connect
        # app.connect_to_server('JOE')

        # do what u want

        # app.select_room('room1')
        #app.send_msg_to_room('room1', 'hello man!')

        # start consuming
        # app.async_consumer()

        self.app.default_format()

        # listener.async_consumer(app.on_message_recieved)

        # root is your root window
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

        self.root.mainloop()


# c = Chatroom()
# c.run(user="self.USERNAME")
