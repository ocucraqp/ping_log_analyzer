import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('log', help='Path of log file')
    parser.add_argument('task', help='Task number'
                                     '1. Failure period\n'
                                     '2. Failure period after a certain number of timeouts\n'
                                     '3. Overload condition Period\n'
                                     '4. Network failure period for each subnet\n')
    parser.add_argument('-N', help='Indicators of failure')
    parser.add_argument('-m', help='Number of response times to account for overloads')
    parser.add_argument('-t', help='The average response time to be overloaded')
    args = parser.parse_args()
    return args
