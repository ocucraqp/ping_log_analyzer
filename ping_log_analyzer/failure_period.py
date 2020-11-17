from . import get_args, get_logs


def output_failure_period(log_file_path):
    """
    故障状態のサーバアドレスとそのサーバの故障期間をミリ秒で出力
    :param log_file_path: ログファイルのパス
    :return:
    """
    logs = get_logs.get_logs(log_file_path)
    for log in logs.values():
        timeout_num = 0
        timeout_start_time = 0
        for res in log.ping_response:
            if res[1] == -1:
                timeout_num += 1
                timeout_start_time = res[0]
            else:
                if timeout_num > 0:
                    print('IP:{}'.format(log.ip))
                    print('    Timeout Start:{}'.format(timeout_start_time * 1000))
                    print('    Timeout End  :{}'.format(res[0] * 1000 + res[1]))
                    timeout_num = 0

        if timeout_num > 0:
            print('IP:{}'.format(log.ip))
            print('    Timeout Start:{}'.format(timeout_start_time * 1000))
            print('    Timeout End  :Out of Service')


if __name__ == '__main__':
    args = get_args.get_args()
    log_file_path = args.log
    output_failure_period(log_file_path)