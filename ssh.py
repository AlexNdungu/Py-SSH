import paramiko
import getpass

#Create a ssh client
ssh_client = paramiko.SSHClient()

#Get credentials
hostname = input("Hostname: ")
username = input("Username: ")
password = getpass.getpass(prompt = 'Password :')


#Add to known
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect(hostname='192.168.100.9', username='user', password='joyce2001')
stdin, stdout, stderr = ssh_client.exec_command('free -m')

#Get the output
print(stdout.readlines())

ssh_client.close()