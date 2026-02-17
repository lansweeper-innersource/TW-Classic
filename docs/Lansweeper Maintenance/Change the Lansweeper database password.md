<!-- # Change the Lansweeper database password -->
If you install the Lansweeper database under Microsoft SQL LocalDB or Microsoft SQL Server, the Lansweeper installer automatically creates a SQL user that is used by the Lansweeper scanning service and web console to connect to the database. The default SQL user is lansweeperuser.

From Lansweeper version 6.0.100.0 onward, a random password is generated for lansweeperuser. For security reasons, this password is not displayed anywhere, so you may want to update it to a custom password of your choice if you intend to connect external tools to the Lansweeper database.

Only Lansweeper databases installed under SQL LocalDB or SQL Server have a password. Databases hosted under the deprecated Microsoft SQL Compact database server can only be queried by services running locally on your Lansweeper server and do not have a user account or password.

1. Stop the **Lansweeper Server** service in Windows Services.  
   ![procedure-stopping-the-lansweeper-service.jpg](/docs/.document360/assets/article_094/image_001.jpg)
2. Stop your web server service in Windows Services. Keep in mind that this will log everyone out of the console. Your web server service is either **IIS Express** or **World Wide Web Publishing Service** (IIS). If you're unsure which web server your console is running under, browse to the **Configuration > Website Settings**section of the web console and check the WebServer field.  
   ![procedure-stopping-the-web-server-service.jpg](/docs/.document360/assets/article_094/image_002.jpg)
3. Open SQL Server Management Studio. If SQL Server Management Studio isn't installed on your Lansweeper server, we recommend downloading it online.  

   If your database is hosted in SQL LocalDB, the SQL instance name you need to submit in Management Studio is (localdb)\.\LSInstance and you can log in with the Windows user that initially installed Lansweeper. If your database is hosted in SQL Server, you would have configured your SQL instance name and password when you installed SQL Server.
4. Right-click the lansweeperuser database user under **Security > Logins** and select **Properties**.  
   ![changing-the-lansweeper-database-password-1.jpg](/docs/.document360/assets/article_094/image_003.jpg)
5. Submit your new password twice in the available fields and select **OK**.  
   ![changing-the-lansweeper-database-password-2.jpg](/docs/.document360/assets/article_094/image_004.jpg)  

   Do not submit "mysecretpassword0\*" or "Mysecretpassword0\*" as your new database password. These were the default database passwords in old Lansweeper releases and are no longer accepted as valid by Lansweeper.
6. Run the ConfigEditor tool found at `Program Files (x86)\Lansweeper\Tools\ConfigEditor.exe` on the server(s) hosting your Lansweeper Server service and web console.  
   ![menu-configeditor.jpg](/docs/.document360/assets/article_094/image_005.jpg)
7. Click through any warnings the tool may be giving you about your password being incorrect.
8. Select the Password field and select **Edit**.![procedure-configeditor-service-password-change.jpg](/docs/.document360/assets/article_094/image_006.jpg)
9. Submit the same password you previously submitted in SQL Server Management Studio and select **Save**.
10. If the ConfigEditor tool has multiple tabs due to your server hosting multiple Lansweeper components, select the other tab, click through any warnings and repeat the password changing process.  
    ![procedure-configeditor-website-password-change.jpg](/docs/.document360/assets/article_094/image_007.jpg)
11. Restart the Lansweeper and web server services in Windows Services.  
    **![procedure-starting-the-web-server-service.jpg](/docs/.document360/assets/article_094/image_008.jpg)**
12. If you have multiple scanning servers, update the database password on those servers as well by stopping the Lansweeper service, using the ConfigEditor tool and restarting the service.
