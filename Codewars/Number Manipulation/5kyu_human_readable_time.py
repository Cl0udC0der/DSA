def make_readable(seconds):
    #divmod takes the quotient and the remainder, so we use it twice here
    #first is for the remainder of seconds, next is for the remainder of min
    #then we use the print format to align it with what's being asked
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return (f'{h:02d}:{m:02d}:{s:02d}')
    #print(str(hours) + ':' + str(min) + ':' + str(sec))
    #return (str(hours) + ':' + str(min) + ':' + str(sec))

def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)

def make_readable(seconds):
    h= seconds/60**2
    m= (seconds%60**2)/60
    s= (seconds%60**2%60)
    return "%02d:%02d:%02d" % (h, m, s)
    # Do something