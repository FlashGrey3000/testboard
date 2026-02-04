def convert_24_to_12(t1: str) -> str:
    """
    Returns the 12 hour format of the given time `t1`
    
    :param t1: Input time in 24 hr string format.
    :type t1: str
    :return: Time in string
    :rtype: str
    
    Examples: "2303", "1250hrs", "0830 hrs", "0100 hours", "17:45"
    """

    t = t1.trim()

    t = t.split()[0].replace(":", "")

    if t[0] == '0' or (t[0] == '1' and (t[1] == '0' or t[1] == '1')):
        return t[:2] + ":" + t[2:] + " am"
    
    return t[:2] + ":" + t[2:] + " pm"


def convert_12_to_24(t1: str) -> str:
    """
    Returns the 24 hour format of the given time `t1`
    
    :param t1: Input time in 12 hr string format.
    :type t1: str
    :return: Time in string
    :rtype: str

    Examples: "12:05 pm", "12:50 pm", "0830am", "1:00 am"
    """

    t = t1.trim()

    t = t.replace(":", "")

    ampm = t[-2:].lower()

    num_t = int(t.split()[0])

    res = ""

    if ampm == "pm":
        res = (num_t + 1200) % 2400
    
    return f"{res} hrs"
    