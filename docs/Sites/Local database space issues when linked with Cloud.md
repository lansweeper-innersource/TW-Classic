<!-- # Local database space issues when linked with Cloud -->
As both SQL LocalDB and SQL Server Express databases are limited in capacity by Microsoft to 10 GB, it is important to keep an eye on the size of your [Lansweeper](https://www.lansweeper.com/) database, to prevent it from reaching its maximum size.

When the database is full or almost full, your Lansweeper server might stop functioning as it should, resulting in incomplete or out of date data. If your on-prem installation is linked to Cloud this may result in this same incomplete or out of date data being synced to Cloud, or your sync stopping altogether.  
Additionally, if your database reaches its size limit during a Lansweeper update, the update may fail.   
When the database reaches the size limit of 90% a notification will be shown in the on-prem web console.



This notification will only be shown to users that have the **Access Configuration** permission. The notification can be dismissed, and it will automatically disappear if the database size issue is resolved.

The current size of your database is listed in the Scanning Status widget or sync status section of the **Configuration > Link With Cloud Site** menu.



## Reduce your database size

1. Determine which database server is hosting your Lansweeper database by using the ConfigEditor tool. You can follow the instructions in [this knowledge base article](/docs/identify-which-database-server-lansweeper-is-using).
2. Stop the **Lansweeper Server** and web server service in Windows Services on all of your scanning servers. Keep in mind that this will log everyone out of the console. Your webserver service is either IIS Express or World Wide Web Publishing Service (IIS).  
   
3. Run the DatabaseMaintenance tool on your Lansweeper server. The tool can be found at `Program Files (x86)\Lansweeper\Tools\DatabaseMaintenance.exe`.  
   
4. Select **Truncate logs**, then **Shrink** and then **Compact**. Each operation may take a while to complete.  

   This step will clear the tblNtlog and tblNtlogMessage tables in your database, deleting all Windows event log information from your database. Event log data generally takes up the most space. You can still scan new events afterward.
5. Restart the **Lansweeper Server** and web server service in Windows Services, and wait a few minutes for the automated cleanup process to complete.

If you keep running into the database size limit, we recommend moving your Lansweeper database to a licensed SQL Server edition that has no fixed database size limit.   
To move your SQL LocalDB database to SQL Server, you can follow the steps in [this article](/docs/move-your-database-from-sql-localdb-to-sql-server). If you are already using SQL Server Express, you can follow [these steps](/docs/move-your-sql-server-database-to-a-different-server-or-sql-server-instance) to move to another SQL Server instance.

For more information about managing your database size, refer to [this knowledge base article](/docs/perform-automated-database-cleanups).
