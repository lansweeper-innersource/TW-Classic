<!-- # Lansweeper installation requirements -->
Please note that a number of SQL and OS versions will no longer be supported as from March 1, 2023. For more information regarding the retiring versions, refer to the [Lansweeper Installation Requirements Update](https://www.lansweeper.com/updates/lansweeper-installation-requirements-update/).

The [Lansweeper](https://www.lansweeper.com/ "Lansweeper") software is agent-less. You only need to install Lansweeper on one computer, which scans your entire network. No additional software is needed on the client machines you're scanning. Though two scanning agents are included in the software, these are optional. Information on the LsPush and LsAgent scanning agents can be found in [this knowledge base article](/classic/docs/lspush-vs-lsagent-scanning-agent).

Lansweeper scans Linux, Unix, Mac and Windows computers, VMware servers and other network devices, but must be installed on a Windows computer. Lansweeper installation requirements can be found below.

## Architecture

64-bit, x64 architecture  
If your Lansweeper installation is running on a 32-bit server, you can [move your installation to a different server](/classic/docs/move-your-lansweeper-installation-to-a-different-server).

## Virtual or physical

You can install the Lansweeper software on either a virtual or physical computer.

## Operating system

You can install the Lansweeper software on non-Home, non-Core and non-Starter editions of any of the operating systems listed below. A Windows Server OS is recommended for networks of more than 1,000 assets, though not strictly required.

- Windows 10 21H2 (LTSC) or higher, with the exception of:  
  - Windows 10 1809 (LTSC)
  - Windows 10 1607 (LTSB)
  - Windows 10 1507 (RTM) (LTSB)
- Windows 11
- Windows Server 2016 (End of mainstream support; extended support available until January 12, 2027)
- Windows Server 2019 (End of mainstream support; extended support available until January 9th, 2029)
- Windows Server 2022
- Windows Server 2025

## Disk space

Lansweeper data, reports and settings are stored in a database. Your database is hosted in either the Microsoft SQL LocalDB, Microsoft SQL Server or (deprecated) Microsoft SQL Compact database server.   
The size of your database can vary greatly depending on how much data you're scanning and how much history you're keeping. However, as a general rule, we recommend reserving 1 GB of disk space per 1000 Windows computers. Non-Windows machines have less of an impact on database size.

## Database server

The database servers below are supported for hosting the Lansweeper database. Only SQL Server versions installed on a Microsoft Windows operating system are supported.

- Microsoft SQL LocalDB
- Microsoft SQL Server 2016, any edition (Express, Standard, Enterprise...) including Cumulative Update 11 or higher
- Microsoft SQL Server 2017, any edition (Express, Standard, Enterprise...) including Cumulative Update 18 or higher
- Microsoft SQL Server 2019, any edition (Express, Standard, Enterprise...) including Cumulative Update 2 or higher
- Microsoft SQL Server 2022, any edition (Express, Standard, Enterprise...)
- Microsoft SQL Server 2025, any edition (Express, Standard, Enterprise...)

For more information on supported database servers, check out [Compatible SQL servers to host the Lansweeper database](/classic/docs/compatible-sql-database-servers-for-hosting-the-lansweeper-database).

Microsoft SQL Server 2014 is only supported for Lansweeper versions 11.2.2.0 or earlier.

## Web browser

Lansweeper has a web interface, which can be viewed in a web browser locally from the Lansweeper server or remotely from other machines. Below is a list of officially supported browsers for interface viewing. Browsers not listed below may work as well, especially if they're Chromium-based. Unsupported browsers have not been tested for possible layout issues and may not be able to run asset or user actions.

The minimum supported screen resolution for viewing the Lansweeper interface is 1280 x 720 pixels. This applies to all supported web browsers.

- Google Chrome, updated to the latest version
- Mozilla Firefox, updated to the latest version
- Opera, updated to the latest version
- Microsoft Edge, updated to the latest (Chromium-based) version

## Other installed software

- The computer you install Lansweeper on must have .NET Framework 4.8 or a more recent .NET version installed, updated to the latest service pack.
- The computer you install Lansweeper on must have Windows Installer 2.0.
- If you are running an old Lansweeper version and chose SQL Compact as your database server, Visual C++ 2012 is required on your Lansweeper server as well. SQL Compact is no longer supported or offered as a database server option for Lansweeper. If you are still using SQL Compact as your Lansweeper database server, you should [convert your database to SQL LocalDB or SQL Server.](/classic/docs/convert-a-deprecated-sql-compact-database)

  If you do not already have .NET Framework 4.8, the Lansweeper installer will automatically try to download and install this for you. If your machine does not have Internet access, you may have to download and install this component manually in order to meet the Lansweeper installation requirements. When .NET Framework 4.8 is manually or automatically installed, a reboot of your Lansweeper server may be required.

| Database server | Packaged with Lansweeper | Max database size | Support for distributed Lansweeper components | Support for multiple scanning servers | Lansweeper support status |
| --- | --- | --- | --- | --- | --- |
| SQL Compact | ✔ | 4 GB | ✘ | ✘ | unsupported from March 2020 onward |
| SQL LocalDB | ✔ | 10 GB | ✘ | ✘ | supported database server |
| SQL Server | ✘ (manual install required prior to installing Lansweeper) | - 10 GB (free Express edition 2014 or higher) - unlimited (other editions) | ✔ | ✔ | supported database server |

Azure SQL Managed Instance is currently not supported by Lansweeper as a database provider.
