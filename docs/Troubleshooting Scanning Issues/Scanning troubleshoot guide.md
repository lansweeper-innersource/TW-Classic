<!-- # Scanning troubleshoot guide -->
[Lansweeper](https://www.lansweeper.com/ "Lansweeper ") can scan a variety of devices using different ports and protocols. Troubleshooting steps for scanning issues are provided for Windows, Linux/Unix, Mac, ESX/vCenter/Citrix servers, and network devices. The LsAgent and LsPush scanning agents are recommended for scanning computers without an agent. Common issues include closed ports, incorrect credentials, and firewall configurations.

For an overview of all your scanning options, see [Lansweeper's Scanning Guide](https://www.lansweeper.com/resources/lansweeper-scanning-guide/ "Scanning Guide").

This guide provides troubleshooting steps for issues you may encounter while scanning:

- [Windows computers](#heading1)
- [Linux or Unix computers](#heading2)
- [Mac computers](#heading3)
- [ESX, vCenter or Citrix servers](#heading4)
- [Network devices like printers, switches, etc](#heading5)

## Windows computers

Below is an overview of issues you may encounter while scanning Windows computers and information on how to fix them.

If scanning a computer without an agent fails, you can always use the [LsAgent](/docs/introduction-to-lsagent-for-windows-linux-and-mac) or [LsPush](/docs/introduction-to-the-lspush-scanning-agent-for-windows) scanning agent instead. Because they scan locally, the scanning agents are immune to almost all scanning errors, including access denied and firewall errors.

- **No asset is created for a scanned Windows computer.**

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/no-asset-created-for-scanned-computer-or-device).
- **Windows computer is detected as NAS.**

  A Windows computer may be detected as NAS if port 135 is permanently or temporarily closed in the client machine's firewall. This port is used by Lansweeper to determine whether a machine is Windows or non-Windows. For correct identification of Windows computers, port 135 must be open in the computers' firewalls.
- **Scanning error: Scanning access denied** **(0x80070005)**.

  This error indicates that an incorrect scanning credential or other configuration issue is causing the computer not to respond to requests for WMI data. Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/wmi-access-is-denied-0x80070005).
- **Scanning error:** **Computer is online but firewalled**.

  This error indicates that the computer responds to a ping request but not to a request for WMI data. It is usually caused by an incorrect firewall configuration. Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/the-rpc-server-is-unavailable-0x800706ba).
- **Scanning error:** **Computer is offline or firewalled**.

  This error indicates that the computer does not respond to a ping request or a request for WMI data. It is usually caused by an incorrect firewall configuration. Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/the-rpc-server-is-unavailable-0x800706ba).
- **Scanning error:** **The RPC server is unavailable**.

  This error indicates that the computer does not respond to a request for WMI data. It is usually caused by an incorrect firewall configuration. Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/the-rpc-server-is-unavailable-0x800706ba).
- **Scanning error: -2147418110 Call was canceled by the message filter. (Exception from HRESULT: 0x80010002 (RPC\_E\_CALL\_CANCELED)).**

  This error indicates that the computer does not respond to a request for WMI data. It is usually caused by a bad network connection or by a third-party firewall blocking access to the computer. If the issue is firewall related, you can resolve it by either allowing \*all\* WMI traffic through your firewalls, setting up a fixed WMI port or scanning with the LsAgent or LsPush scanning agent instead.
- **Scanning error: The object invoked has disconnected from its clients. (Exception from HRESULT: 0x80010108 (RPC\_E\_DISCONNECTED)).**

  This error indicates that the computer does not respond to a request for WMI data. It is usually caused by a bad network connection or a WMI query taking too long to return data.
- **Scanning error:** **-2147221164 Class not registered (Exception from HRESULT: 0x80040154 (REGDB\_E\_CLASSNOTREG))**.

  This error occurs when attempting to scan a Windows computer running Windows NT 4.0 or an older operating system. Lansweeper only supports scanning of Windows 2000 and more recent operating systems. This error can also occur when the Windows computer has a supported OS but a corrupt WMI implementation. Instructions for resolving WMI corruption issues can be found in [this knowledge base article](/docs/repair-a-corrupt-wmi-installation).
- **Scanning error:** **Computer name <name of client machine> does not resolve to an IP address. Please check your DNS settings**.

  This error indicates that the name of the computer, the one specified in the error, does not resolve to an IP address. This is a DNS problem, not a Lansweeper problem, and must be discussed with your network administrator. Your network admin must ensure that the DNS server configured on your Lansweeper scanning server resolves computer names to the correct IP addresses.
- **Scanning error:** **Corrupt LsPush file, repair WMI on this computer**.

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/repair-a-corrupt-wmi-installation).
- **Scanning error:** **WMI service is disabled on this machine**.

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/wmi-service-is-disabled-on-this-machine).
- **Socket errors occur when sending data scanned by the LsPush scanning agent directly to the Lansweeper server.**

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/socket-errors-when-scanning-with-the-lspush-scanning-agent).
- **Scan files generated by the LsPush scanning agent fail to import.**

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/lspush-scan-files-failing-to-import).

