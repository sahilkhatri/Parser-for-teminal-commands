## terminal command to execute this code:
## python demoparser.py copy path1 path2
## python demoparser.py remove path1

## this code is for COPY and REMOVE commands only, with reference to this code we can create for
## other terminal commands also
 
import sys
import os
import subprocess



# type_checking function takes input the user defined command to perform, and the path on which it is # to be executed.    
def type_checking(command, path):

	#dictionary to map the TERMINAL COMMANDS with with a user defined command
	# i.e. "mkdir" (make directory) is mapped with "make"

    command_maps = {
                    "remove":"rm",
                    "copy": "cp"}
    try:
        terminal_command = command_maps[command]
        call_list = [terminal_command]
        
        call_list.extend(path)
        print(call_list)
        #subprocess.call([terminal_command,path[0]])
        
        
	# if path does not exist then raise error
        for each_path in path:
            if not os.path.exists(each_path):
                raise NameError("path not found...")

	# if path exist then make a subprocess call to execute the TERMINAL COMMAND
        subprocess.call(call_list)
        
    except KeyError as k:
        raise Exception("message")
        #print(k,"key not found")
    except Exception as e:
        print(e)

# take 2 arguments from the user 
# 1. the user defined command to execute
# 2. path/paths required to execute the command

try:
    command = sys.argv[1]    
    path =sys.argv[2:] 
    
# raise error if atleast 2 inputs are not provided by the user

except IndexError as ie:
    print(ie,"2 inputs expected")
# if proper input is provided by the user then, call the type_checking function
else:
    type_checking(command,path)




                
    
    
    
        
    
    
