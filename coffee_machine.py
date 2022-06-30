MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# 기존에 갖고있는 재료의 양
water = 300
milk = 200
coffee = 100
money = 0
turn_on = True


# 어떤 종류의 커피를 선택할 것인가

def choice_menu(menu):
    return MENU[menu]


## 사용자가 넣은 금액은 총 얼마인가

def total_coin(quarters, dimes, nickles, pennies):
    return round(quarters + dimes + nickles + pennies, 2)


while turn_on:
    menu = input("What would you like? (espresso/latte/cappuccino): ")
    if menu == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")
    elif menu == "turn off":
        turn_on = False
    else:
        ## 원하는 커피를 만드는데 재료의 양은?
        need_water = choice_menu(menu)["ingredients"]["water"]
        need_milk = choice_menu(menu)["ingredients"]["milk"]
        need_coffee = choice_menu(menu)["ingredients"]["coffee"]
        cost = choice_menu(menu)["cost"]
        change = 0
        ### 원하는 커피를 만드는 재료가 충분한가?
        if water >= need_water:
            if milk >= need_milk:
                if coffee >= need_coffee:
                    # 어떤 동전으로 얼만큼 넣을 것인가
                    quarters = int(input("how many quarters?: ")) * 0.25
                    dimes = int(input("how many dimes?: ")) * 0.1
                    nickles = int(input("how many nickles?: ")) * 0.05
                    pennies = int(input("how many pennies?: ")) * 0.01
                    user_cost = total_coin(quarters, dimes, nickles, pennies)
                    ### 사용자가 넣은 금액이 충분한가
                    #### 원하는 커피를 만들고 거스름돈을 계산하고 재료 상태를 업데이트한다.
                    if user_cost >= cost:
                        change = round(user_cost - cost, 2)
                        water -= need_water
                        milk -= need_milk
                        coffee -= need_coffee
                        money += cost
                        print(f"Here is ${change} in change.")
                        print(f"Here is your {menu}. Enjoy!")
                    else:
                        print("Sorry that's not enough money. Money refunded")
                else:
                    print("Sorry ther is no enough coffee")
            else:
                print("Sorry there is not enough milk")
        else:
            print("Sorry there is not enough water.")
