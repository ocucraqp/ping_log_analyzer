class Log():
    def __init__(self, confirm_time, ip, response_time):
        self.ip = ip
        self.ping_response = [[confirm_time, response_time], ]

    def add_ping_log(self, confirm_time, response_time):
        self.ping_response.append([confirm_time, response_time])
