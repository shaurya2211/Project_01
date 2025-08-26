def datechecker(dateinput):
    # DD-MM-YYYY
    chkinitial = (len(dateinput) == 10) and (dateinput[2] == '-') and (dateinput[5] == '-')

    if not chkinitial:
        return False

    date, month, year = dateinput.split('-')
    date, month, year = int(date), int(month), int(year)

    monthdate = [31,29,31,30,31,30,31,31,30,31,30,31]

    chkmonth = month >= 1 and month <= 12

    if not chkmonth:
        return False

    chkdate = date >= 1 and date <= monthdate[month - 1]

    if not chkdate:
        return False
    
    return True
