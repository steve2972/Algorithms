def solution(new_id):
    # Step 1
    assert type(new_id) == str
    new_id = new_id.lower()
    # Step 2
    for c in new_id:
        if c.isalnum() == False and c not in '-._': 
            new_id = new_id.replace(c, '')

    # Step 3
    dot_idx = None
    idx = 0
    while idx < len(new_id):
        if new_id[idx] == '.':
            if dot_idx == None: 
                dot_idx = idx
                idx += 1
            elif idx == dot_idx + 1:
                new_id = new_id[:idx] + new_id[idx+1:]
            else: 
                dot_idx = idx
                idx += 1
        else: idx += 1
    # Step 4
    new_id = new_id.lstrip('.').rstrip('.')
    # Step 5
    if new_id == '': new_id='a'

    # Step 6
    if len(new_id) > 15: new_id = new_id[:15]
    new_id = new_id.rstrip('.')

    # Step 7
    if len(new_id) <= 2:
        new_id = new_id + new_id[-1]*(3-len(new_id))

    return new_id

s ="123_.def"
print(solution(s))