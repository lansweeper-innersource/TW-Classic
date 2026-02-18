<!-- # A network-related or instance-specific error occurred -->
[Lansweeper](https://www.lansweeper.com/) stores data, reports and settings in a database. Your database is hosted in either the Microsoft SQL Compact, Microsoft SQL LocalDB or Microsoft SQL Server database server. If you install Lansweeper under SQL LocalDB or SQL Server and the connection to your SQL instance is lost at some point, you may encounter errors such as the ones below.

A network-related or instance-specific error occurred while establishing a connection to SQL Server. The server was not found or was not accessible. Verify that the instance name is correct and that SQL Server is configured to allow remote connections.

Sqlcmd: Error: Microsoft SQL Native Client: An error has occurred while establishing a connection to the server. When connecting to SQL Server 2005, this failure may be caused by the fact that under the default settings SQL Server does not allow remote connections.

These errors indicate that Lansweeper is unable to locate the SQL instance hosting your Lansweeper database. It's important to note that this does not point to database corruption or to an issue with the database itself.

Though there are many possible causes for a loss of SQL connectivity, below are some troubleshooting steps you can try to resolve the issue.   
This article is divided into steps for the SQL Server database and steps for the SQL LocalDB server. You can [verify which database server you are using](/classic/docs/identify-which-database-server-lansweeper-is-using) with the ConfigEditor tool or in the Lansweeper web console.

## Resolving SQL connection errors under SQL Server

To resolve the SQL connection errors if your database server is a SQL Server (most commonly SQL Server Error 53), follow these steps:

1. Stop the **Lansweeper Server** service in **Windows Services**.

   
2. Stop your web server service in **Windows Services**. Your web server service is either IIS Express or World Wide Web Publishing Service (IIS).

   
3. Make sure the **SQL Server** and **SQL Server Browser** services are running at all times on the server hosting your SQL instance.  
   - Right-click one of the services in Windows Services.  
     
   - Select the **Properties** menu item.  
     
   - Set the service's startup type to **Automatic** in the resulting pop-up and select **OK**.  
     
   - Right-click the service and select **Start**, if the service is not already started.  
     
4. Log into SQL Server Management Studio. If SQL Server Management Studio isn't installed on your Lansweeper server, we recommend downloading it online.
5. Make sure your SQL instance is configured for mixed (Windows and SQL) authentication, as the Lansweeper service and web console use a SQL user called "lansweeperuser" to connect to the database.  
   - Right-click your SQL instance name in SQL Server Management Studio.
   - Select the **Properties** menu item.  
     
   - Select the **Security** tab in the resulting pop-up.
   - Tick **SQL Server and Windows Authentication mode**. ****
   - Right-click your SQL instance name and select **Restart**.  
     
6. If your Lansweeper service and/or web console are hosted on a different server than the Lansweeper database, make sure your SQL instance is set up to allow remote database connections.  
   - Right-click your SQL instance name in SQL Server Management Studio, select **Properties** and open the **Connections** tab in the resulting pop-up.  
     
   - Tick **Allow remote connections to this server**.  
     
   - Open SQL Server Configuration Manager and select the **Protocols** item under SQL Server Network Configuration. There should be a shortcut to SQL Server Configuration Manager in your Start menu.
   - Right-click **Named Pipes** and select **Enable**, right-click **TCP/IP** and select **Enable**.  
     
   - Right-click **TCP/IP**, select **Properties** and ensure that connectivity is enabled for the appropriate IPs in the **IP Addresses** tab.  
     
   - Right-click the SQL Server service under SQL Server Services and select **Restart**.  
     
7. If your Lansweeper service and/or web console are hosted on a different server than the Lansweeper database, make sure SQL Server traffic is allowed through your firewall(s). TCP port 1433 is the most basic port used by SQL Server, though other ports are sometimes used as well.   
   More info on allowing SQL Server traffic through firewalls can be found in [this Microsoft knowledge base article](https://support.microsoft.com/en-us/kb/287932).
8. Make sure your Data Source (SQL instance name) is correctly submitted in the ConfigEditor tool, found at `Program Files (x86)\Lansweeper\Tools\ConfigEditor.exe` on the servers hosting your **Lansweeper Server** service and web console.   
   If the tool has multiple tabs due to your server hosting multiple Lansweeper components, make sure the Data Source is correct in both tabs. The SQL instance name submitted in ConfigEditor should match what you see in SQL Server Management Studio.   
     
   If it doesn't, select the Data Source in each ConfigEditor tab and select **Edit** to correct it.  
     
   - Make sure DNS is up-to-date and your database server's NetBIOS name resolves to an IP address. In the example above, the database connection will fail if DELPHINE cannot be successfully pinged from Command Prompt on the servers hosting the Lansweeper Server service and web console.
   - Within your Lansweeper configuration files you can replace your database server's NetBIOS name with its IP address, e.g. 192.168.1.4\SQLEXPRESS. This may not be a good idea in DHCP enabled networks however, as IP changes will break the database connection.
   - If (and only if) your Lansweeper Server service and web console are hosted on the same machine as the Lansweeper database, you can replace your database server's NetBIOS name with localhost, e.g. localhost\SQLEXPRESS.
9. Restart the **Lansweeper** **Server** and web server services in **Windows Services**.

## Resolving SQL connection errors under SQL LocalDB

To resolve the SQL connection errors if your database server is a SQL LocalDB, follow these steps:

1. Make sure the Startup Type of the **Lansweeper LocalDB Service** in **Windows Services** on your Lansweeper server is set to **Automatic**. If necessary, right-click the service, select **Properties** and correct the Startup Type.
2. (Re)start the **Lansweeper LocalDB Service** on your Lansweeper server.

   
3. (Re)start the **Lansweeper Server** service**.**

   
4. (Re)start your web server service. Your web server service is either IIS Express or World Wide Web Publishing Service (IIS).

   
