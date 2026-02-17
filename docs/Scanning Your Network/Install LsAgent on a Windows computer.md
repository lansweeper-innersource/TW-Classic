<!-- # Install LsAgent on a Windows computer -->
[Lansweeper](https://www.lansweeper.com/) includes several agentless scanning methods to scan the assets in your network. You can scan the Linux, Unix, Mac, and Windows computers, VMware servers, and other devices in your network without installing any Lansweeper software on the machines you're scanning. Optionally, you can scan your computers with a scanning agent as well.

If you are using Lansweeper Sites, the IT Agent Discovery scanning agent might be the optimal choice over LsAgent. To determine if IT Agent Discovery aligns with your needs, explore the [Install IT Agent Discovery](/docs/install-it-agent-discovery) guide.

LsAgent is a cross-platform, lightweight program that you can install on Windows, Linux, and Mac computers, that automatically collects an inventory from the computer it's installed on.

LsAgent sends scanned data back to your Lansweeper installation, either directly or through our relay server in the cloud. Data is securely sent to the relay server over HTTPS, stored in an encrypted format, and deleted once a scanning server has retrieved it.

When an LsAgent scan is imported, an Active Directory (AD) lookup is performed. The credentials associated with the domain's NetBIOS name are used during this process.

Thanks to the relay server connectivity, LsAgent can even scan computers outside of your network and over the internet. If you want to try out LsAgent yourself, you can always [download LsAgent](https://www.lansweeper.com/download/lsagent/).

## Install LsAgent

To install LsAgent on a Windows computer and subsequently have LsAgent scan the machine:

1. Make sure the computer has .NET Framework 4.8 (or higher) is installed, as this is a requirement for running LsAgent.
2. If you will be scanning the Windows computer over the internet, make sure outbound traffic is allowed on your Lansweeper scanning server.   
   Specifically, the scanning server must be able to make an outbound connection to port 443 of lsagentrelay.lansweeper.com, our cloud relay server, to retrieve data scanned by LsAgent. The relay server is a server hosted in Azure (Microsoft cloud environment) by us, Lansweeper. If LsAgent cannot send data directly to a Lansweeper scanning server, it will send the data to the relay instead, where the scanning server can collect it.
3. If you will be scanning the Windows computer over the Internet, enable access to the Lansweeper relay server under **Scanning > Relay Configuration** in the Lansweeper web console. The relay access check may take a couple dozen seconds. If you have multiple scanning servers, you can configure which one collects relay data.

   The LsAgent relay configuration can only be switched on from the Lansweeper Classic web console. If you don't have access to the web console yet, see [enabling the Lansweeper Classic web console](/docs/enable-the-lansweeper-on-premises-web-console).

   ![procedure-requesting-relay-access.jpg](/docs/.document360/assets/article_199/image_002.jpg)
4. Copy the Cloud Relay Authentication Key seen on the page, as you will need to submit this in the LsAgent installer later.

   ![procedure-relay-access-granted.jpg](/docs/.document360/assets/article_199/image_003.jpg)
5. Grab the LsAgent installer for Windows from `Program Files (x86)\Lansweeper\Client` on your Lansweeper server or through [this download page](https://www.lansweeper.com/download/lsagent/).

   ![installing-lsagent-on-a-windows-computer-1.jpg](/docs/.document360/assets/article_199/image_004.jpg)
6. Run the LsAgent installer on your Windows client machine and select **Next**.

   ![installing-lsagent-on-a-windows-computer-2.jpg](/docs/.document360/assets/article_199/image_005.jpg)
7. Choose an installation directory and click **Next**.

   ![installing-lsagent-on-a-windows-computer-3.jpg](/docs/.document360/assets/article_199/image_006.jpg)
8. Submit one or both of the following:
   - Your scanning server name or IP and its listen port.   
     You can see your listen port (9524 by default) listed in the **Configuration > Server Options** section of the web console. If you fill in these fields, LsAgent will first try to send scanned data directly to the listen port of your scanning server.
   - The Cloud Relay Authentication Key.   
     If you fill in this field, LsAgent will send scanned data to the Lansweeper relay server, where your scanning server can collect it. If you submit both your scanning server and the relay authentication key, LsAgent will first try to send data directly to the scanning server and, if that fails, to the relay server. Data is securely sent to the relay server over HTTPS, stored in an encrypted format, and deleted once a scanning server has retrieved it.

     ![installing-lsagent-on-a-windows-computer-4.jpg](/docs/.document360/assets/article_199/image_007.jpg)
9. Click **Next** and **Finish** to complete the installation process. The client machine will automatically be scanned by LsAgent, by default once per day. Data will be sent to the scanning server and, if that fails, to the relay server where the scanning server can retrieve it.   
   You can find the client machine in the Lansweeper web console like any other Windows client machine by performing a search for the computer's name in the search bar. The machine's **Scan Time** tab will indicate that it was scanned with LsAgent.

   ![installing-lsagent-on-a-windows-computer-7.jpg](/docs/.document360/assets/article_199/image_008.jpg)
10. You can change the machine's scanning schedule in the **Scanning > LsAgent Scanning** section of the Lansweeper web console.   
    Here you can divide machines scanned with LsAgent into groups, configure a scanning schedule for each group and enable/disable/delete LsAgent installations. Keep in mind that the minimum scan interval for LsAgent is 1 hour. If you choose a more frequent schedule, your LsAgent installations will silently default to an interval of 1 hour. LsAgent uses the same schedules as deployment packages, so the link for creating a new schedule takes you to a deployment configuration page.

    ![installing-lsagent-on-a-windows-computer-8.jpg](/docs/.document360/assets/article_199/image_009.jpg)

    ![procedure-changing-lsagent-schedule.jpg](/docs/.document360/assets/article_199/image_010.jpg)
11. If you have multiple scanning servers, you can link additional servers to your LsAgent group on the same page. If an LsAgent installation then attempts to send scanned data to a scanning server and that server cannot be reached, another server is tried. If all linked scanning servers cannot be reached and if you submitted your relay key during LsAgent installation, scanned data is sent to the relay instead.

    ![procedure-linking-scanning-servers-to-lsagent-group.jpg](/docs/.document360/assets/article_199/image_011.jpg)
