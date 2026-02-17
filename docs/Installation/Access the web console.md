<!-- # Access the web console -->
![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_071/image_001.jpg) **This page explains how you can access and log in to the Lansweeper On-premises web console.**

Once you've installed Lansweeper, you can access the web console. The web console displays scanned and custom data in a comprehensible way.

Additionally, it allows you to make changes to your settings. By default, everyone in your network has access to the web console and can log in with minimal permissions to just the help desk. [Access can also be restricted](/docs/restrict-access-to-the-web-console), however.

## Access the web console

To access the web console:

- On the machine hosting the web console, use the **Lansweeper Web Console** shortcut that was copied to your desktop and Start menu during installation.![accessing-the-web-console-1.jpg](/docs/.document360/assets/article_071/image_002.jpg)  
    
  Alternatively, submit the web console URL directly in your browser's address bar. On the machine hosting the web console, you can use **localhost** in the URL. Unless you're using port 81, the port number specified during installation should be included in the URL as well: `http://localhost:<port number>/`   
    
  ![accessing-the-web-console-2.jpg](/docs/.document360/assets/article_071/image_003.jpg)
- From a machine other than the one hosting the console, submit the complete web console URL in your browser's address bar. **localhost** should be replaced with the IP address or name of the machine hosting the console. Unless you're using port 81, the port number specified during installation should be included in the URL as well. Access to this port on the web server should also be allowed in any firewalls you may be using. Web console URLs are formatted as follows: `http://<IP address or name of the machine hosting your web console>:<port number>/`  
    
  ![accessing-the-web-console-3.jpg](/docs/.document360/assets/article_071/image_004.jpg)

## Log into the web console

When you access the console for the first time, you are presented with a [First Run Wizard](/docs/install-lansweeper-on-prem#FRW), which allows you to set up scanning and configure some basic options.

The First Run Wizard is only meant for submitting an initial configuration. You'll only see and need to configure this wizard once. After completing this setup, you will be prompted to log in the next time you want to access the console.

There are several login options available to you.

### Built-in admin

If you have previously configured a username and password for the built-in admin, you will need to submit these details before clicking the button.

Use the built-in admin option if you have not yet configured website access, as it provides full access to all areas of the web console. For security reasons, we recommend disabling the built-in admin after completing your initial configuration.

### Windows username and password

Submit a Windows username and password, then select **Windows Login**.

Use this option once you’ve configured website access and specified who has permission to access various areas of the console. If you haven’t configured website access yet and select **Windows Login**, your permissions will be limited, and you will only be able to access the Help Desk section to submit your own tickets.

### Domain login

If your Lansweeper installation is on a domain computer, you can log in using any domain user. Submit the user in the format: `NetBIOS domain name\username`.

### Workgroup login

If your Lansweeper installation is on a workgroup computer, you can use any Windows user configured on the computer hosting the console to log in. Submit the user in the format: `.\username`.

![web-console-login-screen.jpg](/docs/.document360/assets/article_071/image_005.jpg)
