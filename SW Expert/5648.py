import sys
sys.stdin = open("input.txt", "r")

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for test_case in range(T):
    energy = 0
    n = int(input())
    atoms = {}
    for i in range(n):
        x, y, d, k = list(map(int, input().split()))
        atoms[i] = [x,y,d,k]
    remaining = set(atoms.keys())

    while remaining:
        cur_pos = {}
        for i in remaining:
            x, y, d, k = atoms[i]
            nx = x + dx[d] * 0.5
            ny = y + dy[d] * 0.5
            if (nx, ny) not in cur_pos:
                cur_pos[(nx,ny)] = [[i], k]
            else:
                atom_list, energies = cur_pos[(nx,ny)]
                atom_list.append(i)
                cur_pos[(nx,ny)] = [atom_list, energies + k]
            atoms[i] = [nx, ny, d, k]

        for key in cur_pos.keys():
            atom_list, energies = cur_pos[key]
            if len(atom_list) > 1:
                energy += energies
                for i in atom_list:
                    remaining.remove(i)
                    del atoms[i]

        for i in remaining:
            x, y, _, _ = atoms[i]
            if abs(x) > 1000 or abs(y) > 1000:
                del atoms[i]
        remaining = set(atoms.keys())
    print(f"#{test_case+1} {energy}")
