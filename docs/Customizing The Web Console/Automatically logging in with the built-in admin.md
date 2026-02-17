<!-- # Automatically logging in with the built-in admin -->
From Lansweeper 9.1 onward, it is for security reasons no longer possible to automatically log into the web console with the built-in admin. If you are using Lansweeper 9.1 or higher, the instructions below will no longer work.

When you access the Lansweeper web console for the first time, you are presented with a First Run Wizard, which allows you to set up scanning and configure some basic options. The First Run Wizard is only meant for submitting an initial configuration. You only see and need to configure this wizard once. Any subsequent times you access the console, you are presented with a login screen and are asked to log in first.

By default, everyone in your network can access all of Lansweeper's features and menus simply by browsing to the web console URL and selecting **Built-in Admin**. You can also restrict access to the console to certain Windows users and configure what those users can see or do once they've been granted access. Info on restricting web console access can be found in [this knowledge base article](/docs/restrict-access-to-the-web-console). As explained in the last step of the aforementioned article, it is possible to have your browser automatically log you into the console with the Windows user account currently logged into your computer.

If you do not want to restrict access to the console however, it is also possible to automatically log in with the built-in admin. The procedure for this is explained below.

To automatically log into the console with the built-in admin and skip the login screen:

1. Take your main web console URL. On the machine hosting your Lansweeper installation, you can use the shortcut that was placed on your desktop and in your Start menu to access the web console.   
   In the example below, our main web console URL is <http://LAN-001:81/>.  
   ![automatically-logging-in-with-the-built-in-admin-1.jpg](/docs/.document360/assets/article_031/image_001.jpg)
2. Add "/login.aspx?admin=1" after the port number in the URL.
3. Browse to the new URL, which will automatically log you in with the built-in admin account. You won't have to manually select **Built-in Admin** in the login screen. In our example, the URL we browse to is <http://LAN-001:81/login.aspx?admin=1>.  
   ![automatically-logging-in-with-the-built-in-admin-2.jpg](/docs/.document360/assets/article_031/image_002.jpg)
