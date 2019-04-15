import paramiko


def ssh_connect(ip, port, user, passwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, user, passwd)
    return ssh


def ssh_exec(ssh: paramiko.SSHClient, command):
    stdin, stdout, stderr = ssh.exec_command(command)
    print(stdout.read().decode('utf-8'))
    return stdin, stdout, stderr


if __name__ == "__main__":
    ip = "192.168.150.130"
    port = 22
    user = "root"
    passwd = "toor"
    ssh = ssh_connect(ip, port, user, passwd)
    command = input()
    while (command != 'quit'):
        ssh_exec(ssh, command)
        command = input()
