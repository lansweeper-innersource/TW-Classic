<!-- # Add a report to your Lansweeper installation -->
The [report library](https://www.lansweeper.com/report/) houses a vast amount of reports, ranging from network reports, to vulnerability reports or even [Patch Tuesday](https://www.lansweeper.com/blog/patch-tuesday/?category=1880) reports. If you find a SQL query in the report library that you would like to import into your own Lansweeper Classic installation, you can do so in just a few easy steps.

Lansweeper data, reports and settings are stored in a database. Your database is hosted in either the Microsoft SQL LocalDB, Microsoft SQL Server or (deprecated) Microsoft SQL Compact database server. Any built-in or custom Lansweeper reports are in fact SQL queries that are run on your SQL database.

## Import a SQL query as a report

1. Browse to the **Reports > Create New Report**section of the web console to open the report builder.  
   ![menu-reports-create-new-report.jpg](/docs/.document360/assets/article_149/image_002.jpg)
2. Replace the default SQL query at the bottom of the report builder with the one you want to import. The screenshot below shows what needs to be changed. Make sure to replace the entire SQL query with your own.  
   ![how-to-add-a-report-to-your-lansweeper-installation-1.jpg](/docs/.document360/assets/article_149/image_003.jpg)
3. Give your report a title in the report builder.  
   ![how-to-add-a-report-to-your-lansweeper-installation-2.jpg](/docs/.document360/assets/article_149/image_004.jpg)
4. Wait for your SQL query change to apply, if it hasn't already. You'll see the new query be applied in the upper section of the report builder, both in the visual representation of tables and in the expression list.
5. Select **Save & Run** to execute the report you just imported. The SQL query is now run on your database and the report results are displayed.  
   ![how-to-add-a-report-to-your-lansweeper-installation-3.jpg](/docs/.document360/assets/article_149/image_005.jpg)
6. After the report is run, you can:
   - Export the report results or perform other actions on the report.
   - Filter the report further within the report results, using the boxes above each column.
   - [Set up an alert for the report](/docs/send-report-and-event-log-alerts), so you are automatically notified of its results. The alert can automatically export the report results to a folder or send them via email to email addresses specified by you.  
     ![how-to-add-a-report-to-your-lansweeper-installation-4.jpg](/docs/.document360/assets/article_149/image_006.jpg)
