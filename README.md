# ping_log_analyzer

## Requirements

- Python
- pip

## Installation

```bash
# リポジトリのクローン
git clone
cd 
# ライブラリのインストール
pip install
```

## Usage

./logsディレクトリ下に処理したいlogファイルを設置する．
（sample_log.txtのみ設置しており，sample_log.txt以外はgitで管理しない．）

### Task1

```bash
python -m ping_log_analyzer <log_file_name>

1. Failure period
2. Failure period after a certain number of timeouts
3. Overload condition Period
4. Network failure period for each subnet
5. Exit

Please what you want to output: 1
```

### Task2

```bash
python -m ping_log_analyzer <log_file_name>

1. Failure period
2. Failure period after a certain number of timeouts
3. Overload condition Period
4. Network failure period for each subnet
5. Exit

Please what you want to output: 2
```

### Task3

```bash
python -m ping_log_analyzer <log_file_name>

1. Failure period
2. Failure period after a certain number of timeouts
3. Overload condition Period
4. Network failure period for each subnet
5. Exit

Please what you want to output: 3
```

### Task4

```bash
python -m ping_log_analyzer <log_file_name>

1. Failure period
2. Failure period after a certain number of timeouts
3. Overload condition Period
4. Network failure period for each subnet
5. Exit

Please what you want to output: 4
```

ネットワークの故障期間（Network failure period）は，N回以上のタイムアウトの期間もしくは過負荷状態になっている期間または，その両方を出力する．

## Author

Masaya Ohura