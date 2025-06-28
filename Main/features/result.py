def result(choices_made):
    result_list = []
    result_value = 0.0
    for i in range(1, 16):
        result_value += choices_made[i]
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

def diagnosis_type(diagnosis):
    if diagnosis == ['ブラックユーモア型', 'センス型', 'シュール型']:
        return "BCS"
    elif diagnosis == ['ブラックユーモア型', 'センス型', 'ストレート型']:
        return "BCG"
    elif diagnosis == ['ブラックユーモア型', 'リアクション型', 'シュール型']:
        return "BRS"
    elif diagnosis == ['ブラックユーモア型', 'リアクション型', 'ストレート型']:
        return "BRG"
    elif diagnosis == ['ホワイトユーモア型', 'センス型', 'シュール型']:
        return "WCS"
    elif diagnosis == ['ホワイトユーモア型', 'センス型', 'ストレート型']:
        return "WCG"
    elif diagnosis == ['ホワイトユーモア型', 'リアクション型', 'シュール型']:
        return "WRS"
    else:
        return "WRG"

def diagnosis_sentences(diagnosis_type):
    if diagnosis_type == "BCS":
        return """
        <div style="text-align:center; font-size:18px; color:#dddddd; max-width:700px; margin:auto;">
        <p>あなたは、知的な深淵に微笑む“観察者タイプ”</p>

        <p>◆ あなたの特徴：</p>
        <p>世間の「当たり前」にどこか冷めた視点を持ち、</p>

        <p>ただ笑うだけでなく「この笑い、刺さるな…」と心の奥でニヤリとするタイプ。</p>

        <p>他人には説明しづらい“ズレ”や“毒”のバランス感覚に、美学すら感じる。</p>

        <p>自分の中に「影」や「不安定さ」を抱えながらも、それすら笑いに変える強さを持っている。</p>

        <p>◆ あなたが惹かれるもの：</p>
        <p>コントや漫才の裏に隠れた社会風刺や構造の巧妙さ</p>

        <p>一見意味不明だけど、よく考えると深い皮肉や哲学が込められているネタ</p>

        <p>誰も大声で笑っていない場面で、ひとり静かに笑える“ひねくれ美”</p>

        <p>◆ あなたにぴったりの芸人は：</p>
        <p>バカリズム（構成・毒・ズレ）</p>

        <p>くっきー！（狂気と芸術）</p>

        <p>ラーメンズ（世界観と静かな破壊力）</p>

        <p>◆ ひとこと診断：</p>
        <p>「あなたにとって笑いとは、“逃避”ではなく“思考”であり、“破壊”であり、“再構築”です。</p>
        <p>他人が笑い終えたあとに、ひとりで考え続けているような人。」</p>

        </div>
        """
    elif diagnosis_type == "BCS":
        return None
    elif diagnosis_type == "BCS":
        return None
    elif diagnosis_type == "BCS":
        return None
    elif diagnosis_type == "BCS":
        return None
    elif diagnosis_type == "BCS":
        return None
    elif diagnosis_type == "BCS":
        return None
    else:
        return None