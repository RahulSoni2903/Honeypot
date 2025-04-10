# main file for running purpose.
# Libraries
import argparse
from ssh_honey import honeypot  # Import honeypot function from ssh_honey module

# Parse arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a simple honeypot on specified protocol.")
    parser.add_argument('-a', '--address', type=str, required=True, help='IP address to bind the honeypot')
    parser.add_argument('-p', '--port', type=int, required=True, help='Port to bind the honeypot')
    parser.add_argument('-u', '--username', type=str, help='Username for SSH honeypot')
    parser.add_argument('-pw', '--password', type=str, help='Password for SSH honeypot')
    parser.add_argument('-s', '--ssh', action="store_true", help='Run SSH based honeypot')
    parser.add_argument('-w', '--http', action="store_true", help='Run HTTP based honeypot')

    args = parser.parse_args()

    try:
        if args.ssh:
            print("[*] Running SSH based Honeypot...")
            username = args.username if args.username else "honeypot"
            password = args.password if args.password else "honeypot123"
            honeypot(args.address, args.port, username, password)

        elif args.http:
            print("[*] Running HTTP based Honeypot... (To be implemented)")

        else:
            print("[!] Please choose either SSH (-s) or HTTP (-w) honeypot mode.")

    except Exception as e:
        print(f"[!] Error occurred while running honeypot: {e}")
        print("[!] Exiting honeypot.")
