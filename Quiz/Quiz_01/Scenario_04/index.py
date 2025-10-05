def perform_operations(numbers):
    total = 0
    product = 1
    
    for num in numbers:
        total += num           
        product *= num         
        
    average = total / len(numbers)  
    return total, product, average

numbers = [1, 2, 3, 4, 5]
total, product, average = perform_operations(numbers)

print(f"Total: {total}")
print(f"Product: {product}")
print(f"Average: {average}")
