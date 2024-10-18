import operator

def solution(genres, plays):

    musics = {}
    best_album = []
        
    for i, g in enumerate(genres):
        if g in musics:
            musics[g]['total'] += plays[i]
            musics[g]['plays'].append((plays[i], i))
        else:
            musics[g] = {"total": plays[i], "plays": [(plays[i], i)]}

    genre_rank = sorted(musics.keys(), key=lambda x: musics[x]['total'], reverse=True)
    
    for r in genre_rank:
        p = musics[r]['plays']
        p.sort(key=lambda x: (-x[0], x[1]))
        n = min(2, len(p))
        for i in p[:n]:
            best_album.append(i[1])   
    return best_album