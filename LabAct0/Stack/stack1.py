file_stack = [] # Stack representing a file stack on a desk

file_stack.append("File 1") # Add files on the stack
file_stack.append("File 2")
file_stack.append("File 3")
file_stack.append("File 4")
file_stack.append("File 5")

print("\nFiles currently on stack:", file_stack) # Print the stack contents

most_recent_file = file_stack[-1] # Retrive the top file from the stack
print("Most recent file:", most_recent_file)

removed_file = file_stack.pop() # Remove the top file from the stack
print("Top file removed:", removed_file)
print("\nFiles currently on stack after removing top file:", file_stack)

is_stack_empty = len(file_stack) == 0 # Check if the file stack is empty
print("Is the file stack empty?", is_stack_empty)

file_amount = len(file_stack) # Check how many files are on the stack
print(f"There are currently {file_amount} files on the stack.\n")
