def calculate_result(res:list):
    total_marks=0
    # Loop to calculate total marks
    for i in res:
        total_marks+=i
    # Pr calculation
    percentage=total_marks/len(res)
    # Result delivery
    return total_marks,percentage,percentage>=40

marks=[] #List to store marks
ind=0 
subjects=['Maths','Social','Chemistry','Physics','Computer'] #List of subjects

# Loop to validate the entered marks
while(ind<len(subjects)):
    mark=input(f"Enter marks(between 0 to 100) for {subjects[ind]}: ")
    if mark.isdigit() and int(mark)>=0 and int(mark)<=100:
        marks.append(int(mark))
        ind+=1
    else:
       continue

total_marks,percentage,result=calculate_result(marks)

# Result
print("Total marks: ",total_marks)
print("Percentage: ",percentage)
if result:
    print('PASS')
else:
    print('FAIL')