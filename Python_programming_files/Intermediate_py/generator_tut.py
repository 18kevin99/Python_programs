CORRECT_COMBO = (3, 6, 1)

#instead of doing this

##found_combo = False
##for c1 in range(10):
##    if found_combo:
##        break
##    for c2 in range(10):
##        if found_combo:
##            break
##        for c3 in range(10):
##            if (c1,c2,c3) == CORRECT_COMBO:
##                print('found combo:{}'.format((c1,c2,c3)))
##                found_combo = True
##                break
##            print(c1,c2,c3)


# do this

def pass_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1,c2,c3)

for (c1,c2,c3) in pass_gen():
    if (c1,c2,c3) == CORRECT_COMBO:
        print('found combo:{}'.format((c1,c2,c3)))
        break
    print(c1,c2,c3)
