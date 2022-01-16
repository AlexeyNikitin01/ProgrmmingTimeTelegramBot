import read_time_txt


from datetime import timedelta


def _get_h_m_today():
    h, m = read_time_txt._read_time_today()
    return h, m


def _get_time_today():
    h, m = _get_h_m_today()
    time_today = timedelta(hours=h, minutes=m)
    return time_today


def _get_total_time():
    h, m, days = read_time_txt._read_time_total()
    total_time = timedelta(days=days, hours=h, minutes=m)
    return total_time


def _write_file_txt(time_today, total_time):
    if time_today < timedelta(hours=24, minutes=0):
        read_time_txt._write_file_today(time_today)
        read_time_txt._write_file_total(total_time)


def _get_parsed_time(text_time: str):
    parsed_time = text_time.split(':')
    hours, minutes = list(map(int, parsed_time))
    return hours, minutes


def _get_delta(hours: int, minutes: int):
    delta = timedelta(hours=hours, minutes=minutes)
    return delta
