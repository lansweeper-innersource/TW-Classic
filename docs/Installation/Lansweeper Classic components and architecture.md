<!-- # Lansweeper Classic components and architecture -->
Lansweeper allows you to scan networks ranging from just a few to hundreds of thousands of assets. In this article, and in the video below, we illustrate the internal structure of the Lansweeper software, discuss the roles of the separate components and how they form a scalable, flexible network management solution.

A Lansweeper Classic installation consists of 3 components. A default setup contains one database, one web console and one scanning service, all located on the same machine. Depending on the size and complexity of your network you can choose to spread out your components and/or add additional scanning services across several machines.

This article explains the layout and function of both a default Lansweeper Classic setup and an advanced, custom setup.

## Default setup

When you perform an Easy Install of Lansweeper Classic, all components are installed on one machine, interacting as shown in the below diagram:



- **Database:**The database stores asset data that has been scanned or manually submitted as well as your scanning targets and encrypted credentials, reports, settings and helpdesk data. When performing an Easy Install, a Microsoft SQL LocalDB database is included. SQL LocalDB databases have a maximum capacity of 10 GB, a limit set by Microsoft.
- **Web Console:**The web console displays scanned and custom data, helpdesk data, reports and settings in a comprehensible way and allows you to make changes to them. By default, any user in your network can [access the console](/classic/docs/access-the-web-console) if they know the URL, but [access can also be restricted](/classic/docs/restrict-access-to-the-web-console).   
  During the Easy Install, the web console is installed under IIS Express. You can see your web server listed as a service in Windows Services. Starting/stopping the service will enable/disable access to the web console.

  
- **Scanning Service:**The scanning service performs the agentless scanning of all assets in your network, gathers the data and sends it back to the database. It also handles deployments for Windows computers. In order to send and receive emails and to retrieve asset warranty data for supported manufacturers, the scanning service requires access to the internet.   
  The scanning service is also responsible for handling database cleanup actions. You can see the scanning service listed as Lansweeper Server in Windows Services. Starting/stopping the service will enable/disable scanning, deployments, warranty scanning and all email handling.

  

## Advanced setup

By performing an Advanced Install of Lansweeper Classic you can manually select the components you wish to install. This allows you to spread out the components over several machines or install additional scanning services.   
We recommend using multiple of these so-called "scanning servers" if you have several thousand assets or remote sites connected through VPN or WAN. Using multiple scanning servers allows for more efficient load balancing as the scanning load, deployment requests and network traffic are divided among multiple machines.

The below diagram shows how multiple scanning servers work together to scan your network. Each scanning server can be configured to scan separate subnets, domains and more. Regardless of the number of scanning servers, all data is collected in one central database.



- **Database:**As SQL LocalDB does not allow for remote connections, it cannot be used to host an installation with components spread out across several machines. Also, as your network grows you may want to increase your database capacity and performance.   
  When performing an Advanced Install, you can choose to install the database under Microsoft SQL LocalDB or Microsoft SQL Server, which has several advantages over installing under SQL LocalDB. [This knowledge base article](/classic/docs/compatible-sql-database-servers-for-hosting-the-lansweeper-database) explains the differences between the database server options.
- **Web Console:**The web console displays asset information and configurations for your entire network, regardless of which scanning server collected the information. Scanning targets can be configured separately for all scanning servers through the web console. The advanced install allows you to install the web console under IIS Express or IIS (World Wide Web Publishing). You could, for example, host the web console on a remote server hosting IIS, along with other web applications.
- **Scanning Service:**Multiple scanning servers will work together to scan each part of your network. Each scanning server contacts the database to retrieve its scanning targets and credentials. The data they retrieve is collected and sent back to the database. Helpdesk emails will be handled by a dedicated scanning server whereas software deployments will be pushed by the last scanning server that tried to scan a machine. Information on setting up an installation with multiple scanning servers can be found in [this knowledge base article](/classic/docs/set-up-an-installation-with-multiple-scanning-servers).  
  Theoretically, an infinite number of scanning servers can be used, allowing you to control each and every part of your network, across the street or across the world.


