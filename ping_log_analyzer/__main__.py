import sys

from . import failure_period, get_args

# パラメータの取得
args = get_args.get_args()
log_file_path = args.log
task = int(args.task)

# タスク毎に解析を実行
if task == 1:
    failure_period.output_failure_period(log_file_path)
elif task == 2:
    try:
        N = int(args.N)
        failure_period.output_failure_period(log_file_path, N=N, task=task)
    except TypeError as e:
        print('Error: Please input N', file=sys.stderr)
elif task == 3:
    try:
        N = int(args.N)
        m = int(args.m)
        t = int(args.t)
        failure_period.output_failure_period(log_file_path, m=m, t=t, task=task)
    except TypeError as e:
        print('Error: Please input N, m, t', file=sys.stderr)
elif task == 4:
    try:
        N = int(args.N)
        failure_period.output_failure_period(log_file_path, N=N, task=task)
    except TypeError as e:
        print('Error: Please input N', file=sys.stderr)
else:
    print('Error: Please input 1~4', file=sys.stderr)
