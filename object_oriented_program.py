import re
from datetime import datetime

class User:
    def __init__(self, name, contact_no, password, DOB, address=""):
        self.name = name
        self.contact_no = contact_no
        self.password = password
        self.DOB = DOB
        self.address = address

class Order:
    def __init__(self):
        self.users = []
        self.order_history = []
        self.order_counter = 1
        self.current_user = None

    def choose_Option(self):
        print('''Please Enter 1 for Sign up.
Please Enter 2 for Sign in.
Please Enter 3 for Quit.''')

    def signUp(self):
        # Asking the user to fill all the details required for sign up
        self.name = input("\nPlease enter your name: ")
        self.contact_no = input("\nPlease enter your mobile number: ")
        self.password = input("\nPlease enter your Password: ")
        self.password1 = input("\nPlease confirm your Password: ")
        self.DOB = input("\nPlease enter your date of birth # DD/MM/YYYY (No space): ")
        self.address = input("\nPlease enter your address (optional): ")

        if not self.contact_no_check(self.contact_no):
            return False
        if not self.validate_dob(self.DOB):
            return False
        if not self.password_check(self.password, self.password1):
            return False

        # Storing the name, contact number, and password in users to verify during sign in
        self.users.append({'name': self.name, 'contact_no': self.contact_no, 'password': self.password, 'DOB': self.DOB, 'address': self.address})
        return True

    def contact_no_check(self,contact_no):
        if self.contact_no == "0000000000":
            print("You have entered an invalid contact number.")
            return False

        if len(self.contact_no) == 10 and self.contact_no.isdigit() and self.contact_no.startswith('0'):
            return True
        else:
            print("You have entered an invalid contact number.")
            return False

    def validate_dob(self, DOB):
        # DOB should in the format DD/MM/YYYY
        pattern = r'^\d{2}/\d{2}/\d{4}$'
        valid = bool(re.match(pattern, self.DOB))
        if(valid):
            dob_year = datetime.strptime(self.DOB, '%d/%m/%Y')
            age = datetime.now().year - dob_year.year
            if(age >= 16): # The user should atleast 16 years old.
                return True
            else:
                print("You have not met the age criteria, the user should atleat 16 years old.")
                return False
        else:
            print("You have entered the Date of Birth in invalid format.")
            return False

    def password_check(self, password, password1):
        # The Password must initiate with alphabets followed by either one of @, & and ending with numeric.
        pattern = r'^[a-zA-Z]+[@&][0-9]+$'
        if re.match(pattern, self.password):
            # The password confirmation should match the initial entered password
            if self.password == self.password1:
                return True
            else:
                print("Your passwords are not matching.")
        else:
            print("Your password is not as per the guidelines.")
        return False

    def signIn(self):
        self.contact_no = input("\nPlease enter your Username (Mobile Number): ")
        login_attempts = 0
        max_login_attempts = 3 
        # User is allowed with only 3 attempts for unsuccessful login
        while login_attempts < max_login_attempts:
            password = input("\nPlease enter your password: ")
            found_user = None
            for user in self.users:
                # Check username in users
                if user['contact_no'] == self.contact_no:
                    found_user = user
                    break

            if found_user:
                # Check password for the specific user
                if found_user['password'] == password:
                    print("You have successfully Signed in")
                    return True
                else:
                    print("You have entered the wrong Password. \nPlease try again")
            else:
                print("You have not Signed up with this Contact Number, Please Sign up first.")
                return False
            login_attempts += 1

        print("You have used the maximum attempts of Login.")
        self.unsuccessfulLogin()
        return False

    def unsuccessfulLogin(self):
        print("Please reset the password by entering the below details:")
        while True:
            number = input("\nPlease enter your Username (Mobile Number) to confirm: ")
            found_user = None
            for user in self.users:
                if user['contact_no'] == number: # Username (mobile number) must be verified
                    found_user = user
                    break

            if found_user:
                dob = input("\nPlease enter your Date of Birth in DD/MM/YYYY format, to confirm: ")
                if dob == found_user['DOB']: # DOB must be verified
                    new_password = input("\nPlease enter your new password: ")
                    new_password_confirm = input("\nPlease re-enter your new password: ")
                    if self.password_check(new_password, new_password_confirm):
                        # The user is not allowed to set a password, which they have used previously
                        if new_password != found_user['password']:
                            found_user['password'] = new_password
                            print("Your Password has been reset successfully.")
                        else:
                            print("You cannot use the password used earlier.")
                        break
                else:
                    print("Incorrect Date of Birth.")
            else:
                print("User not found.")

    # =============================================================================
    # Home page
    # =============================================================================
    def home_page(self):
        print(" Please Enter 2.1 to Start Ordering.")
        print(" Please Enter 2.2 to Print Statistics.")
        print(" Please Enter 2.3 for Logout.")
        
    # =============================================================================
    # Ordering page
    # =============================================================================
    def ordering_page(self):
        print(" Please Enter 1 for Dine in.")
        print(" Please Enter 2 for Order Online.")
        print(" Please Enter 3 to go to Login Page.")
        
    # =============================================================================
    # Order online
    # =============================================================================
    def order_online(self):
        print(" Enter 1 for Self Pickup.")
        print(" Enter 2 for Home Delivery.")
        print(" Enter 3 to go to Previous Menu.")
        
    # =============================================================================
    # Function for food menu 
    # =============================================================================
    def food_menu(self):
        print("Enter 1  for Noodles    Price AUD 2")
        print("Enter 2  for Sandwich   Price AUD 4")
        print("Enter 3  for Dumpling   Price AUD 6")
        print("Enter 4  for Muffins    Price AUD 8")
        print("Enter 5  for Pasta      Price AUD 10")
        print("Enter 6  for Pizza      Price AUD 20")
        print("Enter 7  for Drinks Menu:")

    # =============================================================================
    # Function for drink menu
    # =============================================================================
    def drink_menu(self):
        print("Enter 1  for Coffee     Price AUD 2")
        print("Enter 2  for Colddrink  Price AUD 4")
        print("Enter 3  for Shake      Price AUD 6")
        print("Enter 4  for Checkout:")

    def get_price_for_food_item(self, item_option):
        if item_option == 1:
            return 2
        elif item_option == 2:
            return 4
        elif item_option == 3:
            return 6
        elif item_option == 4:
            return 8
        elif item_option == 5:
            return 10
        elif item_option == 6:
            return 20
        else:
            return 0 

    def get_price_for_drink_item(self, drink_choice):
        if drink_choice == 1:
            return 2
        elif drink_choice == 2:
            return 4
        elif drink_choice == 3:
            return 6
        else:
            return 0

    def food_order_dine_in(self):
        total_order_price = 0
        checkout_bool = False
        while True:
            if checkout_bool == True:
                break
            self.food_menu()
            item_option = int(input())
            if 1 <= item_option <= 6:
                item_price = self.get_price_for_food_item(item_option)
                total_order_price += item_price 
            elif item_option == 7:
                while True:
                    self.drink_menu()
                    drink_option = int(input())
                    if 1 <= drink_option <= 3:
                        item_price = self.get_price_for_drink_item(drink_option)
                        total_order_price += item_price 
                    elif drink_option == 4:
                        checkout_bool = True
                        break
                    else:
                        print("Enter options between 1 to 4")
            else:
                print("Enter options between 1 to 7")
        print('''Please Enter Y to proceed to Checkout or 
Enter N to cancel the order:''')
        checkout = input()
        if checkout == 'Y':
            return True, total_order_price
        else:
            print("Order cancelled.")
            return False, total_order_price

    def dine_in(self, total_price):
        print("Your total payable amount is: {} including AUD {} for Service Charges.".format(total_price*1.15, total_price*0.15))
        Date = input("Please enter the Date of Booking for Dine in: ")
        Time = input("Please enter the Time of Booking for Dine in: ")
        no_of_persons = input("Please enter the Number of Persons: ")
        print("Thank you for entering the details, Your Booking is confirmed.\n")
        return Date, total_price*1.15, "Dine in"


    def food_menu_online(self):
        print("Enter 1  for Noodles    Price AUD 2")
        print("Enter 2  for Sandwich   Price AUD 4")
        print("Enter 3  for Dumpling   Price AUD 6")
        print("Enter 4  for Muffins    Price AUD 8")
        print("Enter 5  for Pasta      Price AUD 10")
        print("Enter 6  for Pizza      Price AUD 20")
        print("Enter 7  for Checkout")

    def food_order_order_online(self, delivery_type):
        self.total_order_price = 0  
        checkout_bool = False
        while True:
            if checkout_bool:
                break
            self.food_menu_online()
            item_option = int(input())
            if 1 <= item_option <= 6:
                item_price = self.get_price_for_food_item(item_option)
                self.total_order_price += item_price
            elif item_option == 7:
                checkout_bool = True
                break
            else:
                print("Enter options between 1 to 7")
        print('''Please Enter Y to proceed to Checkout or 
    Enter N to cancel the order:''')
        checkout = input()
        if checkout == 'Y':
            if delivery_type == 2:
                found_user = None
                for user in self.users:
                    # Check username in users
                    if user['contact_no'] == self.contact_no:  # Corrected attribute name
                        found_user = user
                        break
                if found_user:
                    # Check address for the specific user
                    if found_user['address'] == '':
                        print('''You have not mentioned your address, while signing up.
    Please Enter Y if you would like to enter your address.
    Enter N if you would like to select another mode of order.''')
                        choose = input()
                        if choose == 'Y':
                            address = input("Please enter your address: ")
                            found_user['address'] = address
                            return True, self.total_order_price  # Return a tuple with boolean and total_price
                        else:
                            return False, 0  # Return a tuple with boolean and 0
            return True, self.total_order_price  # Return a tuple with boolean and total_price
        else:
            print("Order cancelled.")
            return False, 0


    def pick_up(self, total_price):
        print("Your total payable amount is: {}.".format(total_price))  # Corrected attribute name
        Date = input("Please enter the Date of Pick up: ")
        Time = input("Please enter the Time of Pick up: ")
        name_of_person = input("Please enter the Name of the Person: ")
        print("Thank you for entering the details, Your Booking is confirmed.\n")
        return Date, total_price, "Pick up"

    def delivery(self, total_price):
        print("Your total payable amount is: {} and there will be additional charges for Delivery.".format(total_price))  # Corrected attribute name
        Date = input("Please enter the Date of Delivery: ")
        Time = input("Please enter the Time of Delivery: ")
        distance = int(input("Please enter the Distance from the restaurant: "))
        delivery_cost = self.delivery_charges(distance)
        if delivery_cost == 0:
            choose_pick_up = input("Delivery is not provided for distances above 15 km. Enter Y to choose Pick up option, otherwise enter N: ")
            if choose_pick_up == 'Y':
                print("Thank you for your Order, Your Order has been confirmed.\n")
                return Date, total_price, distance, "Pick up"
            else:
                return None, None, None, None
        print("Thank you for your Order, Your Order has been confirmed.\n")
        return Date, total_price, distance, "Delivery"


    def delivery_charges(self, distance):
        self.distance = distance
        if 0 <= self.distance <= 5:
            return 3
        elif 5 < self.distance <= 10:
            return 6
        elif 10 < self.distance <= 15:
            return 10
        else:
            return 0

    def summary_of_transactions(self):
        print("Please Enter the option to Print the Statistics.")
        print("1 - All Dine in Orders.")
        print("2 - All Pick up Orders.")
        print("3 - All Deliveries.")
        print("4 - All Orders (Ascending Order).")
        print("5 - Total Amount Spent on All Orders.")
        print("6 - To go to Previous Menu.")

    def order_details(self):
        order_id = 'A' + str(self.order_counter).zfill(3)
        self.order_counter += 1
        return order_id

    def show_order_history(self, option):
        if option == 1:
            header = "Order ID     Date     Total Amount Paid     Type of Order"
            dine_in_orders = [order for order in self.order_history if order[3] == "Dine in"]
            output = [f"{order[0]:<9} {order[1]:<14} {order[2]:<23} {order[3]:<45}" for order in dine_in_orders]
            output.insert(0, header)
            return "\n".join(output)
        elif option == 2:
            header = "Order ID     Date     Total Amount Paid     Type of Order"
            pickup_orders = [order for order in self.order_history if order[3] == "Pick up"]
            output = [f"{order[0]:<9} {order[1]:<14} {order[2]:<23} {order[3]:<45}" for order in pickup_orders]
            output.insert(0, header)
            return "\n".join(output)
        elif option == 3:
            header = "Order ID     Date     Total Amount Paid     Type of Order"
            delivery_orders = [order for order in self.order_history if order[3] == "Delivery"]
            output = [f"{order[0]:<9} {order[1]:<14} {order[2]:<23} {order[3]:<45}" for order in delivery_orders]
            output.insert(0, header)
            return "\n".join(output)
        elif option == 4:
            header = "Order ID     Date     Total Amount Paid     Type of Order"
            all_orders_sorted = sorted(self.order_history, key=lambda x: x[2], reverse=True)
            output = [f"{order[0]:<9} {order[1]:<14} {order[2]:<23} {order[3]:<45}" for order in all_orders_sorted]
            output.insert(0, header)
            return "\n".join(output)
        elif option == 5:
            total_amount_spent = sum(order[2] for order in self.order_history)
            return f"Total Amount Spent: {total_amount_spent}"
        elif option == 6:
            return "Go to previous menu."
        else:
            return "Invalid option"

    def main(self):
        while True:
            self.choose_Option()
            option = int(input())
            if option == 1:
                while True:
                    if self.signUp():
                        print("You have Successfully Signed up.")
                        break
                    else:
                        print("Please start again.")
            elif option == 2:
                while True:
                    success = self.signIn()
                    if success:
                        order = False
                        while True:
                            if order:
                                break
                            self.home_page()
                            sub_option = float(input())
                            if sub_option == 2.1:
                                while True:
                                    self.ordering_page()
                                    sub_sub_option = int(input())
                                    if sub_sub_option == 1:
                                        dine_in_bool, total_order_price = self.food_order_dine_in()
                                        if dine_in_bool:
                                            date, amount, order_type = self.dine_in(total_order_price)
                                            order_id = self.order_details()
                                            self.order_history.append([order_id, date, amount, order_type])
                                            order = True
                                        break
                                    elif sub_sub_option == 2:
                                        self.order_online()
                                        delivery_type = int(input())
                                        if delivery_type == 1:
                                            pick_up_bool, total_price = self.food_order_order_online(delivery_type)
                                            if pick_up_bool:
                                                date, amount, order_type = self.pick_up(total_price)
                                                order_id = self.order_details()
                                                self.order_history.append([order_id, date, amount, order_type])
                                                order = True 
                                            break
                                        elif delivery_type == 2:
                                            address_bool, total_price = self.food_order_order_online(delivery_type)
                                            if address_bool:
                                                date, amount, distance, order_type = self.delivery(total_price)
                                                delivery_cost = self.delivery_charges(distance)
                                                if order_type == 'Pick up' or order_type == 'Delivery':
                                                    order_id = self.order_details()
                                                    self.order_history.append([order_id, date, amount + delivery_cost, order_type])
                                                    order = True
                                                else:     
                                                    break 
                                            else:
                                                pass
                                            break
                                        else:
                                            break
                                    else:
                                        break
                            elif sub_option == 2.2:
                                self.summary_of_transactions()
                                while True:
                                    select = int(input())
                                    if 1 <= select <= 5:
                                        print(self.show_order_history(select))
                                    elif select == 6:
                                        print(self.show_order_history(select))
                                        break
                            elif sub_option == 2.3:
                                break
                            else:
                                print("Invalid sub-option. Please choose a valid option (2.1, 2.2, or 2.3).")
                        break
                    break
            elif option == 3:
                print("Thank You for using the Application.")
                break
            else:
                print("Invalid option. Please choose a valid option (1, 2, or 3).")

if __name__ == '__main__':
    order_system = Order()
    order_system.main()
