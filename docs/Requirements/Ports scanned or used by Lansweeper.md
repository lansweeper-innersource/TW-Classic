<!-- # Ports scanned or used by Lansweeper -->
Below is an overview of ports scanned by [Lansweeper](https://www.lansweeper.com/) on client machines and ports used for internal communication between Lansweeper components.

To check the status of your ports, check out the pro tip [Ports Status](https://www.lansweeper.com/pro-tips/ports-status/).

- **Lansweeper web console access**

  HTTP port specified in the Lansweeper installer

  HTTPS port specified in the Lansweeper installer, when the default web server (IIS Express) is used. When using the alternate IIS web server, an HTTPS port must be configured directly in IIS Manager.
- **Lansweeper service and web console to Microsoft SQL Server database**

  Port: 1433/TCP and possibly other SQL Server related ports

  Which ports must be opened on the machine hosting your SQL Server instance depends on how your instance is configured. Port 1433 is a common port used for SQL Server traffic, but additional ports may need to be opened as well. Please review [this Microsoft knowledge base article](https://docs.microsoft.com/en-us/sql/sql-server/install/configure-the-windows-firewall-to-allow-sql-server-access?view=sql-server-ver15) for detailed information on how to allow SQL Server traffic through a firewall.
- **Lansweeper service and Lansweeper Network Discovery sensor to Active Directory domain controllers**

  Port: 389/TCP (LDAP) or [another LDAP(S) port of your choice](/classic/docs/use-ldaps-for-active-directory-scanning)  
  Port: 88 (if Kerberos is enabled or enforced)
- **Lansweeper service and Lansweeper Network Discovery sensor to scanned Windows computers**

  Port: 135/TCP (DCOM to establish the initial WMI session with the computer)

  Port: 139/TCP (NetBIOS Session Service)

  Port: 445/TCP (SMB)

  Random ports in the 1025-5000 or 49152-65535 range (to send the WMI data)

  By default, Windows sends WMI data over random ports, as explained in [this Microsoft knowledge base article](https://docs.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-on-a-remote-computer). There are three options to ensure the data stream:   
  1. Configure your firewalls to allow all WMI traffic. Windows Firewall includes a remote administration exception that you can enable to allow WMI traffic, as explained in [this knowledge base article](/classic/docs/configure-windows-firewall-for-agentless-scanning-of-computers). For third-party firewalls, consult your firewall's documentation.
  2. [Configure a fixed WMI port](https://docs.microsoft.com/en-us/windows/win32/wmisdk/setting-up-a-fixed-port-for-wmi) and allow traffic through that port.
  3. If you are unable to allow WMI traffic through your firewalls, scan your computers with the [LsAgent](/classic/docs/introduction-to-lsagent-for-windows-linux-and-mac) or [LsPush](/classic/docs/introduction-to-the-lspush-scanning-agent-for-windows) scanning agent instead, which does not require firewall reconfiguration.
- **Lansweeper service and Lansweeper Network Discovery sensor to scanned Linux, Unix and Mac computers**

  Port: 22/TCP (SSH) or a custom SSH port of your choice
- **Lansweeper service and Lansweeper Network Discovery sensor to scanned VMware servers**

  Port: 443/TCP (HTTPS)
- **Lansweeper service and Lansweeper Network Discovery sensor to scanned network devices**

  ICMP Ping

  Port: 21/TCP (FTP)

  Port: 22/TCP (SSH) or a custom SSH port of your choice

  Port: 23/TCP (Telnet)

  Port: 25/TCP (SMTP)

  Port: 80/TCP (HTTP)

  Port: 135/TCP (EPMAP)

  Port: 137/UDP (NetBIOS Name Service)

  Port: 139/TCP (NetBIOS Session Service)

  Port: 161 (SNMP)

  Port: 443/TCP (HTTPS)

  Port: 445/TCP (SMB)

  Port: 1400/TCP (Sonos devices HTTP)

  Port: 1900/TCP (SSDP, UPnP)

  Port: 1900/UDP (SSDP, UPnP)

  Port: 5060 (SIP) or a custom SIP port of your choice

  Port: 5353/TCP (mDNS, DNS-SD)

  Port: 5353/UDP (mDNS, Bonjour, DNS-SD)  
  Port: 5985/TCP (without SSL; WinRM HTTPS for Windows cluster log scanning and Hyper-V log scanning)

  Port: 5986/TCP (with SSL; WinRM HTTPS for Windows cluster log scanning and Hyper-V log scanning)

  Port: 8008/TCP (Chromecast)

  Port: 8080/TCP (HTTP)

  Port: 8443/TCP (HTTPS)

  Port: 9100/TCP (JetDirect)

  Port: 16992/TCP (Intel vPro HTTP)

  Port: 16993/TCP (Intel vPro HTTPS)

  Port: 62078/TCP (iTunes sync port for iOS device identification)
- **Scanned computers to Lansweeper service, if the LsAgent or LsPush scanning agent is used for scanning, with a direct connection to the Lansweeper server**

  Port: 9524/TCP or a custom port of your choice

  This port must be open in the firewall of the Lansweeper scanning server, i.e. the server hosting the Lansweeper Server service. You can choose a custom port in the **Service Options** section of the **Configuration > Server Options**menu.
- **Scanned computers to Lansweeper Network Discovery hub, if the IT Agent (portable) is used for discovery, with a direct connection to the Lansweeper Network Discovery** **hub**Port: 59525/TCP or a custom port of your choice  

  This port must be open in the firewall of the Lansweeper Network Discovery hub, i.e., the server hosting the Lansweeper Network Discovery hub service. You can override it with a custom port by modifying all instances of **59525** in `C:\Program Files\Lansweeper Network Discovery\hub\appsettings.json` and restarting the Lansweeper Network Discovery hub service.
