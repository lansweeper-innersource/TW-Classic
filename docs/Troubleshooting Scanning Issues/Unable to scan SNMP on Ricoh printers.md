<!-- # Unable to scan SNMP on Ricoh printers -->
If you're unable to scan SNMP on Ricoh printers:

1. Ensure that SNMP is enabled on your printer.
2. Run Lansweeper's [Devicetester](/classic/docs/troubleshoot-device-scanning-issues-with-devicetester "Use Devicetester to troubleshoot scan issues") and resolve any issues that it discovers.
3. If Devicetester is unable to access SNMP, set the **SNMP** version to **Version 1** and select **Scan device**.
4. If you are able to access SNMP, modify your Lansweeper credentials to only use SNMP version 1. In the web console, go to **Scanning > Scanning credentials > Add new credential**.
5. In **Type**, select **SNMP (V1/V2)** and deselect **Use SNMP (v2)**. Select **Ok**.

[Run a scan](/classic/docs/scan-a-network-device "Scan a network device"). You should be able to scan SNMP on your Ricoh printer.
