import pyinputplus as pyip



def order_sandwich():
    print("Welcome, lets customize your sandwich")

    prices = {
         'wheat': 2.0, 'white': 1.5, 'sourdough': 2.5,
        'chicken': 3.0, 'turkey': 3.5, 'ham': 3.0, 'tofu': 2.5,
        'cheddar': 1.0, 'Swiss': 1.2, 'mozzarella': 1.5,
        'mayo': 0.5, 'mustard': 0.5, 'lettuce': 0.7, 'tomato': 0.7
    }

    #Get bread type
    bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt= "choose your bread type:\n", numbered = True)

    #Get protein type 
    protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt="What protein would you like ?\n", numbered=True)

    #Cheese preference
    wants_cheese = pyip.inputYesNo(prompt="Would you like Cheese (yes/no)\n?")
    cheese = ''
    if wants_cheese == "yes":
        cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozarella'], prompt="Choose your cheese type\n", numbered=True)
    
    #toppings type
    wants_toppings = pyip.inputYesNo(prompt="Do you want toppings? (yes/no)\n")
    topping = ''
    if wants_toppings == "yes":
        topping = pyip.inputMenu(['mayo','mustard','lettuce', 'tomato'], prompt = 'Choose your type\n', numbered=True)
    #Number of sandwiches
    num_sandwiches = pyip.inputInt("How many sandwiches would you like?(1 or more)\n", min=1)

    total_price = (prices[bread]+prices[protein]) * num_sandwiches
    if cheese:
        total_price += prices[cheese] * num_sandwiches
    if topping:
        total_price += prices[topping] * num_sandwiches

    #Print order summary
    print("\n Your order summary:")

    print(f"Bread:{bread}")
    print(f"Protein:{protein}")
    if cheese : 
        print(f"Cheese:{cheese}")
    if wants_toppings == 'yes':
        print(f"Toppings:{topping}")
    print(f"Number of sandwiches:{num_sandwiches}")
    print(f"your bill will be  : ${total_price:.2f}")
    print("Thank you for your order!") 

order_sandwich()