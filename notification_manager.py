import config
import smtplib as smt


class NotificationManager:
    def __init__(self, fl_list, user_list):
        self.flight_list = fl_list
        self.send_list = []
        self.receiver = user_list

    def send(self):
        for i in self.flight_list:
            self.send_list.append(f"From {i['From']} to {i['To']}\nOnly at {i['Price']} EUR  On {i['Departure Date']} at {i['Departure Time']}")
        send = "\n\n\n".join(self.send_list)
        with smt.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()  # tls = Transfer Layer Security
            connection.login(user=config.MAIL_ID, password=config.PASSWORD)
            for email in self.receiver:
                connection.sendmail(from_addr=config.MAIL_ID, to_addrs=email,
                                    msg=f"Subject:'Low Price Alert !!!!'\n\n{send}")
