Website Blocker
This Python script helps manage website access during working hours by modifying the system's hosts file to block specific websites. It automatically updates the hosts file to redirect specified websites to 127.0.0.1 (localhost) during defined working hours and restores access outside of those hours.

Features
Automatic Website Blocking: Blocks access to specified websites during working hours by redirecting them to 127.0.0.1.
Restores Access: Removes the blocking redirections outside working hours to allow unrestricted access.
Customizable Time and Websites: Easily configure working hours and the list of websites to block.
Requirements
Python 3.x: The script is compatible with Python 3.x versions.
Administrative Privileges: Modifying the hosts file requires administrative privileges.
Usage
Prepare the Script:

Save the script to a file, for example, website_blocker.py.
Modify the Script:

Update the host_path variable if your hosts file is located in a different directory.
Modify the websites list to include the websites you want to block during working hours.
Adjust the working hours by changing the times in the dt function calls.
Run the Script:

Open a command prompt or terminal with administrative privileges.

Execute the script using Python:

python website_blocker.py

Verify Changes:

During working hours (between 8 AM and 4 PM by default), the specified websites will be blocked.
Outside of working hours, the websites will be accessible again.
Code Overview
Host File Path: The host_path variable specifies the path to the hosts file, which is modified to block or unblock websites.
Redirect Address: The redirect variable is set to 127.0.0.1, which is used to block the websites.
Websites List: The websites list contains the domains that should be blocked during working hours.
Time Check: The script checks the current time to determine whether it is within working hours.
Blocking Websites:
During working hours, the script adds entries to the hosts file to redirect the specified websites to 127.0.0.1.
Restoring Access:
Outside of working hours, the script removes the blocking entries from the hosts file.
Important Notes
Administrative Rights: Ensure you run the script with administrative rights to modify the hosts file.
System Impact: Be cautious when modifying the hosts file as it affects how websites are resolved by your system.
Example
During working hours (8 AM - 4 PM):

facebook.com is blocked.
filehippo.com is blocked.

Outside working hours:

facebook.com is accessible.
filehippo.com is accessible.

Contributing
Contributions are welcome! If you have suggestions for improvements or additional features, please submit an issue or a pull request.
