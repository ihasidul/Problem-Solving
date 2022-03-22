def make_readable(seconds):
    hour = seconds // 3600
    seconds = seconds - (3600 * hour)
    min = seconds // 60
    seconds = seconds - (60 * min)
    return '{:02}:{:02}:{:02}'.format(hour, min, seconds)

