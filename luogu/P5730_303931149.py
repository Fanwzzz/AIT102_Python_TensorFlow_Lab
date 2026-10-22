n = int(input())
dis = {"0": ["XXX","X.X","X.X","X.X","XXX"], 
       "1": ["..X","..X","..X","..X","..X"], 
       "2": ["XXX","..X","XXX","X..","XXX"],
       "3": ["XXX","..X","XXX","..X","XXX"],
       "4": ["X.X","X.X","XXX","..X","..X"],
       "5": ["XXX","X..","XXX","..X","XXX"],
       "6": ["XXX","X..","XXX","X.X","XXX"],
       "7": ["XXX","..X","..X","..X","..X"],
       "8": ["XXX","X.X","XXX","X.X","XXX"],
       "9": ["XXX","X.X","XXX","..X","XXX"]}

num = str(input())
for i in range(5):
    row = []
    for j in range(n-1):
        row.append(dis[num[j]][i]+".")
    row.append(dis[num[n-1]][i])
    print("".join(row))