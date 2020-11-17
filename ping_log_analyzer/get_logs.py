class Log:
    def __init__(self, confirm_time, ip, response_time):
        self.ip = ip
        # pingがタイムアウトした場合，response_timeは-1
        self.ping_response = [[confirm_time, response_time], ]

    def add_ping_log(self, confirm_time, response_time):
        self.ping_response.append([confirm_time, response_time])


class Network:
    def __init__(self, confirm_time, ip, subnet, response_time):
        # ip_conditionがN以上のとき故障
        self.ip_condition = {}
        self.ip_condition[ip] = 0
        self.subnet = subnet
        # pingがタイムアウトした場合，response_timeは-1
        self.ping_response = [[ip, confirm_time, response_time], ]

    def add_ip(self, ip):
        self.ip_condition[ip] = 0

    def add_ping_log(self, ip, confirm_time, response_time):
        self.ping_response.append([ip, confirm_time, response_time])


def get_logs(log_file_path):
    """
    ログデータを解析して取得する
    :param log_file_path: ログファイルのパス
    :return: logs: ip毎の解析済みログデータ
    :return: networks: subnet毎の解析済みログデータ
    """
    parse_logs = []
    with open(log_file_path) as log_file:
        for line in log_file:
            line = line.rstrip('\n')
            parse_logs.append(line.split(','))

    logs = {}
    networks = {}
    for parse_log in parse_logs:
        confirm_time, ip, response_time = parse_log

        if response_time == '-':
            # pingがタイムアウト('-')した場合，response_timeは-1
            response_time = -1

        if ip in logs:
            logs[ip].add_ping_log(int(confirm_time), int(response_time))
        else:
            logs[ip] = Log(int(confirm_time), ip, int(response_time))

        ip, subnet = ip.split('/')
        if subnet in networks:
            if ip not in networks[subnet].ip_condition:
                networks[subnet].add_ip(ip)
            networks[subnet].add_ping_log(ip, int(confirm_time), int(response_time))
        else:
            networks[subnet] = Network(int(confirm_time), ip, subnet, int(response_time))

    return logs, networks
