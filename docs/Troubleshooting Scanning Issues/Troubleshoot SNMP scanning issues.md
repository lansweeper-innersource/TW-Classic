<!-- # Troubleshoot SNMP scanning issues -->
SNMP is one of the protocols through which Lansweeper can retrieve data regarding network devices like printers, switches, routers etc.

If the SNMP protocol was not scanned for a device in your network:

1. Follow the steps in [No asset created for scanned computer or device](/docs/no-asset-created-for-scanned-computer-or-device) to ensure there is no general scanning issues.
2. Make sure that TCP port 135 is closed on the device, as having this port open will cause the device to be identified as a Windows computer. Windows computers are not scanned via SNMP.
3. Make sure SNMP is enabled on the device.  

   The procedure to enable SNMP can vary greatly between devices. Consult your vendor's documentation.
4. Make sure SNMP on the device responds to a read request on OID 1.3.6.1.2.1.1.2.0. This is a system OID that should exist on SNMP-enabled devices. Lansweeper tries to read this OID first. If no response is given, it is assumed SNMP is disabled or not working and Lansweeper skips SNMP scanning.
5. Make sure SNMP traffic in your network (over port 161) isn't blocked. Scanning requests are sent outbound by your Lansweeper server and are accepted inbound on your network devices.
6. Make sure the device responds to SNMP requests on the same IP address as they were received. If the device responds from a different IP address, Lansweeper will ignore this data.
7. If you're using an SNMPv3 credential, make sure FIPS compliance is not enabled on your Lansweeper server.
8. Use the devicetester.exe tool, found in the "Program Files (x86)\Lansweeper\Actions" folder on your Lansweeper server, to test the SNMP connection to the device. Launch the tester from your Lansweeper server directly, then submit the IP address of the device and your SNMP credential. Read-only rights are sufficient for your credential. A successful SNMP test should list the ObjectID of the device.
9. Once SNMP access works in the test tool, make sure the correct SNMP community string with read access (the one previously used in devicetester) is submitted under **Scanning > Scanning Credentials** in Lansweeper and mapped to the device.
10. Rescan the network device by selecting **Rescan Asset** on the device's Lansweeper webpage.
11. Verify whether SNMP was scanned by looking for an OID in the **Summary** tab of the device's webpage. If no OID is present, SNMP wasn't scanned and custom OIDs cannot be scanned either.
