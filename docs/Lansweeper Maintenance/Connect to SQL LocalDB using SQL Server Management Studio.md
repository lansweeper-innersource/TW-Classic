<!-- # Connect to SQL LocalDB using SQL Server Management Studio -->
From Lansweeper 7.2 onward, [SQL LocalDB](/docs/introduction-to-the-sql-localdb-database-server) is one of the available database server options for hosting your Lansweeper database. Lansweeper LocalDB is a custom variant of Microsoft SQL (MSSQL) Server 2014 Express. It was introduced as a replacement for the now deprecated Microsoft SQL Compact database server.

To perform certain actions such as [backing up](/docs/back-up-your-installation) and [restoring your database](/docs/restore-your-installation-from-a-backup), you will need to be able to manage your database directly. This knowledge base article explains how to connect to your Lansweeper SQL LocalDB database using SQL Server Management Studio (SSMS).

## Connect to your Lansweeper SQL LocalDB database

To connect to your LocalDB instance, you can use SQL Server Management Studio (SSMS). A connection requires you to submit a server name and a user account to authenticate.

1. Run SQL Server Management Studio on your Lansweeper server. Microsoft SQL LocalDB does not support remote connections. As such the database must be connected to from your Lansweeper server itself. Install and run SQL Server Management Studio (SSMS) on the same machine where you've installed Lansweeper. SSMS can be downloaded via the Microsoft website.  

   You can only connect to your SQL LocalDB instance locally on the machine hosting your Lansweeper installation.
2. Submit the server name. For SQL LocalDB the server name should always be "(localdb)\.\LSInstance". ![LocalDB_Server_Name.jpg](/docs/.document360/assets/article_097/image_002.jpg)
3. Select your authentication type. You can use Windows Authentication or SQL Server Authentication.
   - Windows Authentication  
     The user account you are logged on as is automatically selected when you select Windows Authentication. Make sure to log on with the user account that last installed or updated Lansweeper as this is the SA account to your SQL LocalDB instance. Only the SA account can connect to the LocalDB instance. ![LocalDB_Windows_Authentication.jpg](/docs/.document360/assets/article_097/image_003.jpg)   
     You can verify which user performed the last installation or update by opening the Registry Editor on your Lansweeper server.   
     Navigate to: `HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Lansweeper_is1`  
     Check the value for: **Inno Setup CodeFile: InstalledBy**.  
     If the user account that last installed or updated Lansweeper is no longer available, you can modify the **Inno Setup CodeFile: InstalledBy** value in the registry to another user account.  
     Make sure to restart the Lansweeper LocalDB service afterwards.  

     Only the user that installed Lansweeper can connect to your LocalDB instance via Windows Authentication.
   - SQL Server Authentication  
     By default, the SQL user lansweeperuser has access to your SQL LocalDB instance. This user is created during the installation of Lansweeper and is assigned a random password. The first time you connect to your LocalDB instance, you will need to log in as the Windows user that performed the Lansweeper installation. Once you're connected to your instance, you can [configure a custom password](/docs/change-the-lansweeper-database-password) for the lansweeperuser account. ![LocalDB_SQL_Server_Authentication.jpg](/docs/.document360/assets/article_097/image_004.jpg)
