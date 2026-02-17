<!-- # Grouping assets -->
Lansweeper allows you to group various assets, making it quick and easy to look at specific network segments. You can group based on IP range (IP location group), other criteria like asset name or model (dynamic group) or manually (static group). To view the members of any group, hover over the **Assets** section in the web console and click the group name.

This article explains how to configure the three types of available groups: [IP address range locations](#heading1), [static asset groups](#heading2), and [dynamic asset groups](#heading3).  
![grouping-assets-1.jpg](/docs/.document360/assets/article_132/image_001.jpg)

An asset can belong to an unlimited number of asset groups. Asset groups are configured in the **Configuration > Asset Groups**section of the web console.  
![menu-configuration-asset-groups.jpg](/docs/.document360/assets/article_132/image_002.jpg)

## IP address range locations

IP range locations allow you to assign a name to an IP range. Any asset that belongs to the specified range will be placed in the corresponding IP location you've created.

Select **Add IP range location** in the **IP Address Range locations**menu, enter an IP location name, a start IP and an end IP address, and select **Ok**. The share, username and password fields are only relevant for [software deployment](/docs/deployment-requirements).  
![grouping-assets-5.jpg](/docs/.document360/assets/article_132/image_003.jpg)

IP range locations are only meant for grouping assets. They do not affect which IP ranges are scanned. To scan an IP range, submit it under the **Scanning > Scanning Targets** menu of the web console.

- If a machine or device doesn't belong to any IP location you've created, it is automatically added to the built-in Undefined group. This group cannot be renamed or deleted.
- From Lansweeper 6.0 onward, it is possible to import IP locations from Active Directory using the **Import From AD** button. These groups are fetched from **Active Directory Sites and Services**.
- From Lansweeper 6.0 onward, it is possible to import IP locations from a .csv file as well. Download the available template, add IP locations to it, save as .csv and upload the file using the **Import** button.

## Static asset groups

Static groups allow you to select any number of random machines or devices and add them to a group.

Select **Add Static Group** in the **Static Asset Groups**menu, enter a group name into the pop-up window and select **Ok**. You can then add assets to the group by clicking **Add Assets** and ticking the checkboxes in front of the assets.  
![grouping-assets-3.jpg](/docs/.document360/assets/article_132/image_004.jpg)

Selecting a static group will display a list that only shows group members whose state is Active. Assets set to Stock are not listed. To list machines of any state, you can build a custom report in the **Reports** menu or look at the group members under **Configuration > Asset Groups**. More info on states can be found in [this knowledge base article](/docs/create-use-and-change-asset-states).

- You can change the name of a group you've created by placing your cursor in the **Group Name**column, making the desired change, and pressing Enter while your cursor is still in the line.
- To remove assets from a group, select the group, tick the checkboxes in front of the assets and select **Remove Selected Assets**. You can delete a group by selecting the **Delete** button next to the group name.
- The **Default Group** is a built-in group containing all assets whose state is "active." This group cannot be renamed or deleted.
- You can group assets by going to the **Assets** section, ticking the checkboxes in front of the assets, and select **Add To Group**. You can search through one or more columns to quickly find specific assets.

## Dynamic asset groups

Dynamic groups allow you to group machines or devices based on criteria.

Select **Add Dynamic Group** in the **Dynamic Asset Groups**menu, enter a group name into the pop-up window and select **Ok**. You can then specify criteria the assets in the group have to meet by selecting **Add Filter**. In the resulting pop-up, you can select a database field, an operator (to look for exact or partial matches), and a value.  
![grouping-assets-4.jpg](/docs/.document360/assets/article_132/image_005.jpg)

- Use the Like/Not Like operators to look for partial matches.
- If you add filters for multiple fields, only machines or devices that meet the specified criteria will be added to the group.
- If you add multiple filters to the same field, assets that meet either criterion will be listed.
- In the example above, the dynamic group will contain active Windows 7/8 computers in any domain that contains the word "LAN".
- The dynamic group builder is a simplified version of the report builder found in the **Reports**menu of the web console. It only supports a limited number of database fields. To group based on fields not found in the dynamic group builder, create a report in the **Reports**menu instead.
