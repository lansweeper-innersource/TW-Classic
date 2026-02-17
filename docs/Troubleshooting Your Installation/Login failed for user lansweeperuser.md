<!-- # Login failed for user lansweeperuser -->

Lansweeper data, reports and settings are stored in a database. Your database is hosted in either the Microsoft SQL Compact, Microsoft SQL LocalDB or Microsoft SQL Server database server. If you install Lansweeper under SQL LocalDB or SQL Server, the installer automatically creates a SQL user called "lansweeperuser". This user is used by the Lansweeper scanning service and web console to connect to the database.

If lansweeperuser gets corrupted, or has its password changed without an accompanying update of the Lansweeper configuration files, the service and console will no longer be able to connect to the database and you may see errors like the one below. The error below indicates that, even though Lansweeper is able to find the SQL instance hosting the lansweeperdb database, it is unable to access the database with the lansweeperuser account. It's important to note that this does not point to database corruption or an issue with the database itself. It simply indicates that the database cannot be accessed to read or write information. To resolve this issue, lansweeperuser needs to be reset.

Cannot connect to database, check your config file, service will be stopped. Login failed for user 'lansweeperuser'.

To reset lansweeperuser and have the service and console successfully connect to the database again, follow these steps:

1. Stop the **Lansweeper Server** service in **Windows Services**

   
2. Stop your web server service in **Windows Services**. Your web server service is either IIS Express or World Wide Web Publishing Service (IIS).

   
3. Log into SQL Server Management Studio. If SQL Server Management Studio isn't installed on your Lansweeper server, we recommend downloading it online.  

   If your database is hosted in SQL LocalDB, the SQL instance name you need to submit in Management Studio is (localdb)\.\LSInstance and you must log in on your Lansweeper server itself with the Windows user that initially installed Lansweeper. If your database is hosted in SQL Server, you would have configured your SQL instance name and password when you installed SQL Server.
4. If your database server is SQL Server, make sure your SQL instance is configured for mixed (Windows and SQL) authentication. If your database server is SQL LocalDB, your SQL instance should already be configured for mixed authentication by default.
   - Right-click your SQL instance name in SQL Server Management Studio.
   - Select the **Properties** menu item.

     
   - Select the Security tab in the resulting pop-up, and tick **SQL Server and Windows Authentication mode**.

     ****
   - Right-click your SQL instance name and select **Restart**.  
     
5. Execute the script below in SQL Server Management Studio to reset the lansweeperuser SQL user used by the Lansweeper service and web console to connect to the database. Replace what's marked in **bold** with the password you'd like to use for the lansweeperuser database user, leaving the single quotes in the script.

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
   ```
6. Run the **ConfigEditor.exe** tool, found at `Program Files (x86)\Lansweeper\Tools\ConfigEditor.exe` on the servers hosting your Lansweeper Server service and web console.

   
7. Click through any warnings the tool may be giving you about your password being incorrect.
8. Select the **Password** field and select **Edit**.

   
9. Submit the same password you previously used in the database script and select **Save**.
10. If the ConfigEditor tool has multiple tabs due to your server hosting multiple Lansweeper components, select the other tabs, click through any warnings and repeat the password changing process.

    
11. Select **Save** and restart the Lansweeper and web server services.
