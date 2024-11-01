def solution(wallpaper):
    x_idx, y_idx = [], []
    for i, file in enumerate(wallpaper):
        for j, f in enumerate(file):
            if f == '#':
                x_idx.append(i)
                y_idx.append(j)

    answer = [min(x_idx), min(y_idx), max(x_idx)+1, max(y_idx)+1]
    
    return answer