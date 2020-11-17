from . import get_args, get_logs


def output_failure_period(log_file_path):
    """
    故障状態のサーバアドレスとそのサーバの故障期間を出力
    :param log_file_path: ログファイルのパス
    :return:
    """
    logs = get_logs.get_logs(log_file_path)


if __name__ == '__main__':
    args = get_args.get_args()
    log_file_path = args.log
    output_failure_period(log_file_path)
