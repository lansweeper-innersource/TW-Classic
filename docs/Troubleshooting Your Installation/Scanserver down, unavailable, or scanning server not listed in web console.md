<!-- # Scanserver down, unavailable, or scanning server not listed in web console -->
![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_297/image_001.jpg) **This page provides troubleshooting steps for resolving issues with the Lansweeper scanning service connecting to the database.**

This page is for Lansweeper Classic. For Lansweeper Sites (in the cloud), see [Scan server status unknown or sync server status down](/docs/scan-server-status-unknown-or-sync-server-status-down).

When you install [Lansweeper](https://www.lansweeper.com/ "Lansweeper"), a service called **Lansweeper Server** is added to Windows Services on the machine hosting your installation. This service is mostly responsible for scanning your network and sending data back to your Lansweeper database. It also pushes configured deployments to Windows computers and processes emails.

For an overview of all your scanning options, see [Lansweeper's Scanning Guide](https://www.lansweeper.com/resources/lansweeper-scanning-guide/ "Scanning Guide").

The **Lansweeper Server** service is referred to as the scanning service and the machine hosting the service as a scanning server. A Lansweeper installation has at least one scanning server, though multiple scanning servers can be configured as well. By default, the scanning service is configured to automatically start, as the service needs to be running to be able to scan your network.

However, you may at some point notice that the service is marked as "scanserver unavailable" or that a secondary scanning server you're trying to connect to your installation doesn't show up in the web console. If a scanning server is marked as down or unavailable or if a secondary scanning server doesn't have its own configuration tab in the web console, this means the server isn't connecting to your Lansweeper database. Even if a secondary scanning service installed successfully, it could still fail to connect to the database, as our installer adds a random username and password to the server's configuration file.

![scanserver-unavailable-or-scanning-server-not-listed-in-web-console-1.jpg](/docs/.document360/assets/article_297/image_002.jpg)

To resolve this issue and have your scanning server successfully connect to the database:

1. If you are trying to connect a secondary scanning server, make sure the secondary server doesn't have the same name as one of your other scanning servers. Having multiple scanning servers with the same name is not supported.
2. If your Lansweeper database is hosted in SQL LocalDB or SQL Server and you never configured your own custom database password before, do so now by following the instructions in [this knowledge base article](/docs/change-the-lansweeper-database-password).
3. Stop the **Lansweeper Server** service in **Windows Services** on the problem scanning server or the server that is marked as "scanserver unavailable".

   ![procedure-stopping-the-lansweeper-service.jpg](/docs/.document360/assets/article_297/image_003.jpg)
4. Run the ConfigEditor tool found at `Program Files (x86)\Lansweeper\Tools\ConfigEditor.exe` on the problem scanning server.

   ![menu-configeditor.jpg](/docs/.document360/assets/article_297/image_004.jpg)
5. Make sure the ConnectionString listed in the **Service** tab of the ConfigEditor tool matches the one in the **Website** tab of **ConfigEditor.exe** on the server hosting the web console.   
   If your database is hosted in the SQL Compact database server, the connection string will just be a reference to an .sdf file and should already be correct.   
   If your database is hosted in SQL LocalDB or SQL Server though, make sure the Data Source (SQL instance name), Initial Catalog (Lansweeper database name), username and password in the connection string are correct.  
     
   On remote servers, you will have to replace any localhost references in the Data Source with your database server's actual name or IP address. If you are able to see data in the web console, you know that your console is successfully connecting to the database and that its connection string is correct. The scanning server should be able to connect to the database as well, if it uses the same database connection details.

   ![procedure-configeditor-website-connection-string-check.jpg](/docs/.document360/assets/article_297/image_005.jpg)
6. Restart the **Lansweeper Server** service in **Windows Services** on the problem scanning server.

   ![procedure-restarting-the-lansweeper-service.jpg](/docs/.document360/assets/article_297/image_006.jpg)
7. If the "scanserver unavailable" issue persists, look for recent entries in the **Errorlog.txt** file below, found at `Program Files (x86)\Lansweeper\Service\Errorlog.txt` on the problem scanning server.   
   There may be an error message providing more information on the database connection failure. The following knowledge base articles can help resolve database connection errors like ["login failed"](/docs/login-failed-for-user-lansweeperuser) and ["a network-related or instance-specific error occurred"](/docs/a-network-related-or-instance-specific-error-occurred).
