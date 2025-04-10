
## 🛡️ Honeypot-Based Network Intrusion Detection System

This project is a **Honeypot System** designed to act as a **decoy environment** for potential attackers targeting a company's network infrastructure. When an unauthorized user attempts to access the network, this honeypot system acts as a **middleware layer**, mimicking the behavior of the real network.

### ❓ Why Honeypot is Required

In today’s digital landscape, organizations face constant threats from hackers, malware, and advanced persistent threats (APTs). Traditional security systems like firewalls and antivirus software often detect threats only after the damage has begun. A **honeypot** provides an extra layer of proactive security by:

- **Deceiving attackers** into interacting with fake systems instead of real infrastructure.
- **Detecting unknown and zero-day threats** that may bypass conventional defenses.
- **Collecting valuable threat intelligence** such as attack patterns, tools used, and IP addresses.
- **Reducing attack surface** by diverting malicious traffic away from actual systems.
- **Alerting security teams in real-time**, allowing faster response and containment.

By deploying a honeypot, organizations can **stay ahead of attackers**, analyze intrusion behavior safely, and strengthen their overall cybersecurity defense strategy.

### 🔍 How It Works

- The honeypot is strategically deployed within the internal network of the organization.
- When an attacker initiates a scan or attack, their traffic is **intercepted and redirected** to the honeypot.
- The honeypot is configured to simulate the services and behavior of the original network, tricking the attacker into believing they are interacting with real assets.
- Meanwhile, **no actual systems are harmed**, and the real production environment remains untouched.
- All malicious activities and intrusion attempts are **logged and monitored** for further analysis, alerting the network defenders in real-time.

### 🎯 Key Features

- Acts as a **fake network environment** to lure attackers.
- Prevents direct access to the original servers or systems.
- Logs attacker IP, payloads, access time, and suspicious commands.
- Supports integration with a central monitoring system or security information and event management (SIEM) solution.
- Helps improve overall network security posture by analyzing attacker behavior and techniques.
Great! Here's a short and professional description you can include in your `README.md` under a new **Technologies Used** section:

### 🧰 Technologies Used

- **Python**: The core language used to develop the honeypot system due to its flexibility, simplicity, and rich set of libraries for network programming and automation.

- **Paramiko**: A powerful Python library for handling SSH connections. It is used to simulate SSH services, allowing the honeypot to mimic real SSH servers and log attacker interactions.

- **Argparse**: A built-in Python module used for parsing command-line arguments. It allows users to easily customize and run the honeypot with different configurations directly from the terminal.

## 🗺️ Deployment Diagram

Below is the high-level deployment architecture of the honeypot system:

![honeypy](https://github.com/user-attachments/assets/afecf0d8-094f-4fb1-a0fd-3f2cde99a482)

## 🧪 Practical Demonstration – SSH Honeypot Running
###### SSH Server
The following screenshot captures a live instance of the SSH Honeypot in action. It shows the honeypot being executed using the `python3 ssh_honey.py` command. Once initiated, the honeypot listens on a custom port (`2225`) and simulates an SSH server environment for attackers to interact with.

This allows logging of malicious connection attempts and shell activity without exposing the real infrastructure.

![ssh server](https://github.com/user-attachments/assets/52f9ccbd-184f-4a05-86b0-83b33636b969)

## 🧑‍💻 Attacker's Machine – Simulated Unauthorized Access

📌 **Label:** Attacker's Machine

This screenshot captures the activity of an attacker connecting to a private network service hosted within the XYZ infrastructure. The attacker has successfully established an SSH connection to the honeypot system, which emulates a vulnerable server environment.

- **Username:** `username`  
- **Password:** `password`  
- **Target IP Address:** `127.0.0.1` (localhost)  
- **Port:** `2225`  

After authentication, the attacker is granted access to a decoy shell interface. Within this fake environment, the attacker attempts basic reconnaissance, such as listing directories and reading configuration files. These interactions are logged for monitoring and analysis purposes.

This setup allows researchers and administrators to observe and study real-world attacker behavior in a controlled and safe environment.

![ubuntu](https://github.com/user-attachments/assets/d8db4f13-39e4-4af2-9df8-6a8a1595afc8)

## 📄 Audit Logging – Core of the SSH Honeypot

📌 **Label:** Audit Logging System

This screenshot represents the core functionality of the honeypot — the **audit logging** mechanism. When an unauthorized user attempts to access the SSH service, the system captures critical metadata including the **IP address**, **username**, and **password** used during the login attempt.

- **Captured IP:** `127.0.0.1` (Localhost in this simulation)
- **Username:** `username`
- **Password:** `password`

In this setup, both the SSH honeypot server and the simulated attacker are hosted on the same local machine, which is why the IP address logged is `127.0.0.1`. In a **real-world deployment**, this would be replaced with the **public IP address** of the attacker attempting to breach the network perimeter.

These logs serve as an essential tool for cybersecurity analysts to:
- Track unauthorized access attempts.
- Understand attacker behavior.
- Improve network defenses based on observed patterns.

All logs are stored persistently in the `audits.log` file and are available for further analysis.

![audit](https://github.com/user-attachments/assets/b7b9f11f-de93-43ee-9dd6-e8eb53b94162)







