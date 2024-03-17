import sys
import os
import subprocess

def execute_command(command):
    try:
        # Execute the command in the shell
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # Check if the command executed successfully
        if result.returncode == 0:
            #print("Command output:")
            print(result.stdout)
        else:
            #print("Command failed with error:")
            print(result.stderr)
    except Exception as e:
        print("Error executing command:", e)

def main():
    # Skip the first argument because it's the script name itself
    arguments = sys.argv[1:]
    
    # Save all the arguments in a string variable
    arguments_string = ' '.join(arguments)
    
    #bundle_dir = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.abspath(os.path.dirname(__file__))
    
    # Path to the bundled file
    #file_path = os.path.join(bundle_dir, 'out.loza')
    
    exe_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    
    # Construct the path to the embedded file
    file_path = os.path.join(exe_dir, 'out.loza')
    
    #with open(file_path, 'r') as file:
    #    content = file.read()
    
    # Print the string variable
    execute_command("loza "+file_path+" "+arguments_string)

if __name__ == "__main__":
    main()