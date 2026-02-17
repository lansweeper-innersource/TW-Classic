<!-- # Restore your installation from a backup -->
If you [manually created a backup](/docs/back-up-your-installation) of your Lansweeper installation, you can always restore it at a later date if necessary. Which restore procedure you should follow depends on which database server you are using, Microsoft SQL Compact or Microsoft SQL Server. If you perform an Easy Install, your database is hosted in SQL Compact. If you perform an Advanced Install, your database can be hosted in SQL Compact or SQL Server. If you are unsure which database server you are using, browse to the following section of the web console: **Configuration > Your Lansweeper License**.



## Restoring a backup if you are using SQL Compact

1. Stop the **Lansweeper Server** service in Windows Services.

   
2. Stop the **Lansweeper Auto-update** service in Windows Services.
3. Stop your web server service in Windows Services. Keep in mind that this will log everyone out of the console. Your web server service is either IIS Express or World Wide Web Publishing Service (IIS).
4. Make sure your database backup file is called `lansweeperdb.sdf` and place it in `Program Files (x86)\Lansweeper\SQLData`, overwriting the database file currently present in the folder.
5. Restore the **Website** subfolders and **Encryption.txt** file you created a backup of.
6. Restart the Lansweeper and web server services in Windows Services.

## Restoring a backup if you are using SQL Server or SQL LocalDB

1. Stop the **Lansweeper Server** service in Windows Services.
2. Stop the Lansweeper Auto-update service in Windows Services.  
   
3. Stop your web server service in Windows Services. Keep in mind that this will log everyone out of the console. Your web server service is either IIS Express or World Wide Web Publishing Service (IIS).
4. Right-click the lansweeperdb database in SQL Server Management Studio and select **Tasks > Restore > Database...** to open the restore wizard. If SQL Server Management Studio isn't installed on your Lansweeper server, we recommend downloading it online.
5. In the **General** tab of the restore wizard, select the correct destination (lansweeperdb) and source for the restore operation. If your backup is a .bak file, select the **Device** option under **Source** and select the button with the three dots to open a pop-up where you can select your file.  

   If you're restoring a SQL LocalDB database, do not change the file path of your mdf and ldf files in the Files tab. They must be stored in the Lansweeper\SQL Data folder. The Restore As path in the Files tab must be the Lansweeper\SQL Data folder belonging to your Lansweeper database.
6. In the **Options** tab of the restore wizard, tick **Overwrite The Existing Database**, and select **OK** to perform the database restore.  

   Make sure the overwrite box is checked. Otherwise, the following error may be generated: "The backup set holds a backup of a database other than the existing 'lansweeperdb' database."
7. Log into SQL Server Management Studio with a user that has sysadmin rights. Then execute the script below to reset the lansweeperuser SQL user used by the Lansweeper service and web console to connect to the database. Replace **'lansweeperuserpassword'** with the password you want to set for lansweeperuser, leaving the single quotes in the script.  

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
   USE lansweeperdb;
   IF EXISTS
   (
       SELECT principal_id
       FROM sys.database_principals
       WHERE name = 'lansweeperuser'
   )
       BEGIN
           DROP USER lansweeperuser;
   END;
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

   /* Optional step to grant lansweeperuser additional permissions, which are required for syncing with Cloud */

   USE MASTER;
   GO
   ALTER SERVER ROLE [dbcreator] ADD MEMBER [lansweeperuser];
   GO
   GRANT VIEW SERVER STATE TO lansweeperuser;
   GO
   ```

   Don't skip this step! Restoring a database backup almost always corrupts the SQL user used by the Lansweeper service and web console to connect to the database. If you don't reset the user, the service and web console will be unable to connect to the database.
8. Run the ConfigEditor tool on the server(s) hosting your **Lansweeper Server** service and web console. The tool can be found at `Program Files (x86)\Lansweeper\Tools\ConfigEditor.exe`.
9. Click through any warnings the tool may be giving you about your password being incorrect.
10. Select the **Password** field and select **Edit**.
11. Submit the same password you used in the database script and select **Save**.
12. If the ConfigEditor tool has multiple tabs due to your server hosting multiple Lansweeper components, select the other tab, click through any warnings and repeat the password-changing process.
13. Restore the **Website** subfolders and Encryption.txt file you created a backup of. [Restore only these folders](/docs/where-are-lansweeper-data-reports-and-settings-stored#heading2 "Where lansweeper data reports and settings are stored").
14. Restart the Lansweeper and web server services in Windows Services.
15. If you have multiple scanning servers, update the database password on those serversby stopping the Lansweeper service, using the ConfigEditor tool and restarting the service.
