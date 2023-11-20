# PCS_PROJECT_TEAM7
# Introduction
The goal of this project is to create a reliable and safe peer-to-peer (P2P) file storage system that uses a decentralized network for file management and sharing. We will accomplish this by utilizing the Kademlia. Data integrity, security, and user-friendliness are guaranteed by the system's extensive feature set, which includes version control, access control, data encryption, and auditing.

# Working


**Onboarding and Node Integration:**

When a user joins our network, they become a part of the Kademlia DHT, which forms the foundation of our system. Kademlia assigns a unique identifier (Node ID) to each user based on their user ID. The user's node seamlessly integrates into the network by reaching out to an existing node and contributing to the Kademlia routing table.

**Decentralized File Fragmentation and Distribution:**

Users can upload files to the system, and these files are fragmented into smaller, cryptographically hashed chunks. Each chunk is distributed across the Kademlia network and stored on nodes based on their Node IDs. Our system implements data replication mechanisms to ensure redundancy, thereby enhancing data resilience and availability.

**Version Tracking and Management:**

Our system employs robust version control to meticulously track changes to files and maintain an extensive history of file versions. When a user makes modifications to a file, our system generates a new version, assigns it a unique timestamp or version number, and securely stores it alongside the file's metadata. This feature empowers users to access and restore specific file versions, fostering data integrity and collaborative work.

**Fine-Grained Access Control and Permissions:**

Users enjoy precise control over file and directory access permissions, allowing them to determine who can read, write, or delete files. Access control lists (ACLs) are diligently maintained for each file or directory, ensuring that only authorized users can access or modify them.

**Data Security and Privacy Measures:**

Our system is committed to data privacy and security. File contents and metadata are thoroughly encrypted, limiting access to only authorized users. Secure communication protocols protect data during transit, and robust user authentication mechanisms prevent unauthorized access. Detailed auditing and logging processes closely monitor user activities, enhancing both security and accountability.

**Efficient Concurrent Write and Read Management:**

To handle concurrent read and write operations effectively, our system enforces mechanisms such as file locking and conflict resolution. In scenarios where multiple users attempt to modify the same file simultaneously, the system identifies conflicts and resolves them using predefined strategies.

**Streamlined File Retrieval:**

When a user requests a specific file, our system leverages the Kademlia DHT to precisely locate the file's chunks based on their Node IDs. The system then retrieves these chunks from their respective nodes, assembles the file, and decrypts it if necessary.

**Enhanced Data Redundancy and Availability:**

Our system boosts data availability by replicating data across multiple nodes within the Kademlia network. This strategic redundancy minimizes data loss in cases of node failures, thereby fortifying data availability and fault tolerance.

**User-Centric Interface:**

Our system features an intuitive and user-friendly interface, providing users with the tools to manage their files, review version histories, configure permissions, and restore specific file versions. 

Our P2P file storage system offers a comprehensive and secure solution for users to store, manage, and retrieve their files within a decentralized network, harnessing the robust Kademlia DHT. The system places a strong emphasis on data integrity, privacy, and effective collaboration, making it a powerful tool for contemporary file management.

After a successful login, the user will have access to the following options:

View a list of all files.
Create new files.
Read existing files.
Write to existing files.
Delete files.
Add new users.
Grant permissions.
Revoke permissions.
Create directories.
Delete directories.
