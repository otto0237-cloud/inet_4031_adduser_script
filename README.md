# inet_4031_adduser_script

Program Description

This Python program automates user creation on Ubuntu. Instead of manually running commands like adduser, passwd, and usermod, the script executes them automatically using Python’s subprocess module.

Program User Operation

This program automates creating new user accounts on an Ubuntu system. The user provides an input file containing user details, and the script reads each line, then runs the necessary Linux commands adduser, passwd, and usermod automatically. The comments in the code will explain how each step works internally.

Input File Format

Each line in the input file needs to include user information such as username, password, full name, and any groups to join, separated by spaces. To skip a line, leave it blank or add a # at the beginning to mark it as a comment. If no groups are listed, the new user will not be added to any groups.

Command Execution

To run the program, make sure the Python file is executable:

chmod +x create-users.py


Then run it with:

./create-users.py < createusers.input


The script then reads user data from the createusers.input file.

"Dry Run"

If the user enables the “dry run” option, the script will display which commands would be executed without actually making any system changes. This allows the user to safely review and verify the process before running it for real.
