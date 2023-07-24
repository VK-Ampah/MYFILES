# Comment like a pro.
'''
Total = 0
Nums = []
while True:
    Number = int(input("Enter a number (-1 to end): "))
    if Number == -1:
        break
    Nums.append(Number)
    Total += Number
print(Total)
print(Nums)
Nums.sort()  # Can I sort in Descending order??
print(Nums)
Total2 = sum(Nums)
print(Total2)
FName = "Maurice"
StLen = len(FName)
print(StLen)
LstLen = len(Nums)
print(LstLen)
Average = Total2 / len(Nums)
print(Average)
MaxValue = max(Nums)
print(MaxValue)
MinValue = min(Nums)
print(MinValue)
Dups = []
for i in range(0, MaxValue + 1):
    CountOcc = Nums.count(i)
    if CountOcc >= 2:
        Dups.append(i)
print(Dups)
'''
QuizTitle = input("Enter a title for this quiz: ")
NumQuestions = int(input("Enter the number of questions: "))
'''
AnsKey = []
for i in range(1, NumQuestions + 1):
    Answer = input("Enter the answer for question " + str(i) + ": ").upper()
    AnsKey.append(Answer)
print(AnsKey)
'''
AnsKey = ['A', 'B', 'C', 'D', 'A']
NumQuizzes = int(input("How many quizzes are to be graded: "))
for j in range(1, NumQuizzes + 1):
    StudentName = input("Enter the student name: ")
    StudentAnswer = []
    for i in range(1, NumQuestions + 1):
        Answer = input("Enter the answer for question " + str(i) + ": ").upper()
        StudentAnswer.append(Answer)
    # Compare the student answers to the Answer Key.
    # Keep track of the number the get correct.
    # Calculate the grade.
    # Store the name, Number Correct and The Grade in three lists.
# Display the output based on the printer spacing chart provided.