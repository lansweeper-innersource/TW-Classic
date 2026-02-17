<!-- # Enable authentication in IIS Express -->
By default, everyone in your network has access to the Lansweeper Classic web console. Access can also be restricted however, by following [these instructions](/docs/restrict-access-to-the-web-console).

To have your browser handle authentication of anyone accessing the console, you will need to make changes to your web server settings. Your web server is either IIS or IIS Express. If you're unsure which web server you're using, have a look at the **Configuration > Website Settings** section of the Lansweeper Classic console.

If you have your browser handle authentication, you may be prompted for a username and password whenever you open the web console. Login prompts are browser specific. Some browsers will, by default, prompt for credentials. Others will, by default, automatically log into the console as the currently logged on Windows user. To enable or disable prompts, follow the instructions in [this knowledge base article](/docs/manage-web-browser-login-prompts).

## Enable authentication in IIS Express

If your web console is hosted in IIS Express, do the following to enable authentication in your web server settings:

1. Right-click the ExpressAuthentication.exe executable, found at `Program Files (x86)\Lansweeper\IISexpress\ExpressAuthentication.exe` on the machine hosting your console, and select **Run** as administrator.  
   ![enabling-authentication-in-iis-express-1.jpg](/docs/.document360/assets/article_037/image_002.jpg)  

   If you don't run the executable as an administrator, it may be unable to make changes to your IIS Express configuration file and Windows may throw the following generic permissions error: **Unhandled exception has occurred in your application**.   
   If you select **Continue**, the application will ignore this error and attempt to continue.   
   If you select **Quit**, the application will close immediately. Access to the path `C:\Program Files (x86)\Lansweeper\IISexpress\iisexpress.config` is denied.
2. Select **Integrated authentication** and select **Change**. Keep in mind that this will log everyone out of the console.  
   ![enabling-authentication-in-iis-express-2.jpg](/docs/.document360/assets/article_037/image_003.jpg)
