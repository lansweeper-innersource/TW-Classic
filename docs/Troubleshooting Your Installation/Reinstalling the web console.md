<!-- # Reinstalling the web console -->
If your Lansweeper web console stops working for some reason or won't load at all, the first thing you should try is restarting the web server service that runs the console. Your web server service is either IIS Express or World Wide Web Publishing Service (IIS). If restarting the service in Windows Services does not resolve the issue, you can try reinstalling the console.

Reinstalling only the web console won't affect scanned data or settings, which are stored in a separate database hosted in either Microsoft SQL LocalDB or Microsoft SQL Server.

## Reinstall the web console

1. Determine which database server is hosting your Lansweeper database by using the ConfigEditor tool. You can follow the instructions in [this knowledge base article](/docs/identify-which-database-server-lansweeper-is-using).
2. If your Lansweeper database is hosted in SQL LocalDB or SQL Server and you never configured your own custom database password before, do so now by following the instructions in [this knowledge base article](/docs/change-the-lansweeper-database-password).
3. Stop your web server service in Windows Services. Your web server service is either **IIS Express** or **World Wide Web Publishing Service (IIS)**.  
   
4. If you added any documents, images or widgets to Lansweeper, create a backup of these files. Information on which website subfolders store which data can be found in [this knowledge base article](/docs/where-are-lansweeper-data-reports-and-settings-stored#heading2 "Where lansweeper data reports and settings are stored").  

   Do not back up the entire **Website** folder. Only back up the specific subfolders you need. Backing up and restoring the entire folder can lead to issues.
5. If it exists, create a backup copy of the Encryption file as well, which can be found at `Program Files (x86)\Lansweeper\Key\Encryption.txt`.
6. Download and run [the latest Lansweeper installer](https://www.lansweeper.com/install-lansweeper/).
7. Select **Next**, review the terms of use and tick **I accept the agreement**.
8. Select **New installation**, and then choose **Advanced install**.  
   
9. Tick **New Lansweeper Website** and, depending on which database server is hosting your database, tick **SQL LocalDB** or **SQL Server** as well.  
     

   Do not tick **New Lansweeper Database** or **New Lansweeper Service**. If you do, the Lansweeper database and/or service will be reinstalled as well. If you reinstall the database, all your scanned data and settings will be lost.
10. If your database is hosted in SQL Server, point the installer to your existing SQL instance and select **Next**. You can connect to the instance with the "lansweeperuser" SQL user and the database password you configured earlier.
11. Select the web server you'd like to install the console under. Selecting **Recommended** will install the web console under IIS Express, while selecting **Advanced** will install the web console under IIS. The Advanced option will only be available if IIS is already enabled on your computer. Instructions for enabling IIS can be found in [this knowledge base article](/docs/install-iis-internet-information-services).   
    You can choose a custom HTTP and (if offered by the installer) HTTPS port to install the web console under. If you don't choose custom ports, the installer will automatically select the first available ports for installation.   
    
12. You can choose a custom folder to install under. Select **Install** to start the installation process. The web console will be installed under the web server of your choice and your preferred ports. It will connect to the existing database server (SQL LocalDB or SQL Server) specified by you.  
    
13. Stop your web server service in Windows Services  
    
14. Restore the **Website** subfolders you need, and the Encryption.txt file you created a backup of earlier.
15. If your database is hosted in SQL LocalDB or SQL Server, run the ConfigEditor tool on your Lansweeper server and click through any warnings about your database password being incorrect. The tool can be found at `Program Files (x86)\Lansweeper\Tools\ConfigEditor.exe`.  
    
16. The web console reinstallation will have added a random password to the web console connection string. If your database is hosted in SQL LocalDB or SQL Server, change the database password in the **Website** tab to the one you configured earlier.  
    
17. Restart your web server service in Windows Services.  
    
