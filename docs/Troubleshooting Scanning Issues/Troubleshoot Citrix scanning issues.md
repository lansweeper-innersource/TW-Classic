<!-- # Troubleshoot Citrix scanning issues -->

If you encounter issues while scanning your Citrix XenServer machines:

1. Make sure that there are no general scanning issues by ensuring [an asset was created in the web console for your computer or device](/classic/docs/no-asset-created-for-scanned-computer-or-device "No asset created for scanned computer or device"). Once you've confirmed an asset was created, [rescan your Citrix XenServer hosts](/classic/docs/how-to-scan-a-citrix-xenserver "How to scan a Citrix XenServer").
2. Use [Devicetester](/classic/docs/troubleshoot-device-scanning-issues-with-devicetester "Troubleshoot device scanning issues with Devicetester") to make sure that the Citrix XenServer host meets the [Citrix scanning requirements](/classic/docs/citrix-scanning-requirements).
3. Scan for Open Ports. Ensure that the TCP port **443 (HTTPS)** is open on the XenServer host.

   
4. Scan HTTPS. Ensure the Title of the machine contains the text **XenServer** or **Citrix Hypervisor**.
5. Open a command prompt on the Lansweeper scanning server as an administrator, then Telnet to the IP address of the XenServer host in question on port 443 and check if a connection between Lansweeper and the XenServer can be made. For example, if your IP address is `192.168.2.119`, enter `telnet 192.168.2.119 443` in the command prompt.
