<!-- # Scanning with an IP Range scanning target -->
An IP Range target is an agentless, scheduled scanning target that scans any IP range specified by you. The IP Range Scanning is suitable for Linux, Unix, Mac and Windows computers, VMware servers and other network devices. Some examples of network devices are: cameras, firewalls, mail servers, music systems, NAS devices, printers, routers, switches, UPS devices, VOIP phones and web servers. Windows computers submitted for scanning with an IP Range target can belong to a domain or a workgroup. You can submit an unlimited number of [IP Range targets](https://www.lansweeper.com/feature/ip-scanner/) for scanning and specify a separate scanning configuration for each.

To submit an IP Range target for scanning, click the **Add Scanning Target** button in the **Scanning > Scanning Targets** section of the web console and choose the IP Range scanning type in the resulting pop-up. If you have multiple scanning servers, there will be separate configuration tabs on the **Scanning Targets** page, one for each server. Instead of manually submitting IP ranges one by one, you can also import them from a .csv file. Download the import template next to the **Import IP Ranges** button in the **Scanning Targets** menu, add your IP ranges to it and save as a .csv file. You can then import this file using the import button.





As agentless scanning of Linux, Unix, Mac and Windows computers, VMware servers and SNMP enabled network devices requires credentials, make sure to submit and map your scanning credentials as well, by following the instructions in [this knowledge base article](/docs/create-and-map-scanning-credentials).

## IP Range settings

The IP Range scanning target offers a variety of settings to help you customize and optimize your scan requests. Below is an overview of available options and settings. Each IP Range target submitted for scanning can be configured differently.



- **IP Start**: the IP address that starts the range should be entered.
- **IP End**: the IP address that ends the range should be entered.
- **Ping Time-out**: indicates the amount of time, in seconds, Lansweeper will spend waiting for a ping response from an asset before deeming the asset unreachable and moving on to the next IP address. In high traffic networks, increasing the timeout by several seconds is recommended.

  Based on the start IP, end IP and timeout you've configured, as well as your IP thread setting under **Configuration > Server Options**, an estimate is made of how long the scan of the IP range will take. Estimated scan times of 4 hours or more are displayed in red to warn you that these ranges may take a long time to finish scanning.
- **Don't ping**: if checked, Lansweeper will try to scan all IP addresses in the range, regardless of whether they can be pinged or not.  

  Checking Don't Ping will slow down scanning. It is generally recommended that you only enable this if you have devices that don't respond to ping requests.
- **Save pinged IP**: if checked, asset pages will be generated for all IP addresses that respond to a ping request, even if no data can be pulled from any of the following protocols: Bonjour, DNS-SD, FTP, HTTP, HTTPS, JetDirect, mDNS, SIP, SMTP, SNMP (SNMPv1, SNMPv2 or SNMPv3), SSDP, SSH, Telnet, UPnP or WMI.
- **Ignore Windows**: if checked, Windows computers within the IP range will not be scanned. Enabling this option is useful if you are already using other scanning targets to scan Windows computers. You can then opt to use the IP Range target just for scanning Linux, Unix and Mac computers, VMware servers and other network devices.
- **Scan New Windows Only**: if checked, only Windows computers that are not in the database yet will be scanned by the IP Range target. This setting only affects Windows computers; any non-Windows devices will still be scanned.
- **No SSH**: if checked, the SSH protocol will not be queried on the assets in the IP range.
- **Description**: a custom description of the scanning target can be entered.
- **SSH port**: the SSH port used for scanning should be entered. This is 22 by default.
- **SIP port**: the SIP port used for scanning should be entered. This is 5060 by default.
- **Schedule**: determines when (on which days of the week and at what time) the IP range will be scanned.
- **Enable**: toggle this option to enable or disable scanning of the IP range.
