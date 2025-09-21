# Prompt for task information
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process based on priority using match case
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Please address it as soon as possible.")
    
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
        else:
            print(f"Note: '{task}' is a medium priority task. Consider completing it this week.")
    
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task with a deadline. Complete it when possible.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    
    case _:
        print("Invalid priority level entered. Please use high, medium, or low.")

# Optional: Add a celebratory message
print("\n Well done on completing this project! Let the world hear about this milestone achieved.")
print(" Click here to tweet! 🚀")