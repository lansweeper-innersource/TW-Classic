<!-- # ExecuteReader: CommandText property has not been initialized -->
If you install the Lansweeper database under Microsoft SQL Server or Microsoft SQL LocalDB, any built-in or custom reports seen in the **Reports** tab of the web console are added as views to your SQL instance. Report views are called "web40rep..." or "web50rep...".

If someone deletes report views from your SQL instance, or if your Lansweeper database is moved without moving the report views as well, you will encounter one of the errors below when opening the affected reports in the **Reports** tab of the web console. The exact error message depends on the Lansweeper version used. The name of the missing report view can be seen in the web console URL.

Error: ExecuteReader: CommandText property has not been initialized

![executereader-commandtext-property-has-not-been-initialized-1.jpg](/docs/.document360/assets/article_285/image_001.jpg)

Error: Report cannot be found

![executereader-commandtext-property-has-not-been-initialized-3.jpg](/docs/.document360/assets/article_285/image_002.jpg)

![executereader-commandtext-property-has-not-been-initialized-2.jpg](/docs/.document360/assets/article_285/image_003.jpg)

To resolve these errors and regain access to the affected reports, do one of the following:

- If you previously created one, restore a database backup that still contains the report views. More info on restoring database backups can be found in [this knowledge base article](/docs/restore-your-installation-from-a-backup#heading2 "Restoring your installation from a backup").
- If the reports were built-in, retrieve the faulty reports' original SQL queries from our report center and use these queries to recreate the reports in Lansweeper. [Our report center](https://community.lansweeper.com/t5/forums/filteredbylabelpage/board-id/Lansweeper_General_Forum/label-name/report%20center "Report Center") stores all built-in reports.  Instructions for importing a report from a SQL query can be found in [this knowledge base article](/docs/add-a-report-to-your-lansweeper-installation).
