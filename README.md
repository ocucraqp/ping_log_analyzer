# ping_log_analyzer

pingで得たログの解析を行う．

## 準備

- Python:3.8
- pipenv

```bash
# リポジトリのクローン
git clone https://github.com/ocucraqp/ping_log_analyzer.git
cd ping_log_analyzer
# テストを実行する場合
pipenv install
```

## ディレクトリ構成

.  
├── `Pipfile`  
├── `Pipfile.lock`  
├── `README.md`  
├── `logs`  
│　　　└── `sample_log.txt`  
├── `ping_log_analyzer`(プロジェクト)  
│　　　├── `__init__.py`  
│　　　├── `__main__.py`  
│　　　├── `failure_period.py`  
│　　　├── `get_args.py`  
│　　　└── `get_logs.py`  
└── `tests`  
　　├── `__init__.py`  
　　├── `test_failure_period.py`  
　　├── `test_log_answers`  
　　│　　└── テストの解答  
　　└── `test_logs`  
　　　　　└── テスト用ログ  

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
# テストの実行
pytest
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

- ログ終了まで故障状態が終了しない場合は，`Timeout condition`と出力される
- ログ終了まで過負荷状態が終了しない場合は，`Overload conditions`と出力される

## テストについて
テスト用のソースコードは`tests/test_failure_period.py`である．
また，テストに用いているログとテストの解答はそれぞれ，`tests/test_logs`と`tests/test_log_answer`下に配置している．
現段階で用意しているテスト8つに対してはすべて通過を確認している

## Author

Masaya Ohura
