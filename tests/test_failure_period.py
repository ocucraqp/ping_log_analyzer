from ping_log_analyzer.failure_period import output_failure_period


def test_output_failure_period_1_1():
    # タイムアウトがあったとき
    with open('tests/test_log_answers/answer_1_1.txt') as f:
        s = f.read()
        output = output_failure_period('tests/test_logs/test_log_1_1.txt')
        output = output.replace('\n', '')
        s = s.replace('\n', '')
        assert output == s


def test_output_failure_period_1_2():
    # タイムアウト後回復したとき
    with open('tests/test_log_answers/answer_1_2.txt') as f:
        s = f.read()
        output = output_failure_period('tests/test_logs/test_log_1_2.txt')
        output = output.replace('\n', '')
        s = s.replace('\n', '')
        assert output == s


def test_output_failure_period_1_3():
    # タイムアウトがなかったとき
    with open('tests/test_log_answers/answer_1_3.txt') as f:
        s = f.read()
        output = output_failure_period('tests/test_logs/test_log_1_3.txt')
        output = output.replace('\n', '')
        s = s.replace('\n', '')
        assert output == s


def test_output_failure_period_2_1():
    # N回以上連続タイムアウトがなかったとき
    with open('tests/test_log_answers/answer_2_1.txt') as f:
        s = f.read()
        output = output_failure_period('tests/test_logs/test_log_2_1.txt', N=2, task=2)
        output = output.replace('\n', '')
        s = s.replace('\n', '')
        assert output == s


def test_output_failure_period_2_2():
    # N回以上連続タイムアウトがあったとき
    with open('tests/test_log_answers/answer_2_2.txt') as f:
        s = f.read()
        output = output_failure_period('tests/test_logs/test_log_2_2.txt', N=2, task=2)
        output = output.replace('\n', '')
        s = s.replace('\n', '')
        assert output == s


def test_output_failure_period_3_1():
    # 過負荷状態があったとき
    with open('tests/test_log_answers/answer_3_1.txt') as f:
        s = f.read()
        output = output_failure_period('tests/test_logs/test_log_3_1.txt', N=2, m=2, t=9, task=3)
        output = output.replace('\n', '')
        s = s.replace('\n', '')
        assert output == s


def test_output_failure_period_4_1():
    # ネットワーク障害があったとき
    with open('tests/test_log_answers/answer_4_1.txt') as f:
        s = f.read()
        output = output_failure_period('tests/test_logs/test_log_4_1.txt', N=2, task=4)
        output = output.replace('\n', '')
        s = s.replace('\n', '')
        assert output == s


def test_output_failure_period_4_2():
    # ネットワーク障害がなかったとき（1台がすぐに復旧）
    with open('tests/test_log_answers/answer_4_2.txt') as f:
        s = f.read()
        output = output_failure_period('tests/test_logs/test_log_4_2.txt', N=2, task=4)
        output = output.replace('\n', '')
        s = s.replace('\n', '')
        assert output == s
