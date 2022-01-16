from datetime import date


def _read_time_today():
    with open("time_today.txt", "r") as f:
        content = f.readline().split()
        date_str_today = str(date.today())
        date_text_today = content[0]

        if date_text_today != date_str_today:
            h, m = 0, 0
            return h, m

        time_text = content[2].split(":")[0:2]
        h, m = list(map(int, time_text))
        return h, m


def _read_time_total():
    with open("time_total.txt", "r") as f:
        content = f.readline().split()
        parsed_time = content[3].split(":")[0:2]
        days = int(content[1])
        h, m = list(map(int, parsed_time))
    return h, m, days


def _write_file_total(total_time):
    with open("time_total.txt", "w") as f:
        if total_time.days == 0:
            f.write(f"total {total_time.days} days, {total_time}")
        else: 
            f.write(f"total {total_time}")


def _write_file_today(time_today):
    with open("time_today.txt", "w") as f:
        f.write(f"{date.today()} today {time_today}")

