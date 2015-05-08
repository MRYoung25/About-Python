def ToSeconds(days, hours, minutes, seconds):
    ToSeconds = days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds
    return  ToSeconds
print ToSeconds(11, 13, 46, 40)
