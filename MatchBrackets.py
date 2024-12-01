def matchBrackets(Object):
    bracs = str(Object)

    openn = "{[("
    close = "}])"

    track=""
    bracket_map = {
    '(': ')',
    ')': '(',
    '{': '}',
    '}': '{',
    '[': ']',
    ']': '['
    }
    n = len(bracs)
    i=0
    for brac in bracs:
        i = i+1
        if bracs[0] in close:
            return False
        elif brac in openn and i != n:
            track = track+brac
        elif brac in close and len(track) > 0 :
            if brac == bracket_map[track[-1]]:
                track = track[:-1]

                if i > n-1 and len(track) == 0:
                    # sli=track[:len(track)-1]
                    # track = sli
                    # print(track)
                    return True
            else:
                return False
        else:
            return False   



test = "([])}{"
print(matchBrackets(test))
