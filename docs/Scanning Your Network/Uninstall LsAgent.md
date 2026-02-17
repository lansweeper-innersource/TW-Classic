<!-- # Uninstall LsAgent -->
[Lansweeper](https://www.lansweeper.com/) includes several scanning methods to scan the assets in your network, both agent-based and agentless. One of our agent-based scanning methods is called LsAgent, which is a cross-platform scanning agent that can scan computers both inside and outside of your network. For an in-depth look at LsAgent, check out [Introduction to LsAgent](/docs/introduction-to-lsagent-for-windows-linux-and-mac).

However, you might want to uninstall LsAgent for a number of reasons: you may want to shift to agentless scanning instead, meaning LsAgent is no longer necessary, or perhaps you want to enjoy the [benefits](/docs/install-it-agent-discovery#benefits) of IT Agent Discovery.

You won’t lose any data when uninstalling LsAgent, as all data is sent to your scanning server and isn’t saved on the relay server.

## Uninstall LsAgent on Windows

1. Go to the \LansweeperAgent\ folder.
2. Run the uninstall.exe file.
3. In the pop-up, select **Yes**.
4. Select **Ok**.

LsAgent has now been uninstalled.

Alternatively, you can uninstall LsAgent from the web console.

1. In your web console, go to **Scanning > LsAgent Scanning**.
2. Tick the LsAgent assets you want to uninstall.
3. Select **Delete**.
4. In the pop-up, select **Yes**.

The next time the service is restarted, LsAgent will be uninstalled.

You can restart the LsAgent service manually by opening **Task Manager > Services**, and selecting **Restart** for the **LansweeperAgentService** service.

## Uninstall LsAgent on macOS

1. Go to the /Applications/LansweeperAgent folder.
2. Run the uninstall.app file.
3. In the pop-up, select **Yes**.
4. Select **Ok**.

LsAgent has now been uninstalled.

## Uninstall LsAgent on Linux

1. Open a terminal, and enter the following:  
   `$ sudo /opt/LansweeperAgent/uninstall`
2. Enter “**Y**” to uninstall LsAgent and all of its modules.

LsAgent has now been uninstalled.

Alternatively, you can uninstall LsAgent from the web console.

1. In your web console, go to **Scanning > LsAgent Scanning**.
2. Tick the LsAgent assets you want to uninstall.
3. Select **Delete**.
4. In the pop-up, select **Yes**.

The next time the service is restarted, LsAgent will be uninstalled.

You can restart the LsAgent service manually by opening a terminal and entering:   
`$ sudo systemctl restart ls-agent.service`
