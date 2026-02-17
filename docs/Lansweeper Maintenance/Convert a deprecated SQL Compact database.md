<!-- # Convert a deprecated SQL Compact database -->

From March 2020 onward, Microsoft SQL Compact is deprecated and is no longer a supported database server for hosting the Lansweeper database. SQL Compact is no longer offered as an option in the Lansweeper installer. In addition, when updating a SQL Compact installation to Lansweeper version 8.0 or higher, you are informed that a conversion to SQL LocalDB or SQL Server is required prior to updating.

Existing data, reports and settings remain intact after converting a deprecated database. The exact procedure you should follow for converting your SQL Compact database depends on which Lansweeper version you are currently using.   
It also depends on whether you have a fully functional Lansweeper installation under SQL Compact, or just a SQL Compact database file. If you have a functional Lansweeper installation, you can check its version number in the **Configuration > Your Lansweeper License** section of the web console.

- Convert a SQL Compact installation on Lansweeper version 7.2.107.4 or lower
- Convert a SQL Compact installation on Lansweeper version 7.2.108.6
- Converting if you only have a SQL Compact database file

## Convert SQL Compact installation on version 7.2.107.4 or lower

If your SQL Compact installation is on Lansweeper version 7.2.107.4 or lower, you can easily migrate to SQL LocalDB by updating your Lansweeper installation using [this 7.2.108.6 installer](https://cdn.lansweeper.com/download/7.2.108/6/LansweeperSetup.exe).

Run the installer on your Lansweeper server and choose the **Upgrade** option. The update converts your database to SQL LocalDB. This process is automatic and requires no user input, though the installer will indicate that this conversion is about to happen. Once your Lansweeper installation has been updated to version 7.2.108.6 and converted to SQL LocalDB, you can continue to update it to more recent Lansweeper versions.

## Convert SQL Compact installation on version 7.2.108.6

If your SQL Compact installation is on Lansweeper version 7.2.108.6, you must manually convert it to SQL LocalDB or SQL Server.

1. Your SQL Compact installation can be converted to SQL LocalDB or SQL Server.
   - If you choose to convert your SQL Compact installation to SQL Server, first install your SQL Server instance on a machine of your choice.
   - If you choose to convert your SQL Compact installation to SQL LocalDB, you don't need to set up the SQL instance yourself. The Lansweeper installer will do this for you.
   - If you're unsure whether you should choose SQL Server or SQL LocalDB as your database server, we recommend reviewing [this database server comparison article](/docs/compatible-sql-database-servers-for-hosting-the-lansweeper-database).
2. Stop the **Lansweeper Server** service in Windows Services. 
3. Stop your web server service in Windows Services. Your web server service is either **IIS Express** or **World Wide Web Publishing Service** (IIS). Keep in mind that this will log everyone out of the console.   
   
4. Back up your SQL Compact database and other Lansweeper files. Your SQL Compact database stores all of your data, reports and settings. Create a copy of your SQL Compact database file and move it to a safe location outside of the Program Files folder. Your SQL Compact database file can be found at `Program Files (x86)\Lansweeper\SQLData\lansweeperdb.sdf`. 
5. If you added any documents, images, widgets or other files to Lansweeper, back these up as well. Information on which folders store which files can be found in this knowledge base article. Make sure to back up Encryption.txt as well, which is used to encrypt and decrypt the credentials in your database. The file can be found at `Program Files (x86)\Lansweeper\Key\Encryption.txt`.  

   Do not back up the entire Website folder. Only back up the specific subfolders you need. Backing up and restoring the entire Website folder can lead to issues.
6. Download and run [the 7.2.108.6 installer](https://cdn.lansweeper.com/download/7.2.108/6/LansweeperSetup.exe), choose **New installation** and then **Advanced install**.
7. Select your preferred database server, SQL LocalDB or SQL Server. If you select SQL Server, you will be asked to point the installer to your SQL Server instance.  

   Reinstall all Lansweeper components: the database, service and web console.
8. Migrate the SQL Compact data by stopping the Lansweeper and web server services in Windows Services.
9. Run CompactToServer.exe found at `Program Files (x86)\Lansweeper\Tools\CompactToServer.exe` on the machine hosting your Lansweeper service. 
10. Select the upper **Browse...** button, select the lansweeperdb.sdf file you created a backup of earlier and select **Open**. If you chose SQL Server as your preferred database server, you may also need to select the lower **Browse...** button to select your SQL Server instance. The schema versions of the source and destination databases should match, indicating that they're both on the same Lansweeper version. Select **Migrate Database** to start the migration process. Note that depending on the size of your database, this process may take a while to complete.
11. Restore the Website subfolders and Encryption.txt file you created a backup of earlier. Afterward, restart the Lansweeper and web server services in Windows Services. 

## Convert SQL Compact database file: lansweeperdb.sdf

If you only have a SQL Compact lansweeperdb.sdf file and not a fully functional Lansweeper installation, you can convert it to SQL LocalDB or SQL Server.

1. Perform a new, Easy Lansweeper installation using [this 7.2.107.4 installer](https://cdn.lansweeper.com/download/7.2.107/4/LansweeperSetup.exe).
2. Stop the **Lansweeper Server** and **IIS Express services** in Windows Services.
3. Place your lansweeperdb.sdf file in the `Program Files (x86)\Lansweeper\SQLData` folder, overwriting the default file already in there, and restart the services. You now have a functional 7.2.107.4 SQL Compact installation that you can convert to SQL LocalDB or SQL Server.
4. Convert your SQL Compact installation to SQL LocalDB or SQL Server.
   - If you choose to convert your SQL Compact installation to SQL Server, first install your SQL Server instance on a machine of your choice.
   - If you choose to convert your SQL Compact installation to SQL LocalDB, you don't need to set up the SQL instance yourself, as the Lansweeper installer will do this for you.
   - If you're unsure whether you should choose SQL Server or SQL LocalDB as your database server, we recommend reviewing [this database server comparison article](/docs/compatible-sql-database-servers-for-hosting-the-lansweeper-database).
5. Stop the **Lansweeper Server** service in Windows Services.  
   
6. Stop your web server service, **IIS Express**, in Windows Services. Keep in mind that this will log everyone out of the console.  
   
7. Back up your SQL Compact database and other Lansweeper files. Your SQL Compact database stores all of your data, reports and settings. Create a copy of your 7.2.107.4 SQL Compact database file and move it to a safe location outside of the Program Files folder. Your SQL Compact database file can be found at `Program Files (x86)\Lansweeper\SQLData\lansweeperdb.sdf`. 
8. If you added any documents, images, widgets or other files to Lansweeper, back these up as well. Information on which folders store which files can be found in this knowledge base article. Make sure to back up Encryption.txt as well, which is used to encrypt and decrypt the credentials in your database. This file can be found at `Program Files (x86)\Lansweeper\Key\Encryption.txt`.  

   Do not back up the entire Website folder. Only back up the specific subfolders you need. Backing up and restoring the entire Website folder can lead to issues.
9. Run [the same 7.2.107.4 installer](https://cdn.lansweeper.com/download/7.2.107/4/LansweeperSetup.exe) you used earlier, choose **New installation** and then **Advanced install**.
10. Select your preferred database server, SQL LocalDB or SQL Server. If you select SQL Server, you will be asked to point the installer to your SQL Server instance.  

    Reinstall all Lansweeper components: database, service and web console.
11. Migrate the SQL Compact data by stopping the Lansweeper and web server services in Windows Services.
12. Run CompactToServer.exe, found at `Program Files (x86)\Lansweeper\Tools\CompactToServer.exe` on the machine hosting your Lansweeper service. 
13. Select the upper **Browse...** button, select the lansweeperdb.sdf file you created a backup of earlier and select **Open**. If you chose SQL Server as your preferred database server, you may also need to click the lower **Browse...** button to select your SQL Server instance. The schema versions of the source and destination databases should match, indicating that they're both on the same Lansweeper version. Select **Migrate Database** to start the migration process. Note that depending on the size of your database, this process may take a while to complete.
14. Restore the Website subfolders and Encryption.txt file you created a backup of earlier. Afterward, restart the Lansweeper and web server services in Windows Services. 
