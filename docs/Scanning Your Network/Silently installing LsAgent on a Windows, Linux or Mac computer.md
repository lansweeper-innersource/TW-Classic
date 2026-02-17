<!-- # Silently installing LsAgent on a Windows, Linux or Mac computer -->
[Lansweeper](https://www.lansweeper.com/) includes several agentless scanning methods to scan the assets in your network. You can scan the Linux, Unix, Mac and Windows computers, VMware servers and other devices in your network without installing any Lansweeper software on the machines you're scanning.

Optionally, you can scan your computers with a scanning agent instead. LsAgent is a scanning agent introduced in Lansweeper 7.0. It is a cross-platform, lightweight program that you can install on Windows, Linux and Mac computers and that automatically collects an inventory from the computer it's installed on. LsAgent sends scanned data back to your Lansweeper installation, either directly or through our relay server in the cloud. Data is securely sent to the relay server over HTTPS, stored in an encrypted format and deleted once a scanning server has retrieved it.

If you are using a Lansweeper Site, the IT Agent Discovery scanning agent might be the optimal choice over LsAgent. To determine if IT Agent Discovery aligns with your needs, explore the [Install IT Agent Discovery](/docs/install-it-agent-discovery) guide.

Thanks to the relay server connectivity, LsAgent can even scan computers outside of your network and over the internet. LsAgent can be visibly or silently installed on Windows, Linux and Mac computers. When LsAgent's been installed on a computer, it automatically starts scanning the machine once per day. Scanning schedules can be customized further through the Lansweeper web console.

Available parameters for silent LsAgent installation are mentioned further in this article, along with some sample commands. Once you've put together your silent install command, you can add it to scripts, policies, jobs or (in the case of Windows computers) Lansweeper deployment packages.

As of Lansweeper version 8.4.100, Windows clients must have .NET 4.8 (or higher) installed in order to be scanned by LsAgent. If the LsAgent installer detects a lower version is installed, it will automatically try to update the client's .NET framework to the required .NET 4.8 version, using a downloaded (on demand) Microsoft .NET installer. After this update, the device may require a reboot. Whether a reboot is required or not is detected by the Microsoft .NET installer and depends on whether or not .NET dependency files were in use at the moment of update or not. The installation does not trigger a reboot.

## LsAgent installers

There is a separate LsAgent installer for Windows, Linux and Mac.

- Windows: available on [this download page](https://www.lansweeper.com/download/lsagent/) or from the following folder on your Lansweeper server: `Program Files (x86)\Lansweeper\Client`.
- Linux: available on [this download page](https://www.lansweeper.com/download/lsagent/). A legacy installer version 9.5.0.2 is also available on this page for legacy operating systems that do not support .NET 6.0.
- Mac: available on [this download page](https://www.lansweeper.com/download/lsagent/). A legacy installer version 9.5.0.2 is also available on this page for legacy operating systems that do not support .NET 6.0.

## LsAgent silent install parameters

LsAgent accepts the following parameters:

- `--server <name or IP address of your Lansweeper scanning server>`   
  If you want LsAgent to send scanned data directly to your Lansweeper installation, you must include the NetBIOS name, FQDN or IP address of your Lansweeper scanning server in your LsAgent install command.
- `--port <scanning server listen port>`   
  If you want LsAgent to send scanned data directly to your Lansweeper installation, you must also include your scanning server's listen port in your LsAgent install command. You can see your listen port (9524 by default) listed in the **Configuration > Server Options** section of the Lansweeper web console.
- `--agentkey <cloud relay authentication key>`   
  If you want LsAgent to send scanned data to our relay server in the cloud, where your Lansweeper scanning server can retrieve it, you must include your relay authentication key in your LsAgent install command. Your relay authentication key is the key you can see in the **Scanning > Relay Configuration** section of the Lansweeper Classic web console after enabling relay access on the same page. If you include both your scanning server and relay authentication key in your LsAgent install command, LsAgent will first try to send data directly to the scanning server. If that fails, LsAgent will send data to our cloud relay server instead, where your scanning server can collect it. To access the relay server, your scanning server must be able to make an outbound connection to port 443 of lsagentrelay.lansweeper.com.  

  The LsAgent relay configuration can only be switched on from the Lansweeper Classic web console. If you don't have access to the web console yet, see [enabling the Lansweeper Classic web console](/docs/enable-the-lansweeper-on-premises-web-console).
- `--prefix <installation folder>`   
  You can include the LsAgent install directory in your command. If this parameter is omitted, the default install directory is used.
- `--mode unattended`   
  A required parameter to force the LsAgent installation to be performed silently.

## LsAgent silent install sample commands

Below are just a few sample commands illustrating the silent install procedure for LsAgent.

- In the sample command below, we're silently installing LsAgent on a **Windows** computer and having it send scanned data directly to our scanning server LAN-001 with port 9524. We also included our relay authentication key in our command so that scanned data is sent to the relay server in case the scanning server cannot be reached directly. The scanning server will then retrieve the scanned data from the relay server.  

  ```
  LsAgent-windows.exe --server LAN-001 --port 9524 --agentkey 4c2db649-014a-41f5-a01d-08950d7af --mode unattended
  ```
- In the sample command below, we're silently installing LsAgent on a **Linux** computer and opting to only have it send scanned data to the relay server, where the scanning server can retrieve it.  

  ```
  LsAgent-linux-x64.run --agentkey 4c2db649-014a-41f5-a01d-08950d7af --mode unattended
  ```
- In the sample command below, we're silently installing LsAgent on a **Mac** computer and opting to only have it send scanned data to the relay server, where the scanning server can retrieve it. LsAgent-osx.app can be found within the mounted .dmg file.  

  ```
  LsAgent-osx.app/Contents/MacOS/installbuilder.sh --agentkey 4c2db649-014a-41f5-a01d-08950d7af --mode unattended
  ```
