def main():
    # Ask about the time from the user
    time=input(" What time is it? ")
    # Defining the time ranges for the meal times
    if 7<=convert(time)<=8:
        print("breakfast time")
    elif 12<=convert(time)<=13:
        print("lunch time")
    elif 18<=convert(time)<=19:
        print("dinner time")
    else:
        pass
# conversion of the time
def convert(time):
    # In case the time is inputed in 12 hours format
    if ".m." in time:
        time, t_format=time.split(" ")
        hour, min=time.split(":")
        hour,min=float(hour),float(min)
    # If the time is in the am
        if t_format=="a.m.":
            f_t=hour + (min/60)
    # if the time is in the pm then 12 hours will be added
        elif t_format=="p.m.":
            f_t= 12 + hour + (min/60)
    # In case the time is in 24 hours format
    else:
        hour, min=time.split(":")
        hour,min=float(hour),float(min)
        f_t=hour + (min/60)
    return f_t

if __name__ == "__main__":
    main()
