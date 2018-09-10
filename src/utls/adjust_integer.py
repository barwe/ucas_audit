def adjust_integer(num):
    num = str(num)
    if num.endswith('.0'):
        return int(num.strip('.0'))