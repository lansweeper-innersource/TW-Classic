<!-- # Integrate Lansweeper with SCCM -->
SCCM integration is a feature introduced in Lansweeper 7.2. You will need to [update your installation](http://lansweeper.com/knowledgebase/updating-your-installation/ "updating your installation") if you are running a lower Lansweeper version.

From version 7.2 onward, Lansweeper supports integration with System Center Configuration Manager (SCCM). Specifically, Lansweeper can scan machines that are visible in the **Assets & Compliance > Devices** section of your SCCM server and cross-reference them with Lansweeper assets. Scanned SCCM data includes device name, domain, IP address, manufacturer, model, operating system, processor, memory, resource ID, serial number, site, client details, network adapters, software and more.   
Lansweeper assets are also automatically created for any Windows, Linux and Mac computers that are found in SCCM and that were not previously found by Lansweeper.

To ensure a smooth Lansweeper integration with SCCM, follow the steps in this article.

### Step 1: make sure you meet the SCCM integration requirements

When Lansweeper scans an SCCM server, it does so without an agent and uses WMI (Windows Management Instrumentation) to retrieve assets from the SCCM database. To make this process work, you must:

- Provide Lansweeper with the name, IPv4 address or IPv6 address of an SMS Provider server in your SCCM environment.
- Ensure your SCCM server meets [the general Windows scanning requirements](/docs/windows-domain-scanning-requirements) for agentless scanning.
- Provide Lansweeper with a user account that has local administrative permissions on the SCCM server and, at a minimum, the Read-Only Analyst security role within SCCM's Administrative Users.

### Step 2: set up the SCCM integration

To set up an SCCM scan, click **Add Scanning Target** in the **Scanning > Scanning Targets** section of the web console. If you have multiple scanning servers, there will be a separate configuration tab for each server. ![menu-scanning-scanning-targets.jpg](/docs/.document360/assets/article_200/image_001.jpg)

In the resulting pop-up, choose SCCM as your scanning type. You will then be asked to submit:

- Name: a name for your scanning target. This is for personal reference only.
- Username: your user. You can use a down-level logon name like NetBIOS domain name\username (domain credentials), a user principal name (UPN) like username@yourdomain.local (domain credentials), .\username (local credentials) or username@outlook.com (Microsoft accounts).
- Password: the user's password.
- SCCM Server: an SMS Provider server in your SCCM environment. You can submit the server's name, IPv4 address or IPv6 address.
- Description: an optional description for your scanning target. This is for personal reference only.
- A scanning schedule.

![integrating-lansweeper-with-sccm-1.jpg](/docs/.document360/assets/article_200/image_002.jpg)

### Step 3: scan the SCCM target

Once you've configured your SCCM scanning target, you can start scanning it. You can either wait for your scanning schedule to trigger or manually initiate a scan with the **Scan now** button next to the scanning target. Keep in mind that SCCM scans do not visually show up in your scanning queue. They're processed silently in the background. ![integrating-lansweeper-with-sccm-2.jpg](/docs/.document360/assets/article_200/image_003.jpg)

### Step 4: view SCCM data

The integration with SCCM is now complete. SCCM data can be viewed in the **Config > SCCM** tab of your SCCM server and client machines. The **Summary** tab of a client machine detected through SCCM also indicates what the machine's SCCM server is. Scanned SCCM data can be viewed using built-in or custom reports or the built-in SCCM Coverage widget as well. Perform a search for "SCCM" in the **Reports** menu. ![integrating-lansweeper-with-sccm-3.jpg](/docs/.document360/assets/article_200/image_004.jpg)  
  
![integrating-lansweeper-with-sccm-4.jpg](/docs/.document360/assets/article_200/image_005.jpg)
