from statistics import mean

from . import get_args, get_logs


def output_failure_period(log_file_path, N=1, m=-1, t=-1, task=1):
    """
    故障状態のサーバアドレスとそのサーバの故障期間をミリ秒で出力
    :param network_flg: ネットワークの故障期間を出力するか
    :param log_file_path: ログファイルのパス
    :param N: N回以上のタイムアウトで故障とみなす
    :param m, t: 直近m回の平均応答時間がtミリ秒を超えた場合に過負荷状態とみなす
    :return:
    """
    logs, networks = get_logs.get_logs(log_file_path)

    if task == 1:
        N = 1

    overload_check_flg = False
    if task == 3:
        overload_check_flg = True

    for log in logs.values():
        timeout_num = 0
        timeout_start_time = -1

        overload_start_time = -1
        response_times_for_mean = []

        for res in log.ping_response:
            confirm_time, response_time = res

            # タイムアウト時の処理
            if response_time == -1:
                timeout_num += 1
                if timeout_start_time == -1:
                    timeout_start_time = confirm_time * 1000
            else:
                # 故障期間の出力
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

                    # 過負荷状態期間の出力
                    if mean_response_time <= t and overload_start_time != -1:
                        print('IP:{}'.format(log.ip))
                        print('    Overload Start:{}'.format(overload_start_time))
                        print('    Overload End  :{}'.format(confirm_time * 1000 + response_time))
                        overload_start_time = -1

        # 監視終了時の状態出力
        if timeout_num >= N:
            print('IP:{}'.format(log.ip))
            print('    Timeout Start:{}'.format(timeout_start_time))
            print('    Timeout End  :Fault condition')
        if overload_start_time != -1:
            print('IP:{}'.format(log.ip))
            print('    Overload Start:{}'.format(overload_start_time))
            print('    Overload End  :Overload conditions')

    # ネットワーク故障状態の出力
    if task == 4:
        for network in networks.values():
            timeout_start_time = -1

            for res in network.ping_response:
                ip, confirm_time, response_time = res

                # タイムアウト時の処理
                if response_time == -1:
                    if network.ip_condition[ip] < N:
                        network.ip_condition[ip] += 1
                    if sum(network.ip_condition.values()) >= N * len(network.ip_condition) and timeout_start_time == -1:
                        timeout_start_time = confirm_time * 1000
                else:
                    # 故障期間の出力
                    if sum(network.ip_condition.values()) >= N * len(network.ip_condition):
                        print('Network:{}'.format(network.subnet))
                        print('    Timeout Start:{}'.format(timeout_start_time))
                        print('    Timeout End  :{}'.format(confirm_time * 1000 + response_time))
                        network.ip_condition[ip] = 0
                        timeout_start_time = -1

            # 監視終了時の状態出力
            if sum(network.ip_condition.values()) >= N * len(network.ip_condition):
                print('Network:{}'.format(network.subnet))
                print('    Timeout Start:{}'.format(timeout_start_time))
                print('    Timeout End  :Fault condition')


if __name__ == '__main__':
    args = get_args.get_args()
    log_file_path = args.log
    task = args.task
    try:
        N = int(args.N)
    except TypeError as e:
        N = 1
    try:
        m = int(args.m)
        t = int(args.t)
    except TypeError as e:
        m = -1
        t = -1
    output_failure_period(log_file_path, N, m, t, task)
