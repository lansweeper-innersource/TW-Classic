<!-- # Locked out of the web console -->
If you perform a new [Lansweeper](https://www.lansweeper.com/) installation, you are presented with a First Run Wizard upon accessing the web console for the first time. Any subsequent times you access the console, you are presented with a login screen.

By default, you can log in with full access to all areas of the web console by browsing to the web console URL and using the Built-in Admin user that you configured in the First Run Wizard. Website access can also be restricted however, by following [these instructions](/classic/docs/restrict-access-to-the-web-console).

Should you accidentally lock yourself out of certain parts of the web console (e.g. the **Configuration** tab) or the web console entirely:

1. Make sure authentication is disabled in your web server settings. The exact procedure you should follow to disable authentication depends on the web server you are using.
   - If you are using the default IIS Express web server, run the ExpressAuthentication tool on your Lansweeper server, choose **Anonymous Access** and click the **Change** button.

     `Program Files (x86)\Lansweeper\IISexpress\ExpressAuthentication.exe`
   - If you are using the IIS web server, run the IIS Manager (inetmgr) tool on your Lansweeper server, select your Lansweeper website on the left and go to the **Authentication** menu. Right-click **Anonymous Authentication** and choose **Enable**, right-click **Windows Authentication** and choose **Disable**.
   - If you are using the old UltiDev web server, which is no longer offered in our installer, run the UWS.Explorer tool on your Lansweeper server, select your Lansweeper website on the left and then the **Authentication** tab. Choose **Anonymous** under **Authentication Types** and select Save **Config Changes** button.

     `Program Files (x86)\UltiDev\Web Server\UWS.Explorer.exe`
2. Run the ResetWebUserRoles tool on your Lansweeper server and select **Enable Built-in Administrator**. When enabling the Built-in Administrator account again, you will be asked to provide a username and password for the account.

   `Program Files (x86)\Lansweeper\Service\ResetWebUserRoles.exe`

   
3. Restart your web browser. You should see the login screen now when browsing to the Lansweeper web console. If you submit your built-in admin username and password and select **Built-in Admin**, you are logged in with full access to all areas of the web console.

   
