def add_time(start, duration, start_day=None):
    hours, minutes_meridiem = start.split(":")
    minutes, meridiem = minutes_meridiem.split(" ")
    duration_hours, duration_minutes = duration.split(":")

    # calculation
    sum_hours = int(hours) + int(duration_hours)
    sum_minutes = int(minutes) + int(duration_minutes)
    while sum_minutes >= 60:
        sum_minutes -= 60
        sum_hours += 1

    if sum_minutes < 10:
        sum_minutes = "0" + str(sum_minutes)
    count = 0  # count the number of days later
    while sum_hours >= 12:
        sum_hours -= 12
        if meridiem == "PM":
            meridiem = "AM"
            count += 1
        else:
            meridiem = "PM"
    if sum_hours == 0:
        sum_hours = 12

    if start_day is None:
        if count:
            if count == 1:
                later = "(next day)"
            else:
                later = f"({count} days later)"
            new_time = f"{sum_hours}:{sum_minutes} {meridiem} {later}"
        else:
            new_time = f"{sum_hours}:{sum_minutes} {meridiem}"
        return new_time

    else:

        my_dict = {
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6,
            "Sunday": 0
        }
        day = my_dict[start_day.title()]
        day += count
        day = day % 7
        weekday = list(my_dict.keys())[list(my_dict.values()).index(day)]
        if count:
            if count == 1:
                later = "(next day)"
            else:
                later = f"({count} days later)"
            new_time = f"{sum_hours}:{sum_minutes} {meridiem}, {weekday} {later}"
        else:
            new_time = f"{sum_hours}:{sum_minutes} {meridiem}, {weekday}"

        return new_time

