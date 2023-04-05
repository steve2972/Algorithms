def biggerIsGreater(w):
    word = list(w)
    for i in range(len(word)-1, 0, -1):
        if word[i] > word[i-1]:
            for j in range(len(word)-1, i-1, -1):
                if word[j] > word[i-1]:
                    word[i-1], word[j] = word[j], word[i-1]
                    word[i:] = sorted(word[i:])
                    return ''.join(word)
                
    return 'no answer'