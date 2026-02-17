<!-- # LsAgent installation requirements -->
Lansweeper includes several agentless scanning methods to scan the assets in your network. You can scan Linux, Unix, Mac and Windows computers, VMware servers, and other devices in your network without installing any Lansweeper software on the machines you're scanning. Nevertheless, you can scan your computers with a scanning agent as well. This article explains what the installation requirements are for the LsAgent scanning agent.

LsAgent is a cross-platform, lightweight program that you can install on Windows, Linux and Mac computers, which automatically collects an inventory from the computer it's installed on. LsAgent sends scanned data back to your Lansweeper installation, either directly or through our relay server in the cloud.   
Data is securely sent to the relay server over HTTPS, stored in an encrypted format and deleted once a scanning server has retrieved it. Thanks to the relay server connectivity, LsAgent can even scan computers outside your network and over the Internet.

LsAgent can be successfully installed and run on machines that meet the below requirements. [The LsAgent installers](https://www.lansweeper.com/download/lsagent/) can be downloaded through our website.

## LsAgent requirements for Windows

Windows client machines must have .NET Framework 4.8 (or higher) installed in order to run and be scanned by LsAgent. The following operating systems support .NET Framework 4.8 and can be scanned by LsAgent if .NET 4.8 (or higher) is installed:

- Windows 7, SP1 (32-bit and 64-bit)
- Windows 8.1 (32-bit and 64-bit)
- Windows 10 1607 or higher (32-bit and 64-bit)
- Windows 11 (64-bit)
- Windows Server 2008 R2, SP1 (64-bit)
- Windows Server 2012 (64-bit)
- Windows Server 2012 R2 (64-bit)
- Windows Server 2016 (64-bit)
- Windows Server 2019 (64-bit)
- Windows Server 2022 (64-bit)

The LsAgent installer will automatically attempt to update .NET to 4.8 if necessary. To do so, it connects to microsoft.com and runs the Microsoft .NET installer. A reboot may be required afterward.

## LsAgent requirements for Linux

Starting from version 10.2, LsAgent for Linux comes packaged with .NET 6.0, which is required to run successfully. The following Linux operating systems support .NET 6.0 and meet the LsAgent installation requirements:

- Alpine Linux, version 3.13 or higher (64-bit)
- CentOS, version 7 or higher (64-bit)
- Debian, version 10 or higher (64-bit)
- Fedora, version 33 or higher (64-bit)
- Linux Mint, version 17 or higher (64-bit)
- openSUSE, version 15 or higher (64-bit)
- Oracle Linux, version 7 or higher (64-bit)
- Red Hat Enterprise Linux, version 8 or higher (64-bit)
- SUSE Linux Enterprise Server (SLES), version 12 SP2 or higher (64-bit)
- Ubuntu, version 16.04, 18.04 and 20.04 or higher (LTS) or higher (64-bit)

For operating systems that do not support .NET 6.0, a legacy version of LsAgent for Linux, version 9.5.0.2, remains on our [download page](https://www.lansweeper.com/download/lsagent/). This version of LsAgent for Linux requires that the operating system supports .NET Core 3.1.

Only use LsAgent version 9.5.0.2 for legacy Linux operating systems that do not support .NET 6.0. The latest fixes and improvements are not included in this version.

## LsAgent requirements for Mac

Starting from version 10.2.0.0, LsAgent for Mac comes packaged with .NET 6.0, which is required to run successfully. The following Mac operating systems support .NET 6.0 and meet the LsAgent installation requirements:

- macOS 10.15 or higher (64-bit)

For operating systems that do not support .NET 6.0, a legacy version of LsAgent for Mac, version 9.5.0.2, remains on our [download page](https://www.lansweeper.com/download/lsagent/). This version of LsAgent for Mac requires that the operating system supports .NET Core 3.1.

Only use LsAgent version 9.5.0.2 for legacy Mac operating systems that do not support .NET 6.0. The latest fixes and improvements are not included in this version.
