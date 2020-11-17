import argparse
import sys

from . import failure_period

# 引数の処理
parser = argparse.ArgumentParser()
parser.add_argument('log', help='ログファイルのパス')
args = parser.parse_args()

# ログファイルのパスの取得
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
    failure_period.output_failure_period()
elif task_num == 2:
    pass
elif task_num == 3:
    pass
elif task_num == 4:
    pass
elif task_num == 5:
    # exit
    pass
else:
    print('Error: Please input 1~5', file=sys.stderr)
