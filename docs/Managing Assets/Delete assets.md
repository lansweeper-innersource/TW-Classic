<!-- # Delete assets -->
![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_130/image_001.jpg) **This page explains how to automatically and manually delete assets.**

This page is for Lansweeper Classic. For Lansweeper Sites, see [Delete assets](/docs/delete-assets).

You may want to delete certain assets from your Lansweeper database after a while, particularly if those assets have been decommissioned and are no longer on the network. By default, Lansweeper does not remove any previously scanned assets from your database or web console. You must instruct your Lansweeper installation to remove assets.

You can either have automatic cleanups performed or manually remove any unwanted assets from your database and web console.

## Automatically deleting unwanted assets

If you are looking to delete assets that have been decommissioned and are no longer present in your network, the easiest way to do this would be through [your database cleanup options](/docs/perform-automated-database-cleanups), found in the web console under **Configuration > Server options**.

![menu-configuration-server-options.jpg](/docs/.document360/assets/article_130/image_002.jpg)  

If enabled, most of the cleanup operations are performed when the Lansweeper Server service starts on your Lansweeper server and automatically every 24 hours afterward.

## Manually deleting one or more unwanted assets

1. Go to the **Assets** section of the web console.![procedure-clicking-assets-link.jpg](/docs/.document360/assets/article_130/image_003.jpg)
2. Tick the checkboxes in front of the assets you want to delete.![deleting-assets-1.jpg](/docs/.document360/assets/article_130/image_004.jpg)
   - You can search one or more columns to easily find specific assets. In the example above, we filtered the Domain column to only list assets within the "lansweeper" domain.
   - You could also tick the top checkbox to select all assets in the current search results.
3. Select **Delete** under **Basic Actions**.  

   Deleting an asset removes it from your database and web console. Any historical information and custom data associated with the asset is lost. This operation cannot be undone without [restoring a database backup](/docs/restore-your-installation-from-a-backup). Make sure you've selected the correct assets before selecting **Delete**.

   Deleting an asset does not prevent it from being rescanned. If the asset is still present in your network and submitted for scanning under **Scanning > Scanning Targets**, it will be rescanned and added to the web console again. To prevent the asset from being rescanned, you can [exclude it](/docs/exclude-assets-from-scanning).

## Manually deleting a single unwanted asset

1. Browse to the asset's detailed page and select **Edit asset** under **Asset options**.![deleting-assets-2.jpg](/docs/.document360/assets/article_130/image_005.jpg)
2. Select **Delete asset** under **Asset options**.![deleting-assets-3.jpg](/docs/.document360/assets/article_130/image_006.jpg)
