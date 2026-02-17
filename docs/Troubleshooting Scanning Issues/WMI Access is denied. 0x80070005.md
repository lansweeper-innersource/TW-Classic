<!-- # WMI Access is denied. 0x80070005 -->
This page is for Lansweeper Classic. For Lansweeper Cloud, see [WMI Access is denied. 0x80070005](/docs/wmi-access-is-denied-0x80070005).

[Lansweeper](https://www.lansweeper.com/) pulls Windows computer data from WMI (Windows Management Instrumentation), a management infrastructure built into Windows operating systems. When scanning Windows computers without a scanning agent, you may at some point encounter machines that return "access denied" scanning errors. These errors are usually caused by your scanning credential lacking administrative privileges on the client machine, but can be caused by incorrect DCOM or other settings as well.

To successfully perform an agentless scan with [RequireIntegrityActivationAuthenticationLevel](https://support.microsoft.com/en-us/topic/kb5004442-manage-changes-for-windows-dcom-server-security-feature-bypass-cve-2021-26414-f1400b52-c141-43d2-941e-37ed901c769c) set to 1, [KB5005033](https://support.microsoft.com/en-au/topic/august-10-2021-kb5005033-os-builds-19041-1165-19042-1165-and-19043-1165-b4c77d08-435a-4833-b9f7-e092372079a4) or newer must be installed.

## Troubleshoot the "access denied" error

1. Make sure the client machine is running a non-Home edition of Windows.  
   Older versions of Windows Home operating systems cannot be scanned remotely and will need to be scanned with LsAgent or LsPush. Non-Home editions of Windows can be scanned remotely without issue.  

   You can scan Windows computers locally with the [LsAgent](/docs/introduction-to-lsagent-for-windows-linux-and-mac) or [LsPush](/docs/introduction-to-the-lspush-scanning-agent-for-windows) scanning agents. Scanning with an agent returns the same data and is a guaranteed solution to any access denied errors.
2. Make sure the client machine's OS is fully patched, as older Windows builds had issues with remote WMI access.
3. Look at the **Last scan attempt**date in the computer's **Summary** tab in the Lansweeper Classic web console to determine when the scanning error occurred.  
   If the scanning error is not recent, rescan the computer first to verify whether the scanning issue is still present. To rescan the computer, go to **Assets**, select the computer and click **Rescan**.
4. Make sure the user account you submitted as a scanning credential in Lansweeper has administrative privileges on the client machine.
5. Make sure you have the correct password for the user account and that the password has not expired.  
   You can re-submit the user account's password in the Lansweeper Classic web console to ensure it's correct.
6. Make sure the client machine's firewall is configured to allow WMI traffic.   
   If the machine uses Windows Firewall, read through the configuration instructions found in [Configure Windows Firewall for agentless scanning of computers](/docs/configure-windows-firewall-for-agentless-scanning-of-computers).
7. Make sure the computer meets the other Windows [domain](/docs/windows-domain-scanning-requirements) or [workgroup](/docs/windows-workgroup-scanning-requirements) scanning requirements.  
   You can download (right-click and Save Link As) and run [this script](https://www.lansweeper.com/files/lansweeper.vbs) within an elevated Command Prompt on a problem computer to ensure DCOM, Windows Firewall, and some other settings are correct. If you are using third-party firewalls, you will still need to check their configuration separately.
8. Run the testconnection tool found at `Program Files (x86)\Lansweeper\Actions\testconnection.exe` on your Lansweeper scan server and submit the same scanning credentials used by Lansweeper.

   You must open the test tool on your Lansweeper scanning server, i.e. on the machine that has the Lansweeper Server service installed to replicate the exact network conditions experienced by Lansweeper.
9. In the test tool, verify that the computer name is resolving to the correct IP address and that the WMI part is green.   
   If the WMI part is green, Lansweeper should be able to scan the machine as well.

   
10. Make sure the local time is correctly configured on the client computer, the Lansweeper scanning server, and your domain controller.   
    A time difference of more than 15 minutes between the client and server can cause unexpected results in Active Directory domains.
11. Try removing the computer from your domain and re-adding it.
