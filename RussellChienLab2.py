################################################
# Program Header                               #
# Course: CS 3A Object-Oriented Programming    #
#         Methodologies in Python              #
# Name:   Russell Chien                        #
# Description:  Programming with Numbers and   #
# Strings; Controlling Selection               #
# Your Supermarket Coupons – The Grocery Bill  #
# Date:  07/11/2019                            #
################################################

# Program Source Statements
cost = input("Please enter the cost of your groceries: ")
cost = float(cost)

MIN_COST = 10
FIRST_COST = 60
SECOND_COST = 150
THIRD_COST = 210
FIRST_COUPON = .08
SECOND_COUPON = .1
THIRD_COUPON = .12
FOURTH_COUPON = .14

if cost < MIN_COST:
    print("No discount coupon won,",
    "spend $10 or more to get one.")
    
elif cost >= MIN_COST and cost <= FIRST_COST:
    coupon = cost * FIRST_COUPON
    round(coupon, 2)
    coupon_string = "$%.2f."%coupon
    print("You win a discount coupon of", coupon_string,
    "(8% of your purchase)")
    
elif cost >= FIRST_COST and cost <= SECOND_COST:
    coupon = cost * SECOND_COUPON
    round(coupon, 2)
    coupon_string = "$%.2f."%coupon
    print("You win a discount coupon of", coupon_string,
    "(10% of your purchase)")
    
elif cost >= SECOND_COST and cost <= THIRD_COST:
    coupon = cost * THIRD_COUPON
    round(coupon, 2)
    coupon_string = "$%.2f."%coupon
    print("You win a discount coupon of", coupon_string,
    "(12% of your purchase)")
    
else:
    coupon = cost * FOURTH_COUPON
    round(coupon, 2)
    coupon_string = "$%.2f."%coupon
    print("You win a discount coupon of", coupon_string,
    "(14% of your purchase)")
    
# Program Output##############################################
# Please enter the cost of your groceries: 70                #
# You win a discount coupon of $7.00 (10% of your purchase)  #
############################################################## 
