<!-- # Network device scanning requirements -->

Apart from scanning Linux, Unix, Mac and Windows computers, as well as VMware servers, Lansweeper is also capable of scanning network devices. Some examples of network devices are cameras, firewalls, mail servers, music systems, NAS devices, printers, routers, switches, UPS devices, VOIP phones and web servers.

More specifically, Lansweeper can pull data from any device that has one or more of the following protocols enabled: Bonjour, DNS-SD, FTP, HTTP, HTTPS, JetDirect, mDNS, SIP, SMTP, SNMP (SNMPv1, SNMPv2 or SNMPv3), SSDP, SSH, Telnet, UPnP or WMI.

![network-device-scanning-requirements-1.jpg](/docs/.document360/assets/article_169/image_002.jpg)

SNMP generally provides Lansweeper with the most detailed device information. Many network devices have SNMP enabled by default and use public and private as their default SNMP community strings (i.e. passwords), public being for read-only access and private for read/write access. A community string with read-only access is sufficient for Lansweeper scanning.

![network-device-scanning-requirements-2.jpg](/docs/.document360/assets/article_169/image_003.jpg)

For information on configuring SNMP or another protocol on your device itself, you will need to consult the device documentation, as protocol support and setup differ from device to device. If you are unsure which protocols are enabled on a device, or would like to test your SNMP or SSH credential, run the **Devicetester.exe**tool on your Lansweeper server. It tests access to the various protocols supported by Lansweeper, and can be found in `Program Files (x86)\Lansweeper\Actions\Devicetester.exe`.  
Don't forget to submit your SNMP or SSH credential in the tester, if relevant. Also make sure to run the tool from the machine hosting the Lansweeper Server service, as this is the only way to simulate exactly which protocols your Lansweeper installation will have access to as well.

If [the **Save Pinged IP** option](/docs/scanning-with-an-ip-range-scanning-target#heading1 "Scanning with an IP Range scanning target") is enabled for your IP ranges, assets are generated for all IP addresses that respond to a ping request. If **Save Pinged IP** is not ticked, an asset is only generated for a network device if data can be pulled from one or more of the following protocols on the device: Bonjour, DNS-SD, FTP, HTTP, HTTPS, JetDirect, mDNS, SIP, SMTP, SNMP (SNMPv1, SNMPv2 or SNMPv3), SSDP, SSH, Telnet, UPnP or WMI.

Keep in mind that SSH scanning is only supported for \*nix based systems like Linux, Unix and Mac. Ideally, other network devices are scanned through SNMP. We have scanning requirements for [Linux/Unix](/docs/linux-and-unix-agentless-scanning-requirements) and [Mac.](/docs/apple-mac-scanning-requirements)
