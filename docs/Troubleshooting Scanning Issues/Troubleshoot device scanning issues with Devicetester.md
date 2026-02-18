<!-- # Troubleshoot device scanning issues with Devicetester -->
The Lansweeper Devicetester is a powerful tool for troubleshooting scanning problems that affect non-Windows devices. If you need to contact support, provide the full output of the Devicetester for the device that is causing problems.

The Devicetester.exe tool is included in your Lansweeper installation. You can find it in the following folder on your Lansweeper server:

**Program Files (x86)\Lansweeper\Actions**

If you are experiencing [RPC unavailable](/classic/docs/the-rpc-server-is-unavailable-0x800706ba) or [access denied](/classic/docs/wmi-access-is-denied-0x80070005) errors on a Windows machine, use the Lansweeper testconnection.exe tool instead.

Always run the program on the same machine as the Lansweeper Service otherwise connection errors may go undetected.

The Devicetester runs the following tests:

- Ping If the ping fails, no other tests will be executed Will be skipped if ?Don't ping? is selected
- Open ports
- SNMP Only if an SNMP community is provided
- MAC address Only if the host is in the same subnet
- NetBIOS
- FTP Only if port 21 is open
- SMTP Only if port 25 is open
- HTTP Only if port 80 is open
- HTTPS Only if port 443 is open
- VMware Only if VMware server is detected
- SSH Only if port 22 is open and a username and password are provided

A hostname or FQDN can be used instead of an IP address for most tests. However, some of the tests will only work if you use an IP address.
