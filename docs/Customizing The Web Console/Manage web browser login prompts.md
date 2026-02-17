<!-- # Manage web browser login prompts -->
By default, the Lansweeper Classic web console presents you with a login screen. On this screen, you can either log in to [Lansweeper](https://www.lansweeper.com/try/ "Lansweeper") with the built-in administrator or with a Windows user account and password. You can log in with a Windows user that exists locally on your Lansweeper server, a Windows user in your Lansweeper server's domain or a Windows user in a trusted domain.

If you enable authentication in your web server settings, the login screen disappears and the login process is handled by your web browser instead. You can have your web browser automatically log you in as your current Windows user or have it present a login prompt.



Whether your browser starts prompting you for a username and password depends on the web browser itself. Some browsers will by default prompt for credentials. Others will by default automatically log into the console as the currently logged on Windows user, a process that is often referred to as Single Sign-On or SSO. To enable or disable web browser login prompts, you will need to make changes to your browser configuration. This article contains configuration instructions for:

- Chromium Browsers (e.g. Google Chrome, Microsoft Edge, Opera)
- Mozilla Firefox

## Manage login prompts in Chromium Browsers

1. Check which web server your Lansweeper Classic web console is using by browsing to the **Configuration > Website settings**section of the console.  
   
2. Make sure your web server is properly configured. The knowledge base contains configuration instructions for [IIS Express](/docs/enable-authentication-in-iis-express) and [IIS](/docs/enable-authentication-in-iis).
   - If you want the web console to present you with the default login screen, disable authentication in your web server settings.
   - If you want your web browser to either automatically log you in or present you with a login prompt, enable authentication in your web server settings.
3. In the Start menu, search for and select **Internet Options**.  
   
4. In the **Security**tab, select **Trusted sites** and click **Sites**.  
   
5. Submit your web console's URL in the upper input box, select **Add** and then **Close**. Web console URLs are generally formatted as follows:

   **http://<IP address or name of the machine hosting your web console>:<port number>/  
   **
6. Select **Custom level...**   
   
7. Enable **Prompt for user name and password** to have the browser prompt for credentials.   
   Enable **Automatic log-on with current username and password** to have the browser automatically log in as the currently logged on Windows user.  
   
8. Restart your browser. To ensure that your browser is fully stopped before restarting, you can open Windows Task Manager (Ctrl+Shift+Esc), right-click the browser's process(es) under **Processes** and select **End Process**.

## Manage login prompts in Mozilla Firefox

1. Check which web server your Lansweeper web console is using by browsing to the **Configuration > Website settings**section of the console.  
   
2. Make sure your web server is properly configured. The knowledge base contains configuration instructions for [IIS Express](/docs/enable-authentication-in-iis-express) and [IIS](/docs/enable-authentication-in-iis).
   - If you want the web console to present you with the default login screen, disable authentication in your web server settings.
   - If you want your web browser to either automatically log you in or present you with a login prompt, enable authentication in your web server settings.
3. Open Firefox, type "about:config" into the address bar and select Enter.
4. Firefox will warn you that incorrectly editing your settings can lead to stability, security and performance issues. Select **Accept the Risk and Continue**.  
   
5. Search for "network.automatic-ntlm-auth.trusted-uris" in the available search bar.  
     
   - Remove your Lansweeper Classic web console's URL to have Firefox prompt for credentials.
   - Add your console's URL to have Firefox automatically log in as the currently logged on Windows user. If you already disabled prompts for another website, you can use a comma separated list to add the Lansweeper Classic web console. Web console URLs are generally formatted as follows:

     **http://<IP address or name of the machine hosting your web console>:<port number>/**
6. Restart Firefox. To ensure that Firefox is fully stopped before restarting, you can open Windows Task Manager (Ctrl+Shift+Esc), right-click the firefox.exe process(es) under **Processes** and select **End Process**.
