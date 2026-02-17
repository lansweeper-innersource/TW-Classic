<!-- # A potentially dangerous Request .Form value was detected from the client -->
Both the scanning service and web console have a configuration file, which stores information on which Lansweeper database to connect to. If the "httpRuntime" tag is missing from your web console configuration file, you may encounter errors similar to the one below when trying to create a new ticket in the help desk.

![potentially-dangerous-requestform-value-detected-from-the-client-1.jpg](/docs/.document360/assets/article_278/image_001.jpg)

To resolve this issue, follow these steps:

1. In **Windows Services** on the machine hosting your web console, stop the web server service running the console. Keep in mind that this will log everyone out of the console. Your web server service is either IIS Express or World Wide Web Publishing Service (IIS).   
   If you're unsure which web server your console is running under, browse to the following section of the web console and check the **WebServer** field: **Configuration > Website Settings**

   ![procedure-stopping-the-web-server-service.jpg](/docs/.document360/assets/article_278/image_002.jpg)
2. Open the following file with Notepad or another text editor: `Program Files (x86)\Lansweeper\Website\web.config`.
3. Add the line below in the location shown in the screenshot below and save your changes.

   ```
   <httpRuntime requestValidationMode="2.0" maxRequestLength="201900" executionTimeout="600" />
   ```

   ![potentially-dangerous-requestform-value-detected-from-the-client-2.jpg](/docs/.document360/assets/article_278/image_003.jpg)
4. Restart the web server service in **Windows Services**.
5. Refresh any web browser tabs where the web console is currently open.
