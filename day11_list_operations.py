# Day 11 Challenge: Basic list operations - add, remove, and display items
def manage_shopping_list():
    shopping_list = []
    
    while True:
        print("\n--- Shopping List Manager ---")
        print("1. Add item")
        print("2. Remove item") 
        print("3. View list")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"Added '{item}' to your list!")
            
        elif choice == "2":
            if shopping_list:
                print("Current list:", shopping_list)
                item = input("Enter item to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"Removed '{item}' from your list!")
                else:
                    print("Item not found in list!")
            else:
                print("List is empty!")
                
        elif choice == "3":
            if shopping_list:
                print("Your shopping list:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your list is empty!")
                
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the shopping list manager
manage_shopping_list()