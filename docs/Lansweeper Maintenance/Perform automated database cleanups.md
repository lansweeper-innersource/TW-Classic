<!-- # Perform automated database cleanups -->
![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_109/image_001.jpg) **This page explains the various options provided by Lansweeper On-premises to manage your database size. You will also find information on where to locate these options and gain insight into their specific functionalities.**

Once an asset is scanned and added to the database, Lansweeper will not remove it unless instructed to do so.

You can [manually delete](/docs/delete-assets) old assets or have them deleted automatically through your several cleanup options, found in the Lansweeper On-prem web console under **Configuration > Server Options**or **Scanning > Scanning Targets**. These options can be used to delete assets as well as other stale data.

There are [Asset Cleanup Options](#heading1), [User Cleanup Options](#heading2) and [History Cleanup Options](#heading3).  
![Automated database cleanups 1.png](/docs/.document360/assets/article_109/image_002.jpg)

If enabled, most of the cleanup operations are performed when the Lansweeper Server service starts on your Lansweeper server and automatically every 24 hours afterward.

You can prevent specific assets from being deleted or having their state changed by your cleanup options. Go to the **Assets** section of the console, tick the checkboxes in front of the assets, select **Mass Edit Assets** and tick the **Not Affected By Cleanup Options** field.

## Asset Cleanup Options

Below is an overview of currently available asset cleanup options. You'll find these options in the **Configuration > Server options** section of the web console.

- **Automatically make non-active assets active when they are rescanned**

  This changes the state of any assets whose state is not "active" to "active" when the assets are rescanned. If this option is enabled, the asset below for instance will be set to "active" when rescanned.

  ![performing-automated-database-cleanups-1.jpg](/docs/.document360/assets/article_109/image_003.jpg)
- **Automatically make non-active assets active when they are rescanned with an indirect scan**This changes the state of any assets whose state is not "active" to "active" when the assets are rescanned with an indirect scan. This can only be enabled if the previous option is enabled.
- **Set assets to non-active if not seen in the last X days**

  This changes the state of any assets that have not been detected in your network in the last X days to "non-active". "Non-active" assets are excluded from most reports. This setting only affects assets that have been successfully scanned at least once.
- **Permanently delete assets not seen in the last X days**

  This deletes any assets that have not been detected in your network in the last X days from your Lansweeper database. This setting only affects assets that have been successfully scanned at least once. This operation cannot be undone without restoring a database backup.
- **Remove computers not found in on-premises Active Directory from the Lansweeper database**

  This deletes domain assets that no longer exist in Active Directory from your Lansweeper database. This operation cannot be undone without restoring a database backup.
- **Set computers to non-active if not found in on-premises Active Directory**

  This changes the state of domain assets that no longer exist in Active Directory to "non-active". "Non-active" assets are excluded from most reports.
- **Remove computers disabled in on-premises Active Directory from the Lansweeper database**

  This deletes domain assets that are disabled in Active Directory from your Lansweeper database. The assets are only deleted from your Lansweeper database, not from Active Directory itself. This operation cannot be undone without restoring a database backup.
- **Set computers to non-active if disabled in on-premises Active Directory**

  This changes the state of domain assets that are disabled in Active Directory to "non-active". "Non-active" assets are excluded from most reports.
- **Permanently delete SCCM data not scanned by an SCCM scanning target after X days**

  This deletes both stale SCCM data from the SCCM database tables and stale assets that were only detected through SCCM scanning. More info on SCCM scanning can be found in [this knowledge base article](/docs/integrate-lansweeper-with-sccm).

## On-Premises Active Directory Scanning Options

Below is an overview of currently available on-premises Active Directory scanning cleanup options. You'll find these options in the **Scanning > Scanning Targets**section of the web console.

- **Refresh on-premises Active Directory computer details (OU, description...)**

  This forces a periodic update of the Active Directory details of domain assets already present in the Lansweeper database. A domain asset's AD details are also updated when the asset is rescanned, if an update did not already occur in the last 20 hours.
- **Refresh on-premises Active Directory user details (Department, telephone,... ) in the Lansweeper database**This forces a periodic update of the Active Directory user details of domain assets already present in the Lansweeper database.

## User and Group Cleanup Options

Below is an overview of currently available user cleanup options. You'll find these options in the **Configuration > Server options** section of the web console.

### **Asset Radar**

- **Set Asset Radar assets to non-active if not seen in the last X days**
- **Permanently delete Asset Radar assets if not seen in the last X days**
- **Set Asset Radar assets of the types 'Unknown' and 'Network device' to non-active if not seen in the last X days**
- **Permanently delete Asset Radar assets of the type 'Unknown' and 'Network device' if not seen in the last X days**

### **On-premises Active Directory**

- **Remove users not found in on-premises Active Directory from the Lansweeper database**

  This deletes domain users that no longer exist in Active Directory from your Lansweeper database. This operation cannot be undone without restoring a database backup.
- **Remove users disabled in on-premises Active Directory from the Lansweeper database**

  This deletes domain users that are disabled in Active Directory from your Lansweeper database. The users are only deleted from your Lansweeper database, not from Active Directory itself. This operation cannot be undone without restoring a database backup.
- **Remove groups not found in on-premises Active Directory from the Lansweeper database**  
  This deletes domain groups that no longer exist in Active Directory from your Lansweeper database. This operation cannot be undone without restoring a database backup.

### **Azure Active Directory**

- **Remove users not found in Azure Active Directory from the Lansweeper database**  
  This deletes domain users that no longer exist in Azure Active Directory from your Lansweeper database. This operation cannot be undone without restoring a database backup.
- **Remove users disabled in Azure Active Directory from the Lansweeper database**  
  This deletes domain users that are disabled in Active Directory from your Lansweeper database. The users are only deleted from your Lansweeper database, not from Active Directory itself. This operation cannot be undone without restoring a database backup.
- **Remove groups not found in Azure Active Directory from the Lansweeper database**  
  This deletes domain groups that no longer exist in Azure Active Directory from your Lansweeper database. This operation cannot be undone without restoring a database backup.

## History Cleanup Options

Below is an overview of currently available history cleanup options. You'll find these options in the **Configuration > Server options** section of the web console.

- **Delete history from all history tables after X days**

  This deletes historical information found in the **History** tab of Windows computer webpages.

  ![performing-automated-database-cleanups-2.jpg](/docs/.document360/assets/article_109/image_004.jpg)
- **Delete eventlog entries after X days**

  This deletes the Event Viewer entries found in the **Event Log** tab of Windows computer webpages.

  ![performing-automated-database-cleanups-3.jpg](/docs/.document360/assets/article_109/image_005.jpg)
- **Delete serverlog entries after X days**

  This deletes the debug messages generated by the Lansweeper Server service and found in the web console under **Configuration >****Server** **Log**.

  ![menu-configuration-server-log.jpg](/docs/.document360/assets/article_109/image_006.jpg)
- **Delete logon information after X days**

  This deletes the user logon events found in the **Config > User Info > Last Logon** menu of Windows computer webpages.

  ![performing-automated-database-cleanups-4.jpg](/docs/.document360/assets/article_109/image_007.jpg)
- **Delete uptime data after X days**

  This deletes uptime calendar events found in the **Uptime** tab of Windows computer webpages.

  ![performing-automated-database-cleanups-5.jpg](/docs/.document360/assets/article_109/image_008.jpg)
- **Delete deployment logs after X days**

  This deletes the deployment logs found in the web console under **Deployment** **>****Deployment Logs**.

  ![Automated database cleanups 2.png](/docs/.document360/assets/article_109/image_009.jpg)
- **Delete configurations older than X days**

  This deletes information on who made changes to assets or Lansweeper settings and when. More info on this logging feature can be found in [this knowledge base article](/docs/track-lansweeper-classic-logins-and-setting-changes).
- **Delete Lansweeper login logs after X days**

  This deletes information on who logged into the Lansweeper web console and when. More info on this logging feature can be found in [this knowledge base article](/docs/track-lansweeper-classic-logins-and-setting-changes).
- **Delete performance counter data after X days**

  This deletes performance information found in the **Performance** tab of Windows and Linux computer webpages. More info on the performance scanning feature can be found in [this knowledge base article](/docs/how-to-scan-performance-information-of-windows-and-linux-computers).
- **Delete Windows cluster logs after X days**

  This deletes event log entries retrieved as part of Windows cluster scanning. These are the events visible in the **Windows Cluster** tab of computer webpages. More info on Windows cluster scanning can be found in [this knowledge base article](/docs/scan-windows-failover-cluster-details-and-logs).
- **Delete Hyper-V logs after X days**

  This deletes event log entries retrieved as part of Hyper-V log scanning. These are the events visible in the **Hyper-V Log** tab of computer webpages. More info on Windows cluster log and Hyper-V log scanning can be found in [this knowledge base article](/docs/scan-windows-failover-cluster-details-and-logs).
- **Delete Asset Radar logs after X days**
- **Delete unique records from already removed data after X days**  
  Delete detail data for Windows assets that are no longer in the inventory (Features, Services, Shares, Drivers, etc).
- **Delete expired LAPS credentials after X days**
