<!-- # Scan Windows computers with LsPush in a group policy -->
[Lansweeper](https://www.lansweeper.com/ "Lansweeper") includes several scanning methods to scan the assets in your network. You can scan the Linux, Unix, Mac and Windows computers, VMware servers and other devices in your network without installing any Lansweeper software on the machines you're scanning.

For Windows computers, however, you can choose to perform your scans with a scanning agent. Lansweeper's scanning agent is called LsPush. One of the ways it can be implemented is by using a scheduled task. LsPush is a small executable that scans the computer locally when run on a Windows computer. LsPush cannot and does not need to be installed on the computer you're scanning. The LsPush executable must simply be executed on the computer whenever you want to scan the machine. The LsPush scan results can be sent directly to your Lansweeper server for automatic processing or stored in a file that can be imported into your Lansweeper installation later on.

There are many ways to run LsPush on your machines. Any process that can run the LsPush executable, preferably with a parameter, can trigger LsPush scans of your machines. For instance, LsPush scans can be fully automated by integrating the scanning agent into logon scripts, group policies, or scheduled tasks.  
This article explains how to scan Windows computers with the LsPush agent in a group policy and have the scan results automatically sent back to your Lansweeper server. This scanning approach allows you to scan your domain computers as soon as users log into them.

This article only explains how to scan Windows computers with the LsPush scanning agent in a group policy, so domain computers are scanned as soon as users log into them. There are many other methods to run LsPush on one or more machines in your network. In a workgroup environment, LsPush can be deployed with a scheduled task for instance. A list of other ways to run LsPush can be found in [this knowledge base article](/docs/introduction-to-the-lspush-scanning-agent-for-windows).

## Scanning with LsPush in a group policy

To scan Windows computers with the LsPush scanning agent in a group policy, follow these steps:

1. On the machine hosting your Lansweeper installation, browse to `Program Files (x86)\Lansweeper\Client` and copy the LsPush executable contained within.

   ![file-lspush.jpg](/docs/.document360/assets/article_239/image_002.jpg)

   When you update your Lansweeper installation, the latest version of the LsPush executable is automatically added to the Client folder on your Lansweeper server. Make sure to use the latest LsPush executable to scan your machines, as scanning with old agents can cause incomplete data to be returned. If you have just updated Lansweeper and are scanning with LsPush in a logon script, group policy or scheduled task, copy the up-to-date LsPush to any folder referenced by your script, policy or task.
2. On one of the domain controllers in your domain, paste the LsPush executable into the `%logonserver%\netlogon` folder.

   ![how-to-scan-windows-computers-with-the-lspush-scanning-agent-in-a-group-policy-1.jpg](/docs/.document360/assets/article_239/image_003.jpg)
3. For testing purposes, open Command Prompt on a computer you want to scan and run the command below, replacing `LansweeperServer` with the name of your Lansweeper scanning server, i.e. a server hosting the Lansweeper Server service.   
   This command triggers a local scan of the computer and sends the scan results directly to your Lansweeper server for import. After a short while, you will receive visual feedback in a pop-up window indicating whether the connection to the Lansweeper server succeeded. This test is just to confirm the command works prior to implementing it in a group policy.

   ```
   "%logonserver%\netlogon\LsPush.exe" LansweeperServer /showresult
   ```

   ![how-to-scan-windows-computers-with-the-lspush-scanning-agent-in-a-group-policy-2.jpg](/docs/.document360/assets/article_239/image_004.jpg)

   By default, LsPush traffic is sent to port 9524 on your Lansweeper server. If the test above does not succeed, make sure incoming traffic over port 9524 is allowed in your Lansweeper server's firewall settings.
4. Open Notepad and copy/paste the script below, replacing `LansweeperServer` with the name or IP address of the Lansweeper scanning server you want to send the LsPush data to. The "0" at the end of the script makes the script run asynchronously, so users don't have to wait for the LsPush scan to finish to be able to log into their computers.  

   ```
   Set WshShell = CreateObject("Wscript.Shell")   
   WshShell.run "%logonserver%\netlogon\LsPush.exe LansweeperServer",0
   ```
5. From the **File** menu, select **Save As...** and save the file with a name ending in the .vbs extension.

   ![how-to-scan-windows-computers-with-the-lspush-scanning-agent-in-a-group-policy-3.jpg](/docs/.document360/assets/article_239/image_005.jpg)
6. On one of the domain controllers in your domain, open your **Start** menu and open **Run**.
7. In the input box, type "gpmc.msc" and select **OK**. This opens the Group Policy Management Console (GPMC).

   ![menu-gpmc.jpg](/docs/.document360/assets/article_239/image_006.jpg)
8. Under your domain, right-click **Group Policy Objects**, select **New** and give your policy a name. After clicking **OK**, a new policy object appears in the list of group policies.

   ![procedure-creating-group-policy.jpg](/docs/.document360/assets/article_239/image_007.jpg)

   ![how-to-scan-windows-computers-with-the-lspush-scanning-agent-in-a-group-policy-4.jpg](/docs/.document360/assets/article_239/image_008.jpg)
9. Right-click your newly created group policy and select **Edit**.

   ![how-to-scan-windows-computers-with-the-lspush-scanning-agent-in-a-group-policy-5.jpg](/docs/.document360/assets/article_239/image_009.jpg)
10. In the resulting pop-up, navigate to **`User Configuration\Policies\Windows Settings\Scripts (Logon/Logoff)`**.
11. In the right pane, right-click **Logon** and select **Properties**.

    ![how-to-scan-windows-computers-with-the-lspush-scanning-agent-in-a-group-policy-6.jpg](/docs/.document360/assets/article_239/image_010.jpg)
12. Click the **Show Files...** button and copy and paste the .vbs script you created earlier in the folder that's opened.

    ![how-to-scan-windows-computers-with-the-lspush-scanning-agent-in-a-group-policy-7.jpg](/docs/.document360/assets/article_239/image_011.jpg)
13. Back in the **Logon Properties** window, click **Add...**, then **Browse...** and select your .vbs script in the resulting pop-up. Select **Open** afterwards and **OK** twice to close all pop-ups.

    ![how-to-scan-windows-computers-with-the-lspush-scanning-agent-in-a-group-policy-8.jpg](/docs/.document360/assets/article_239/image_012.jpg)
14. Apply your group policy to your domain computers by right-clicking your domain name or a specific OU, selecting **Link an Existing GPO...** and choosing your newly created policy from the resulting pop-up.

    ![procedure-linking-group-policy.jpg](/docs/.document360/assets/article_239/image_013.jpg)

    It may take several hours for your group policy to fully apply and become active on your domain computers. You can run "gpupdate /force" in Command Prompt on computers to force their group policies to apply.
15. Once your group policy has become active and a user has logged into a computer to be scanned, perform a search for the name of the computer in the web console search bar, which takes you to the machine's Lansweeper webpage. The **Scan time** tab of the machine's asset page should also indicate an LsPush scan has taken place.   
    If the search bar finds no asset for the scanned computer, the LsPush scan may have failed for any of the following reasons: you've reached your Lansweeper license's asset limit, your Lansweeper database is full, the Windows computer is excluded from scanning.

    ![procedure-searching-for-windows-computer.jpg](/docs/.document360/assets/article_239/image_014.jpg)

    ![menu-scan-time-tab-last-lspush.jpg](/docs/.document360/assets/article_239/image_015.jpg)
