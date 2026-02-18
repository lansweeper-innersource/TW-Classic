<!-- # Cloud requirement: database -->
The database cloud requirement was removed in Lansweeper 10.5.0.7. [Upgrade to the latest version](https://www.lansweeper.com/update-lansweeper/) of Lansweeper for the most up-to-date experience.

When you start setting up a link with your Cloud site, some prerequisite checks are performed to ensure your installation is ready to link. When you select **Link with Cloud site** in your local web console, a pop-up is presented with a pass/fail indication for a number of prerequisite checks. One of the checks is whether the setup and permissions of your local Lansweeper database are correct.

In addition to your database needing to be hosted on a compatible database server on a Windows machine, your database permissions must be correct in order for the link with Cloud to work.

## Why are the database rights checked?

When you first set up a link with Cloud, a backup is performed of your local Lansweeper database. This backup is what is initially synced with your Cloud site. After this initial sync, the database backup is removed and any further changes to your database are continuously synced up to Cloud as well.

In order for Lansweeper to create a backup of your database, the user used for your local database connection "lansweeperuser" must have **dbcreator** rights within your database instance. In order for Lansweeper to verify whether enough space is available for the database backup, the user must also have **VIEW SERVER STATE** rights within your database instance.   
In Lansweeper installations performed under the default SQL LocalDB database server, these rights are automatically granted.   
In installations performed under SQL Server, these rights are not automatically granted, and you must manually grant them.

You can remove the **dbcreator** and **VIEW SERVER STATE** rights from "lansweeperuser" once the initial push to Cloud has finished. These rights are only required for the initial sync, not the continuous sync with Cloud.

## What do I do if the database rights check fails?

Install SQL Server Management Studio if not already present on your machine. Log into the application with a user that has sysadmin rights, a user other than "lansweeperuser", and connect to your database instance.

If your database is hosted in SQL LocalDB, the SQL instance name you need to submit in Management Studio is "**(localdb)\.\LSInstance**" and you can log in with the Windows user that initially installed Lansweeper.   
If your database is hosted in SQL Server, you have configured your SQL instance name and password when you installed SQL Server. Once you're logged into SQL Server Management Studio, you can run the script below to grant "lansweeperuser" **dbcreator** and **VIEW SERVER STATE** rights.

```
/* Grant lansweeperuser dbcreator and view server state 
to be able to sync your database */
USE master;
GO
EXEC sp_addsrvrolemember [lansweeperuser], [dbcreator];
GO 
GRANT VIEW SERVER STATE TO [lansweeperuser];
GO
```

"lansweeperuser" is the default and only officially supported SQL user account to connect Lansweeper components to the Lansweeper database. While custom user accounts may technically work as well, they are not supported. "lansweeperuser" has a randomized password by default, [which you can customize if you want](/classic/docs/change-the-lansweeper-database-password).
