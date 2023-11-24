
import socket 
from threading import Thread 
from socketserver import ThreadingMixIn
import os
import base64
import pickle
import shutil
import pyaes, pbkdf2
import cryptography
import base64



running = True

def getKey(): #generating key with PBKDF2 for AES
    password = "s3cr3t*c0d3"
    passwordSalt = '76895'
    key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
    return key

def decrypt(enc): #AES data decryption
    aes = pyaes.AESModeOfOperationCTR(getKey(), pyaes.Counter(31129547035000047302952433967654195398124239844566322884172163637846056248223))
    decrypted = aes.decrypt(enc)
    return decrypted

def startDistributedCore():
    class CoreThread(Thread): 
 
        def __init__(self,ip,port): 
            Thread.__init__(self) 
            self.ip = ip 
            self.port = port 
            print('Request received from Client IP : '+ip+' with port no : '+str(port)+"\n") 
 
        def run(self): 
            data = conn.recv(100000)
            dataset = pickle.loads(data)
            request = dataset[0]
            if request == "createdir":
                user = dataset[1]
                dirname = dataset[2]
                dirname = base64.b64decode(dirname)
                dirname = decrypt(dirname)
                dirname = dirname.decode("utf-8")
                print(dirname)
                # dirname = base64.b64decode(dataset[2]).decode('utf-8')
                if os.path.exists('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user) == False:
                    os.mkdir('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user)
                if os.path.exists('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user+"/"+dirname) == False:
                    os.mkdir('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user+"/"+dirname)
                conn.send("Directory Created".encode())
                print("Directory Created: "+dirname)
            if request == "createfile":
                user = dataset[1]
                dirname = dataset[2]
                filename = dataset[3]
                print(user,dirname,filename)
                dirname = base64.b64decode(dirname)
                dirname = decrypt(dirname)
                dirname = dirname.decode("utf-8")
                filename = base64.b64decode(filename)
                filename = decrypt(filename)
                filename = filename.decode("utf-8")
                print(dirname,filename)
                if os.path.exists('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user+"/"+dirname):
                    open('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user+"/"+dirname+"/"+filename, 'w').close()
                    conn.send("File Created".encode())
                    print("File Created: "+filename)
                else:
                    conn.send("Given path does not exists".encode())
                    print("Given path does not exists: "+filename)
            if request == "deletefile":
                user = dataset[1]
                dirname = dataset[2]
                if os.path.exists('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user+"/"+dirname):
                    if os.path.isdir('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user+"/"+dirname):
                        shutil.rmtree('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user+"/"+dirname)
                    if os.path.isfile('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user+"/"+dirname):    
                        os.remove('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user+"/"+dirname)
                    conn.send("Given file deleted".encode())
                    print("Given file deleted: "+dirname)
                else:
                    conn.send("file does not exists".encode())
                    print("file does not exists: "+dirname)
            if request == "writefile":
                user = dataset[1]
                dirname = dataset[2]
                filename = dataset[3]
                encrypt = dataset[4]
                if os.path.exists('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user+"/"+dirname+"/"+filename):
                    f = open('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user+"/"+dirname+"/"+filename, "w")
                    f.write(encrypt)
                    f.close()
                    conn.send("file data saved at server".encode())
                    print("file data saved at server: "+filename)
                else:
                    conn.send("file does not exists".encode())                
                    print("file does nots exists: "+filename)

            if request == "renamefile":
                user = dataset[1]
                dirname = dataset[2]
                oldname = dataset[3]
                newname = dataset[4]
                if os.path.exists('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user+"/"+dirname+"/"+oldname):
                    os.rename('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user+"/"+dirname+"/"+oldname,'C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user+"/"+dirname+"/"+newname)
                    conn.send("file rename at server".encode())
                    print("file rename at server: "+newname)
                else:
                    conn.send("file does not exists".encode())
                    print("file does not exists")

            if request == "listfiles":
                user = dataset[1]
                file_list = []
                for root, dirs, directory in os.walk('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user):
                    for j in range(len(directory)):
                        file_list.append(root+"/"+directory[j])
                file_list = pickle.dumps(file_list)
                conn.send(file_list)
                print("file list sent to user")        
                        
            if request == "readfile":
                user = dataset[1]
                dirname = dataset[2]
                filename = dataset[3]
                features = []
                if os.path.exists('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user+"/"+dirname+"/"+filename):
                    with open('C:/Users/Chaimama/Desktop/Pcs_Project/cmsc626distributed-file-system-main/'+user+"/"+dirname+"/"+filename) as f:
                        data = f.read()
                    f.close()
                    features.append("correct")
                    features.append(data)
                    features = pickle.dumps(features)
                    conn.send(features)
                    print("file sent to server: "+filename)
                else:
                    features.append("incorrect")
                    features = pickle.dumps(features)
                    conn.send(features)
                    print("file does not exists")    
                
            
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    server.bind(('localhost', 2778))
    threads = []
    print("Distributed File System Started\n\n")
    while running:
        server.listen(4)
        (conn, (ip,port)) = server.accept()
        newthread = CoreThread(ip,port) 
        newthread.start() 
        threads.append(newthread) 
    for t in threads:
        t.join()

def startCore():
    Thread(target=startDistributedCore).start()


startCore()


