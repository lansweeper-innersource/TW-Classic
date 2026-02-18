<!-- # Install LsAgent on a Mac computer -->
[Lansweeper](https://www.lansweeper.com/) includes several agentless scanning methods to scan the assets in your network. You can scan the Linux, Unix, Mac and Windows computers, VMware servers and other devices in your network without installing any Lansweeper software on the machines you're scanning.

Optionally, you can scan your computers with a scanning agent instead. LsAgent is a cross-platform, lightweight program that you can install on Windows, Linux and Mac computers and that automatically collects an inventory from the computer it's installed on. LsAgent sends scanned data back to your Lansweeper installation, either directly or through our relay server in the cloud. Data is securely sent to the relay server over HTTPS, stored in an encrypted format and deleted once a scanning server has retrieved it.

If you are using a Lansweeper Site, the IT Agent Discovery scanning agent might be the optimal choice over LsAgent. To determine if IT Agent Discovery aligns with your needs, explore the [Install IT Agent Discovery](/classic/docs/install-it-agent-discovery) guide.

Thanks to the relay server connectivity, LsAgent can even scan computers outside of your network and over the internet.

## Install LsAgent on macOS

1. Make sure your OS is supported [as described in this article](/classic/docs/lsagent-installation-requirements#heading3 "LsAgent installation requirements").
2. If you are scanning the Mac computer over the internet, ensure outbound traffic is allowed on your Lansweeper scanning server.   
   Specifically, the scanning server must be able to make an outbound connection to port 443 of lsagentrelay.lansweeper.com, our cloud relay server, to retrieve data scanned by LsAgent. The relay server is hosted in Azure (Microsoft cloud environment) by us. If LsAgent cannot send data directly to a Lansweeper scanning server, it will send the data to the relay instead, where the scanning server can collect it.
3. If you will be scanning the Mac computer over the internet, enable access to the Lansweeper relay server under **Scanning > Relay Configuration** in the Lansweeper web console. The relay access check may take a minute to complete. If you have multiple scanning servers, you can configure which one collects relay data.

   The LsAgent relay configuration can only be switched on from the Lansweeper Classic web console. If you don't have access to the web console yet, see [enabling the Lansweeper Classic web console](/classic/docs/enable-the-lansweeper-on-premises-web-console).

   
4. Copy the Cloud Relay Authentication Key seen on the page, as you will need to submit this in the LsAgent installer later.  
   
5. Download the LsAgent installer for Mac on [this download page](https://www.lansweeper.com/download/lsagent/).
6. Run the LsAgent installer on your Mac client machine, double-click LsAgent-osx in the resulting pop-up and choose **Next**. Should the software be blocked, click the Apple icon in the upper left corner of your screen, choose **System Preferences** followed by **Security & Privacy**. There should be an option to unblock the software in this menu.  
   
7. Accept the Terms of Use and select **Next**.
8. Choose an installation directory and click **Next**.  
   
9. Submit one or both of the following:
   - Your scanning server name or IP and its listen port.   
     You can see your listen port (9524 by default) listed in the **Configuration > Server Options** section of the web console. If you fill in these fields, LsAgent will first try to send scanned data directly to the listen port of your scanning server.
   - The Cloud Relay Authentication Key you copied earlier.   
     If you fill in this field, LsAgent will send scanned data to the Lansweeper relay server, where your scanning server can collect it. If you submit both your scanning server and relay authentication key, LsAgent will first try to send data directly to the scanning server and, if that fails, to the relay server. Data is securely sent to the relay server over HTTPS, stored in an encrypted format and deleted once a scanning server has retrieved it.
10. Choose **Next** and **Finish** when the installation process has completed.

LsAgent has now been installed on your macOS computer.

## Scan macOS using LsAgent

The client machine will automatically be scanned by LsAgent, by default, once per day. Data will be sent to the scanning server and, if that fails, to the relay server, where the scanning server can retrieve it. You can find the client machine in the Lansweeper web console like any other Mac client machine by performing a search for the computer's name in the search bar.  


### Scan schedule

You can choose to change the machine's scanning schedule in the **Scanning > LsAgent Scanning** section of the Lansweeper web console.   
Here you can divide machines scanned with LsAgent into groups, configure a scanning schedule for each group and enable/disable/delete LsAgent installations. Keep in mind that the minimum scan interval for LsAgent is 1 hour. If you choose a more frequent schedule, your LsAgent installations will silently default to an interval of 1 hour. LsAgent uses the same schedules as deployment packages, so the link for creating a new schedule takes you to a deployment configuration page.  


### Link scanning servers

If you have multiple scanning servers, you can link additional servers to your LsAgent group on the same page.   
If an LsAgent installation then attempts to send scanned data to a scanning server and that server cannot be reached, another server is tried. If all linked scanning servers cannot be reached and if you submitted your relay key during LsAgent installation, scanned data is sent to the relay instead.  

