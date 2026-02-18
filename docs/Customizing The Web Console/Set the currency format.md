<!-- # Set the currency format -->
The currency used throughout the web console, e.g. in the license compliance modules and for custom currency fields, can be customized by modifying the configuration file of the console.

To change the web console's currency format:

1. In Windows Services on the machine hosting your web console, stop the web server service running the console. Keep in mind that this will log everyone out of the console.   
     

   Your web server service is either IIS Express or World Wide Web Publishing Service (IIS). If you're unsure which web server your console is running under, browse to the **Configuration > Website Settings**section of the web console and check the WebServer field.
2. Copy the line below and replace "en-US" with your preferred culture. The website culture determines the currency format or symbol used in the console.  

   ```
   <globalization culture ="en-US"/>
   ```

   Some common currencies and their culture values are listed below, but a complete list of culture values can be found in [this knowledge base article](/classic/docs/list-of-currency-culture-codes).   
   $ = en-US   
   £ = en-GB   
   € = de-DE   
   ₹ = hi-IN   
   ¥ = ja-JP
3. Open the Web.config file at `Program Files (x86)\Lansweeper\Website\web.config` with Notepad or another text editor.
4. Add the line you previously copied in the location shown in the screenshot below and save your changes.  
   
5. Restart the web server service in Windows Services.
6. Refresh any web browser tabs where the web console is currently open. You should see the new currency format being used.
