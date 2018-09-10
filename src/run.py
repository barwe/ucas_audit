import os, logging
logging.basicConfig(level=logging.WARNING)
from parse_my_schedule import parse_my_schedule
from parse_complete_classes import parse_complete_classes
from filter import filter
from dump_as import dump_all, dump_part

project_dir = os.path.abspath('.{}..'.format(os.sep))
static_dir = '{1}{0}static'.format(os.sep, project_dir)

_fp = os.path.abspath('{1}{0}my_schedule.csv'.format(os.sep, static_dir))
my_schedule = parse_my_schedule(_fp) # dict:int->list(11)

_fp = os.path.abspath('{1}{0}complete_classes.xlsx'.format(os.sep, static_dir))
complete_classes, header = parse_complete_classes(_fp) # generator

vcls = filter(my_schedule=my_schedule, complete_classes=complete_classes)

dump_part(vcls, header, output_fp='{1}{0}result_part.csv'.format(os.sep, project_dir))
dump_all(vcls, header, output_fp='{1}{0}result_all.csv'.format(os.sep, project_dir))
