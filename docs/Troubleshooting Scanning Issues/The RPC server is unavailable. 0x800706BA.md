<!-- # The RPC server is unavailable. 0x800706BA -->
This page is for Lansweeper Classic. For Lansweeper Sites (in the cloud), see [RPC server is unavailable. 0x800706BA](/classic/docs/rpc-server-is-unavailable-0x800706ba).

When [Lansweeper](https://www.lansweeper.com/ "Lansweeper") scans Windows computers without a scanning agent, you may encounter "firewalled" or "RPC server unavailable" errors.

These errors can occur due to:

1. Incorrect firewall set ups
2. Offline machines
3. DCOM issues
4. Incorrect settings

For an overview of all your scanning options, see [Lansweeper's Scanning Guide](https://www.lansweeper.com/resources/lansweeper-scanning-guide/ "Scanning Guide").

To successfully perform an agentless scan with [RequireIntegrityActivationAuthenticationLevel](https://support.microsoft.com/en-us/topic/kb5004442-manage-changes-for-windows-dcom-server-security-feature-bypass-cve-2021-26414-f1400b52-c141-43d2-941e-37ed901c769c) set to 1, [KB5005033](https://support.microsoft.com/en-au/topic/august-10-2021-kb5005033-os-builds-19041-1165-19042-1165-and-19043-1165-b4c77d08-435a-4833-b9f7-e092372079a4) or newer must be installed.

If you're encountering errors, consider installing a scan agent. Scanning with an agent returns the same data and is a guaranteed solution to any "RPC server unavailable" or firewall errors. For more information, see:

- [Use LsPush to scan Windows computers](/classic/docs/introduction-to-the-lspush-scanning-agent-for-windows "Use LsPush to scan Windows computers")
- [Use LsAgent to Scan Windows, Linux, and Mac computers](/classic/docs/introduction-to-lsagent-for-windows-linux-and-mac "Use LsAgent to Scan Windows, Linux, and Mac computers")

## Troubleshoot the RPC server error

1. Look at the **Last scan attempt** date in the computer's **Summary** tab to determine when the scanning error occurred.
2. If the scanning error is not recent, rescan the computer first to verify whether the scanning issue is still present. You can rescan one or more machines by selecting **Assets** in the web console, ticking the checkboxes in front of the assets and selecting **Rescan**.
3. Make sure the computer is switched on. Computers that are offline will generate RPC errors as well.
4. Run the following tool on your Lansweeper server, as it will help in the troubleshooting process: `Program Files (x86)\Lansweeper\Actions\testconnection.exe`.

   You must open the test tool on your Lansweeper scanning server, i.e. on the machine that has the Lansweeper Server service installed. Tests initiated from other machines cannot be used for troubleshooting purposes, as they do not replicate the exact network conditions (e.g. firewalls) experienced by Lansweeper.
5. Run multiple tests in the test tool, connecting to the problem computer's IP address, NetBIOS name and (in the case of a domain computer) Fully Qualified Domain Name (FQDN).

   When running your tests, submit the same credential that was also submitted in Lansweeper for scanning.
6. When running tests to NetBIOS name or FQDN of the computer, make sure the DNS section of the tool shows the computer name being resolved to the correct IP address.   
   Based on which scanning method you are using to scan your computer, Lansweeper will try to connect to IP address, NetBIOS name or FQDN. It is important that connecting to either of those properties brings you to the correct client machine. If there is a DNS issue for instance and connecting to your computer's name returns an incorrect IP address as a result, this will lead to scanning issues. Discuss any DNS issues that may be visible in the test tool with your network admin, as they must be resolved in your network itself.
7. Look at the Scanning TCP Ports and Scanning WMI sections of the tool to determine whether necessary ports are open for scanning.   
   Lansweeper must have access to TCP port 135 (to set up the initial DCOM connection to the client machine) and the random ports that are used by Windows to send WMI data. Our knowledge base contains firewall configuration instructions for [Windows Firewall](/classic/docs/configure-windows-firewall-for-agentless-scanning-of-computers) and [Symantec Endpoint Protection](/classic/docs/configure-symantec-endpoint-protection-for-use-with-lansweeper). For other third-party firewalls, we recommend consulting the vendor's documentation.

   Opening port 135 is not sufficient to accomplish an agentless scan of a Windows computer. Lansweeper pulls Windows computer data from WMI (Windows Management Instrumentation), a management infrastructure built into Windows operating systems.   
   By default, Windows sends WMI data over random ports. You need to either:
   - Configure your firewalls in such a way that all WMI traffic (over random ports) is allowed. Windows Firewall includes an exception that you can enable to allow WMI traffic, as explained in [this knowledge base article](/classic/docs/configure-windows-firewall-for-agentless-scanning-of-computers). For third-party firewalls, you'll need to consult your firewall documentation.
   - [Configure a fixed WMI port](https://docs.microsoft.com/en-us/windows/win32/wmisdk/setting-up-a-fixed-port-for-wmi) and allow traffic through that port. Setting up a fixed port is supported by all recent Windows operating systems starting from Windows Vista.
   - If you are unable to allow WMI traffic through your firewalls, scan your computers locally with the [LsAgent](/classic/docs/introduction-to-lsagent-for-windows-linux-and-mac) or [LsPush](/classic/docs/introduction-to-the-lspush-scanning-agent-for-windows) scanning agent instead. This does not require firewall reconfiguration.
8. Make sure the RPC service is running on the computer you're trying to scan. By default in Windows, this service is configured to run automatically. It may have been manually stopped, however, resulting in "RPC server unavailable" errors.
9. Make sure the computer meets the other Windows [domain](/classic/docs/windows-domain-scanning-requirements) or [workgroup](/classic/docs/windows-workgroup-scanning-requirements) scanning requirements. You can download (right-click and Save Link As) and run [this script](https://www.lansweeper.com/files/lansweeper.vbs) within an elevated Command Prompt on a problem computer to ensure DCOM, Windows Firewall and some other settings are correct. If you are using third-party firewalls, you will still need to check their configuration separately.
10. Make sure the local time is correctly configured on the client computer, the Lansweeper scanning server and your domain controller. A time difference of more than 15 minutes between client and server can cause unexpected results in Active Directory domains.
