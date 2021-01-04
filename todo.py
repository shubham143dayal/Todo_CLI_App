import sys
import os.path
from datetime import datetime


def printHelp():

	# Function to print Usage Section when asked for help.
	todohelp="""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics"""
	sys.stdout.buffer.write(todohelp.encode('utf8'))		# Print the Usage as the default print() generates unexpected results.
	

def addToList(st):
	
	# To add a new Todo in the todo.txt file.
	if os.path.isfile('todo.txt'):					
	    with open("todo.txt",'r') as todoFileOri:
	    	data=todoFileOri.read()
	    with open("todo.txt",'w') as todoFileMod:
	    	todoFileMod.write(st+'\n'+data)
	else:											
	    with open("todo.txt",'w') as todoFile:
	    	todoFile.write(st+'\n')
	print('Added todo: "{}"'.format(st))


def showList():

	# Function to List and print the available todo's in the latest format order.
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as todoFileOri:
	    	data=todoFileOri.readlines()
	    ct=len(data)
	    st=""
	    for line in data:
	    	st+='[{}] {}'.format(ct,line)
	    	ct-=1
	    sys.stdout.buffer.write(st.encode('utf8'))			# Print the Tasks in Reverse Order as the default print() generates unexpected results.
	else:
	    print ("There are no pending todos!") 


def delFromList(num):

	# Function to Delete the task from the List. (If available)
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as todoFileOri:
	    	data=todoFileOri.readlines()
	    ct=len(data)
	    if num>ct or num<=0:
	    	print(f"Error: todo #{num} does not exist. Nothing deleted.")
	    else:
	    	with open("todo.txt",'w') as todoFileMod:
	    		for line in data:
	    			if ct!=num:
	    				todoFileMod.write(line)
	    			ct-=1
	    	print("Deleted todo #{}".format(num))
	else:
	    print("Error: todo #{} does not exist. Nothing deleted.".format(num))


def markDone(num):

	# Function to mark the given task as Done. (If available)
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as todoFileOri:
	    	data=todoFileOri.readlines()
	    ct=len(data)
	    if num>ct or num<=0:
	    	print("Error: todo #{} does not exist.".format(num))
	    else:
	    	with open("todo.txt",'w') as todoFileMod:
	    		if os.path.isfile('done.txt'):						# Produces output according to the availability of done.txt file.
	    			with open("done.txt",'r') as doneFileOri:
				    	doneData=doneFileOri.read()
			    	with open("done.txt",'w') as doneFileMod:
			    		for line in data:
			    			if ct==num:
			    				doneFileMod.write("x "+datetime.today().strftime('%Y-%m-%d')+" "+line)
			    			else:
			    				todoFileMod.write(line)
			    			ct-=1
			    		doneFileMod.write(doneData)
		    	else:
		    		with open("done.txt",'w') as doneFileMod:
			    		for line in data:
			    			if ct==num:
			    				doneFileMod.write("x "+datetime.today().strftime('%Y-%m-%d')+" "+line)
			    			else:
			    				todoFileMod.write(line)
			    			ct-=1

	    	print("Marked todo #{} as done.".format(num))
	else:
	    print("Error: todo #{} does not exist.".format(num))


def generateReport():

	# Function to Generate the Report.
	countTodo=0
	countDone=0
	if os.path.isfile('todo.txt'):
	    with open("todo.txt",'r') as todoFile:
	    	todoData=todoFile.readlines()
	    countTodo=len(todoData)
	if os.path.isfile('done.txt'):
	    with open("done.txt",'r') as doneFile:
	    	doneData=doneFile.readlines()
	    countDone=len(doneData)
	st=datetime.today().strftime('%Y-%m-%d') + " Pending : {} Completed : {}".format(countTodo,countDone)
	sys.stdout.buffer.write(st.encode('utf8'))


def main(): 

	# Main Function
	if len(sys.argv)==1:
		printHelp()
	elif sys.argv[1]=='help':
		printHelp()
	elif sys.argv[1]=='ls':
		showList()
	elif sys.argv[1]=='add':
		if len(sys.argv)>2:
			addToList(sys.argv[2])
		else:
			print("Error: Missing todo string. Nothing added!")
	elif sys.argv[1]=='del':
		if len(sys.argv)>2:
			delFromList(int(sys.argv[2]))
		else:
			print("Error: Missing NUMBER for deleting todo.")
	elif sys.argv[1]=='done':
		if len(sys.argv)>2:
			markDone(int(sys.argv[2]))
		else:
			print("Error: Missing NUMBER for marking todo as done.")
	elif sys.argv[1]=='report':
		generateReport()
	else:
		print('Option Not Available. Please use "./todo help" for Usage Information')

if __name__=="__main__": 
    main()