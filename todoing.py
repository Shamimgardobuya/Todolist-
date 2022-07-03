#create a class of todos and using def init create unique attributes
#create empty list
#append the object
#create function to loop through and print all the objects,

#create empty list and append the items
#create condition to access the items
#if completed ,remove using .pop
#
# class Todo:
#     task2=str(input("Enter a task"))
#     def __init__(self,task):
#         self.task=task
#     lista=[]
#     lista.append(Todo("Finishing Kotlin recycler view"))
#     lista.append(Todo("Reading originals"))
#     for task in lista:
# 
#         print(task)

# task=str(input("Enter a task")) 
# quantity=int(input("How many tasks would you wish to add"))

# def Tasking():
#   def trying():  
#    task=str(input("Enter a task"))
  
#    quantity=int(input("How many tasks would you wish to add"))
#    p=[]
#    p.append(task)
#    print(p) 
#    if len(p)<quantity:
#     quest=str("Do you still wish to add another task?Yes or No ").lower()
#     if quest=="yes":
#         trying()

#   trying()
#   # p=[]
  
        
#         # for i in p:
#         #     print(p)
# #    addying()

# Tasking()
#   #request user for input 
   #request forusers input
   #create a list and append the input
   #keep on appending the task to list
# task=str(input("Enter a task"))


#
# from secrets import choice


quantity=int(input("How many tasks would you wish to add "))
p=[]
while len(p)<quantity:            
     
     def tasking():
        task2=str(input("Enter a task "))
        p.append(task2)

     tasking()
print(p)
choice=str(input("Do you wish to remove a task?Yes/No ")).lower()
while(choice=="yes"):
   removing=str(input("Which item do you wish to remove "))
   if (removing in p):
     result=p.index(removing)
     p.pop(result)
     print(f"{p} are the tasks left in your to do list ")
     break
else:
      print(f"Sorry you do not hav{removing} in your days list")



# def done():
#      #check if item to be removed is actually in list 
#    if (removing in p):
#      result=p.index(removing)
#      p.pop(result)
#      print(f"{p} are the tasks left in your to do list ")
#    else:

#         print(f"Sorry,you do not have {removing} in your task")
# done()



     #remove item in list ,
             #request user for input 
             #remove the specific item using indexing wth dot pop
             #print new list 


  

  
# tasking()
# print(p)


  






  
