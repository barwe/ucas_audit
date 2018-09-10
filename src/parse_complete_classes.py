import xlrd
import os

def parse_complete_classes(fp):
    workbook = xlrd.open_workbook(fp)
    worksheet = workbook.sheet_by_index(0)
    classes = worksheet.get_rows()
    header = next(classes)
    return classes, header