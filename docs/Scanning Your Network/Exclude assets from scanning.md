<!-- # Exclude assets from scanning -->

Keep in mind that each scanning target works independently. If an asset is part of only one scanning target, Lansweeper will attempt to scan the asset. However, if an asset is part of one scanning target, it will continue to be scanned regardless of whether it's part of other scanning targets as well. You can determine which scanning targets scanned a Windows machine and when by looking at the **Scan Time** tab of the machine's Lansweeper webpage.

In the example below, computer LAN-001 was scanned by the LsPush scanning agent on March 5th and by an IP Range scanning target on March 6th.

![excluding-assets-from-scanning-1.jpg](/docs/.document360/assets/article_182/image_002.jpg)

To prevent unwanted assets from being scanned, make sure those assets are not part of any scanning target or specifically exclude them from scanning. Your scanning targets and asset exclusions are configured in the **Scanning > Scanning Targets**section of the web console.

![menu-scanning-scanning-targets.jpg](/docs/.document360/assets/article_182/image_003.jpg)

Changing your scanning setup or excluding an asset from scanning only prevents future scan attempts from taking place. If the asset was already scanned prior to excluding or changing your scanning setup, it will not automatically be removed from your database. You can always [delete the asset](/docs/delete-assets) separately.

If an excluded asset is part of a scanning target, the asset will still be scanned but the data will be ignored as the exclusion has priority over the scanning target.

To exclude assets from scanning, click the **Add Exclusion** button in the **Scanning > Scanning Targets** section of the web console. There are 4 types of asset exclusions, listed below.

If you have multiple scanning servers, you can choose to add the exclusion to all servers at once. From Lansweeper 7.2 onward, you are forced to submit an exclusion reason when creating an asset exclusion for one or more scanning servers. You can choose one of the predefined reasons from the dropdown or manually type a reason by choosing the **Other** option.

- **Asset Type**: tick the asset type(s) you would like to exclude in the pop-up window.  
  ![excluding-assets-from-scanning-6.jpg](/docs/.document360/assets/article_182/image_004.jpg)

  Excluding an asset type from scanning only prevents assets of the specified type from being added to the database. It doesn't prevent Lansweeper from querying assets of the specified type, as a device's asset type cannot be determined without querying the device.

  If you're excluding types because you've reached your license's asset limit, keep in mind that [some monitors do not count toward your limit](/docs/assets-that-count-toward-your-licensed-asset-limit). Excluding the Monitor asset type may not have an effect on your licensed asset count.
- **IP Address or Range**: enter an individual IP address or an IP range into the exclusion pop-up window.  
  The ability to exclude entire IP ranges was added in Lansweeper 6.0.  
  ![excluding-assets-from-scanning-7.jpg](/docs/.document360/assets/article_182/image_005.jpg)
- **Windows Computer**: the NetBIOS name of the Windows computer you would like to exclude should be entered in the exclusion pop-up window.  
  ![excluding-assets-from-scanning-8.jpg](/docs/.document360/assets/article_182/image_006.jpg)

  You can use "%" as a wildcard:  
  Entering **LAN%** into the pop-up window excludes any Windows computer whose name starts with the word "LAN" from scanning.   
  Entering **%LAN** into the pop-up window excludes any Windows computer whose name ends in the word "LAN" from scanning.  
  Entering **%LAN%** into the pop-up window excludes any Windows computer whose name contains the word "LAN" from scanning.
- **Workgroup or Domain**: the NetBIOS name of the domain you would like to exclude should be entered in the exclusion pop-up window.  
  ![excluding-assets-from-scanning-9.jpg](/docs/.document360/assets/article_182/image_007.jpg)
