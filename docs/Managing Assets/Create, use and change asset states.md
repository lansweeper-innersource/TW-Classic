<!-- # Create, use and change asset states -->

Every scanned or manually created computer and device in Lansweeper has an asset state. States are a Lansweeper feature that allow you to keep track of which machines are active in your network, which have been decommissioned, which are in stock etc.

There are built-in states, but you can create your own as well. By default, a machine's state is set to "active". However, this state can be changed, either manually or by enabling automated cleanup options.

Reports found in the **Reports** tab of the web console can also be modified to list machines with other states. Assets with a state other than "active" can be found through the search bar as well and in the list in the **Assets** section of the web console. This article explains how you can create your own asset states, change an asset's state manually or change an asset's state through automated cleanup options.

![creating-using-and-changing-asset-states-1.jpg](/docs/.document360/assets/article_129/image_002.jpg)

## Create asset states

1. Browse to the **Configuration > Asset Pages**section of the web console.![menu-configuration-asset-pages.jpg](/docs/.document360/assets/article_129/image_003.jpg)
2. Select **Add Asset state** in the **Asset States** section of the page.![creating-using-and-changing-asset-states-2.jpg](/docs/.document360/assets/article_129/image_004.jpg)
3. Enter a state name into the State Name field of the pop-up window.
4. Select **Ok**. The state is now included in any state dropdowns within the web console.

## Change an asset's state manually

Try one of the following options to change an asset's state, depending on whether you want to update a single asset or multiple assets at once:

- Browse to an asset's detailed page and select **Edit asset** under **Asset options**. Select an asset state from the dropdown and select **Save asset**.![creating-using-and-changing-asset-states-3.jpg](/docs/.document360/assets/article_129/image_005.jpg)
- Go to the **Assets** section of the web console, tick the checkboxes in front of the assets of your choice and select **Mass Edit Assets** under **Asset Actions**. In the resulting pop-up, select the State field, choose your preferred asset state for the assets you selected and select **Change Field(s)**.
  - You can search through one of the columns to more easily find specific assets.
  - You can tick the top checkbox to select all assets in the current search results.![creating-using-and-changing-asset-states-5.jpg](/docs/.document360/assets/article_129/image_006.jpg)
- Go to the **Assets** section of the web console and select **Editing Mode** under **Options**. Place your cursor in the State column, select a state from the dropdown and select **Ok**.![creating-using-and-changing-asset-states-7.jpg](/docs/.document360/assets/article_129/image_007.jpg)

## Change an asset's state by enabling automated cleanup options

Instead of manually changing states, you can also configure Lansweeper to automatically change the state of stale, decommissioned or recommissioned machines. Several automated cleanup options are available for this in the **Configuration > Server Options** section of the web console, though they are disabled by default.

If enabled, most of these cleanup operations are performed when the Lansweeper Server service starts on your Lansweeper server and automatically every 24 hours afterward. More information on available cleanup options can be found in [this knowledge base article](/docs/perform-automated-database-cleanups).

![creating-using-and-changing-asset-states-8.jpg](/docs/.document360/assets/article_129/image_008.jpg)
