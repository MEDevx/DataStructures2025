customer_queue = [] # Queue representing a line of customer in a fast food chain

customer_queue.append("Dimitri")  # Each arriving customer is added to the queue
customer_queue.append("Mercedes")
customer_queue.append("Ingrid")
customer_queue.append("Annette")

print(f"\nHere are the customers waiting in line to order: {customer_queue}")
customer_number = len(customer_queue) # Count the customers in the queue
print(f"There are {customer_number} customers.")

front_customer = customer_queue[0] # Customer in front of the queue
print(f"\nAfter {front_customer} got his order, he left the line and sat at a table.")
customer_queue.pop(0) # Remove the front customer from the queue

front_customer = customer_queue[0]
print(f"\n{front_customer} then proceeded to order.")
print(f"Here are the remaining customers: {customer_queue}")
print(f"There are {len(customer_queue)} customers left.")

print("\nAt the end of the day, all the customers left.")
customer_queue.clear() # Clear the queue
is_queue_empty = len(customer_queue) == 0 # Determine if queue is empty
print(f"Is queue empty? {is_queue_empty}\n")