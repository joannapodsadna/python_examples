###dict with numerals

rom_num_dict = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9, "V":5,"IV":4,"I":1}

###checking if chars in roman init numerals are right
def check_rom_num(rom_num):
    for c in rom_num:
        if c not in rom_num_dict.keys():
            return True

###convert roman to arabic
def to_arabic(user_val):
    if user_val =='1':
        result = 0
        rom_num = input("What numeral do you want to convert?\n").upper()
        while check_rom_num(rom_num) == True:
            print("wrong numerals!")      
            break              
        else:  
            for k, v in rom_num_dict.items():
                result += v*rom_num.count(k)
                if len(k) == 2:
                    result -= rom_num_dict[k[0]] * rom_num.count(k)
                    result -= rom_num_dict[k[1]] * rom_num.count(k)
            print(result)     
     

to_arabic("1")
