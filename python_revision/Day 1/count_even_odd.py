# Function to count evens and odds from list
def count_even_odd(numbers:list):
    even_count=0
    odd_count=0

    # Main logic
    for i in numbers:
        if i%2==0:
            even_count+=1
        else:
            odd_count+=1
    
    # Result delivery
    return even_count,odd_count

# List to store input
numbers=[]

# Size
n=int(input("Enter number of inputs to be entered: "))

# Input loop
while(len(numbers)<n):
    num=input("Enter number: ")
    # Input validation
    try:
        numbers.append(int(num))
    except ValueError:
        continue
# Result
even_count,odd_count=count_even_odd(numbers)
print(f"\nCount of even numbers: {even_count}\nCount of odd numbers: {odd_count}")