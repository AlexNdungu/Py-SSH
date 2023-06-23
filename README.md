## Connecting To Remort Device Using SSH

### SSH

&rarr; It is a network protocol that helps us securely access and communicate with remote machines (mostly remote servers). It provides strong encryption and is widely used by network administrators and developers to manage remote systems & applications, execute commands, share files, etc

### [Paramiko](https://pypi.org/project/paramiko/)

&rarr; Paramiko is a pure-[Python](https://www.python.org/) (3.6+) implementation of the SSHv2 protocol, providing both client and server functionality. It provides the foundation for the high-level SSH library [Fabric](https://www.fabfile.org/).



```
pip install paramiko
```

```
#Example code snippet adapted from paramiko documentation

import paramiko

ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.connect('ssh.example.com')
stdin, stdout, stderr = ssh_client.exec_command('ls -l')
```