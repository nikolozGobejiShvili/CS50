while True:
        try:
            status=input("fraction: ").split("/")
            x= int(status[0])
            y= int(status[1])

            f=round((x / y * 100))

            if  1 < f < 99 :
                  print(str(f) + "%" )
                  break

            elif  99 <= f <= 100:
                  print("F")
                  break

            elif  f <= 1:
                  print("E")
                  break

            elif f > 100:
                  continue

        except(Exception):
            continue
