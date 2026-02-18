<!-- # Socket errors when scanning with the LsPush scanning agent -->

You may encounter errors if you attempt to send [LsPush](/classic/docs/introduction-to-the-lspush-scanning-agent-for-windows "Introduction to the LsPush scanning agent for Windows") data directly to your Lansweeper server and the connection fails.

When you include `/showresult`  in your LsPush command, the following errors may be displayed in a pop-up window:

- Socket Error # 11001
- Socket Error # 10013
- Socket Error # 10061
- Connection refused
- Connection to server failed
- Connect timed out
- Host not found



These instructions resolve socket errors that might have occurred when sending LsPush data directly to your Lansweeper server for import. LsPush can be run other ways as well. For more information, see [Introduction to the LsPush scanning agent for Windows](/classic/docs/introduction-to-the-lspush-scanning-agent-for-windows "Introduction to the LsPush scanning agent for Windows").

To resolve socket errors:

## Update Lansweeper

1. In the web console, go to **Configuration > Your Lansweeper license**.
2. Select **Check for updates now**.
3. If your Lansweeper installation is outdated, select **Download now** to update your installation.

## Use the latest LsPush executable

When you update your Lansweeper installation, the latest version of the LsPush executable is also updated. If you are using a logon script, group policy, or scheduled task:

1. In **File explorer**, navigate to **Program Files (x86)\Lansweeper\Client**.
2. Copy **lspush.exe** to your clipboard.
3. Paste the executable to the folder referenced by your script, policy, or task.  
   

## Ensure your LsPush command is correct

Your LsPush socket errors may result from pointing to the wrong server. Your LsPush command should include the up-to-date name or IP address of your Lansweeper scanning server. For more information, see [What parameters LsPush accepts](/classic/docs/introduction-to-the-lspush-scanning-agent-for-windows#heading6 "Introduction to the LsPush scanning agent for Windows").

## Ensure the Lansweeper Server service is running

By default, the Lansweeper Server service automatically starts and scans your data. However, it may have been manually stopped, meaning no LsPush data can be imported or processed.

1. Navigate to **Windows Services**.
2. Locate and right-click **Lansweeper Server** from the list.
3. If the server has stopped, select **Start**.  

   

## Verify your listen port

By default, the listen port is 9524. To verify what port is used:

1. In the web console, go to Scanning > Server options > Service options.
2. If the listen port is not port 9524, ensure your LsPush command includes the listen port.   
   For example, when sending data to scanning server LAN-001 over custom listen port 9500, the command is: `lspush.exe LAN-001 9500 /showresult`.

## Ensure inbound traffic is allowed

When you install Lansweeper, rules are automatically added to Windows Firewall on your Lansweeper server to allow inbound traffic over listen port 9524. If you use another listen port or firewall, you must manually configure your firewall to allow traffic over the appropriate port.



## Ensure outbound traffic is allowed

By default, Windows Firewall does not block outbound connections. However, if you use a custom firewall or custom firewall configuration, outbound traffic might be blocked and you might need to reconfigure your firewall.


