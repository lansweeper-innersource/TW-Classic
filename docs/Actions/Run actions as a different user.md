<!-- # Run actions as a different user -->
Actions seen in the individual asset and user pages of the [Lansweeper](https://www.lansweeper.com/) web console are run in the security context of the user initiating the action. More specifically, the username and password combination of the user account your web browser is running under is used to execute the command.

This implies that if an action requires administrative privileges on the target machine, the user who opened the web browser and clicked on the action must have those administrative privileges on the target machine. Scanning credentials submitted in the **Scanning > Scanning Credentials** section of the web console are not used to run asset or user actions.

![running-actions-as-a-different-user-1.jpg](/docs/.document360/assets/article_006/image_002.jpg)

## Run an asset or user action as a different user

1. Run the browser you're accessing the Lansweeper web console with under that user. **Right-click** your browser shortcut and select **Run as different user**.  
   ![running-actions-as-a-different-user-2.jpg](/docs/.document360/assets/article_006/image_003.jpg)
2. Submit your username/password combination in the pop-up. Use the format NetBIOS domain name\username for domain users and .\username for local users.  
   ![running-actions-as-a-different-user-3.jpg](/docs/.document360/assets/article_006/image_004.jpg)
3. Browse to the **Configuration > Asset Pages** section of the Lansweeper web console and place the following around your action command, inserting your own username and action command into the syntax:  

   ```
   runas.exe /profile /env /user:<your user account> "<your action>"
   ```

   Use the format NetBIOS domain name\username for domain users and .\username for local users. The action will be run under the specified user.  
   ![menu-configuration-asset-pages.jpg](/docs/.document360/assets/article_006/image_005.jpg)  

   This changes the action path of the action you are running to include "runas.exe". Runas.exe is a tool built into Windows operating systems that can be used to run processes under different users.
