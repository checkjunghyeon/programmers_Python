import re

def solution(record):
    logs = []
    user = {}
    
    for r in record:
        user_data = r.split(" ")
        mode, uid = user_data[:2]
        nickname = user_data[-1] if len(user_data) > 2 else None

        if mode == "Enter":
            logs.append(str(uid) + '님이 들어왔습니다.')
            user[uid] = nickname
        elif mode == "Leave":
            logs.append(str(uid) + '님이 나갔습니다.')
        else:
            user[uid] = nickname

    answer = []
    for log in logs:
        _uid = log.split('님')[0]
        answer.append(log.replace(_uid, user.get(_uid, _uid)))
    
    return answer
