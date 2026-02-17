<!-- # WMI service is disabled on this machine -->
If the "WMI service is disabled on this machine" error occurs in the testconnection.exe tool included in your Lansweeper installation folder, it is possible that the service has been manually stopped or disabled.

![wmi-service-is-disabled-on-this-machine-1.jpg](/docs/.document360/assets/article_276/image_001.jpg)

To resolve this scanning error:

1. On the Windows computer you are attempting to scan, open **Windows Services**.
2. Find the **Windows Management Instrumentation** service and right-click it. Select **Properties**.  
   ![wmi-service-is-disabled-on-this-machine-2.jpg](/docs/.document360/assets/article_276/image_002.jpg)
3. Set the **Startup type** to **Automatic**.  
   ![wmi-service-is-disabled-on-this-machine-3.jpg](/docs/.document360/assets/article_276/image_003.jpg)
4. Start the **Windows Management Instrumentation**.  
   ![wmi-service-is-disabled-on-this-machine-4.jpg](/docs/.document360/assets/article_276/image_004.jpg)
5. In Lansweeper's web console, go to **Assets**, find the Windows computer, select the checkbox next to it, then select **Rescan**.
