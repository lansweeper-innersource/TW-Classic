<!-- # Move your database from SQL LocalDB to SQL Server -->

Lansweeper data, reports and settings are stored in a database, which is hosted in either Microsoft SQL Compact, Microsoft SQL LocalDB or Microsoft SQL Server. If your database is hosted in LocalDB, you can move it to SQL Server on the same or a different machine, if at some point required. If you are unsure which database server you are using, browse to the **Configuration > Your Lansweeper License**section of the web console.  
![Moving-your-database-from-SQL-LocalDB-to-SQL-Server-1.jpg](/docs/.document360/assets/article_106/image_002.jpg)

Prior to the migration, make sure to install SQL Server on the machine where the new database will be hosted. You should install SQL Server 2022 or higher, as Lansweeper's LocalDB database server is based on SQL Server 2022.

1. Stop the **Lansweeper Server** service in Windows Services. ![procedure-stopping-the-lansweeper-service.jpg](/docs/.document360/assets/article_106/image_003.jpg)  
   Next, stop your web server service in Windows Services. Keep in mind that this will log everyone out of the console. Your web server service is either **IIS Express** or **World Wide Web Publishing Service** (IIS).  
   ![procedure-stopping-the-web-server-service.jpg](/docs/.document360/assets/article_106/image_004.jpg)
2. Back up your LocalDB database. Log into SQL Server Management Studio. If SQL Server Management Studio isn't installed on your Lansweeper server, we recommend downloading it online. The instance name you need to submit in Management Studio to access your LocalDB database is "(localdb)\.\LSInstance" and you can access the instance with the Windows user that performed your Lansweeper installation. Create a backup of your LocalDB database by right-clicking the lansweeperdb database in SQL Server Management Studio and selecting **Tasks > Back Up ...**in the menu. ![Moving-your-database-from-SQL-LocalDB-to-SQL-Server-2.jpg](/docs/.document360/assets/article_106/image_005.jpg)  
   - Database: lansweeperdb
   - Backup type: Full
   - Backup component: Database
   - Back up to: Disk, add a location where the backup file will be stored.
   - In the Options tab, you can tick **Verify Backup When Finished** to check the integrity of the backup file.  
     ![Moving-your-database-from-SQL-LocalDB-to-SQL-Server-3.jpg](/docs/.document360/assets/article_106/image_006.jpg)![Moving-your-database-from-SQL-LocalDB-to-SQL-Server-4.jpg](/docs/.document360/assets/article_106/image_007.jpg)
3. Download [the latest Lansweeper installer](https://www.lansweeper.com/install-lansweeper/) and run it on your new database server.
4. Configure the installation exactly as shown below. This will install a default Lansweeper database in the SQL Server instance specified by you. ![Moving-your-database-from-SQL-LocalDB-to-SQL-Server-10.jpg](/docs/.document360/assets/article_106/image_008.jpg)  

   Don't try to manually create the database. Let the installer do this for you.
5. Restore your database backup on your new server by right-clicking the "lansweeperdb" database in SQL Server Management Studio and selecting **Tasks > Restore > Database...** in the menu.   
   ![Moving-your-database-from-SQL-LocalDB-to-SQL-Server-6.jpg](/docs/.document360/assets/article_106/image_009.jpg)
6. Select **Device** under **Source** and browse to the backup file "lansweeperdb.bak" that you previously created. Make sure you've selected the correct destination "lansweeperdb" and source for the restore operation.  
   ![Moving-your-database-from-SQL-LocalDB-to-SQL-Server-7.jpg](/docs/.document360/assets/article_106/image_010.jpg)
7. In the **Files** tab select **Relocate all files to folder** and check **Overwrite the existing database** in the Options tab. Select **OK** to perform the restore.  ![Moving-your-database-from-SQL-LocalDB-to-SQL-Server-9.jpg](/docs/.document360/assets/article_106/image_011.jpg) ![Moving-your-database-from-SQL-LocalDB-to-SQL-Server-8.jpg](/docs/.document360/assets/article_106/image_012.jpg)
8. Execute the script below in SQL Server Management Studio to reset the lansweeperuser SQL login used by the Lansweeper service and web console to connect to the database. Replace **'lansweeperuserpassword'** with the password you want to use for the lansweeperuser login, leaving the single quotes in the script.

```
/* Makes sure there are no objects in the lansweeperuser schema, so the lansweeperuser SQL user can be reset */
USE lansweeperdb
GO
DECLARE c_ALTSCHEMA CURSOR FOR
SELECT 'ALTER SCHEMA dbo TRANSFER lansweeperuser.'+name +';'
FROM sys.objects
WHERE SCHEMA_NAME(SCHEMA_ID) = 'lansweeperuser'
DECLARE @SQLStmt NVARCHAR(200)
OPEN c_ALTSCHEMA
FETCH NEXT FROM c_ALTSCHEMA INTO @SQLStmt
WHILE @@FETCH_STATUS = 0
BEGIN
EXEC(@SQLStmt)
FETCH NEXT FROM c_ALTSCHEMA INTO @SQLStmt
END
CLOSE c_ALTSCHEMA
DEALLOCATE c_ALTSCHEMA
GO
/* Resets the lansweeperuser SQL user */
USE lansweeperdb
GO
DROP SCHEMA lansweeperuser
GO
DROP USER lansweeperuser
GO
EXECUTE sp_droplogin lansweeperuser
GO
USE MASTER
GO
EXEC sp_addlogin 'lansweeperuser', 'lansweeperuserpassword', 'lansweeperdb', [English]
GO
USE lansweeperdb
GO
EXEC sp_grantdbaccess 'lansweeperuser', 'lansweeperuser'
GO
EXEC sp_addrolemember [db_owner], 'lansweeperuser'
GO

/* Optional step to grant lansweeperuser additional permissions, which are required for Syncing with Cloud */
USE MASTER
GO
ALTER SERVER ROLE [dbcreator] ADD MEMBER [lansweeperuser]
GO
GRANT VIEW SERVER STATE TO lansweeperuser
GO
```

Don't skip this step. Restoring a database backup almost always corrupts the SQL user used by the Lansweeper service and web console to connect to the database. If you don't reset the user, the service and web console will be unable to connect to the database.

9. Submit the SQL instance name and database password in ConfigEditor.
   - Run the ConfigEditor tool, found at `Program Files (x86)\Lansweeper\Tools\ConfigEditor.exe` on the servers hosting your Lansweeper Server service and web console. ![menu-configeditor.jpg](/docs/.document360/assets/article_106/image_013.jpg)
   - Click through any warnings the tool may be giving you about your password being incorrect.
   - Select the Data Source field, select **Edit** and submit the name of your new SQL Server instance.
   - Select the Password field, select **Edit** and submit the same password you previously used in the database script.**![procedure-configeditor-service-password-change.jpg](/docs/.document360/assets/article_106/image_014.jpg)**
   - If the ConfigEditor tool has multiple tabs due to your server hosting multiple Lansweeper components, select the other tab, click through any warnings and repeat the password and instance changing process. ![procedure-configeditor-website-password-change.jpg](/docs/.document360/assets/article_106/image_015.jpg)
   - Select **Save configs and restart service**. You've now successfully migrated your SQL LocalDB database to SQL Server. ![procedure-configeditor-save-and-restart.jpg](/docs/.document360/assets/article_106/image_016.jpg)
