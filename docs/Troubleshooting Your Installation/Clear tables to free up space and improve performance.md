<!-- # Clear tables to free up space and improve performance -->
![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_280/image_001.jpg) **This page explains how you can clear tables in your database to free up space or improve performance in general.**

In general, the cleanup options found in the web console under **Configuration > Server Options** should keep the size of your Lansweeper database within limits. Cleanups are performed when the Lansweeper Server service is started and subsequently every 24 hours. If you're scanning a lot of Windows data however, and storing a lot of historical information, a more radical cleanup of your Lansweeper database may be required.

If Lansweeper is using more memory, processor resources or disk space than desired, or if web console or service performance is not like it used to be, clearing some of your largest database tables is recommended. Databases hosted in SQL LocalDB and SQL Server Express are limited in size by Microsoft.

SQL Compact is no longer a supported database server for hosting Lansweeper. To learn how you to move to SQL LocalDB or SQL Server, see [Convert a deprecated SQL Compact database](/docs/convert-a-deprecated-sql-compact-database).

Uncontrolled database growth will negatively impact performance and may even cause you to reach your database server's built-in size limit, which in turn can lead to errors such as:

[Spoiler](#) (Highlight to read)

The database file is larger than the configured maximum database size. This setting takes effect on the first concurrent database connection only. [Required Max Database Size (in MB; 0 if unknown) = 4091]

Could not allocate space for object in database 'lansweeperdb' because the 'PRIMARY' filegroup is full. Create disk space by deleting unneeded files, dropping objects in the filegroup, adding additional files to the filegroup, or setting autogrowth on for existing files in the filegroup.

The database file is larger than the configured maximum database size. This setting takes effect on the first concurrent database connection only. [Required Max Database Size (in MB; 0 if unknown) = 4091]
Could not allocate space for object in database 'lansweeperdb' because the 'PRIMARY' filegroup is full. Create disk space by deleting unneeded files, dropping objects in the filegroup, adding additional files to the filegroup, or setting autogrowth on for existing files in the filegroup.
