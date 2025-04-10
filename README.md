
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

## 🕵️‍♂️ Command Audit Logging – Monitoring Attacker Behavior

📌 **Label:** Command Activity Log

This section highlights the command logging capabilities of the SSH honeypot. Once an attacker successfully gains access using captured credentials, every command they execute within the fake environment is meticulously logged in the `cmd_audits.log` file.

These logs are crucial for understanding an attacker's intent and behavior. By analyzing the sequence of commands, security teams can assess:
- What files or directories the attacker tried to access
- Whether sensitive or critical configurations were targeted
- The depth of their interaction within the compromised system

![cmd audit](https://github.com/user-attachments/assets/852754fe-5c43-4042-a66e-7aaaf0e4e71d)

## 🌐 Web Honeypot – Simulating Web-Based Attacks

📌 **Label:** Web Honeypot Server

The Web Honeypot is an integral part of this deception-based security infrastructure. Just like the SSH Honeypot, it simulates a vulnerable web application to attract and engage attackers. This system is designed to detect, monitor, and log malicious activity targeting web interfaces.

### 🧠 Objective

The primary purpose of this Web Honeypot is to mimic a real-world web server, tricking attackers into thinking they are interacting with an actual target. It enables defenders to gather information about web-based exploitation attempts, such as:
- Unauthorized form submissions
- Directory traversal attempts
- HTTP methods probing (e.g., GET, POST, PUT)
- Injection attacks and more

### 📂 Web Honeypot Features

- Simulated admin and login interfaces
- Fake pages designed to lure attackers into revealing their methods
- Logs all HTTP requests including IP address, URL paths, and parameters
- Captures credentials or payloads submitted by intruders

![web_honey](https://github.com/user-attachments/assets/aca8601c-0e59-4342-a370-430865383add)

## 🧠 Web Honeypot Logging – HTTP Audit System

📌 **Label:** Web Honeypot Server

This component of the honeypot infrastructure emulates a vulnerable web application interface, capturing malicious interactions with precision. The system is crafted to resemble a real website and is highly effective at deceiving threat actors attempting unauthorized access.

### 🔓 Credential Trap Mechanism

The honeypot presents a fake login form (e.g., `admin.html`) that appears functional to the attacker. Common attacker behavior includes attempting access using **default credentials**, such as:

- **Username:** admin
- **Password:** password

Upon submission, the system simulates a successful login response — but in reality, it silently logs the entire interaction.

### 🕵️ HTTP Audit Logging

Every HTTP request made to the honeypot is recorded in the `http_audits.log` file. These logs provide:

- 🌐 **Source IP Address**
- 🧑‍💻 **Attempted Credentials**
- 🕒 **Exact Timestamps**
- 🌍 **Targeted Paths (e.g., `/admin.html`, `/login`)**


📌 Purpose of HTTP Audit Logs
The http_audits.log file helps cybersecurity professionals:

Monitor attacker behavior and timing

Capture brute-force or credential-stuffing attempts

Analyze attacker tools and automation scripts

Develop alerting mechanisms based on access patterns

💡 Bonus Insight
By recording exact timestamps and actions, defenders can reconstruct attacker sessions for analysis or legal reporting. These logs also serve as evidence for red-team/blue-team exercises or academic research in web-based attack strategies.

📸 Screenshot Example:
### Wordpress Login page
![webpag](https://github.com/user-attachments/assets/cca11427-bf9b-4ac0-ac73-c5cf0904d7b1)







