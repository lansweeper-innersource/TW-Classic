<!-- # Add comments to assets -->
1. Browse to the asset's Lansweeper webpage and select **Add comment** in the **Comments** tab of the page.
2. Enter a comment into the pop-up window and select **Ok**. There is a comment count in the **Comments** tab header. This allows you to quickly identify machines with comments, without actually opening the **Comments** tab.  

   Comments added to the **Comments** tab are stored in the tblAssetComments database table. You'll notice, when you select **Edit Asset** on an asset page, that there's another Comments field at the bottom of the page. If filled in, this field is shown in the **Summary** tab of the asset's Lansweeper webpage. It is solely provided for backward compatibility with old Lansweeper releases and stores data in the Comments field of tblAssetCustom, not in tblAssetComments.

   You can prevent users from adding comments to the **Comments** tab. More info on restricting web console access can be found in [this knowledge base article](/docs/restrict-access-to-the-web-console).
