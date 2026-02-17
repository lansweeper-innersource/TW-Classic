<!-- # Connect to a SQL Compact database with SQL Compact Toolbox -->
Lansweeper data, reports and settings are stored in a database. Your database is hosted in either the Microsoft SQL LocalDB, Microsoft SQL Server or (deprecated) Microsoft SQL Compact database server.

Though Lansweeper has a built-in report builder and a built-in tool for running database scripts, you may at some point want to connect to your database using an external tool. To connect to SQL LocalDB and SQL Server databases, Microsoft's SQL Server Management Studio can be used. To connect to a SQL Compact database, SQL Compact Toolbox can be used. This article explains how to view the raw data in your SQL Compact database using SQL Compact Toolbox. If you are unsure which database server you are using, you can [verify using the ConfigEditor tool or in the Lansweeper web console](/docs/identify-which-database-server-lansweeper-is-using).

  

Using SQL Compact Toolbox is unnecessary if your goal is to run a report or database script.   
Reports can be run in the Lansweeper web console under **Reports > Create New Report**.   
Scripts can be run in the following tool on your Lansweeper server: `Program Files (x86)\Lansweeper\Tools\DatabaseMaintenance.exe`.  
Please note that  you should only run scripts if requested by the Lansweeper support team

Keep in mind that, from March 2020 onward, SQL Compact is no longer a supported database server for hosting Lansweeper. We recommend [migrating SQL Compact databases to SQL LocalDB or SQL Server](/docs/convert-a-deprecated-sql-compact-database "Converting a deprecated SQL compact database").

1. Download SQL Compact 4.0 SP1 through [this download link](https://www.microsoft.com/en-us/download/details.aspx?id=30709 "SQL Server Compact") and install it on your Lansweeper server.  

   Don't skip this step. SQL Compact must be installed as a separate software on your Lansweeper server to connect to your database with the SQL Compact Toolbox later on.
2. Download the Standalone 4.0 daily build of SQL Compact Toolbox through [this download link](https://marketplace.visualstudio.com/items?itemName=ErikEJ.SQLServerCompactSQLiteToolbox "SQL Server Compact Toolbox") and unzip the file.  

   SQL Compact Toolbox is a third-party tool. The Lansweeper support team cannot troubleshoot potential issues with this tool.
3. Run the Toolbox executable as an administrator on your Lansweeper server.
4. Right-click **No SQL Server Compact Data Connections** **found** and choose **Add SQL Server Compact 4.0 Connection...**in the menu.  
   
5. Select **Browse...** in the resulting pop-up and select your Lansweeper database file. The default path of the file is `Program Files (x86)\Lansweeper\SQLData\lansweeperdb.sdf`.
6. Click the **Close** button in the pop-up window.
7. Expand the Lansweeper database so you can view and query database tables.  

   Do not make changes to data unless you have a deep understanding of [the Lansweeper database structure](/docs/access-lansweeper-database-documentation "Accessing the Lansweeper database") and SQL in general. Manual data changes are likely to break your Lansweeper installation. If you make changes or run a script, [back up your database](/docs/back-up-your-installation#heading1 "Backing up your installation") first.
