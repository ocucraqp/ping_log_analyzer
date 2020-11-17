from statistics import mean

from . import get_args, get_logs


def output_failure_period(log_file_path, N=1, m=-1, t=-1):
    """
    故障状態のサーバアドレスとそのサーバの故障期間をミリ秒で出力
    :param log_file_path: ログファイルのパス
    :param N: N回以上のタイムアウトで故障とみなす
    :param m, t: 直近m回の平均応答時間がtミリ秒を超えた場合に過負荷状態とみなす
    :return:
    """
    logs = get_logs.get_logs(log_file_path)

    overload_check_flg = False
    if m > 0:
        overload_check_flg = True

    for log in logs.values():
        timeout_num = 0
        timeout_start_time = -1

        overload_start_time = -1
        response_times_for_mean = []

        for res in log.ping_response:
            confirm_time, response_time = res
            if response_time == -1:
                timeout_num += 1
                if timeout_start_time == -1:
                    timeout_start_time = confirm_time * 1000
            else:
                if timeout_num >= N:
                    print('IP:{}'.format(log.ip))
                    print('    Timeout Start:{}'.format(timeout_start_time))
                    print('    Timeout End  :{}'.format(confirm_time * 1000 + response_time))
                    timeout_num = 0
                    timeout_start_time = -1

                # 過負荷状態の確認
                if overload_check_flg:
                    # 平均応答時間の計算
                    response_times_for_mean.append(response_time)

                    if len(response_times_for_mean) > m:
                        response_times_for_mean.pop(0)

                    mean_response_time = 0
                    if len(response_times_for_mean) == m:
                        mean_response_time = mean(response_times_for_mean)

                    if mean_response_time > t and overload_start_time == -1:
                        overload_start_time = confirm_time * 1000 + response_time

                    if mean_response_time <= t and overload_start_time != -1:
                        print('IP:{}'.format(log.ip))
                        print('    Overload Start:{}'.format(overload_start_time))
                        print('    Overload End  :{}'.format(confirm_time * 1000 + response_time))
                        overload_start_time = -1

        if timeout_num >= N:
            print('IP:{}'.format(log.ip))
            print('    Timeout Start:{}'.format(timeout_start_time))
            print('    Timeout End  :Fault condition')

        if overload_start_time != -1:
            print('IP:{}'.format(log.ip))
            print('    Overload Start:{}'.format(overload_start_time))
            print('    Overload End  :Overload conditions')


if __name__ == '__main__':
    args = get_args.get_args()
    log_file_path = args.log
    output_failure_period(log_file_path)
