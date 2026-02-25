def convert_24_to_12(t1: str) -> str:
    """
    Returns the 12 hour format of the given time `t1`
    
    Examples: "2303", "1250hrs", "0830 hrs", "0100 hours", "17:45"
    """

    t = t1.strip()
    t = t.split()[0].replace(":", "")

    hours = int(t[:2])
    minutes = t[2:]

    if hours == 0:
        return f"12:{minutes} am"
    elif hours < 12:
        return f"{hours:02}:{minutes} am"
    elif hours == 12:
        return f"12:{minutes} pm"
    else:
        return f"{hours - 12:02}:{minutes} pm"


def convert_12_to_24(t1: str) -> str:
    """
    Returns the 24 hour format of the given time `t1`
    
    Examples: "12:05 pm", "12:50 pm", "0830am", "1:00 am"
    """

    t = t1.strip().lower()
    t = t.replace(":", "")

    ampm = t[-2:]
    t = t[:-2].strip()

    t = t.zfill(4)

    hours = int(t[:2])
    minutes = t[2:]

    if ampm == "am":
        if hours == 12:
            hours = 0
    elif ampm == "pm":
        if hours != 12:
            hours += 12

    return f"{hours:02}{minutes} hrs"