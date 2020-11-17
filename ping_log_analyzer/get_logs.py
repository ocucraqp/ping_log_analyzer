from . import get_args, log


def get_logs(log_file_path):
    """
    ログデータを解析して取得する
    :param log_file_path: ログファイルのパス
    :return: logs: 解析済みログデータ
    """
    parse_logs = []
    with open(log_file_path) as log_file:
        for line in log_file:
            line = line.rstrip('\n')
            parse_logs.append(line.split(','))

    logs = {}
    for parse_log in parse_logs:
        confirm_time, ip, response_time = parse_log
        if ip in logs:
            logs[ip].add_ping_log(confirm_time, response_time)
        else:
            logs[ip] = log.Log(confirm_time, ip, response_time)

    return logs


if __name__ == '__main__':
    args = get_args.get_args()
    log_file_path = args.log
    get_logs(log_file_path)
