<!-- # Scan SCCM targets -->
[Lansweeper](https://www.lansweeper.com/) integrates with System Center Configuration Manager (SCCM). Lansweeper can scan machines that are visible in the **Assets & Compliance > Devices** section of your SCCM server and cross-reference them with Lansweeper assets. Scanned SCCM data includes device name, domain, IP address, manufacturer, model, operating system, processor, memory, resource ID, serial number, site, client details, network adapters, software and more.

Lansweeper assets are also automatically created for any Windows, Linux and Mac computers that are found in SCCM and that were not previously found by Lansweeper.

### Prerequisites

When Lansweeper scans an SCCM server, it does so without an agent and uses WMI (Windows Management Instrumentation) to retrieve assets from the SCCM database. To make this process work, you must:

- Provide Lansweeper with the name, IPv4 address or IPv6 address of an SMS Provider server in your SCCM environment.
- Ensure your SCCM server meets [the general Windows scanning requirements](/docs/windows-domain-scanning-requirements) for agentless scanning.
- Provide Lansweeper with a user account that has local administrative permissions on the SCCM server and at least the Read-Only Analyst security role within SCCM's Administrative Users.

### Add a SCCM scan target

1. In your Lansweeper Cloud environment, navigate to **Scanning > Targets**.
2. Select **Add scanning target**.   
   
3. In the pop-up, choose a scan server and select the **SCCM** scanning target.
4. Enter the target credentials:
   - Name: a name for your scanning target. This is for personal reference only.
   - Username: your user. You can use a down-level logon name like NetBIOS domain name\username (domain credentials), a user principal name (UPN) like username@yourdomain.local (domain credentials), .\username (local credentials) or username@outlook.com (Microsoft accounts).
   - Password: the user's password.
   - SCCM Server: an SMS Provider server in your SCCM environment. You can submit the server's name, IPv4 address or IPv6 address.
   - Description: an optional description for your scanning target. This is for personal reference only.  
     
5. Select a scanning schedule for the SCCM target.
6. Select **Save and exit**, or **Save target**.
7. In the pop-up, choose whether you want to scan the SCCM target immediately.  
   

SCCM scans do not visually show up in your scanning queue. They're processed silently in the background.
