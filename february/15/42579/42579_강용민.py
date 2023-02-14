from collections import defaultdict
def solution(genres, plays):
    answer = []
    dict_genre = defaultdict(int)
    dict_play = defaultdict(list)
    for idx,(genre,play) in enumerate(zip(genres,plays)):
        dict_genre[genre] += play
        dict_play[genre] += [(idx,play)]

    for (genre,play) in sorted(dict_genre.items(),key = lambda item : item[1],reverse= True):
        play_list = sorted(dict_play[genre],key = lambda item : item[1],reverse=True)
        answer.append(play_list[0][0])
        if len(play_list) > 1:
            answer.append(play_list[1][0])  

    return answer