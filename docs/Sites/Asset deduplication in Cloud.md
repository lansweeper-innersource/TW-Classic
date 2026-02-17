<!-- # Asset deduplication in Cloud -->
In specific situations, duplicate assets can be generated in your inventory. These duplicate assets could be intended or unintended. To handle these duplicates, we introduced asset deduplication in [Lansweeper](https://www.lansweeper.com/) Cloud. This helps you identify these duplicates and solve the duplication conflicts. It also allows you to prevent these duplicates from showing up again in your inventory.

## Asset deduplication

Assets that share the same MAC address, model and serial number will be identified as possible duplicates. Duplicate assets will be marked with a duplicate icon in the **Inventory >****All Assets** view.  
![Asset-dedup-1.jpg](/docs/.document360/assets/article_335/image_002.jpg)

All duplication conflicts can be viewed in the **Inventory > Duplicate conflicts**menu.  
![Asset-dedup-2.jpg](/docs/.document360/assets/article_335/image_003.jpg)

## Solve a duplication conflict

1. In the **Inventory****> All assets**menu, hover over the Duplicates icon next to the asset and select **Solve duplicate conflict**.   
   Alternatively, go to the **Inventory > Duplicate conflicts** menu, find the duplicated assets, and select **Solve duplicate conflict**.
2. In the pop-up window, select the affected assets. Both duplicates and correct assets need to be selected.![Deduplication 1.png](/docs/.document360/assets/article_335/image_004.jpg)  

   If you select **None are duplicated**, the assets will remain in your inventory, and they will be flagged not to show up as duplicates in the future.
3. Select **Continue**, and select the asset(s) you want to keep in your inventory.  
   ![Deduplication 2.png](/docs/.document360/assets/article_335/image_005.jpg)
4. Before selecting **Solve duplicate conflict**, you can indicate if you want to delete the duplicate assets from your on-prem installation as well.  
   ![Deduplication 3.png](/docs/.document360/assets/article_335/image_006.jpg)  

   If you choose to delete the duplicates from the local web console, they will be automatically deleted from your on-prem inventory.  
   Please note that when no scanning exclusion is present for these assets, they could potentially be scanned again and synced with your cloud site. To prevent this, make sure to [add a scanning exclusion](/docs/exclude-assets-from-scanning) in your on-prem installation. If you don't check the option to delete the assets from the local web console, they will instead be flagged in your on-prem installation to not be synced again to Cloud.
5. Select **Solve duplicate conflict**.

The duplicate conflict has now been resolved.
