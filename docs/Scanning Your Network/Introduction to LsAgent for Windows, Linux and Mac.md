<!-- # Introduction to LsAgent for Windows, Linux and Mac -->

[Lansweeper](https://www.lansweeper.com/ "Lansweeper") includes several scanning methods to scan the assets in your network. You can scan the Linux, Unix, Mac and Windows computers, VMware servers and other devices in your network without installing any Lansweeper software on the machines you're scanning.

If you are using a Lansweeper Site, the IT Agent Discovery scanning agent might be the optimal choice over LsAgent. To determine if IT Agent Discovery aligns with your needs, explore the [Install IT Agent Discovery](/docs/install-it-agent-discovery) guide.

Optionally, an agent called LsAgent can be installed on Windows, Linux and Mac computers to scan the machines locally instead. LsAgent is a cross-platform scanning agent that can scan computers both inside and outside of your network.   
The video and article below provide an introduction to LsAgent and explain what LsAgent is, how it works and why it's so powerful.

## What LsAgent is

In short, LsAgent is:

- A cross-platform, lightweight program that you can install on Windows, Linux and Mac computers.
- A program that automatically collects an inventory from the computer it's installed on and sends the data back to your Lansweeper installation, either directly or through our relay server in the cloud. Data is securely sent to the relay server over HTTPS (TLS 1.2), stored in an encrypted format and deleted once a scanning server has retrieved it.
- A program that can scan computers outside of your network and over the internet thanks to the relay server connectivity.
- A configurable agent whose scanning schedule can be adjusted through the Lansweeper web console.

## Where to find LsAgent

There is a separate LsAgent installer for Windows, Linux and Mac.

- Windows: available on [this download page](https://www.lansweeper.com/download/lsagent/) or from the following folder on your Lansweeper server: `Program Files (x86)\Lansweeper\Client`.
- Linux: available on [this download page](https://www.lansweeper.com/download/lsagent/). A legacy installer version 9.5.0.2 is also available on this page for legacy operating systems that do not support .NET 6.0.
- Mac: available on [this download page](https://www.lansweeper.com/download/lsagent/). A legacy installer version 9.5.0.2 is also available on this page for legacy operating systems that do not support .NET 6.0.

## How to scan computers with LsAgent

Installing LsAgent on computers to be scanned is quick and easy. Once the installation is completed, LsAgent automatically starts scanning the machine once per day. The scanning schedule can be customized further through the Lansweeper web console, where scanned data is also displayed.

When an LsAgent scan is imported, an Active Directory (AD) lookup is performed. The credentials associated with the domain's NetBIOS name are used during this process.

The following list shows where to find installation guides for Windows, Linux and Mac:

- Windows: the installation guide can be found in [this knowledge base article](/docs/install-lsagent-on-a-windows-computer).
- Linux: the installation guide can be found in [this knowledge base article](/docs/install-lsagent-on-a-linux-computer).
- Mac: the installation guide can be found in [this knowledge base article](/docs/install-lsagent-on-a-mac-computer).
- A guide for silently installing LsAgent on Windows, Linux or Mac can be found in [this knowledge base article](/docs/silently-installing-lsagent-on-a-windows-linux-or-mac-computer).

## Why use LsAgent for scanning

LsAgent largely scans the same data as agentless scanning methods. However, because it scans locally and can access our cloud relay server, LsAgent has several advantages over agentless scanning.

- LsAgent can scan computers of your remote employees over the internet, wherever they are.
- LsAgent does not require you to submit scanning credentials in Lansweeper.
- LsAgent does not require administrative privileges to be able to scan.
- LsAgent does not require you to reconfigure your computers' firewalls for scanning. It does require an outbound connection to your Lansweeper installation or our relay server, but outbound traffic is not usually blocked by firewalls. Windows Firewall for instance allows outbound traffic by default.
- LsAgent is immune to almost all scanning errors, including access denied and firewall errors.

## How data scanned by LsAgent reaches your Lansweeper installation

Data scanned by LsAgent can reach your Lansweeper installation in one of two ways:

- **Direct server connection**  
  If the computers you're scanning are in the same network as your Lansweeper installation or have a connection to the installation through a VPN, scanned LsAgent data can be sent directly to your Lansweeper scanning server. For this, you must submit your scanning server name and listen port during LsAgent installation.
- **Relay server connection**If the computers you're scanning do not have a direct connection to your Lansweeper installation, scanned LsAgent data can be sent to our relay server in the cloud. For this, you must enable relay access in your Lansweeper installation.   
  Scanned LsAgent data is sent securely over HTTPS (TLS 1.2) to the relay server in Microsoft Azure, where it is encrypted as well. Your Lansweeper scanning server can retrieve the scanned data from the relay server, after which it is deleted from the relay. In order to use the relay server, make sure outbound traffic is allowed on your Lansweeper scanning server. Specifically, the scanning server must be able to make an outbound connection to port 443 of lsagentrelay.lansweeper.com, the cloud relay server.

## How scanned LsAgent data is sent to the relay server and processed

LsAgent can scan machines over the internet by sending scanned data to the relay server, where it is retrieved by your Lansweeper installation's scanning server.

- Use of the relay server must explicitly be enabled in the Lansweeper web console. It is not enabled by default.
- The relay server is hosted on a Microsoft Azure machine located in the U.S.
- Data is securely sent by LsAgent to the relay server using HTTPS and TLS 1.2.
- Data is stored in an encrypted format on the relay server. AES encryption is used, with a block size of 128 and a key size of 256.
- Your scanning server checks for new data on the relay server every 1 hour. A connection is made to port 443 of lsagentrelay.lansweeper.com.
- Your scanning server can only access new data on the relay server that is specific to your company. A unique key is used to identify your company on the relay server.
- Once a scanning server has retrieved new data from the relay server, that data is deleted from the relay.

In a [Cloud-first scenario](/docs/install-lansweeper-sites), the LsAgent relay configuration can only be switched on after [enabling the Lansweeper On-prem web console](/docs/enable-the-lansweeper-on-premises-web-console).  
If you have multiple installations that are linked to the same cloud site, each installation will share the same license key, issued from cloud. The relay server also uniquely identifies installations by their license key. As a result, you can only enable the relay on one installation in this scenario.
