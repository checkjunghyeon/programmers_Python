def solution(wallpaper):
    files = [
        [
        wallpaper[i][j] 
        for j in range(len(wallpaper[0]))
        ]
        for i in range(len(wallpaper))
    ]

    all_idx = [
        (i,j) for i in range(len(files)) 
        for j in range(len(files[0])) 
        if files[i][j]=='#']
    
    x_idx = [x[0] for x in all_idx]
    y_idx = [x[1] for x in all_idx]

    answer = [min(x_idx), min(y_idx), max(x_idx)+1, max(y_idx)+1]
    
    return answer