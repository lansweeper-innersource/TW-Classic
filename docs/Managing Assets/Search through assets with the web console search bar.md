<!-- # Search through assets with the web console search bar -->
A search bar is available in the Lansweeper Classic web console that allows you to search through the assets stored in your installation. These include Windows, Linux and Mac computers, servers and other network devices.

When you start typing, the search bar starts displaying search term matches. Press **Enter** after submitting your search term for a complete results list. Search is not case-sensitive. Submitting "lan" or "LAN" for instance returns the same results.

For performance reasons, the search bar only searches specific asset fields and for some fields only returns results that start with the specified search term. More specific searches for other fields or using different filters can be performed using other means: [dynamic asset groups](/classic/docs/grouping-assets#heading3 "Dynamic asset groups"), built-in or custom reports in the **Reports** tab or widgets. Reports allow you to perform "contains" searches in each column, without modifying the report's underlying SQL query.



Below is a list of items searched by the asset search bar. This list also shows the icon that accompanies each type of search result. If the same value is stored in multiple fields of the same asset, that asset may be displayed multiple times in search results, once for each field. The accompanying icon tells you what the search result is for.

-  Asset (NetBIOS) names  
  These search results are accompanied by the icon of the asset's asset type. Examples of asset types are Windows, Linux and Mac. FQDN or DNS names are not searched by the search bar but can be searched using a report.
-  Asset descriptions  
  These search results are accompanied by the icon of the asset's asset type. Examples of asset types are Windows, Linux and Mac. The search bar searches the local descriptions, not the Active Directory descriptions. Active Directory descriptions of Windows computers can be searched using a report.
-  Asset domain and workgroup names
-  Assets' most recently scanned IP addresses   
  These are the IP addresses you see listed at the top of the assets' Lansweeper web pages. Secondary IP addresses are not searched by the search bar but can be searched using a report.
-  Asset MAC addresses
-  Asset barcodes  
  If filled in, these are the values you see in the Barcode field of your assets' Summary tabs.
-  Asset Custom1 through Custom20 fields   
  More info on what custom fields are and how to use them can be found in [this knowledge base article](/classic/docs/configure-and-add-data-to-asset-custom-fields).
-  Asset (purchase) order numbers  
  If filled in, these are the numbers you see in the Order field of your assets' Summary tabs.
-  Asset serial numbers
-  Asset SMBIOSAssetTags  
  These are the tags in the **Config > Hardware > System Chassis** tab of your Windows computers' Lansweeper webpages.
-  Active Directory computer OUs  
  Start your search with "OU=" or "CN=" to search Windows computer OUs.
-  Active Directory user OUs  
  Start your search with "OU=" or "CN=" to search user OUs.
-  Usernames of local Windows and Active Directory users  
  These search results are accompanied by the user's icon or the first letter of the user's name, if the user doesn't have a specific icon.
-  Software names of applications installed on Windows, Linux and Mac computers
-  Report names of reports found in the Reports menu
