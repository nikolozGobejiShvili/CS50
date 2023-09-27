monthes = [" ", "January", "February", "March", "April",
 "May", "June", "July", "August", "September",
 "October", "November", "December"]

#create loop to check if input is correct or not
while True:
    try:
        #variable date from user without whitespaces
        date = input("Date: ").strip()

        #check what is separator to define format of input
        if "/" in date:
            m, d, y = date.split("/")
            #if separator is "/" then monthe must be digit and
            #day must be equal or less than 31
            if m.isdigit() and int(m) <= 12 and int(d) <= 31:
                if len(m) < 2:
                    m = f"0{m}"
                if len(d) < 2:
                    d = f"0{d}"
                print(f"{y}-{m}-{d}")
            #if it is not true continue the loop
            else:
                continue

        #if there is not "/" in date then there should be ","
        elif "," in date:
            m, d, y = date.replace(",", "").title().split()
            #convert text m into the digit
            m_int = monthes.index(m)

            #check if monthe is equal or less than 12 and
            #day is equal or less than 31
            if m_int <= 12 and int(d) <= 31:
                if len(str(m_int)) < 2:
                    m_int = f"0{m_int}"
                if len(d) < 2:
                    d = f"0{d}"
                print(f"{y}-{m_int}-{d}")
            else:
                continue

        #if there is not "/" or "," in date then continue the loop
        else:
            continue

    except ValueError:
        pass
    else:
        break