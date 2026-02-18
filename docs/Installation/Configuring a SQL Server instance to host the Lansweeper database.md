<!-- # Configuring a SQL Server instance to host the Lansweeper database -->
Lansweeper data, reports and settings are stored in a database. Your database is hosted in either the Microsoft SQL LocalDB, Microsoft SQL Server or (deprecated) Microsft SQL Compact database server. If you choose SQL Server as your database server, you'll need to manually install this database server prior to installing Lansweeper. You'll also need to ensure that the SQL Server instance is properly configured prior to running the Lansweeper installer.

If your SQL Server instance is not properly configured, the Lansweeper installer may be unable to access it to create and populate the Lansweeper database. This may result in errors like the one below. This article explains how to correctly configure a SQL Server instance to avoid these issues.

[DBNETLIB][ConnectionOpen (Connect()).]SQL Server does not exist or access denied.



To correctly configure your SQL Server instance so you can install the Lansweeper database in it, follow these steps:

1. Make sure the SQL Server and SQL Server Browser services are running at all times on the server hosting your SQL instance.
   - Right-click one of the services in Windows Services.  
     
   - Select the **Properties** menu item.  
     
   - Set the service's startup type to **Automatic** in the resulting pop-up and click **OK**.  
     
   - Right-click the service and select **Start**, if the service is not already started.  
     
2. Make sure your SQL instance is configured for mixed (Windows and SQL) authentication, as the Lansweeper service and web console will use a SQL user called "lansweeperuser" to connect to the database.   
   You can enable mixed authentication in SQL Server Management Studio. If SQL Server Management Studio isn't installed on your Lansweeper server, we recommend downloading it online.  
   - Right-click your SQL instance name in SQL Server Management Studio.
   - Select the **Properties** menu item.

     
   - Select the **Security** tab in the resulting pop-up.
   - Tick **SQL Server and Windows Authentication mode  
     **
   - Right-click your SQL instance name and select **Restart**.  
     
3. If your Lansweeper service and/or web console will be hosted on a different server than the Lansweeper database, make sure your SQL instance is set up to allow remote database connections.
   - Right-click your SQL instance name in SQL Server Management Studio, select **Properties** and open the **Connections** tab in the resulting pop-up. Select **Allow remote connections to this server**. ****...
   - Open SQL Server Configuration Manager and select the **Protocols** item under SQL Server Network Configuration. There should be a shortcut to SQL Server Configuration Manager in your Start menu.
   - Right-click **Named Pipes** and select **Enable**, right-click **TCP/IP** and select **Enable**.  
     
   - Right-click **TCP/IP**, select **Properties** and ensure that connectivity is enabled for the appropriate IPs in the IP Addresses tab.  
     
   - Right-click the SQL Server service under SQL Server Services and select **Restart**.  
     
4. If your Lansweeper service and/or web console will be hosted on a different server than the Lansweeper database, make sure SQL Server traffic is allowed through your firewall(s). TCP port 1433 is the most basic port used by SQL Server, though other ports are sometimes used as well. More info on allowing SQL Server traffic through firewalls can be found in [this Microsoft knowledge base article](https://support.microsoft.com/en-us/kb/287932).
5. With your SQL Server and firewall configuration taken care of, follow the instructions in [this article](/classic/docs/install-lansweeper-on-prem#heading2 "Advanced install Lansweeper") to install Lansweeper. The SQL instance name you submit in the Lansweeper installer should match what you see in SQL Server Management Studio. The installer will connect to the instance and create the lansweeperdb database. Don't try to manually create the database, as this will likely cause an installation failure.

   

   

   - Make sure DNS is up-to-date and your database server's NetBIOS name resolves to an IP address. In the example above, the database connection will fail if DELPHINE cannot be successfully pinged from Command Prompt on the servers hosting the Lansweeper Server service and web console.
   - Within the Lansweeper installer you can replace your database server's NetBIOS name with its IP address, e.g. 192.168.1.4\SQLEXPRESS. This may not be a good idea in DHCP enabled networks however, as IP changes will break the database connection.
   - If (and only if) your Lansweeper Server service and web console will be hosted on the same machine as the Lansweeper database, you can replace your database server's NetBIOS name with localhost, e.g. localhost\SQLEXPRESS.
