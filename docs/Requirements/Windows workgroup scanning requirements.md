<!-- # Windows workgroup scanning requirements -->
There are two main ways to scan a Windows computer: with a scanning agent or without a scanning agent.  
Both options return the same data, but the scanning agent allows for offsite scanning and is immune to credential and firewall issues.

Outlined below are the requirements for scanning Windows workgroup computers with or without an agent. Lansweeper will pull most Windows computer data from Windows Management Instrumentation (WMI), a management framework built into Windows operating systems. Some data is pulled directly from the client machine's registry as well.

## Requirements for scanning without a scanning agent

You can run [this VBScript](https://www.lansweeper.com/files/lansweeper.vbs) on your workgroup computer to correctly configure most settings, including Windows Firewall, User Account Control and security model settings. A reboot may be required after running the script.

To scan a Windows workgroup computer without an agent, the computer must meet the following requirements:

Windows workgroup scanning will not work unless the following key has been added to your registry. [The VBScript](https://www.lansweeper.com/files/lansweeper.vbs) will automatically add this key to your registry:  
"HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System\LocalAccountTokenFilterPolicy","1","REG\_DWORD"

- **Architecture**32-bit or 64-bit
- **Operating system**Windows XP or any more recent Windows operating system. Agentless scanning only supports non-Home editions of Windows.
- **Firewall**As Lansweeper pulls most Windows computer data from WMI (Windows Management Instrumentation), you need to ensure that WMI traffic is allowed through your client machine's and other firewalls.

By default, Windows sends WMI data over random ports, as explained in [this Microsoft knowledge base article](https://docs.microsoft.com/en-us/windows/win32/wmisdk/connecting-to-wmi-on-a-remote-computer). There are three options to ensure the data stream:   

1. Configure your firewalls to allow all WMI traffic. Windows Firewall includes a remote administration exception that you can enable to allow WMI traffic, as explained in [this knowledge base article](/classic/docs/configure-windows-firewall-for-agentless-scanning-of-computers). For third-party firewalls, consult your firewall's documentation.
2. [Configure a fixed WMI port](https://docs.microsoft.com/en-us/windows/win32/wmisdk/setting-up-a-fixed-port-for-wmi) and allow traffic through that port.
3. If you are unable to allow WMI traffic through your firewalls, scan your computers with [the LsPush scanning agent](/classic/docs/introduction-to-the-lspush-scanning-agent-for-windows) instead, which does not require firewall reconfiguration.

The firewall on the scanning server must whitelist **Lansweeperservice.exe** to make outbound connections and correctly scan your network.

- **Credentials**You must provide Lansweeper with a username/password combination that has administrative privileges on the client machine.
- **User Account Control**If the client machine is running Windows Vista or a more recent operating system, User Account Control (UAC) must be disabled on the computer, at a minimum for the user account you'll use to scan the machine.
- **Security model**The computer's security model must be set to Classic.
- **Installed software**No Lansweeper software is required on the client machine you're scanning. You do need to ensure that the Windows Management Instrumentation service is running on the machine, as this is what Lansweeper will use to retrieve data.

## Requirements for scanning with a scanning agent

To scan a Windows workgroup computer with [our LsPush scanning agent](/classic/docs/introduction-to-the-lspush-scanning-agent-for-windows), the computer must meet the following requirements:

- **Architecture**32-bit or 64-bit
- **Operating system**Windows XP or any more recent operating system. Unlike agentless scanning, agent based scanning supports Home editions of Windows.
- **Firewall**No firewall reconfiguration required
- **Credential**No credentials required
- **User Account Control**No UAC reconfiguration required
- **Security model**No security model reconfiguration required
- **Installed software**No Lansweeper software is required on the client machine you're scanning. You do need to ensure that the Windows Management Instrumentation service is running on the machine, as this is what Lansweeper will use to retrieve data.
