import paramiko
import getpass
import time

#Create a ssh client
ssh_client = paramiko.SSHClient()

#Get credentials
hostname = input("Hostname: ")
port = int(input("Port: "))
username = input("Username: ")
password = getpass.getpass(prompt = 'Enter the password')

#Add to known
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname=hostname, port=port,username=username, password=password)

D_A = ssh_client.invoke_shell()

D_A.send('dir')
#D_A.send('cd\n')

time.sleep(.5)

output = D_A.recv(65000)

print(output.decode())

ssh_client.close()