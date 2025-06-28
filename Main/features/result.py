def result(choices_made):
    result_list = []
    result_value = 0.0
    for i in range(1, 16):
        result_value += choices_made[i]
        print(result_value)
        if i % 5 == 0:
            result_list.append(result_value)
            result_value = 0.0
    return result_list

def diagnosis_based_on_result(result):
    diagnosis = []
    if result[0] < 0.0:
        diagnosis.append("ブラックユーモア型")
    elif result[0] > 0.0:
        diagnosis.append("ホワイトユーモア型")
    if result[1] < 0.0:
        diagnosis.append("センス型")
    elif result[1] > 0.0:
        diagnosis.append("リアクション型")
    if result[2] < 0.0:
        diagnosis.append("シュール型")
    elif result[2] > 0.0:
        diagnosis.append("ストレート型")
    return diagnosis