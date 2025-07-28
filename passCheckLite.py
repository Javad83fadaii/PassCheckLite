def ramz_check(khoda, shomare, meli, ramz):
    khoda = khoda.lower()
    ramz = ramz.lower()

    shomare_sade = ""
    for harf in shomare:
        if harf >= '0' and harf <= '9':
            shomare_sade += harf

    meli_sade = ""
    for adad in meli:
        if adad.isdigit():
            meli_sade += adad

    list1 = []
    list1.append(khoda)
    list1.append(shomare_sade)
    list1.append(meli_sade)

    jam = []

    for i in list1:
        jam.append(i)
        for j in list1:
            if i != j:
                jam.append(i + j)
                for k in list1:
                    if k != i and k != j:
                        jam.append(i + j + k)

    for chizi in jam:
        if chizi != "" and chizi in ramz:
            if chizi == khoda:
                return True, "رمز نباید شامل اسم باشه!"
            elif chizi == shomare_sade:
                return True, "رمز نباید شماره تلفن باشه!"
            elif chizi == meli_sade:
                return True, "رمز نباید کد ملی باشه!"
            elif khoda in chizi and shomare_sade in chizi and meli_sade in chizi:
                return True, "رمز نباید همه اطلاعات رو داشته باشه!"
            elif khoda in chizi and shomare_sade in chizi:
                return True, "رمز نباید اسم و شماره رو داشته باشه!"
            elif khoda in chizi and meli_sade in chizi:
                return True, "رمز نباید اسم و کد ملی رو داشته باشه!"
            elif shomare_sade in chizi and meli_sade in chizi:
                return True, "رمز نباید شماره و کد ملی رو داشته باشه!"

    return False, "رمز خوبه، مشکلی نداره."


if __name__ == "__main__":
    esm = input("اسمت چیه؟ ")
    tel = input("شماره‌تو بگو: ")
    kod = input("کد ملی چیه؟ ")
    ramz = input("یه رمز بده: ")

    natije, payam = ramz_check(esm, tel, kod, ramz)

    if natije:
        print("مشکل:", payam)
    else:
        print(payam)
        print("همه چی ذخیره شد:")
        print("اسم:", esm)
        print("شماره:", tel)
        print("کد ملی:", kod)