## Linux or Unix computers

Below is an overview of issues you may encounter while scanning Linux or Unix computers, and information on how to fix them.

If scanning a computer without an agent fails, you can always scan it using the [LsAgent](/docs/introduction-to-lsagent-for-windows-linux-and-mac) scanning agent instead. Because it scans locally, the scanning agent is immune to almost all scanning errors.

- **No asset is created for a scanned Linux computer.**

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/no-asset-created-for-scanned-computer-or-device).
- **Scanning error:** Cannot connect to SSH server.

  This error indicates that the machine was identified as a Linux or Unix computer but the SSH port on the machine cannot be accessed. This can be due to SSH being disabled on the computer or the SSH port being blocked or incorrectly submitted in Lansweeper. Step-by-step instructions for setting up SSH scanning of Linux and Unix computers can be found in [this knowledge base article](/docs/how-to-scan-a-linux-or-unix-computer).
- **Scanning error: Could not connect to SSH with credentials <name of credential>.**

  This error indicates that the SSH port on the computer can be accessed but data cannot be retrieved using the credential provided. This can be due to the credential lacking the necessary privileges. Step-by-step instructions for setting up SSH scanning of Linux and Unix computers can be found in [this knowledge base article](/docs/how-to-scan-a-linux-or-unix-computer).
- **Scanning error:** LinuxNoSudoRights.

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/linux-scanning-error-linuxnosudorights).
- **Scanning error:** **LinuxNotInstalled dmidecode**.

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/linux-scanning-error-dmidecode).
- **Scanning error:** **Hal-find-by-property not available**.

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/linux-scanning-error-hal-find-by-property).
- **Scanning error:** **LinuxTtyRequired**.

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/linux-scanning-error-tty-required).

## Mac computers

Below is an overview of issues you may encounter while scanning Mac computers, and information on how to fix them.

If scanning a computer without an agent fails, you can always scan it using the [LsAgent](/docs/introduction-to-lsagent-for-windows-linux-and-mac) scanning agent instead. Because it scans locally, the scanning agent is immune to almost all scanning errors.

- **No asset is created for a scanned Mac computer.**

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/no-asset-created-for-scanned-computer-or-device).
- **Scanning error: Cannot connect to SSH server.**

  This error indicates that the machine was identified as a Mac computer but the SSH port on the machine cannot be accessed. This can be due to SSH being disabled on the computer or the SSH port being blocked or incorrectly submitted in Lansweeper. Step-by-step instructions for setting up SSH scanning of Mac computers can be found in [this knowledge base article](/docs/how-to-scan-an-apple-mac-computer).
- **Scanning error: Could not connect to SSH with credentials <name of credential>.**

  This error indicates that the SSH port on the computer can be accessed but data cannot be retrieved using the credential provided. This can be due to the credential lacking the necessary privileges. Step-by-step instructions for setting up SSH scanning of Mac computers can be found in [this knowledge base article](/docs/how-to-scan-an-apple-mac-computer).

## ESX, vCenter or Citrix servers

Below is an overview of issues you may encounter while scanning ESX, vCenter or Citrix servers, and information on how to fix them.

- **No asset is created for a scanned ESX, vCenter or Citrix server.**

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/no-asset-created-for-scanned-computer-or-device).
- **Scanning error: Could not scan VMware with credentials <name of credential>.**

  This error indicates that data cannot be pulled from the ESX server using the credential provided. This can be due to the credential lacking the necessary read-only privileges. Step-by-step instructions for setting up scanning of a VMware server can be found in [this knowledge base article](/docs/how-to-scan-a-vmware-server).
- **Little to no data is listed on a vCenter server's asset page.**

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/troubleshooting-vcenter-scanning-issues).
- **Little to no data is listed on a Citrix server's asset page.**

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/troubleshoot-citrix-scanning-issues).

## Network devices like printers, switches etc

Below is an overview of issues you may encounter while scanning network devices, and information on how to fix them.

- **No asset is created for a scanned network device.**

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/no-asset-created-for-scanned-computer-or-device).
- **Scanning error:** Scan incomplete. SNMP was not scanned, but existing record has SNMP info.

  This error indicates that the device previously returned data through the SNMP protocol but no longer does. Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/troubleshoot-snmp-scanning-issues).
- **Little to no data is listed on a Ricoh printer's asset page.**

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/unable-to-scan-snmp-on-ricoh-printers).
- **SNMP was scanned for the device and an OID is listed in the Summary tab of the device's asset page, but any custom OIDs are not being scanned.**

  Step-by-step instructions for resolving this issue can be found in [this knowledge base article](/docs/troubleshooting-custom-oid-scanning-issues).
