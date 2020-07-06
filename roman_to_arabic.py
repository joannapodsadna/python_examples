rom_num_dict = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9, "V":5,"IV":4,"I":1}



def to_arabic(user_val):
    if user_val =='1':
        result = 0
        rom_num = input("What numeral do you want to convert?\n").upper()
        for k, v in rom_num_dict.items():
            if rom_num == k:
                result += rom_num_dict[k] 

    print(result)

to_arabic("1")

