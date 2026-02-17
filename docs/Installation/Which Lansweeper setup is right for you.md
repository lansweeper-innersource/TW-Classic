<!-- # Which Lansweeper setup is right for you? -->
A Lansweeper installation consists of [several components](/docs/lansweeper-classic-components-and-architecture): database, web console, one or more scan servers. This article helps you select the correct database type, web server type and number of scan servers for your needs. It also includes diagrams of sample Lansweeper setups.

- [Installation recommendations](#heading1)
- [Example Lansweeper setups](#heading2)

## Installation recommendations

### How many installations

The below questions will help you decide how many independent Lansweeper installations to set up. An "installation" consists of a database, web console and at least one scan server. Note that the number of installations you set up may have an impact on how you license Lansweeper.

|  |  |
| --- | --- |
| **Do you have isolated DMZ or other networks that cannot be reached from a central network location?** | |
| No | Yes |
| **Recommendation**: one installation. | **Recommendation**: one installation per isolated network. If you have networks that cannot communicate directly, consider setting up an isolated Lansweeper installation per network. If the networks do have internet access, you can sync their data to [Lansweeper Cloud](https://www.lansweeper.com/resources/getting-started-with-cloud/) to manage it centrally there. |
| **Do you want some admins in your Lansweeper installation to only see a subset of scanned assets?** | |
| No | Yes |
| **Recommendation**: one installation. | **Recommendation**: one installation, linked with [Lansweeper Cloud](https://www.lansweeper.com/resources/getting-started-with-cloud/). In a local Lansweeper installation, website access cannot be restricted on an asset level. However, you can link the local installation with Cloud and restrict asset access there. Give your admins access only to Cloud, not to the local Lansweeper installation. Alternatively, if you want your admins to have local access to a subset of assets, consider setting up multiple Lansweeper installations. You can then choose to give each admin access to only the relevant installation. |

### How many scan servers

A Lansweeper installation has at least one scan server, but it can have multiple. A scan server scans your network and performs [several other functionalities](/docs/lansweeper-classic-components-and-architecture). The below questions help you decide how many scan servers to set up as part of your Lansweeper installation. If the answer to any of the below questions is "yes", consider adding more than one scan server to your installation.

|  |  |
| --- | --- |
| **Do you want to scan more than 1,000 network assets?** | |
| No | Yes |
| **Recommendation**: one scan server. | **Recommendation**: one scan server per 1,000-5,000 assets. The more assets you scan, the more scan server resources it takes to complete those scans. You can increase [your thread settings](/docs/view-and-clear-your-scanning-queue) to make a scan server process more scan requests at a time. However, at some point it becomes advisable to add more servers to handle the scanning load. |
| **Do you want to scan assets in multiple subnets, across multiple LANs?** | |
| No | Yes |
| **Recommendation**: one scan server. | **Recommendation**: one scan server per subnet. By adding a scan server to each subnet you intend to scan, you improve the accuracy with which asset data can be detected. A local scan server is better at detecting your assets' MAC addresses for instance. |
| **Do you want to scan assets in networks that have a VPN connection to your main network?** | |
| No | Yes |
| **Recommendation**: one scan server. | **Recommendation**: one scan server per VPN-connected site. By adding a scan server to each VPN-connected site, you improve the accuracy with which asset data like MAC addresses can be detected. Having local scan servers also ensures most of the scanning traffic is contained within each site, instead of all traffic being sent over VPN. |

### Which database server type

A Lansweeper installation can have either a SQL LocalDB or Microsoft SQL Server database. The below questions help you decide which database server type to choose. If the answer to any of the below questions is "yes", consider using a Microsoft SQL Server database.

|  |  |
| --- | --- |
| **Do you already have a Microsoft SQL Server 2014 or higher instance running in your network?** | |
| No | Yes |
| **Recommendation**: SQL LocalDB. | **Recommendation**: if you are centrally managing your databases in this Microsoft SQL Server instance anyway, consider installing the Lansweeper database here as well. Keep in mind that your SQL Server instance must be [properly configured](/docs/configuring-a-sql-server-instance-to-host-the-lansweeper-database) to allow for the installation of the Lansweeper database. |
| **Do you want to scan more than 10,000 assets?** | |
| No | Yes |
| **Recommendation**: SQL LocalDB. | **Recommendation**: a non-Express edition of Microsoft SQL Server. As a rule of thumb, we recommend reserving 1 MB of database space per scanned asset. Both SQL LocalDB and Express editions of SQL Server are limited by Microsoft to 10 GB of data, so you may run into the size limit when attempting to store 10,000 assets in such a database. For such a large number of assets, use a non-Express edition of SQL Server. |
| **Do you want to set up multiple Lansweeper scan servers?** | |
| No | Yes |
| **Recommendation**: SQL LocalDB. | **Required**: Microsoft SQL Server. SQL LocalDB databases cannot be connected to by remote components. As a result, SQL LocalDB databases cannot be used for setups with multiple scan servers. Use SQL Server for these types of setups instead. |

### Which web server type

A Lansweeper web console can be hosted in either IIS Express or IIS. The below questions help you decide which web server type to choose. If the answer to any of the below questions is "yes", consider using IIS as your web server.

|  |  |
| --- | --- |
| **Do you already have an IIS web server running in your network?** | |
| No | Yes |
| **Recommendation**: IIS Express. | **Recommendation**: if you are centrally managing your websites in this IIS web server anyway, consider installing the Lansweeper web console here as well. |
| **Do you want to manage web console ports and other technical properties through a visual tool?** | |
| No | Yes |
| **Recommendation**: IIS Express. | **Recommendation**: IIS. The built-in IIS Express web server does not come with a visual management tool. For full control of web console properties, use IIS. If you don't already have an IIS web server, you can [set one up](/docs/install-iis-internet-information-services). |

## Example Lansweeper setups

### Basic network with a single subnet

![lansweeper-installation-single-subnet-1.png](/docs/.document360/assets/article_086/image_001.jpg)

### Larger network with multiple subnets

![lansweeper-installation-multiple-subnets.png](/docs/.document360/assets/article_086/image_002.jpg)

### Multiple isolated networks with one or more subnets

![lansweeper-installation-multiple-isolated-networks-1.png](/docs/.document360/assets/article_086/image_003.jpg)
