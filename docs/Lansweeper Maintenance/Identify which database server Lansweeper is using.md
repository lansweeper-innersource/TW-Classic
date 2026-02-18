<!-- # Identify which database server Lansweeper is using -->
Most of the data scanned by Lansweeper and manually submitted in the web console is stored in the Lansweeper database. Your database is hosted in either the Microsoft SQL LocalDB, Microsoft SQL Server or (deprecated) Microsoft SQL Compact database server. You would have selected your preferred database server [when you installed Lansweeper](/classic/docs/install-lansweeper-on-prem).

If you installed Lansweeper and are unsure which database server your Lansweeper installation is using, this article explains how to identify it.

## Identify your Lansweeper database server using ConfigEditor

One way to identify your Lansweeper database server is using the ConfigEditor.exe tool on your Lansweeper server. This tool can be found in the `Program Files (x86)\Lansweeper\Tools` folder on your Lansweeper server. To identify your database server, run the tool and examine the Data Source listed in the **ConnectionString** section.

Below are some screenshots showing possible data source values. If your data source is:

- `|DataDirectory|\lansweeperdb.sdf`, your database server is SQL Compact.   
  SQL Compact is no longer supported or offered as a database server option for Lansweeper. If you are still using SQL Compact as your Lansweeper database server, you should [convert your database to SQL LocalDB or SQL Server](/classic/docs/convert-a-deprecated-sql-compact-database).  
  
- `(localdb)\.\LSInstance`, your database server is SQL LocalDB.  
  
- Something else, your database server is SQL Server.   
  If you have an unnamed SQL Server instance, your data source is simply the name of the server hosting your database. If you have a named SQL Server instance, your data source is the name of your server followed by the instance name specified during SQL Server installation.  
  

## View your database server using the web console

Another way to identify your Lansweeper database server is by browsing to the `Configuration\Your Lansweeper License` section of the Lansweeper web console. Examine the `Current Database` listed on the page. Below are some screenshots showing possible database values. If your database is listed as:

- `SQL Compact`, your database server is SQL Compact.   
  SQL Compact is no longer supported or offered as a database server option for Lansweeper. If you are still using SQL Compact as your Lansweeper database server, you should [convert your database to SQL LocalDB or SQL Server](/classic/docs/convert-a-deprecated-sql-compact-database).  
  
- `SQL Server: (localdb)\.\LSInstance`, your database server is SQL LocalDB.   
  SQL LocalDB is derived from SQL Server Express, which is why it's prefaced by *SQL Server*.  
  
- `SQL Server` followed by something other than `(localdb)\.\LSInstance`, your database server is SQL Server.  
  If you have an unnamed SQL Server instance, SQL Server is followed by the name of the server hosting your database. If you have a named SQL Server instance, SQL Server is followed by the name of the server and the instance name specified during SQL Server installation.  
  
