import config
import  smtplib as smt


class NotificationManager:
    def __init__(self, fl_list):
        self.flight_list = fl_list
