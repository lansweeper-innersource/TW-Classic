<!-- # Track Lansweeper Classic logins and setting changes -->
A record is kept of who logged into the Lansweeper web console and when, as well as who made changes to assets or Lansweeper settings and when. You can see who deleted an asset for instance or who submitted a network segment for scanning.

This record is automatically kept, though old entries are removed from the database on a scheduled basis, to prevent database growth.

## Review logs

1. Make sure your user role includes the **Access Configuration** permission. If it doesn't, you won't be able to view or configure Lansweeper login and configuration logs. More information on configuring website access and specifying who has what permissions can be found in [this knowledge base article](/docs/restrict-access-to-the-web-console).
2. Browse to the **Configuration > Server Options**section of the web console.  
   
3. Configure how long the logs are kept in the database in the **History Cleanup Options** section of the page.
   - The first cleanup option determines how quickly logs related to configuration and asset changes are removed from the database, specifically from the tblConfigLog database table.
   - The second cleanup option determines how quickly logs related to web console logins are removed from the database, specifically from the tblLoginLog table.  
     
4. Open the built-in reports below, found in the **Reports** menu.  
   - Users: Logins into the Lansweeper web console
   - Users: Changes made to Lansweeper configurationThe first report lists who logged into the Lansweeper web console and when, while the second report lists who made changes to assets or Lansweeper settings and when.
