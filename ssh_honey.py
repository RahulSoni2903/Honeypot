print("Created By RAHUL SONI")

import logging
from logging.handlers import RotatingFileHandler
import socket as socklib  
import paramiko
import threading

# === Setup Logging ===
logging_format = logging.Formatter('%(message)s')
SSH_BANNER = "SSH-2.0-MySSHServer_1.0"
host_key = paramiko.RSAKey(filename='server.key', password='hacker')

# Capture login attempts
f_logger = logging.getLogger('Funnel_logger')
f_logger.setLevel(logging.INFO)
f_handler = RotatingFileHandler('audits.log', maxBytes=2000, backupCount=5)
f_handler.setFormatter(logging_format)
f_logger.addHandler(f_handler)

# Capture shell commands
c_logger = logging.getLogger('Creds_logger')
c_logger.setLevel(logging.INFO)
c_handler = RotatingFileHandler('cmd_audits.log', maxBytes=2000, backupCount=5)
c_handler.setFormatter(logging_format)
c_logger.addHandler(c_handler)

# === Emulated Shell ===
def emulated_shell(channel, client_ip):
    channel.send(b'corporate-jumpbox2$')
    command = b""
    while True:
        char = channel.recv(1)
        if not char:
            break
        channel.send(char)
        command += char

        if char == b'\r':
            cmd = command.strip().decode()
            c_logger.info(f"[{client_ip}] {cmd}")

            if cmd == 'exit':
                channel.send(b'\nSSH Session Terminated.\n')
                break
            elif cmd == 'pwd':
                response = b"\n/usr/local/\r\n"
            elif cmd == 'whoami':
                response = b"\ncorpuser1\r\n"
            elif cmd == 'ls':
                response = b"\njumpbox1.conf\r\n"
            elif cmd == 'ls':
                response = b"\nid_rsa\r\n"
            elif cmd == 'cat jumpbox1.conf':
                response = b"\nGo to deeboodah.com\r\n"
            else:
                response = b"\nCommand not found.\r\n"

            channel.send(response)
            channel.send(b'corporate-jumpbox2$')
            command = b""

# === SSH Server Class ===
class Server(paramiko.ServerInterface):
    def __init__(self, client_ip, input_username=None, input_password=None):
        self.event = threading.Event()
        self.client_ip = client_ip
        self.input_username = input_username
        self.input_password = input_password

    def check_channel_request(self, kind, chanid):
        return paramiko.OPEN_SUCCEEDED if kind == 'session' else paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def get_allowed_auths(self, username):
        return "password"

    def check_auth_password(self, username, password):
        f_logger.info(f"[{self.client_ip}] Username: {username} | Password: {password}")
        if self.input_username and self.input_password:
            return paramiko.AUTH_SUCCESSFUL if username == self.input_username and password == self.input_password else paramiko.AUTH_FAILED
        return paramiko.AUTH_SUCCESSFUL

    def check_channel_shell_request(self, channel):
        self.event.set()
        return True

    def check_channel_pty_request(self, *args, **kwargs):
        return True

# === Client Handler ===
def client_handle(client, addr, username, password):
    client_ip = addr[0]
    print(f"{client_ip} has connected to the server.")

    try:
        transport = paramiko.Transport(client)
        transport.local_version = SSH_BANNER
        transport.add_server_key(host_key)

        server = Server(client_ip=client_ip, input_username=username, input_password=password)
        transport.start_server(server=server)

        channel = transport.accept(100)
        if channel is None:
            print("No channel was opened.")
            return

        banner = "Created By RAHUL SONI Welcome to Ubuntu 22.04 LTS\r\n\r\n"
        channel.send(banner.encode())
        emulated_shell(channel, client_ip)

    except Exception as error:
        print(f"[!] Exception: {error}")
    finally:
        try:
            transport.close()
        except:
            pass
        client.close()

# === Honeypot Starter ===
def honeypot(address, port, username, password):
    try:
        sock = socklib.socket(socklib.AF_INET, socklib.SOCK_STREAM)
        sock.setsockopt(socklib.SOL_SOCKET, socklib.SO_REUSEADDR, 1)
        sock.bind((address, port))
        sock.listen(100)
        print(f"SSH Honeypot is listening on {address}:{port} ...")
    except OSError as e:
        print(f"[!] Port {port} is already in use. Try another port.")
        return

    while True:
        try:
            client, addr = sock.accept()
            thread = threading.Thread(target=client_handle, args=(client, addr, username, password))
            thread.start()
        except KeyboardInterrupt:
            print("\n[!] Honeypot stopped by user.")
            break
        except Exception as error:
            print(f"[!] Error: {error}")

    sock.close()

# === Run Honeypot ===
if __name__ == "__main__":
    honeypot('127.0.0.1', 2225, 'username', 'password')
