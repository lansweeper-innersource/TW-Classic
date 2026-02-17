<!-- # Scan a network device -->
![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_214/image_001.jpg) **This page explains how Lansweeper can scan network devices, such as cameras, firewalls, printers, routers, and switches.**

Apart from scanning Linux, Unix, Mac and Windows computers, as well as VMware servers, Lansweeper is also capable of scanning network devices. Some examples of network devices are: cameras, firewalls, mail servers, music systems, NAS devices, printers, routers, switches, UPS devices, VOIP phones and web servers.

The exact data returned depends on the protocols enabled on the device, as well as the device type. Below are two sample device pages, one of a printer and one of a switch.   
Scanned printer data includes device description, network interfaces, manufacturer, model, printed pages, printer status, toner levels, serial number, uptime and more.  
![how-to-scan-a-network-device-1.jpg](/docs/.document360/assets/article_214/image_002.jpg)

Scanned switch data includes device description, manufacturer, model, port mapping information, serial number, uptime and more.  
![how-to-scan-a-network-device-2.jpg](/docs/.document360/assets/article_214/image_003.jpg)

## Scan a network device

1. Make sure you meet [the network device scanning requirements](/docs/network-device-scanning-requirements).
2. Submit your device's [IP range for scanning](https://www.lansweeper.com/feature/ip-scanner/) by selecting **Add Scanning Target** in the **Scanning > Scanning Targets** section of the web console.   
   If you have multiple scanning servers, there will be a separate configuration tab for each server. When submitting your range, you will be asked to specify a scanning schedule. If your device uses a custom SIP or SSH port, make sure to submit the correct port number as well.

   ![menu-scanning-scanning-targets.jpg](/docs/.document360/assets/article_214/image_004.jpg)

   ![procedure-submitting-ip-range-for-scanning.jpg](/docs/.document360/assets/article_214/image_005.jpg)  
     

   If the **Save Pinged IP** option is ticked, which it is by default in recent Lansweeper releases, assets are generated for all IP addresses that respond to a ping request.   
   If **Save Pinged IP** is not ticked, an asset is only generated for a network device if data can be pulled from one or more of the following protocols on the device: Bonjour, DNS-SD, FTP, HTTP, HTTPS, JetDirect, mDNS, SIP, SMTP, SNMP (SNMPv1, SNMPv2 or SNMPv3), SSDP, SSH, Telnet, UPnP or WMI.
3. If your device supports SNMP or SSH, submit your SNMP/SSH credential in the **Scanning > Scanning Credentials** section of the web console.  
   ![menu-scanning-scanning-credentials.jpg](/docs/.document360/assets/article_214/image_006.jpg)   
   You can use the same credential for all SNMP/SSH enabled devices by editing the Global SNMP/SSH credential or submit a non-global credential with the **Add new Credential** button.   
   SNMPv1, SNMPv2 and SNMPv3 are supported.

   ![how-to-scan-a-network-device-3.jpg](/docs/.document360/assets/article_214/image_007.jpg)  

   Keep in mind that SSH scanning is only supported for \*nix based systems like Linux, Unix and Mac computers. Ideally, other network devices are scanned through SNMP. We have scanning requirements for [Linux/Unix](/docs/linux-and-unix-agentless-scanning-requirements) and [Mac.](/docs/apple-mac-scanning-requirements)
4. If the credential you set up is not a global credential, map the credential to your device's IP range by selecting **+ Credential** for the range.

   ![how-to-scan-a-network-device-4.jpg](/docs/.document360/assets/article_214/image_008.jpg)
5. Wait for your scanning schedules to trigger or initiate an immediate scan by selecting **Scan now** next to the range under **Scanning > Scanning Targets**.

   ![procedure-scan-now-under-scanning-targets.jpg](/docs/.document360/assets/article_214/image_009.jpg)
6. Monitor the progress of your scan request under **Scanning > Scanning Queue**.

   ![menu-scanning-scanning-queue.jpg](/docs/.document360/assets/article_214/image_010.jpg)
