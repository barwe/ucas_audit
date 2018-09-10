import logging

from parse_week_ustring import parse_week_ustring
from if_A_is_contained_by_B import is_contained

ID_COL = 1
TIME_COL = 7

def filter(my_schedule, complete_classes):

    previous_id = None
    previous_valid = False
    valid_classes = []
    for item in complete_classes:

        id = item[ID_COL].value.strip('\t')
        time_ustr = item[TIME_COL].value
        nw, t = parse_week_ustring(time_ustr)

        if id != previous_id:
            if not is_contained(t, my_schedule[nw]):
                previous_valid = False
                continue
        else:
            if previous_valid == False:
                continue
            if not is_contained(t, my_schedule[nw]):
                valid_classes.pop()
                logging.info("Pop item(id={}): {}, not free!".format(previous_id, time_ustr))
                continue

        valid_classes.append(item)
        logging.info("Append item(id={}): {}".format(id, time_ustr))
        previous_valid = True

        previous_id = id

    return valid_classes
