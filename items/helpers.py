import time


def timestamp():
    epoch_time_seconds = int(time.time())
    epoch_time_milliseconds = int(time.perf_counter() * 1000)

    return epoch_time_seconds * 1000 + epoch_time_milliseconds


def tl_in_name(value):
    if value == '' or value == '-':
        return ''
    else:
        if len(value) < 2:
            return f' (TL {value})'
        else:
            return f' (TL{value})'


def cost(value):
    value = value.lower()
    if value.startswith('cr'):
        return float(value.lstrip('cr'))
    elif value.startswith('mcr'):
        return float(value.lstrip('mcr'))*1000000
    else:
        return 0
