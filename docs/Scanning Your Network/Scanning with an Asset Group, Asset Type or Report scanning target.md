<!-- # Scanning with an Asset Group, Asset Type or Report scanning target -->
Asset Group, Asset Type and Report are agentless, scheduled scanning targets that rescan assets already in your database, assets in any asset group, report or of any asset type specified by you. These scanning targets are suitable for rescanning Linux, Unix, Mac and Windows computers, VMware servers and other network devices. You can submit an unlimited number of Asset Group, Asset Type and Report targets for scanning and specify a separate scanning schedule for each.

To submit a target like this for scanning, click the **Add Scanning Target** button in the **Scanning > Scanning Targets**section of the web console and choose the Asset Group, Asset Type or Report scanning type in the resulting pop-up. If you have multiple scanning servers, there will be multiple configuration tabs on the **Scanning Targets** page, one for each server.





As agentless scanning of Linux, Unix, Mac and Windows computers, VMware servers and SNMP enabled network devices requires credentials, make sure to submit and map your scanning credentials as well, by following the instructions in [this knowledge base article](/docs/create-and-map-scanning-credentials).

Asset Group, Asset Type and Report scanning targets can only rescan assets that are already in your Lansweeper database.

## Asset Group, Asset Type and Report settings

Below is an overview of available options and settings for Asset Group, Asset Type and Report scanning targets. Each scanning target can be configured differently.



- **Asset Group**, **Asset Type** or **Report**: depending on which scanning type you chose, the category of the scanning type to rescan should be selected. Asset Group can be any built-in or custom [static or dynamic group](/docs/grouping-assets), Asset Type any asset type configured under **Configuration > Asset Mapping** and Report any asset report found in the **Reports** tab of the web console.  

  To submit a custom report for rescanning, make sure your report includes the AssetID field of the tblAssets database table. If it doesn't, it will not be considered an asset report and you will not be able to see or select it in the Report dropdown.
- **Description**: a custom description of the scanning target can be entered.
- **Schedule**: determines when (on which days of the week and at what time) the scanning target will be scanned.
- **Use DNS name**: if checked, Lansweeper will connect to your non-Windows devices' DNS names instead of their IP addresses. This is useful if you have devices that frequently change IP.

  This setting only affects non-Windows assets. Windows computers are always scanned based on computer name by Asset Group, Asset Type and Report targets, never based on IP address.
- **Enable**: toggle this option to enable or disable scanning of the scanning target.
