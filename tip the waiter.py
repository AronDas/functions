def total(billamount, tipperc):
    total = billamount*(1 + 0.01*tipperc)
    total = round(total, 2)
    print(f"Please pay $", total)

total(150, 20)