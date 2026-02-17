<!-- # Back up your installation -->

It is recommended that you back up your [Lansweeper](https://www.lansweeper.com/) installation on a regular basis, especially prior to performing any updates. An unexpected shutdown of your Lansweeper server could lead to an update failure and subsequent database corruption. A manual backup is also required to move your installation from one server to another.

Which backup procedure you should follow depends on which database server you are using. Lansweeper data, reports and settings are stored in a database. Your database is hosted in either the Microsoft SQL LocalDB, Microsoft SQL Server or the deprecated Microsoft SQL Compact database server. You can [verify which database server you are using](/docs/identify-which-database-server-lansweeper-is-using) with the ConfigEditor tool or in the Lansweeper web console.



## Backing up if you are using SQL Compact

SQL Compact was an old database server option that is no longer supported. If you are still using SQL Compact as your Lansweeper database server, you should [convert your database to SQL LocalDB or SQL Server](/docs/convert-a-deprecated-sql-compact-database).

1. Stop the **Lansweeper Server** service in Windows Services.
2. Stop your web server service in Windows Services. Keep in mind that this will log everyone out of the console. Your web server service is either IIS Express or World Wide Web Publishing Service (IIS).
3. Create a copy of your SQL Compact database file, which can be found at `Program Files (x86)\Lansweeper\SQLData\lansweeperdb.sdf`.
4. If you added any documents, images, widgets or other files to Lansweeper, back these up as well. Information on which folders store which files can be found in [this knowledge base article](/docs/where-are-lansweeper-data-reports-and-settings-stored#heading2 "Where lansweeper data reports and settings are stored").  

   Do not back up the entire Website folder. Only back up the specific subfolders, you need, as backing up and restoring the entire Website folder can lead to issues.
5. If it exists, create a backup copy of the following file as well: `Program Files (x86)\Lansweeper\Key\Encryption.txt`.
6. Restart the **Lansweeper Server** and web server services in Windows Services.

## Backing up if you are using SQL LocalDB or SQL Server

1. Stop the **Lansweeper Server** service in Windows Services. 
2. Stop your web server service in Windows Services. Keep in mind that this will log everyone out of the console. Your web server service is either IIS Express or World Wide Web Publishing Service (IIS).
3. Log into SQL Server Management Studio. If SQL Server Management Studio isn't installed on your Lansweeper server, we recommend downloading it online.  

   If your database is hosted in SQL LocalDB, the SQL instance name you need to submit in Management Studio is (localdb)\.\LSInstance and you can log in with the Windows user that initially installed Lansweeper. If your database is hosted in SQL Server, you would have configured your SQL instance name and password when you installed SQL Server.
4. Right-click the lansweeperdb database and select **Tasks > Back Up...** to open the backup wizard.  

   Scanned data, reports, and settings are stored in your database. Scanning servers, which only run the Lansweeper Server service, don't store any data or settings. They retrieve settings from the database and send scanned data directly to the database.
5. In the **General** tab of the backup wizard, configure the source and destination options. By default, the backup destination is a .bak file on your disk drive.
   - Database: lansweeperdb
   - Backup type: Full
   - Backup component: Database
6. In the **Media Options** tab of the backup wizard, tick **Verify Backup When Finished**. This ensures the integrity of the backup is checked once created.
7. In the **Backup Options** tab of the backup wizard, make sure the name of the backup set is something other than lansweeperdb, to avoid overwriting your existing database. Select **OK** to create the database backup.  
   
8. If you added any documents, images, widgets, or other files to Lansweeper, back these up. Information on which folders store which files can be found in [this knowledge base article](/docs/where-are-lansweeper-data-reports-and-settings-stored#heading2 "Where lansweeper data reports and settings are stored").  

   Do not back up the entire Website folder. Only back up the specific subfolders, you need. Backing up and restoring the entire Website folder can lead to issues.
9. If it exists, create a backup copy of the following file as well: `Program Files (x86)\Lansweeper\Key\Encryption.txt`.
10. Restart the **Lansweeper Server** and web server services in Windows Services.
