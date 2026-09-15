def main():
    mois = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    while True:
        try:
            user_input = input("Date: ").replace(' ','/').replace(',','')
            # format mm/dd/yyyy
            if user_input.split('/')[0].isalpha():
                month = (mois.index(user_input.split('/')[0]) + 1)
            else:
                month = int(user_input.split('/')[0])
            day = int(user_input.split('/')[1])
            year = int(user_input.split('/')[2])
            if day > 31 or month > 12:
                raise ValueError
        except ValueError:
            pass
        else:
            break
    print(f"{year:02}-{month:02}-{day:02}")

main()


