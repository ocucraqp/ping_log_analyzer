import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('log', help='ログファイルのパス')
    args = parser.parse_args()
    return args
