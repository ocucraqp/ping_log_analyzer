from . import get_args


def get_logs(log_file_path):
    """
    ログデータを解析して取得する
    :param log_file_path: ログファイルのパス
    :return: logs: 解析済みログデータ
    """
    logs = []
    with open(log_file_path) as log_file:
        for log in log_file:
            log = log.rstrip('\n')
            logs.append(log.split(','))
    return logs


if __name__ == '__main__':
    args = get_args.get_args()
    log_file_path = args.log
    get_logs(log_file_path)
