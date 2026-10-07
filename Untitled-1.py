while True:
    print("\n--- ATM Menu ---")
    print("1. Withdraw Cash")
    print("2. Exit")
    
    choice = input("Select an option (1 or 2): ").strip()

    if choice == "1" or choice == "Withdraw Cash":
        # Loop until they enter a valid multiple of 10
        while True:
            amount = int(input("Enter the amount to withdraw (multiples of 10): "))
            
            if amount % 10 == 0:
                print(f"Amount dispensed: £{amount}")
                break  # Exit the withdrawal loop
            else:
                print("Invalid amount. Please enter a multiple of 10 (e.g., 10, 20, 50).")
        
    elif choice == "2" or choice == "Exit":
        print("Thank you for using the ATM. Goodbye!")
        break  # Exit the ATM program loop
    else:
        print("Invalid choice, please select 1 or 2.")