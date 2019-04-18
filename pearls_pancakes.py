
end_of_day = {'number_checks': 0,'total_in_till' : 0}
def get_table_num () :
    table_num = int(input("Enter table number: "))
    return table_num

def num_guests () :
    num_guests = int(input("Enter number is guests from 1-4: "))
    return num_guests

def order_menu () :
    menu = {'pancakes': 4,'omelette': 5, 'oatmeal': 3, 'hash_browns': 2, 'bacon': 2, 'orange_juice': 2, 'coffee': 2}
    print(menu)
    order = customers_order ()
    total = 0
    for key in menu:
        value = menu[key] * order[key]
        print (value)
        total = total + value
    return total
    
def customers_order () :
    pancakes = int(input("Pancakes ordered: "))
    omelette = int(input("Omelettes ordered: "))
    oatmeal = int(input("Oatmeals ordered: "))
    hash_browns = int(input("Hash browns ordered: "))
    bacon = int(input("Sides of bacon ordered: "))
    orange_juice = int(input("Glasses of orange juice: "))
    coffee = int(input("Cups of coffee: "))
    order = {'pancakes': 0,'omelette': 0, 'oatmeal': 0, 'hash_browns': 0, 'bacon': 0, 'orange_juice': 0, 'coffee': 0}
    order.update({'pancakes': pancakes,'omelette': omelette, 'oatmeal': oatmeal, 'hash_browns': hash_browns, 'bacon': bacon, 'orange_juice': orange_juice, 'coffee': coffee})
    return order




def pos_program () :
    table_num = get_table_num ()
    num_guest = num_guests ()
    number_checks = 0
    total_in_till = 0
    guest = 1
    balance = 0
    quit = 1
    while quit <= 1:
        while guest <= num_guest :
            guest_order = order_menu ()
            print("Guests sub-total for this guest is $" + str(guest_order))

            balance += guest_order
            print("Guests sub-total for this table is $" + str(balance))
            guest += 1
        if guest > num_guest :
            calc_total = int(input("Any more orders? 0 for no, 1 for yes: "))
            if calc_total == 0 :
                print("Calulating total...")
                print("Subtotal: $" + str(round(balance, 2)))
                taxes = balance * .08
                tot_with_taxes = round(taxes + balance, 2)
                
                print("Total tax: $" + str(round(taxes, 2)))
                print("Total with taxes: $" + str(tot_with_taxes))
                print("10% gratuity: $" + str(round(tot_with_taxes * .10, 2)))
                print("15% gratuity: $" + str(round(tot_with_taxes * .15, 2)))
                print("20% gratuity: $" + str(round(tot_with_taxes * .20, 2)))
                print("25% gratuity: $" + str(round(tot_with_taxes * .25, 2)))
                tip = int(input("How much would you like to tip (%) :"))
                grand_total = round((tip / 100) * tot_with_taxes + tot_with_taxes, 2)
                print(grand_total)
                total_in_till += grand_total
                number_checks += 1

                close_out = int(input("Would you like to close out for the day? 0 for no, 1 for yes :"))
                if close_out == 0 :
                    pos_program()
                else :
                    end_of_day.update({'number_checks': number_checks,'total_in_till' : total_in_till}) 
                    guest += 1
                    quit += 1
                    return
                    
            elif calc_total == 1:
                additional_orders = int(input("How man more orders? :"))
                num_guest = additional_orders
                guest = 1
                while guest <= num_guest :
                    guest_order = order_menu ()
                    print("Guests sub-total for this guest is $" + str(guest_order))
                    balance += guest_order
                    guest += 1

pos_program()

print(end_of_day)
