<!-- # Reset the ticket ID counter -->
Each ticket in the Lansweeper helpdesk has a numeric ID, listed next to the ticket title. If you're testing the helpdesk, you may at one point want to delete all of your test tickets and start over. If you do, you may notice that IDs previously assigned to other tickets are not reused. You can manually reset the ticket ID counter to a specific number, so new tickets start counting from that point onward. The exact procedure you should follow depends on whether your database is hosted in the Microsoft SQL LocalDB, Microsoft SQL Server or deprecated Microsoft SQL Compact database server. You can [verify which database server you are using](/classic/docs/identify-which-database-server-lansweeper-is-using) with the ConfigEditor tool or in the Lansweeper web console. 

## Reset the ticket ID counter if you are using SQL Compact

1. To be safe, back up your database first by following [these instructions](/classic/docs/back-up-your-installation#heading1 "Backing up your installation").
2. Delete any tickets you no longer need as explained in [this article](/classic/docs/delete-tickets-from-the-helpdesk).
3. If you are keeping some of your tickets, run the report below in the Lansweeper web console to determine what the highest remaining ticket ID in your Lansweeper database is. You can add this report to your installation by following [these instructions](/classic/docs/add-a-report-to-your-lansweeper-installation). Determining the highest remaining ticket ID is important so you know what you can reset the ticket ID counter to later on.  

   ```
   Select Max(htblticket.ticketid) As [Highest Ticket ID] From htblticket
   ```
4. Run the DatabaseMaintenance tool on your Lansweeper server, found at `Program Files (x86)\Lansweeper\Tools\DatabaseMaintenance.exe`. 
5. Replace "1000" in the script below with the ticket ID you want to start counting from, copy and paste the code into the **Script Execution** tab of the tool and select **Execute**.  

   ```
   ALTER TABLE htblticket ALTER COLUMN ticketid IDENTITY (1000, 1)
   ```

   If there are still tickets in your database, the ticket ID you submit in the script should be higher than the highest ticket ID currently in your database. Otherwise, the database will try to reuse existing IDs and generate errors, e.g. "ticket does not exist" or "duplicate value cannot be inserted into a unique index."
6. Restart your web server service in Windows Services. Keep in mind that this will log everyone out of the console. Your web server service is either IIS Express or World Wide Web Publishing Service (IIS).

## Reset the ticket ID counter if you are using SQL LocalDB or SQL Server

1. To be safe, back up your database first by following [these instructions](/classic/docs/back-up-your-installation#heading2 "Backing up your installation").
2. Delete any tickets you no longer as explained in [this article](/classic/docs/delete-tickets-from-the-helpdesk).
3. If you are keeping some of your tickets, run the report below in the Lansweeper web console to determine what the highest remaining ticket ID in your Lansweeper database is. You can add this report to your installation by following [these instructions](/classic/docs/add-a-report-to-your-lansweeper-installation). Determining the highest remaining ticket ID is important so you know what you can reset the ticket ID counter to later on.  

   ```
   Select Max(htblticket.ticketid) As [Highest Ticket ID] From htblticket
   ```
4. Run the DatabaseMaintenance tool on your Lansweeper server, found at `Program Files (x86)\Lansweeper\Tools\DatabaseMaintenance.exe`.
5. Replace "1000" in the script below with the ticket ID you want to start counting from, copy and paste the code into the **Script Execution** tab of the tool and select **Execute**.  

   ```
   DBCC CHECKIDENT (htblticket, RESEED, 1000)
   ```

   If there are still tickets in your database, the ticket ID you submit in the script should be higher than the highest ticket ID currently in your database. Otherwise, the database will try to reuse existing IDs and generate errors, e.g., "ticket does not exist" or "duplicate value cannot be inserted into a unique index."
6. Restart your web server service in Windows Services. Keep in mind that this will log everyone out of the console. Your web server service is either IIS Express or World Wide Web Publishing Service (IIS).
