<!-- # Configure Windows Firewall for agentless scanning of computers -->
[Lansweeper](https://www.lansweeper.com/) pulls Windows computer data from WMI (Windows Management Instrumentation), a management infrastructure built into Windows operating systems. The initial connection to a client machine is made over TCP port 135. By default, Windows then sends the WMI data over random ports in the 1025-5000 or 49152-65535 range.

Lansweeper first performs broadcasts to identify the Windows devices in your network. Next, discovered devices are added to a queue for further processing. Lansweeper then directly scans the Windows devices to gather detailed data, which involves sending a new WMI request to each device.

In order to remotely scan Windows computers, you must ensure that the machines' firewalls are properly configured to allow all WMI traffic. Simply opening specific ports is not enough, as traffic is sent over random ports in the 1025-5000 or 49152-65535 range. For more information, see [Ports scanned or used by Lansweeper](/classic/docs/ports-scanned-or-used-by-lansweeper).

To learn more about how Lansweeper scans your network, take a look at [our scanning guide](https://www.lansweeper.com/resources/lansweeper-scanning-guide/).

This article specifically explains how to configure Windows Firewall, also known as Windows Defender Firewall, for remote scanning of Windows computers. Windows Firewall has a remote administration setting you can enable to allow WMI traffic. The easiest way to enable this setting for all of your domain computers is using group policies.

If scanning a Windows computer remotely fails due to a firewall or other issue, you can always scan it using the [LsAgent](/classic/docs/introduction-to-lsagent-for-windows-linux-and-mac) or [LsPush](/classic/docs/introduction-to-the-lspush-scanning-agent-for-windows) scanning agent instead. Because they scan locally, the scanning agents are immune to almost all scanning errors, including access denied and firewall errors.

## Configuring Windows Firewall visually

To configure Windows Firewall on your client machines to allow WMI traffic:

1. Open the group policy editor for your client machines.
2. Browse to one of the sections listed below. Which one you have depends on your OS.

   `Computer Configuration\Administrative Templates\Network\Network Connections  
   \Windows Defender Firewall\Domain Profile`

   or

   `Computer Configuration\Administrative Templates\Network\Network Connections  
   \Windows Firewall\Domain Profile`

   
3. Right-click one of the settings listed below and choose **Edit.** Which one you have depends on your OS.
   - Windows Defender Firewall: Allow inbound remote administration exception
   - Windows Firewall: Allow inbound remote administration exception
   - Windows Firewall: Allow remote administration exception
4. Select the **Enabled** option to enable the group policy.

   
5. In the options under **Allow unsolicited incoming messages from these IP addresses**, enter your Lansweeper scanning server's IP address and continue. Alternatively, submit the "\*" wildcard to allow traffic from all IP addresses.

   
6. Wait for your policy to take effect on your client machines, which may take several hours. Alternatively, run the below command on your machines to force the group policy to apply.  
   `gpupdate /force`
7. Verify whether your policy is correctly applied. You can do this by running the below command on a machine.  
   `netsh firewall show state`  

   

## Configuring Windows Firewall through commands or scripts

If you prefer to configure Windows Firewall through commands or scripts, you can either:

- Run the commands below in an elevated command prompt on the client machine. These commands will run successfully on both older and newer operating systems. They may generate deprecation warnings on newer operating systems but will function regardless.  
  `call netsh firewall set service RemoteAdmin enable`  
  `call netsh firewall add portopening protocol=tcp port=135 name=DCOM_TCP135​`