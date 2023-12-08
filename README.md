# PCS_PROJECT_TEAM7

# Introduction:

A peer-to-peer system is a computer network that enables peers to share network resources. The File System supports all the file operations that other systems do, like creating, reading, deleting, Updating retrieving files, Etc. The File system encrypts all the data from unauthorized users and attackers so that only authorized users have access to the files. The file access can be shared with other users.

# Features:

# User Authentication:
Users can log in with existing credentials or sign up for a new account.
User registration details are securely stored in a MySQL database.

# File Operations:

1. Create Directories: Users can create directories to organize their files.
2. Create/Delete Files: Users can create and delete files within the system.
3. Read/Write File Content: Read and write operations are supported for file contents.
4. Share Access: Files and directories can be shared with other users with specified access modes (Read/Write/Delete).
5. Restore Files: Files can be restored after deletion.
6. List Available Files: Users can view the list of available files for efficient management.
7. Display Log: A log entry of all actions are displayed.

# Security:
The system employs Advanced Encryption Standard (AES) for secure data transmission between the Peers.
User credentials and sensitive data are protected during communication.

#Database Interaction:
User registration details and file access control information are stored in a MySQL database.
The database ensures data integrity and provides a reliable storage solution for user-related information.

Working of the System:
# User Authentication:
Users log in using their credentials or sign up for a new account.
Usernames and passwords are validated against the stored records in the MySQL database.

File Operations:
Users interact with a graphical user interface (GUI) to perform file operations.
The system communicates with the server over sockets to execute file-related requests.
Secure AES encryption ensures the confidentiality of data during transmission.

Database Interaction:
User registration details, including usernames, passwords, and contact information, are stored securely.
File access control details, such as sharing and permission information, are managed in the database.

List Available Files:
Users can view the list of available files, including those they own and those shared with them by other users.

# Conclusion:
The Peer-to-peer Encrypted File System offers a robust and secure solution for users to manage files efficiently in a distributed environment. It combines user-friendly features with data security, making it an ideal choice for users requiring remote file management capabilities. The integration of a MySQL database ensures reliable storage and retrieval of user and access control details. The system's use of AES encryption guarantees the confidentiality and integrity of data during communication.

# Implementation

 Markup : 1. Connect to mysql database and create tables as given in database.txt
          2. Check the port number and ip address so that it matches with the mySQL server
          3. In both the server codes there is a global variable path assign with the path where you want to store the files and directories.
          4. Similarly change the path in client.py which takes the name main_path.
          5. In the client.py the path is split and stored in path_elemets and these elements are assigned to different variables based on array indexes so, do check the indexes in order to run the code properly
          6. Now, Run server.py file #Server1 gets started
          7. Run server2.py #Server 2 gets started
          8. Run client.py

After successfully running client.py a GUI interface is opened where you can login or signup and after logging in a new window is opened where all the operations can be perfomed.


