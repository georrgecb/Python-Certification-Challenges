def add_time(start, duration, day_opt = None):

    old_time, old_time_meridiem = start.split(" ")
    hour, minute = old_time.split(":")
    extra_hour, extra_minute = duration.split(":")

    # Minute output:
    sum_minute = int(minute) + int(extra_minute)

    # An extra hour is added to the final output if number of 
    # minutes exceeds 60:
    if sum_minute >= 60 :
        total_minute = sum_minute - 60
        add_hour = 1

    else:
        total_minute = sum_minute
        add_hour = 0

    # Hour output:
    total_hour = int(hour) + int(extra_hour) + int(add_hour)

    days_list = ["monday", "tuesday", "wednesday", "thursday", 
                "friday", "saturday", "sunday"]

    # Count the days from the above list. This will help the script 
    # to return the exact day
    # even if the added time is a month.
    if day_opt :
        count_day = 0
        for day in days_list :
            if day == day_opt.lower() :
                break
            else:
                count_day += 1
                continue

    count_meridiem = 0

    # I'm counting each 12-hour interval. This makes the switch 
    # between AM and PM:
    if total_hour > 12:
        while total_hour > 12 :
            total_hour = total_hour - 12
            count_meridiem += 1

    new_time_day = ""
    new_time_meridiem = ""

    # If the initial time is PM, zero, two, four or any multiple of 2 based 
    # on count_meridiem (number of 12-hour intervals) means PM as well. 
    # Except when the output hour is 12 - there is always a switch
    # of meridiems at 12.
    if old_time_meridiem == "PM" :
        if total_hour < 12 :
            if (count_meridiem % 2) == 0 :
                new_time_meridiem = "PM"
            else:
                new_time_meridiem = "AM"

        elif total_hour == 12 :
                if (count_meridiem % 2) == 0 :
                    new_time_meridiem = "AM"
                else:
                    new_time_meridiem = "PM"

    # If the initial time is AM, zero, two, four or any multiple of 2 based 
    # on count_meridiem (number of 12-hour intervals) means AM as well. 
    # Except when the output hour is 12 - there is always a switch
    # of meridiems at 12.
    elif old_time_meridiem == "AM" :
        if total_hour < 12:
            if (count_meridiem % 2) == 0 :
                new_time_meridiem = "AM"
            else:
                new_time_meridiem = "PM"

        elif total_hour == 12 :
            if (count_meridiem % 2) == 0 :
                new_time_meridiem = "PM"
            else:
                new_time_meridiem = "AM"

    # Hours plus minutes - time output. In case the number of minutes is 
    # less than 2 digits, it will have a zero in front.
    if len(str(total_minute)) < 2:
        new_time_time = str(total_hour) + ":" + "0" + str(total_minute)

    else:
        new_time_time = str(total_hour) + ":" + str(total_minute)

    # If initial time is PM, zero 12-hour intervals mean the same day, 
    # one 12-hour interval means the next day (AM), while
    # for a multiple of 2 of 12-hour intervals I divide the number of 
    # intervals to return the number of days that have passed.
    
    if old_time_meridiem == "PM" :
        if count_meridiem == 0 :
            try:
                new_time_day = days_list[count_day]
                new_time = f"{new_time_time} {new_time_meridiem}, {new_time_day.capitalize()}"
            except:
                new_time = f"{new_time_time} {new_time_meridiem}"

        elif count_meridiem == 1 :
            try:
                new_time_day = days_list[count_day]
                new_time = f"{new_time_time} {new_time_meridiem}, {new_time_day.capitalize()} (next day)"
            except:
                new_time = f"{new_time_time} {new_time_meridiem} (next day)"
        elif count_meridiem == 2 :
            try:
                new_time_day = days_list[count_day + 2]
                new_time = f"{new_time_time} {new_time_meridiem}, {new_time_day.capitalize()} ({count_meridiem} days later)"
            except:
                new_time = f"{new_time_time} {new_time_meridiem} ({count_meridiem} days later)"

        elif (count_meridiem % 2) == 0 and count_meridiem > 2 :
            calculate_day = count_meridiem / 2

            # This loop is activated if more than 7 days have passed in order to find the output day.
            new_var = calculate_day + count_day # number of days that have passed plus the initial day of the week.
            if new_var >= 7 :
                while new_var >= 7 :
                    new_var -= 7
            try:
                new_time_day = days_list[new_var]
                new_time = f"{new_time_time} {new_time_meridiem}, {new_time_day.capitalize()} ({int(calculate_day)} days later)"
            except:
                new_time = f"{new_time_time} {new_time_meridiem} ({int(calculate_day)} days later)"

        # There are cases when the added time is 8.5 12-hour intervals. But when the initial time is PM, that 0.5 is AM,
        # therefore a new day. In that case, the total number of days is 9.
        elif (count_meridiem % 2) != 0 and count_meridiem > 2 :
            calculate_day = int(count_meridiem / 2 + 0.5)
            if day_opt:
              new_var = calculate_day + count_day
              if new_var >= 7 :
                while new_var >= 7 :
                    new_var -= 7
            try:
                new_time_day = days_list[new_var]
                new_time = f"{new_time_time} {new_time_meridiem}, {new_time_day.capitalize()} ({int(calculate_day)} days later)"
            except:
                new_time = f"{new_time_time} {new_time_meridiem} ({int(calculate_day)} days later)"

    if old_time_meridiem == "AM" :
        if count_meridiem == 0 or count_meridiem == 1 :
            try:
                new_time_day = days_list[count_day]
                new_time = f"{new_time_time} {new_time_meridiem}, {new_time_day.capitalize()}"
            except:
                new_time = f"{new_time_time} {new_time_meridiem}"

        elif count_meridiem == 2 :
            try:
                new_time_day = days_list[count_day + 1]
                new_time = f"{new_time_time} {new_time_meridiem}, {new_time_day.capitalize()} (next day)"
            except:
                new_time = f"{new_time_time} {new_time_meridiem} (next day)"

        elif (count_meridiem % 2) == 0 and count_meridiem > 2 :
            calculate_day = count_meridiem / 2

            new_var = calculate_day + count_day
            if new_var >= 7 :
                while new_var >= 7 :
                    new_var -= 7
            try:
                new_time_day = days_list[new_var]
                new_time = f"{new_time_time} {new_time_meridiem}, {new_time_day.capitalize()} ({int(calculate_day)} days later)"
            except:
                new_time = f"{new_time_time} {new_time_meridiem} ({int(calculate_day)} days later)"

        # There are cases when the added time is 8.5 12-hour intervals. But when the initial time is AM, that 0.5 is PM,
        # therefore not a new day. In that case, the total number of days is 8.
        elif (count_meridiem % 2) != 0 and count_meridiem > 2 :
            calculate_day = count_meridiem / 2 - 0.5

            new_var = calculate_day + count_day
            if new_var >= 7 :
                while new_var >= 7 :
                    new_var -= 7
            try:
                new_time_day = days_list[new_var]
                new_time = f"{new_time_time} {new_time_meridiem}, {new_time_day.capitalize()} ({int(calculate_day)} days later)"
            except:
                new_time = f"{new_time_time} {new_time_meridiem} ({int(calculate_day)} days later)"

    # FINAL OUTPUT:
    return new_time