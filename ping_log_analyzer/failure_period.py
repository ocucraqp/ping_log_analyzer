from statistics import mean

from . import get_logs


def output(net_type, net, error_type, start_time, end_time=-1):
    output_str = '{}:{}\n'.format(net_type, net)
    output_str += '    {} Start:{}\n'.format(error_type, start_time)
    if end_time >= 0:
        output_str += '    {} End  :{}\n'.format(error_type, end_time)
    else:
        output_str += '    {} End  :{} condition\n'.format(error_type, error_type)
    print(output_str)
    return output_str


def output_failure_period(log_file_path, N=1, m=-1, t=-1, task=1):
    """
    故障状態のサーバアドレスとそのサーバの故障期間をミリ秒で出力
    :param network_flg: ネットワークの故障期間を出力するか
    :param log_file_path: ログファイルのパス
    :param N: N回以上のタイムアウトで故障とみなす
    :param m, t: 直近m回の平均応答時間がtミリ秒を超えた場合に過負荷状態とみなす
    :return: outputs:
    """

    outputs = ''

    # ログファイルからip毎，ネットワーク毎のログデータを取得
    logs, networks = get_logs.get_logs(log_file_path)

    # flg等の管理
    if task == 1:
        N = 1
    if task == 3:
        overload_check_flg = True
    else:
        overload_check_flg = False
    if task == 4:
        network_flg = True
    else:
        network_flg = False

    # ip毎のログ解析の実行
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
                    outputs += output('IP', log.ip, 'Timeout', timeout_start_time, confirm_time * 1000 + response_time)
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

                    # 過負荷開始時間の計算
                    if mean_response_time > t and overload_start_time == -1:
                        overload_start_time = confirm_time * 1000 + response_time

                    # 過負荷状態期間の出力
                    if mean_response_time <= t and overload_start_time != -1:
                        outputs += output('IP', log.ip, 'Overload', overload_start_time,
                                          confirm_time * 1000 + response_time)
                        overload_start_time = -1

        # 監視終了時の状態出力
        if timeout_num >= N:
            outputs += output('IP', log.ip, 'Timeout', timeout_start_time)
        if overload_start_time != -1:
            outputs += output('IP', log.ip, 'Overload', overload_start_time)

    # ネットワーク故障状態の出力
    if network_flg:
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
                        outputs += output('Network', network.subnet, 'Timeout', timeout_start_time,
                                          confirm_time * 1000 + response_time)
                        network.ip_condition[ip] = 0
                        timeout_start_time = -1

            # 監視終了時の状態出力
            if sum(network.ip_condition.values()) >= N * len(network.ip_condition):
                outputs += output('Network', network.subnet, 'Timeout', timeout_start_time)

    return outputs

# if __name__ == '__main__':
#     args = get_args.get_args()
#     log_file_path = args.log
#     task = args.task
#     try:
#         N = int(args.N)
#     except TypeError as e:
#         N = 1
#     try:
#         m = int(args.m)
#         t = int(args.t)
#     except TypeError as e:
#         m = -1
#         t = -1
#     output_failure_period(log_file_path, N, m, t, task)
