<!-- # WMI service is disabled on this machine -->
If the "WMI service is disabled on this machine" error occurs in the testconnection.exe tool included in your Lansweeper installation folder, it is possible that the service has been manually stopped or disabled.



To resolve this scanning error:

1. On the Windows computer you are attempting to scan, open **Windows Services**.
2. Find the **Windows Management Instrumentation** service and right-click it. Select **Properties**.  
   
3. Set the **Startup type** to **Automatic**.  
   
4. Start the **Windows Management Instrumentation**.  
   
5. In Lansweeper's web console, go to **Assets**, find the Windows computer, select the checkbox next to it, then select **Rescan**.
