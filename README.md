# PCS_PROJECT_TEAM7

# Introduction:

The Distributed File System (DFS) is a client-server application designed to provide users with a secure and interactive platform for managing files remotely. The system is built with a focus on scalability, efficiency, and data security. Users can perform various file operations, including creating directories, creating and deleting files, reading and writing file content, renaming files, and sharing file access.

# Features:

# User Authentication:
Users can log in with existing credentials or sign up for a new account.
User registration details are securely stored in a MySQL database.

# File Operations:

1. Create Directories: Users can create directories to organize their files.
2. Create/Delete Files: Users can create and delete files within the system.
3. Read/Write File Content: Read and write operations are supported for file contents.
4. Rename Files: Users can rename files for better organization.
5. Share Access: File access can be shared with other users with specified access modes (Read/Write).
6. List Available Files: Users can view the list of available files for efficient management.

# Security:
The system employs Advanced Encryption Standard (AES) for secure data transmission between the client and server.
User credentials and sensitive data are protected during communication.
Database Interaction:

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

Users can view the list of available files, including those owned by them and files shared with them by other users.

# Conclusion:
The Distributed File System offers a robust and secure solution for users to manage files efficiently in a distributed environment. It combines user-friendly features with data security, making it an ideal choice for users requiring remote file management capabilities. The integration of a MySQL database ensures reliable storage and retrieval of user and access control details. The system's use of AES encryption guarantees the confidentiality and integrity of data during communication.
