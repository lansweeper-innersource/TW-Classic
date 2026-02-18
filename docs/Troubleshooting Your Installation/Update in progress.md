<!-- # Update in progress -->
This article explains the "update in progress" web console page. It is recommended that you update your Lansweeper installation on a regular basis, to ensure that you have the latest available patches installed and access to any new features that have been released. Any update should be run on the machine hosting the web console as well as any scanning server hosting the Lansweeper Server service, as explained in [this knowledge base article](/classic/docs/update-lansweeper-on-premises).

The first scanning server to be updated will update the database as well, so the update does not need to be run separately on the database server. If an update includes database changes, your scanning server will run a number of scripts on the database to implement the changes. The scripts may take a while to complete if you have a large database, and you may see a message similar to the ones below for the duration of the update.

```
Update in progress. Processing script X of Y.
```

```
Update in progress. Processing script -1 of Y.
```

The message below indicates that your web console is on a higher Lansweeper release than the database and is waiting for the database update scripts to finish processing. It is recommended that you wait at least 15 minutes and refresh the web console to see if the execution of the scripts is progressing as expected. If this message does not change after 15 minutes, however, your scanning server might not be on the same Lansweeper release as the web console. This might suggest that there is an issue with your scanning service connecting to your Lansweeper database or a database issue in general.   
In this article, you can find quick steps and more extensive steps you can perform to resolve this issue.

## Quick Steps to resolve update in progress

The steps below may quickly resolve the issue if you're using [the SQL LocalDB database provider](/classic/docs/introduction-to-the-sql-localdb-database-server).

1. Start or restart the "Lansweeper LocalDB Service" and wait for it to be started or running.
2. Afterward, start or restart the "Lansweeper Server" service.



If SQL LocalDB is your Lansweeper database provider, the Lansweeper LocalDB Service must be started for your Lansweeper installation to be functional in general.

## Extensive Steps

If the issue persists after performing the quick steps, please follow the steps below.

1. Double-check the URL you are accessing to determine which machine is hosting your Lansweeper web console.   
   If localhost is listed in the URL, your console is hosted on the machine you're accessing the console from.   
   If a computer name or IP address is listed in the URL, your web console is hosted on the machine whose name or IP is included in the URL. In the example below, the console is hosted on computer LAN-001.

   
2. Stop the web server service in **Windows Services** on the machine hosting your web console. Keep in mind that this will log everyone out of the console. Your web server service is either IIS Express or World Wide Web Publishing Service (IIS).

   
3. Stop the **Lansweeper Server** service in **Windows Services** on your scanning servers.

   
4. On the machine hosting your web console, open the **Website** tab of **ConfigEditor.exe** and verify which database your web console is connecting to. This tool can be found at `Program Files (x86)\Lansweeper\Tools\ConfigEditor.exe`.   
   If your database is hosted in the (deprecated) Microsoft SQL Compact database server, your connection string will just be a reference to an .sdf file.   
   If your database is hosted in Microsoft SQL LocalDB or Microsoft SQL Server, the string will include a Data Source (SQL instance name), Initial Catalog (Lansweeper database name), username and password.

   
5. On machines hosting the **Lansweeper Server** service, open the **Service** tab of **ConfigEditor.exe** and ensure that the database connection string in the tool matches the one used by your website. This tool can be found at `Program Files (x86)\Lansweeper\Tools\ConfigEditor.exe`.  
   If your database is hosted in SQL Compact, your connection string should already be correct.   
   If your database is hosted in SQL LocalDB or SQL Server though, the SQL instance name, username or password used by the service may be incorrect. Keep in mind of course that, if your scanning service is not on the same machine as your database, you will need to replace any localhost references in your connection string with the name or IP address of your database server.

   
6. Restart the Lansweeper and web server services in Windows Services.
7. Download the latest Lansweeper installer through [this link](https://www.lansweeper.com/update-lansweeper/).
8. Run the installer on both the machine hosting the web console and one of the machines hosting the **Lansweeper Server** service. If available, choose the **Upgrade** option. If the **Upgrade** option is not available, close the installer.

   
9. If the update message still doesn't disappear after waiting 15 minutes and refreshing the web console, look for and resolve database connection failures in the **Errorlog.txt** file, found at `Program Files (x86)\Lansweeper\Service\Errorlog.txt` on the machine hosting the Lansweeper Server service.   
   If the Lansweeper service cannot connect to the database, it cannot run the database update scripts. There are articles in our knowledge base [on resolving "login failed"](/classic/docs/login-failed-for-user-lansweeperuser) and ["network-related or instance-specific"](/classic/docs/a-network-related-or-instance-specific-error-occurred) you may find in the log.
