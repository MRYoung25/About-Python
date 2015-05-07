def LetterGeade(percentage):
    if percentage >= 85 and percentage <= 100:
        print "A"
    elif percentage >= 70 and percentage <= 84:
        print "B"
    elif percentage >= 55 and percentage <= 69:
        print "C"
    elif percentage >= 40 and percentage <= 54:
        print "D"
    elif percentage >= 25 and percentage <= 39:
        print "E"
    elif percentage >= 0 and percentage <= 24:
        print "F"
print LetterGeade(87)
