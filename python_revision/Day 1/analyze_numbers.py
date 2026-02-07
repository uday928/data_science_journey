# Function to analyze numbers:
def analyze_numbers(numbers:list):
    # Handling of empty list
    if not numbers:
        return None,None,None,None
    largest_num=numbers[0]
    smallest_num=numbers[0]
    sum=0
    even_count=0

    # Main logic to count sum, minimum, maximum, even_count
    for num in numbers:
        sum+=num
        if num%2==0:
            even_count+=1
        if num>largest_num:
            largest_num=num 
        if num<smallest_num:
            smallest_num=num
    average=sum/len(numbers)

    # Result delivery
    return largest_num,smallest_num,average,even_count

# List of numbers
numbers=[]
n=int(input("Enter number of inputs to be entered: "))

# Loop to take inputs
while(len(numbers)<n):
    num=input("Enter valid number: ")

    # input validation
    try:
        numbers.append(int(num))
    except ValueError:
        continue

largest_num,smallest_num,average,even_count=analyze_numbers(numbers)

# Result
print(largest_num,smallest_num,average,even_count)