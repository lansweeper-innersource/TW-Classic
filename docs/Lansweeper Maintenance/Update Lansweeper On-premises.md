<!-- # Update Lansweeper On-premises -->
This page is for Lansweeper On-prem. For [Lansweeper Sites](https://www.lansweeper.com/product-overview/), see [Update your Lansweeper scan server](/docs/update-your-lansweeper-sites-scan-server).

Lansweeper now includes an auto-update feature to help you stay up to date. For more information on auto-update, check out [Enable the Lansweeper scan server to auto-update](/docs/enable-the-lansweeper-scan-server-to-auto-update). If you still want to update manually however, follow the instructions in this article.

It is recommended that you update your [Lansweeper](https://www.lansweeper.com/ "Lansweeper") installation on a regular basis, to ensure that you have the latest available patches installed and access to any new features that have been released.

You can [verify whether you have the latest Lansweeper version](/docs/check-for-lansweeper-updates) from the web console and perform an update of a medium sized network in just a few minutes. Updates are free to anyone with an active Lansweeper license. They are installed over your existing installation and leave your existing data and settings intact. Reinstalling is not required in order to update.

## Update your Lansweeper On-prem installation

Lansweeper 4.0 and any more recent Lansweeper releases can safely be updated to the latest Lansweeper version. Updates of older releases (1.x, 2.x or 3.x) are not supported. If you have a 1.x, 2.x or 3.x Lansweeper release, archive your installation for future reference and perform a new installation of the latest Lansweeper version instead.

1. Make sure all computers hosting the scanning service or web console component have .NET Framework 4.8 or a more recent .NET version installed. This is a requirement from Lansweeper 8.2.200 onward. If you're not sure which machines are hosting the Lansweeper service, you can find them listed in the Current Version section of the **Configuration > Your Lansweeper License** page.

   If you run the Lansweeper installer version 8.2.200 or newer on a system that does not have .NET 4.8 or newer installed, the Lansweeper update will pause and install .NET 4.8 automatically. Updating your framework often requires a reboot, if you receive a reboot message at the end of the Lansweeper installer, you must reboot to ensure your Lansweeper components are functional.

   

   
2. [Back up](/docs/back-up-your-installation) your installation, to be safe.
3. Download [the latest Lansweeper installer](https://www.lansweeper.com/update-lansweeper/) and run it on a machine hosting the **Lansweeper Server** service.

   If your Lansweeper database is hosted on a different machine than the Lansweeper service, running the installer on the machine hosting your database is not required. The Lansweeper service will automatically update your database.
4. Select **Next** and review the terms of use, which must be accepted to proceed.  
   
5. Select the **Upgrade** option and click **Next**. If the **Upgrade** option is grayed out, that either means that you are not running the latest installer or that you are already using the latest Lansweeper version. If this is the case, you should not proceed further and you should select **Cancel** to close the installer instead.  
   
6. The installer will automatically detect the Lansweeper components that require updating. Select **Next** to continue.  
   

   If your database is hosted in an Express edition of Microsoft SQL Server and there is less than 300 MB of free space, the installer will clear the database tables that store Windows event log data, to make room for the update. The Windows event log tables are usually the biggest. Express editions of old SQL Server versions are limited to 4 GB by Microsoft, while Express editions of newer SQL Server versions (2008 R2 and beyond) are limited to 10 GB.
7. The installer will automatically update the Lansweeper service, the Lansweeper database and, if it's hosted on the same machine, the Lansweeper web console.
8. Select **Finish** to close the installer.
9. If your Lansweeper web console is hosted on a different machine than the Lansweeper service, you will need to run the Lansweeper installer on that machine as well and once again go through the update procedure.
10. If the Lansweeper service is hosted on multiple machines, which are all connected to your Lansweeper database, you will either need to run the installer on each machine hosting the service and go through the update procedure each time or use the available installer parameters found in [Silently install, uninstall, or update Lansweeper](/docs/silently-install-uninstall-or-update-lansweeper).
11. If you are scanning Windows computers with the LsPush scanning agent, copy the up-to-date LsPush to any folder referenced by your logon script, group policy or scheduled task. After your Lansweeper update, the latest LsPush executable can be found in `Program Files (x86)\Lansweeper\Client` on your Lansweeper server.
12. If you are scanning non-Windows computers with the LsAgent scanning agent, update the LsAgent installations on those machines as well, as they do not auto-update. The latest LsAgent installers can be downloaded through [this page](https://www.lansweeper.com/download/lsagent/).
