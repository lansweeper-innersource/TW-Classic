<!-- # How to use the ConfigEditor tool -->
Lansweeper data, reports and settings are stored in a database. Your database is hosted in either the Microsoft SQL LocalDB, Microsoft SQL Server or (deprecated) Microsoft SQL Compact database server. Apart from a database, your installation also includes a Lansweeper Server service that scans your network and a web console that displays scanned data and settings. Both the Lansweeper Classic service and web console connect to the database and know which database to connect to because of two configuration files stored on your Lansweeper server, one for the scanning service and one for the web console. More information on the interaction between Lansweeper components can be found in [this knowledge base article](/classic/docs/lansweeper-classic-components-and-architecture).

To improve security, from Lansweeper 6.0.100.0 onward, the database connection details in the aforementioned configuration files are obfuscated and no longer displayed in plain text. Databases hosted in SQL LocalDB or SQL Server have a password, but this password is no longer visible in the configuration files or anywhere else.

If you need to make changes to your password or other details in the database connection string, you'll now need to do so by making use of the ConfigEditor tool found at `Program Files (x86)\Lansweeper\Tools\ConfigEditor.exe` on your Lansweeper server.  


This is a short summary of the various sections of the tool:

- If your scanning service and web console are hosted on the same machine, you'll see two tabs in ConfigEditor, one for each component. In each tab, you can specify which database the component connects to. Ordinarily, both components should be connecting to the same database, with the same username and password.

  
- You can specify which database the component connects to in the **ConnectionString** section. If your database is hosted in the deprecated SQL Compact database server, your connection string is just a reference to an .sdf file. If your database is hosted in SQL LocalDB or SQL Server though, your connection string consists of a Data Source (SQL instance name), Initial Catalog (Lansweeper database name), username and password.   
  You can redirect the scanning service and web console to a different database or have them use a different password for the connection by selecting part of the connection string and selecting **Edit**.

    

  If you change the database password, you'll need to change it in SQL LocalDB or SQL Server first. [This knowledge base article](/classic/docs/change-the-lansweeper-database-password) explains in more detail how to update the Lansweeper database password.
- You can change additional settings of the scanning service and web console in the **appSettings** section. In general, you don't need to touch these settings. You may want to change certain settings like debug mode however if you are trying to identify database or other issues or if asked to by the Lansweeper support team for troubleshooting purposes. You can even import debug settings provided by the Lansweeper support team under the **Advanced > Import appSettings** menu of the ConfigEditor tool.

  
- In each tab, you'll find the **Save** button, **Save configs and restart service** button and **Export** button. Changing settings in the ConfigEditor requires that you restart the scanning and web server services. The **Save**button saves your setting changes but requires you to manually restart the services. The **Save configs and restart service**button saves your setting changes and automatically restarts the Lansweeper Server service (scanning service) for you. The web service must still be manually restarted. The **Export**button is one you'll really only use when asked to by the Lansweeper support team. It exports the database connection strings of scanning service and web console, except for the database password, so this can be used for troubleshooting database connection failures.

  
