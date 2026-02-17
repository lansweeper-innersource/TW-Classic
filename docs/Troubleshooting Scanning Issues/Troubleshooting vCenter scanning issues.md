<!-- # Troubleshooting vCenter scanning issues -->
In order for Lansweeper to scan your vCenter servers, you need to ensure that TCP port 443 is open on the vCenter server and that the server's HTTPS title contains the text "ID\_VC\_Welcome".

## VMware vCenter scanning troubleshooting

If you encounter issues while scanning your VMware vCenter servers:

1. Follow the steps in [No asset created for scanned computer or device](/docs/no-asset-created-for-scanned-computer-or-device) to ensure there are no general scan issues, including rescanning your machine.
2. Use the [Lansweeper Devicetester](/docs/troubleshoot-device-scanning-issues-with-devicetester) to make sure that the vCenter server meets the [vCenter scanning requirements](/docs/vcenter-scanning-requirements). Check that TCP port 443 is open on the vCenter server and that the HTTPS title contains the text "ID\_VC\_Welcome".

   ![vCenter-scanning-troubleshooting-1.jpg](/docs/.document360/assets/article_271/image_001.jpg)

   ![vCenter-scanning-troubleshooting-2.jpg](/docs/.document360/assets/article_271/image_002.jpg)
3. Make sure that the machine is a vCenter Server Appliance (vCSA) and that TCP ports 135, 139 and 445 are closed on the vCenter server.  

   Scanning a vCenter Server environment installed as software on a Windows computer is not supported. If Lansweeper determines a machine to be a Windows computer of if it finds TCP port 135 to be open, vCenter scanning is skipped.
4. Check connectivity from your Lansweeper scanning server to the vCenter server using a Telnet connection. Open an administrative Command Prompt on the Lansweeper scanning server. Telnet to the IP address of the vCenter server in question on port 443 and check if a connection can be made. See the example command below:  
   `telnet 192.168.2.119 443`
