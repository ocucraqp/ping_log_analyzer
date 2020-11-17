# ping_log_analyzer

pingで得たログの解析を行う．

## 準備

- Python:3.8

```bash
# リポジトリのクローン
git clone https://github.com/ocucraqp/fixpoint_test.git
cd fixpoint_test
```

## 使い方

./logsディレクトリ下に処理したいlogファイルを設置する．
（sample_log.txtのみ設置しており，sample_log.txt以外はgitで管理しない．）
実行するタスクによって引数を選択する

```bash
# task1
python -m ping_log_analyzer logs/sample_log.txt 1
# task2
python -m ping_log_analyzer logs/sample_log.txt 2 -N 2
# task3
python -m ping_log_analyzer logs/sample_log.txt 3 -N 2 -m 2 -t 9
# task4
python -m ping_log_analyzer logs/sample_log.txt 4 -N 2
```

詳しい引数の使い方は以下の通りである
```bash
usage: __main__.py [-h] [-N N] [-m M] [-t T] log task

positional arguments:
  log         Path of log file
  task        Task number
              1. Failure period
              2. Failure period after a certain number of timeouts
              3. Overload condition Period
              4. Network failure period for each subnet

optional arguments:
  -h, --help  show this help message and exit
  -N N        Indicators of failure
  -m M        Number of response times to account for
              overloads
  -t T        The average response time to be overloaded
```

## 補足

- ログ終了まで故障状態が終了しない場合は，`Fault condition`と出力される
- ログ終了まで過負荷状態が終了しない場合は，`Overload conditions`と出力される

## Author

Masaya Ohura