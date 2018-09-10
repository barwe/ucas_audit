import csv

def parse_my_schedule(fp):

    free_time = {}
    for i in range(1,8):
        free_time[i] = []

    csv_reader = csv.reader(open(fp, 'r'))

    for line in csv_reader:
        if csv_reader.line_num == 1:
            continue
        for i,v in enumerate(line):
            if i == 0:
                continue
            free_time[i].append(int(line[i]))

    # for k in free_time: print(free_time[k])

    return free_time
