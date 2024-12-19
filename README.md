# ObStrike  

## Overview  
ObStrike is a  Command and Control (C2) framework designed for handling multiple reverse TCP  advanced features. Built to enhance the penetration testing experience, ObStrike supports dynamic payload generation, seamless shell session management.  

This project is tailored for both offensive and defensive cybersecurity professionals to better understand obfuscation and persistence techniques while improving system resilience against modern threats.  

---

## Key Features  
- **Payload Generation**:  
  - Supports default, customizable, and user-defined payload templates for Windows.  

- **File Operations**:  
  - Upload files via HTTP.  
  - Execute scripts directly in memory .  
- **Interactive Shell**:  
  - Auto-invoke ConPtyShell for PowerShell reverse shells to obtain fully interactive Windows shells.  
- **Multiplayer Mode**:  
  - Collaborate with team members on active sessions in real-time.  
- **Session Defender**:  
  - Prevent shell hangs by inspecting user-issued commands for potential errors or unintended inputs.  

---

## Technologies Used  
- **Python**: Core scripting and functionality.  
- **PowerShell**: Reverse shell creation and execution on Windows systems.  
- **Kali Linux**: Penetration testing platform.  
- **Ash Scripting**: For automation and Linux shell scripting.  
- **Linode**: Cloud hosting for remote C2 server deployment.  

---

