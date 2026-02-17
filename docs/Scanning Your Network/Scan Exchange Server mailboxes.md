<!-- # Scan Exchange Server mailboxes -->
Exchange Server scanning was introduced in Lansweeper 7.0 and significantly expanded in Lansweeper 7.1. You will need to [update your installation](http://lansweeper.com/knowledgebase/updating-your-installation/ "updating your installation") if you are running a lower Lansweeper version.

From version 7.0 onward, Lansweeper can scan mailbox information of Exchange servers, by running PowerShell commands locally on the Exchange Server. Exchange scanning was expanded and reworked in Lansweeper 7.1 and is now enabled by default.

Kerberos authentication is used for the PowerShell connection. Once scanned, the Exchange data can be found in the **Exchange** tab of the server's Lansweeper webpage. Built-in reports and dashboard widgets are available as well. Scanned Exchange Server data includes version, edition, users, groups, CALs, mailbox lists and sizes, ActiveSync devices and more.

![scanning-exchange-server-mailboxes-7.jpg](/docs/.document360/assets/article_218/image_001.jpg)

## Scanning Exchange Server mailboxes

In order for Lansweeper to scan Exchange Server information from your Windows computers, make sure that the following requirements are met.

- The "EXCHANGE" item is checked under **Scanning > Scanned Item Interval** in the Lansweeper web console. From Lansweeper 7.1 onward, this item is checked by default.
- Your client machine is running Exchange Server 2013 or higher and has .NET Framework 4.0 or higher installed. PowerShell scanning of older Exchange Server versions is not currently supported.
- Scanning server and client machine are in the same domain.
- PowerShell is enabled on the client machine as well as your scanning server.
- The client machine is configured to allow scripts that are signed by a trusted publisher. This can be done by running the below command in PowerShell on the client machine.

  ```
  Set-ExecutionPolicy RemoteSigned
  ```
- The Exchange PowerShell snap-in is enabled on the client machine. Lansweeper automatically tries to enable it. The snap-in is required as this allows Lansweeper to use a single session for data retrieval, even if more PowerShell data is added in the future.
- The **Windows Remote Management** service (WinRM) is running on the client machine.

  ![scanning-exchange-server-mailboxes-5.jpg](/docs/.document360/assets/article_218/image_002.jpg)
- A service whose caption includes "Microsoft Exchange" is running on the client machine and listed in the **Config > Windows > Services** tab of the machine's Lansweeper webpage. If the service is successfully detected by Lansweeper, Exchange scanning will also be performed.
- The client machine's FQDN has been successfully scanned or manually added to the asset in Lansweeper. For Exchange Server scanning, a connection is made to the computer's FQDN.

  ![scanning-exchange-server-mailboxes-3.jpg](/docs/.document360/assets/article_218/image_003.jpg)
- The client machine's FQDN correctly resolves to the computer's IP address from your Lansweeper scanning server. This can be verified by performing a ping request from the Lansweeper server to the client machine's FQDN.

  ![scanning-exchange-server-mailboxes-4.jpg](/docs/.document360/assets/article_218/image_004.jpg)  

  Keep in mind that the online status indicator you see below the client machine's name in Lansweeper is based on a ping request performed from your web server to the computer's NetBIOS name. This status indicator therefore cannot be used as an indication of successful FQDN resolution.
- A domain administrator is submitted and mapped as a credential to the client machine. More info on submitting and mapping credentials can be found in [this knowledge base article](/docs/create-and-map-scanning-credentials).   
  Whereas normal Windows computer scanning can be done with either a domain or local credential, Exchange Server scanning requires a domain credential. Specifically, this credential must be a domain administrator.
- The client machine has been submitted for scanning in the **Scanning > Scanning Targets** section of the web console. More info on how to scan a Windows computer can be found in [this knowledge base article](/docs/how-to-scan-a-windows-computer). Exchange Server scanning is currently only supported for agentless scanning methods.

## Debugging Exchange Server scanning

If Exchange Server information fails to scan after you've double-checked the scanning requirements above, put your scanning server into debug mode:

1. Stop the **Lansweeper Server** service in **Windows Services** on the scanning server you'd like to put into debug mode.

   ![procedure-stopping-the-lansweeper-service.jpg](/docs/.document360/assets/article_218/image_005.jpg)
2. Run the ConfigEditor tool found at `Program Files (x86)\Lansweeper\Tools\ConfigEditor.exe` on the scanning server.

   ![menu-configeditor.jpg](/docs/.document360/assets/article_218/image_006.jpg)
3. Click the **Add** button under appSettings.
4. Configure the pop-up as shown below and click **Add**.

   ![scanning-exchange-server-mailboxes-8.jpg](/docs/.document360/assets/article_218/image_007.jpg)
5. Click **Save** under appSettings.

   ![menu-configeditor-buttons-save-configs.jpg](/docs/.document360/assets/article_218/image_008.jpg)
6. Restart the **Lansweeper Server** service on your scanning server.

   ![procedure-starting-the-lansweeper-service.jpg](/docs/.document360/assets/article_218/image_009.jpg)
7. Click **Rescan Asset** on the left side of the problem client machine's Lansweeper webpage and wait for the **Last scan attempt** or **Last seen**date listed on the page to update.
8. Open the ErrorLog file at `Program Files (x86)\Lansweeper\Service\Errorlog.txt` on your scanning server and look for any errors related to the Exchange Server, which may provide more information on the failure.
9. When you've finished debugging, remove the **LogExchangeScanning** option from your appSettings again, to prevent unnecessary growth of your log file.
