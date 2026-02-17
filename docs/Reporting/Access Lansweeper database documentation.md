<!-- # Access Lansweeper database documentation -->
Lansweeper data, reports and settings are stored in a database. Your database is hosted in either the Microsoft SQL LocalDB, Microsoft SQL Server or (deprecated) Microsoft SQL Compact database server.

As Lansweeper scans and stores a wealth of data, there are many database tables as well. Though there are hundreds of built-in reports in the **Reports** menu, you may at times want to create your own specialized SQL queries. The Lansweeper report builder is a standard SQL editor, so anyone with knowledge of SQL automatically knows how to use the report builder as well.

To help you locate the data you're after, the Lansweeper Classic software has documentation included that explains what each table and field stores.

More reports can be found [in the Report Library](https://www.lansweeper.com/report/).

## Access database documentation

1. Make sure your user role includes the **Edit Reports** permission, as this permission will be required both to access the database documentation and to actually create reports. More information on configuring website access and specifying who has what permissions can be found in [this knowledge base article](/docs/restrict-access-to-the-web-console).
2. Browse to the **Reports > Database Documentation**section of the web console.  
   ![menu-reports-database-documentation.jpg](/docs/.document360/assets/article_148/image_001.jpg)
3. On the resulting page with database documentation, click on a table to jump to that table's documentation.   
   Alternatively, use your web browser's search function (Ctrl+F) to search for specific terms within the documentation.  

   A table you'll likely want to include in any asset report is "tblAssets". This table stores basic asset details like name, IP address, type etc.   
   A table you'll likely want to include in any helpdesk ticket report is "htblticket". This table stores basic ticket details like ticket number, subject, type etc.

## Notes on the documentation

- A link to the database documentation is available within the report builder as well, next to the report title.
- The database contains tables that start with "htbl", "tbl" and "tsys".
  - The htbl tables generally store helpdesk data.
  - The tbl tables generally store asset data.
  - The tsys tables generally store Lansweeper settings. These tables are not documented as Lansweeper settings are generally not included in reports.
- The database contains tables that end in "Hist". These tables are not documented as they store historical Windows computer data. They are identical to their non-Hist counterparts, with the exception of the Action field.   
  A Windows computer's current OS is stored in tblOperatingsystem for instance, while OS changes are stored in tblOperatingsystemHist. The first table is documented, the second one isn't since it's largely the same as the first. History tracking is disabled by default for most scanned data. Information on enabling it and subsequently running reports can be found in [this knowledge base article](/docs/track-software-memory-and-other-changes-on-windows-computers).
