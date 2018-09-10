import csv
import logging

from utls.adjust_integer import adjust_integer

simple_ids = [0, 1, 2, 7, 8]

def dump_all(RowCells_list, header, output_fp=None):
    with open(output_fp, 'w', encoding='utf-8') as writer:
        csv_writer = csv.writer(writer)
        csv_writer.writerow([i.value for i in header])
        for row in RowCells_list:
            csv_writer.writerow([i.value for i in row])
    logging.info("Dump to file {}".format(output_fp))

def dump_part(RowCells_list, header, output_fp=None):
    string = []
    header = [header[i].value for i in simple_ids]
    string.append(','.join(header))
    for row in RowCells_list:
        values = [row[k].value for k in simple_ids]
        # adjust
        values[0] = str(adjust_integer(values[0]))
        values[1] = values[1].strip('\t')
        values[2] = values[2].strip('\t')
        string.append(','.join(values))
    string = '\n'.join(string)
    with open(output_fp, 'w', encoding='utf-8') as writer:
        writer.write(string)
