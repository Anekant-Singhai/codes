while(True):
    inp = input().split(' ')
    if inp == ['0','0']:
        break
    s = list(range(int(inp[1])+1))
    s.remove(0)
    while(True):
        pos = int((len(s)+1)/2 - 1)
        print('1',s[pos])
        domino = input().split(' ')
        if domino == ['0', '0'] or domino == ['-1', '-1']:
            break
        elif int(domino[1]) > s[pos]:
            if len(s) % 4 == 3:
                del s[pos:]
            else:
                del s[:(pos+2)]
        else:
            if len(s) % 4 == 3:
                del s[:(pos+1)]
            else:
                del s[(pos-1):]
