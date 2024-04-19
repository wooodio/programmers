from collections import OrderedDict

def solution(players, callings):
    # for calling in callings:
    #     passing = players.index(calling)
    #     players[passing-1], players[passing] = players[passing], players[passing-1]
    # 리스트의 index()는 시간복잡도가 큼 -> OrderDict 사용
    players_idx = {player:idx for idx,player in enumerate(players)}
    for calling in callings:
        passing = players_idx[calling]
        back = players[passing-1]
        players[passing-1], players[passing] = players[passing], players[passing-1]
        players_idx[calling] -=1
        players_idx[back] +=1

    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"],["kai", "kai", "mine", "mine"]))