#!/usr/bin/python3

# INET4031
# Simon Otto
# Date Created: 10/27/25
# Date Last Modified: 10/27/25

# These imports provide access to system commands, regular expressions, and standard input.
import os
import re
import sys

def main():
    # Asks the user whether to run in dry-run mode or normal mode
    with open("/dev/tty") as tty:
        print("Run in dry-run mode? (Y/N): ", end='', flush=True)
        dry_run = tty.readline().strip().lower() == 'y'

    for line_number, line in enumerate(sys.stdin, start=1):
        # This line skips a line if it is a comment or if it doesn't have >
        match = re.match("^#", line)

        # Remove whitespace and split the line into fields using colons
        fields = line.strip().split(':')

        # This code gets rid of any whitespace and uses the colon to split >
        # In dry run mode it prints out statements showing if comments were skipped, or if there were an invalid amount of fields
        if match or len(fields) != 5:
            if dry_run:
                if match:
                    print(f"[Dry-Run] Line {line_number}: Skipped comment line.")
                elif len(fields) != 5:
                    print(f"[Dry-Run][Error] Line {line_number}: Invalid number of fields ({len(fields)} found, expected 5).")
            continue

        # Takes the username, password, and info to create the user account>
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Splits the last field with commas, to find which groups the user >
        groups = fields[4].split(',')

        # Indicates a new user account is being created
        print(f"==> Creating account for {username}...")
        # Creates user account with the user info but without the password        
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        if dry_run:
            print(f"[Dry-Run] Would run: {cmd}")
        else:
            os.system(cmd)

        # This print statement shows that a password is being made for a us>
        print(f"==> Setting the password for {username}...")
        # This creates a command to set the user's password by grabbing the>
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        if dry_run:
            print(f"[Dry-Run] Would run: {cmd}")
        else:
            os.system(cmd)


        for group in groups:
            # This loop checks to see if the group field is a - or not, if >
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                if dry_run:
                    print(f"[Dry-Run] Would run: {cmd}")
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
