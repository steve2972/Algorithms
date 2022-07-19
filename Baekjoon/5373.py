def rotate(cube,idx):
    for _ in range(2):
        temp = cube[idx][0][0]
        cube[idx][0][0] = cube[idx][1][0]
        cube[idx][1][0] = cube[idx][2][0]
        cube[idx][2][0] = cube[idx][2][1]
        cube[idx][2][1] = cube[idx][2][2]
        cube[idx][2][2] = cube[idx][1][2]
        cube[idx][1][2] = cube[idx][0][2]
        cube[idx][0][2] = cube[idx][0][1]
        cube[idx][0][1] = temp
    

def move(cube, d):
    if d == 'U':
        temp = cube[0][0]
        cube[0][0] = cube[4][0]
        cube[4][0] = cube[5][0]
        cube[5][0] = cube[3][0]
        cube[3][0] = temp
        rotate(cube,2)
        
    elif d == 'D': 
        temp = cube[0][2]
        cube[0][2] = cube[3][2]
        cube[3][2] = cube[5][2]
        cube[5][2] = cube[4][2]
        cube[4][2] = temp
        rotate(cube,1)
        
    elif d == 'F': 
        temp = cube[2][2]
        cube[2][2] = [cube[3][2][2], cube[3][1][2], cube[3][0][2]]
        cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[1][0]
        cube[1][0] = [cube[4][2][0], cube[4][1][0], cube[4][0][0]]
        cube[4][0][0], cube[4][1][0], cube[4][2][0] = temp
        rotate(cube,0)
        
    elif d == 'B': 
        temp = cube[2][0]
        cube[2][0] = [cube[4][0][2], cube[4][1][2], cube[4][2][2]]
        cube[4][2][2], cube[4][1][2], cube[4][0][2] = cube[1][2]
        cube[1][2] = [cube[3][0][0], cube[3][1][0], cube[3][2][0]]
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = temp
        rotate(cube,5)    
        
    elif d == 'L': 
        temp = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[5][2][2], cube[5][1][2], cube[5][0][2]
        cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[1][2][0], cube[1][1][0], cube[1][0][0]
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = temp
        rotate(cube,3)
        
    elif d == 'R': 
        temp = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
        cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[2][2][2], cube[2][1][2], cube[2][0][2]
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = temp
        rotate(cube,4) 
        

for _ in range(int(input())):
    input()
    ops = list(map(str, input().split()))
    cube = [[] for _ in range(6)]
    for _ in range(3):
        cube[0].append(['r','r','r']); cube[1].append(['y','y','y']); cube[2].append(['w','w','w'])
        cube[3].append(['g','g','g']); cube[4].append(['b','b','b']); cube[5].append(['o','o','o'])
    for op in ops:
        d, c = op
        c = 1 if c == '+' else 3
        for _ in range(c): move(cube, d)
    for i in range(3): print(''.join(cube[2][i]))