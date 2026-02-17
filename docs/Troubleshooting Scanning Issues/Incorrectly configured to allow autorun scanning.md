<!-- # Incorrectly configured to allow autorun scanning -->
To prevent the return of incorrect autorun items, Lansweeper scans Win32\_StartupCommand on client machines whose Startup value is incorrectly configured and returns an "incorrectly configured to allow autorun scanning" error in **Configuration > Server log**.

These events are caused by an incorrect configuration of the affected client machine.

![incorrectly-configured-to-allow-autorun-scanning-1.jpg](/docs/.document360/assets/article_252/image_001.jpg)

This error only affects the scanning of autorun items, which runs automatically when the client machine is started. All other computer data will still be scanned without issue. Resolving the error is only necessary if you'd like to retrieve autorun data.

To prevent this error  allow Lansweeper to scan autorun items:

1. Navigate to the client machine that generated the event and open the **Registry Editor**.
2. Point the Startup value in the registry key below to any random, empty folder exists. In the example below, we created a folder called Autorun on our C: drive and pointed the Startup value to that folder.   
   **HKEY\_USERS\S-1-5-18\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders  
   ![incorrectly-configured-to-allow-autorun-scanning-2.jpg](/docs/.document360/assets/article_252/image_002.jpg)  
   ![incorrectly-configured-to-allow-autorun-scanning-3.jpg](/docs/.document360/assets/article_252/image_003.jpg)**
3. In the web console, go to **Assets,**find your machine and select the checkbox next to it. Then select **Rescan**.  
   ![procedure-rescanning-individual-windows-computer-from-assets-menu.jpg](/docs/.document360/assets/article_252/image_004.jpg)
4. Once the scan is complete, you should find the autorun items listed on the machine's entry in Lansweeper, in **Config > Windows > Autorun.**  

   ![incorrectly-configured-to-allow-autorun-scanning-4.jpg](/docs/.document360/assets/article_252/image_005.jpg)
