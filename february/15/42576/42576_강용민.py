from collections import Counter

def solution(participant, completion):
    dict_part = Counter(participant)
    dict_comp = Counter(completion)

    return [key for key in (dict_part - dict_comp)][0]