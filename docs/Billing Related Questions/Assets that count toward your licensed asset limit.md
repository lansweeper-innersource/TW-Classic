<!-- # Assets that count toward your licensed asset limit -->
Most [Lansweeper subscriptions](https://www.lansweeper.com/pricing/) limit the number of assets you can scan. Once you've reached your licensed asset limit, scanning of new and existing assets may stop until you delete some assets or upgrade your subscription.

Any computers, servers, network devices, OT devices, OT cards, Public Cloud workloads (that are included in [Discovery actions](/docs/overview-of-discovery-components-and-configuration#actions)) and manually created assets count toward your limit.

Monitors without [extended display data](/docs/extended-display-scanning) do not count toward the limit. Although monitors are technically assets, they only count if they have extended display data associated with them.

## Assets in Lansweeper Sites

In your site, go to **Configuration > License status**. The total number of assets that count toward your licensed asset limit is listed in **Licensed assets**, as well as the **Asset limit** for Starter or Pro plans.

![license-status.png](/docs/.document360/assets/article_007/image_002.jpg)

## Assets in Lansweeper On-premises

- For a count of all assets in your installation, select the **Assets** tab in the web console.  
  ![Licensed asset limit 1.png](/docs/.document360/assets/article_007/image_003.jpg)
- For a count of all licensed assets, assets that count toward your licensed asset limit, browse to the **Configuration > Your Lansweeper License** section.   
  ![Licensed asset limit 2.png](/docs/.document360/assets/article_007/image_004.jpg)
- Alternatively, go to the **Reports** section in the web console and run "Assets: All licensed assets in Lansweeper".  
  ![Licensed asset limit 3.png](/docs/.document360/assets/article_007/image_005.jpg)

## Example scenario

Consider the following example:

- A Lansweeper installation has a total of 450 assets listed in the **Assets** menu.
- The installation is licensed for 500 assets.
- 60 of the installation's assets are monitors. The rest are a mix of computers, Public Cloud workloads, OT cards, OT devices, and servers.
- 36 of the installation's monitors have extended display data and 24 do not.

In this example, the licensed asset count of the installation would be 426. That count would also be displayed in your Lansweeper Site under **Configuration > Installations > All installations**, and in your Lansweeper On-premises console under **Configuration > Your Lansweeper License**.

426 is the total asset count (450) minus the 24 monitor assets that do not have extended display data associated with them. The installation can scan another 74 assets before running into its licensed asset limit of 500 assets.
