<!-- # Put the scanning service in debug mode -->
To scan your network, trigger deployments and send mails, Lansweeper uses [a service called Lansweeper Server](/docs/lansweeper-classic-components-and-architecture). This service writes its start events and possible errors to a log file on your Lansweeper server, Program Files (x86)\Lansweeper\Service\Errorlog.txt.

If you submit a support ticket, you may at some point be asked by the Lansweeper support team to put the scanning service in debug mode, which will write more detailed information to the log file. Debug mode is useful for identifying database and other issues with your installation that could cause scanning failures, e.g. issues with missing database tables, fields or constraints.

Only put the Lansweeper Server service in debug mode if you are trying to identify database or other issues, or if asked to by the Lansweeper support team. Enabling debug mode will significantly increase the size of your service's **Errorlog.txt** file.

  To put the Lansweeper Server service in debug mode, follow these steps:

1. Stop the Lansweeper Server service in Windows Services on the scanning server you'd like to put into debug mode.

   ![procedure-stopping-the-lansweeper-service.jpg](/docs/.document360/assets/article_295/image_001.jpg)
2. If your current service log found at `Program Files (x86)\Lansweeper\Service\Errorlog.txt` is too big to send to the Lansweeper support team, rename the file or move it to a different folder so a new log will be generated.
3. Run the **ConfigEditor** tool found on the scanning server `Program Files (x86)\Lansweeper\Tools\ConfigEditor.exe`.

   ![menu-configeditor.jpg](/docs/.document360/assets/article_295/image_002.jpg)
4. Select the debug line in the **Service** tab, select **Edit** and change the **Value** in the resulting pop-up from "0" to "1".

   ![putting-the-scanning-service-in-debug-mode-3.jpg](/docs/.document360/assets/article_295/image_003.jpg)
5. Select **Save configs and restart service**. If the service was successfully put into debug mode, a service start event with a debug message will be added to your **Errorlog.txt** file. The Lansweeper Server service will now write more detailed error messages to your **Errorlog.txt** file, as errors occur.

   ![procedure-configeditor-save-and-restart.jpg](/docs/.document360/assets/article_295/image_004.jpg)

   ![putting-the-scanning-service-in-debug-mode-2.jpg](/docs/.document360/assets/article_295/image_005.jpg)

   Once you or the Lansweeper team have finished troubleshooting, turn debugging back off by stopping the service, reverting the debug value to 0 and restarting the service. Leaving debug on will cause exponential growth of your **Errorlog.txt** file.
