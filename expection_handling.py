def division_calculator():
    try:
        # Taking input from user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Performing division
        result = num1 / num2
        print(f"The result of division is: {result}")
    
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    
    except ValueError:
        print("Error: Please enter valid numbers!")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        print("Execution of division operation is complete.")

# Call the function to see exception handling in action
division_calculator()

