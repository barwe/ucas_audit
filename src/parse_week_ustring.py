import logging

WEEKS = {u'周一':1, u'周二':2, u'周三':3, u'周四':4, u'周五':5, u'周六':6, u'周日':7}

def parse_week_ustring(ustring):

    ustrings = ustring.strip(')').split('(')
    num_week = WEEKS.get(ustrings[0])

    if ustrings[1] == '1':
        start, stop = 1, 11
    else:
        start, stop = [int(i) for i in ustrings[1].split('-')]

    time = [0]*11
    for i in range(start-1, stop):
        time[i] = 1
    return num_week, time