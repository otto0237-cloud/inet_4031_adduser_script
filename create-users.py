#!/usr/bin/python3

# INET4031
# Simon Otto
# Date Created: 10/23/25
# Date Last Modified: 10/23/25

#These imports gives access to os commands, regular expression matching, and access to system functions.
import os
import re
import sys

#YOUR CODE SHOULD HAVE NONE OF THE INSTRUCTORS COMMENTS REMAINING WHEN YOU ARE FINISHED
#PLEASE REPLACE INSTRUCTOR "PROMPTS" WITH COMMENTS OF YOUR OWN

def main():
    for line in sys.stdin:

        # This line checks to see if a line in the input starts with #, and then skips the line
        
        match = re.match("^#",line)

        # This code gets rid of any whitespace and uses the colon to split the line into fields
        fields = line.strip().split(':')

        # This line skips a line if it is a  comment or if it doesn't have 5 fields, this is so only valid users are recorded
        if match or len(fields) != 5:
            continue

        # Takes the username, password, and info to create the user account by matching the structure of the entries to /etc/passwd
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # Splits the last field with commas, to find which groups the user belongs to
        groups = fields[4].split(',')

        # Indicates a new user account is being created
        print("==> Creating account for %s..." % (username))
        # Creates user account with the user info but without the password
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        # The following lines are for safety. The print command is for learning about the code and debugging. The os command actually executes the user creation.
        
        #print cmd 
        os.system(cmd)

        # This print statement shows that a password is being made for a user
        print("==> Setting the password for %s..." % (username))
        # This creates a command to set the user's password by grabbing the password input into the password command.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        os.system(cmd)

        for group in groups:
            # This loop checks to see if the group field is a - or not, if it is in a group it adds the user to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                
                os.system(cmd)

if __name__ == '__main__':
    main()
