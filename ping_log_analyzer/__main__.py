import sys

from . import failure_period, get_args

# ログファイルのパスの取得
args = get_args.get_args()
log_file_path = args.log

# Taskの選択
print('1. Failure period\n'
      '2. Failure period after a certain number of timeouts\n'
      '3. Overload condition Period\n'
      '4. Network failure period for each subnet\n'
      '5. Exit\n'
      '\n')
task_num = int(input('Please what you want to output: '))

if task_num == 1:
    failure_period.output_failure_period(log_file_path)
elif task_num == 2:
    N = int(input('Please input Indicators of failure: '))
    failure_period.output_failure_period(log_file_path, N)
elif task_num == 3:
    pass
elif task_num == 4:
    pass
elif task_num == 5:
    # exit
    pass
else:
    print('Error: Please input 1~5', file=sys.stderr)
