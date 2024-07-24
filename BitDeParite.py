def CorrectionPair(msg):
    msg = str(msg)
    if msg.count('1') % 2 == 0:
        msg = '0'+msg
    else:
        msg = '1'+msg
    return msg


def CorrectionImpair(msg):
    msg = str(msg)
    if msg.count('1') % 2 == 0:
        msg = '1'+msg
    else:
        msg = '0'+msg
    return msg


print(CorrectionPair(101110))
