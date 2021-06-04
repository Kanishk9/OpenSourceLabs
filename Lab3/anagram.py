def anagram(c1, c2):
    l1 = len(c1)
    l2 = len(c2)

    if l1 != l2:
        return 0

    s1 = sorted(c1)
    s2 = sorted(c2)

    for i in range(0,l1):
        if s1[i] != s2[i]:
            return 0
    return 1

if anagram('ate','aio'):
    print("Is anagram")
else:
    print('Is not an anagram')