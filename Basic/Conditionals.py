biryani_price = 400
kabab_price = 454
has_money = True
has_food = False

if biryani_price < 150 :
    print("Eat Biryani")
elif kabab_price < 50 :
    print("Eat kabab")
else:
    if has_money != True and has_food == False :
        print("Your are in crisis!")
    elif has_money == True or has_food == True :
        print("Start eating!!!")
    print("Eat Butter bon")
