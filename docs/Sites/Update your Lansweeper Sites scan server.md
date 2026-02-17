<!-- # Update your Lansweeper Sites scan server -->
This page is for Lansweeper Sites. For Lansweeper On-prem, see [Update your Lansweeper On-prem installation](/docs/update-lansweeper-on-premises).

Lansweeper now includes an auto-update feature to help you stay up to date. For more information on auto-update, check out [Enable the Lansweeper scan server to auto-update](/docs/enable-the-lansweeper-scan-server-to-auto-update). If you still want to update manually however, follow the instructions in this article.

It is recommended that you update your [Lansweeper](https://www.lansweeper.com/) installation on a regular basis, to ensure that you have the latest available patches installed and access to any new features that have been released. Updates are free to anyone with an active Lansweeper license. They are installed over your existing installation and leave your existing data and settings intact. Reinstalling is not required in order to update.

## Update your scan server

1. Starting from your Cloud site, browse to the **Configuration**module and select **Installations**. If you aren't sure which version currently have installed, select **All installations**. The current version of your installations will be displayed, preceded by an icon alerting you of its status. If your installation is outdated, continue to the next step.

   ![Updating your LS scan server 2.png](/docs/.document360/assets/article_329/image_002.jpg)
2. In the **Installations** view, select **Download installers**, and click **Download IT installer** to start downloading the latest version of the LansweeperSetup.exe file.  
   ![Download installers 1.png](/docs/.document360/assets/article_329/image_003.jpg)  
   Alternatively, download the latest Lansweeper installer from [the Lansweeper website](https://www.lansweeper.com/update-lansweeper/), or by clicking **Check for updates now**in the **Configuration > Your Lansweeper License** section in Lansweeper Classic web console.
3. Make sure all computers hosting the scanning service have .NET Framework 4.8 or a more recent .NET version installed. This is a requirement from Lansweeper 8.2.200 onward.

   If you run the Lansweeper installer version 8.2.200 or newer on a system that does not have .NET 4.8 or newer installed, the Lansweeper update will pause and install .NET 4.8 automatically. Updating your framework often requires a reboot, if you receive a reboot message at the end of the Lansweeper installer, you must reboot to ensure your Lansweeper components are functional.
4. [Back up](/docs/back-up-your-installation) your installation, to be safe.
5. When the download has been completed, place the file on the scan server that needs to be updated. Run LansweeperSetup.exe to start updating your scan server.

   If your Lansweeper database is hosted on a different machine than the Lansweeper service, running the installer on the machine hosting your database is not required. The Lansweeper service will automatically update your database.
6. Click **Next**, and review the terms of use. The terms of use must be accepted to proceed.  
   ![TLS Checkbox 0.png](/docs/.document360/assets/article_329/image_004.jpg)
7. Select the **Upgrade** option and click **Next**.   
   If the **Upgrade** option is grayed out, that either means that you are not running the latest installer or that you are already using the latest Lansweeper version. If this is the case, you should not proceed further and you should close the installer instead.  
   ![TLS Checkbox 1.png](/docs/.document360/assets/article_329/image_005.jpg)
8. The installer will automatically detect the Lansweeper components that require updating. Select **Next** to continue.  
   ![TLS Checkbox 2.png](/docs/.document360/assets/article_329/image_006.jpg)  

   If your database is hosted in an Express edition of Microsoft SQL Server and there is less than 300 MB of free space, the installer will clear the database tables that store Windows event log data, to make room for the update. The Windows event log tables are usually the biggest. Express editions of old SQL Server versions are limited to 4 GB by Microsoft, while Express editions of newer SQL Server versions (2008 R2 and beyond) are limited to 10 GB.
9. The installer will automatically update the Lansweeper service and the Lansweeper database. The update may take a while, depending on the size of your database.
10. When you get to the screen that confirms the successful update of your Lansweeper installation, click **Finish** to close the installer.
11. If the Lansweeper service is hosted on multiple machines, which are all connected to your Lansweeper database, you will either need to run the installer on each machine hosting the service and go through the update procedure each time, or use the available installer parameters found in [Silently install, uninstall, or update Lansweeper](/docs/silently-install-uninstall-or-update-lansweeper).
12. If you are scanning Windows computers with the LsPush scanning agent, copy the up-to-date LsPush to any folder referenced by your logon script, group policy or scheduled task. After your Lansweeper update, the latest LsPush executable can be found at `Program Files (x86)\Lansweeper\Client` on your Lansweeper server.
13. If you are scanning non-Windows computers with the LsAgent scanning agent, update the LsAgent installations on those machines as well, as they do not auto-update. The latest LsAgent installers can be downloaded through [this page](https://www.lansweeper.com/download/lsagent/).
