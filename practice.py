#question_dict = {}
count = 0
total=0
questions_file=open('questions.txt','r')
questions=[line.strip() for line in questions_file.readlines()]
questions_file.close()

for question in questions:
    questanswer=question.split("=")
    #question_dict[questanswer[0]]= questanswer[1]
    ans=input(f"What is the answer for: {questanswer[0]}")
    if(ans==questanswer[1]):
      count=count+1
    total=total+1
result=str(count/total) 
result_file=open('results.txt','w')
result_file.write(result)
print(result)
result_file.close()
