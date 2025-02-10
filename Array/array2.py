student_record = ["Lysithea","Dedue", "Caspar", "Claude", "Edelgard"]

print(f"\nList of Students: {student_record}")

index = student_record.index("Claude") # Searching
print("\nWhat index is Claude?")
print(f"Claude is in Index {index}.")

print("\nList of Students:")
for index, element in enumerate(student_record): # Traversal
        print(f"{index + 1}. {element}")
print("\n")