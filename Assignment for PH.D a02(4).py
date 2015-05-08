def Middle(n1, n2, n3):
    if n1 == n2 == n3:
        print "Middle:", n1
    elif n1 != n2 != n3:
        s = cmp(n1, n2)
        if s == 1:
            t = cmp(n1, n3)
            if t == -1:
                print "Middle:", n1
            if t == 1:
                u = cmp(n2, n3)
                if u == 1:
                    print "Middle:", n2
                else:
                    print "Middle:", n3
        elif s == -1:
            t = cmp(n2, n3)
            if t == 1:
                print "Middle:", n3
            else:
                print "Middle:", n2
    else:
        print "Middle : invalid arguments"
print Middle(7, 1, 3)
