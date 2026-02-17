<!-- # Enable authentication in IIS -->
By default, everyone in your network has access to the Lansweeper Classic web console. Access can also be restricted however, by following [these instructions](/docs/restrict-access-to-the-web-console).

To have your browser handle authentication of anyone accessing the console, you will need to make changes to your web server settings. Your web server is either IIS or IIS Express. If you're unsure which web server you're using, have a look at the **Configuration > Website Settings** section of the Lansweeper Classic console.

This article explains how to enable authentication under IIS.

If you have your browser handle authentication, you may be prompted for a username and password whenever you open the web console. Login prompts are browser specific. Some browsers will, by default, prompt for credentials. Others will, by default, automatically log into the console as the currently logged on Windows user. To enable or disable prompts, follow the instructions in [this knowledge base article](/docs/manage-web-browser-login-prompts).

## Enable authentication in IIS 6.0

If your web console is hosted in IIS 6.0, do the following to enable authentication in your web server settings:

1. On the machine hosting your web console, open the Start menu and select **Run**.
2. In the input box, enter "inetmgr" and select **Ok**. IIS Manager will open.  
   ![enabling-authentication-in-iis-1.jpg](/docs/.document360/assets/article_036/image_001.jpg)
3. Right-click your web console on the left under `<name of the machine>\Web Sites` and select **Properties**.  
   ![enabling-authentication-in-iis-2.jpg](/docs/.document360/assets/article_036/image_002.jpg)
4. Open the **Directory Security** tab and select the upper **Edit...** button.  
   ![enabling-authentication-in-iis-3.jpg](/docs/.document360/assets/article_036/image_003.jpg)
5. Uncheck **Enable anonymous access**, check **Integrated Windows authentication** and select **OK** twice.  
   ![enabling-authentication-in-iis-4.jpg](/docs/.document360/assets/article_036/image_004.jpg)

## Enable authentication in IIS 7.0, 7.5, 8.0 or 8.5

If your web console is hosted in IIS 7.0, 7.5, 8.0 or 8.5, do the following to enable authentication in your web server settings:

1. On the machine hosting your web console, open the Start menu and select **Run**.
2. In the input box, enter "inetmgr" and select **OK**. IIS Manager will open.  
   ![enabling-authentication-in-iis-5.jpg](/docs/.document360/assets/article_036/image_005.jpg)
3. Select your web console on the left under `<name of the machine>\Sites` and double-click the **Authentication** button.  
   ![enabling-authentication-in-iis-6.jpg](/docs/.document360/assets/article_036/image_006.jpg)
4. Right-click **Anonymous Authentication** and choose **Disable**, right-click **Windows Authentication** and choose **Enable**.  
   ![enabling-authentication-in-iis-7.jpg](/docs/.document360/assets/article_036/image_007.jpg)
5. If your console is hosted on a machine running a non-Server OS and you don't see the **Windows Authentication** option, open the Start menu and select **Run**.
6. In the input box, enter "optionalfeatures" and select **OK**. Windows Features will open.
7. Make sure that the following setting is enabled and select **OK**: Internet Information Services\World Wide Web Services\Security\Windows Authentication  
   ![enabling-authentication-in-iis-8.jpg](/docs/.document360/assets/article_036/image_008.jpg)
