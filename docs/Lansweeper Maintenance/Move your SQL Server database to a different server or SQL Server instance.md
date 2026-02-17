<!-- # Move your SQL Server database to a different server or SQL Server instance -->
Lansweeper data, reports and settings are stored in a database. Your database is hosted in either the Microsoft SQL LocalDB, Microsoft SQL Server or the deprecated Microsoft SQL Compact database server.

If your database is hosted in SQL Server, you can move it to a different machine or different SQL Server if at some point required.

If it's hosted in SQL Compact or SQL LocalDB, only moving the database and not the other Lansweeper components is not possible. SQL Compact and SQL LocalDB databases can only be accessed by services running locally on the server, so all Lansweeper components must be present on the same machine and moved simultaneously when these database servers are used. If you are unsure which database server you are using, you can [verify using the ConfigEditor tool or in the Lansweeper web console](/docs/identify-which-database-server-lansweeper-is-using).

This article only explains how to move the database, and only applies to databases hosted in SQL Server. If you are trying to move all Lansweeper components (scanning service, database and web console) to another machine, follow [these instructions](/docs/move-your-lansweeper-installation-to-a-different-server) instead. More information on components and how they interact can be found in [this knowledge base article](/docs/lansweeper-classic-components-and-architecture).

## Move a SQL Server database to different server or SQL Server instance

1. Stop the **Lansweeper Server service** in Windows Services.
2. Stop your web server service in Windows Services. Keep in mind that this will log everyone out of the console. Your web server service is either **IIS Express** or **World Wide Web Publishing Service (IIS)**.
3. Back up your database by right-clicking lansweeperdb in SQL Server Management Studio and selecting **Tasks > Back Up...** in the menu. If SQL Server Management Studio isn't installed on your Lansweeper server, we recommend downloading it online.
   - Database: lansweeperdb
   - Backup type: Full
   - Backup component: Database
   - Name: make sure this is something other than lansweeperdb, to avoid overwriting your existing database.
   - In the **Options** tab, you can tick **Verify Backup When Finished** to check the integrity of the backup file.
4. Download [the latest Lansweeper installer](https://www.lansweeper.com/install-lansweeper/) and run it on your new database server.
5. Configure the wizard exactly as shown below. This will install a default Lansweeper database in the SQL Server instance specified by you.  

   Don't try to manually create the database. Let the installer do this for you.
6. Restore your database backup on your new server by right-clicking the lansweeperdb database in SQL Server Management Studio and selecting **Tasks > Restore> Database...** in the menu. Make sure you've selected the correct destination (lansweeperdb) and source for the restore operation and that "Overwrite the existing database" is checked in the **Options** tab. Select **Ok** to restore the database.  

   Make sure the overwrite box is checked. Otherwise, the following error may be generated:   
   The backup set holds a backup of a database other than the existing 'lansweeperdb' database.
7. Execute the script below in SQL Server Management Studio to reset the lansweeperuser SQL login used by the Lansweeper service and web console to connect to the database. Replace **'lansweeperuserpassword'**with the password (keep the single quotes) you want to use for the lansweeperuser login, leaving the single quotes in the script.

```
/* Makes sure there are no objects in the lansweeperuser schema, so the lansweeperuser SQL user can be reset */

USE lansweeperdb; 
GO
DECLARE c_ALTSCHEMA CURSOR
FOR SELECT 'ALTER SCHEMA dbo TRANSFER lansweeperuser.' + name + ';'
    FROM sys.objects
    WHERE SCHEMA_NAME(SCHEMA_ID) = 'lansweeperuser';
DECLARE @SQLStmt NVARCHAR(200);
OPEN c_ALTSCHEMA;
FETCH NEXT FROM c_ALTSCHEMA INTO @SQLStmt;
WHILE @@FETCH_STATUS = 0
    BEGIN
        EXEC (@SQLStmt);
        FETCH NEXT FROM c_ALTSCHEMA INTO @SQLStmt;
    END;
CLOSE c_ALTSCHEMA;
DEALLOCATE c_ALTSCHEMA; 
GO

/* Resets the lansweeperuser SQL user */

USE lansweeperdb; 
GO

DROP SCHEMA lansweeperuser; 
GO

DROP USER lansweeperuser; 
GO

EXECUTE sp_droplogin 
        lansweeperuser; 
GO

USE MASTER; 
GO

EXEC sp_addlogin 
     'lansweeperuser', 
     'lansweeperuserpassword', 
     'lansweeperdb', 
     [English]; 
GO

USE lansweeperdb; 
GO

EXEC sp_grantdbaccess 
     'lansweeperuser', 
     'lansweeperuser'; 
GO

EXEC sp_addrolemember 
     [db_owner], 
     'lansweeperuser';
GO
```

Don't skip this step. Restoring a database backup almost always corrupts the SQL user used by the Lansweeper service and web console to connect to the database. If you don't reset the user, the service and web console will be unable to connect to the database.

8. Run the ConfigEditor tool, found at `Program Files (x86)\Lansweeper\Tools\ConfigEditor.exe` on the servers hosting your Lansweeper Server service and web console.
9. Click through any warnings the tool may be giving you about your password being incorrect.
10. Select the Data Source field, select **Edit** and submit the name of your new SQL Server instance.
11. Select the Password field, select **Edit** and submit the same password you previously used in the database script.
12. If the ConfigEditor tool has multiple tabs due to your server hosting multiple Lansweeper components, select the other tabs, click through any warnings and repeat the password and instance changing process.  
    
13. Select **Save configs and restart service**. You've now successfully migrated your SQL Server database.
