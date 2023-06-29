import paramiko
import getpass

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

commands = [
    'dir /ad /b',
    'cd'
]

out_list = []

for comm in commands:

    stdin, stdout, stderr = ssh_client.exec_command(comm)

    #Get the output
    #print(stdout.readlines())
    out_list.append(stdout.readlines())


print(out_list)

#Close Connection
ssh_client.close()