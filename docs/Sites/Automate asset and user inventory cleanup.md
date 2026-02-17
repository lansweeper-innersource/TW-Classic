<!-- # Automate asset and user inventory cleanup -->
![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_332/image_001.jpg) **This page explains the various options provided by Lansweeper Sites to manage your inventory. You will also find information on where to locate these options and gain insight into their specific functionalities.**

Once an asset is scanned and added to your inventory, Lansweeper will not remove it unless instructed to do so.

You can either manually delete old assets, or have them deleted automatically using several cleanup rules.

[Asset cleanup rules](#asset) and [user cleanup rules](#user) are managed separately: enabling asset cleanup rules in Lansweeper Sites will **only** disable asset rules in Lansweeper On-prem; enabling user cleanup rules in Lansweeper Sites will **only** disable user cleanup rules in Lansweeper On-prem.

If your site is linked to a Lansweeper On-prem installation that currently manages your cleanup rules, saving changes in your site will permanently transfer cleanup rule management to Lansweeper Sites and disable on-prem management.   
Update Lansweeper On-prem to version **12.5.1.1** or higher to ensure cleanup rules are properly disabled; On-prem rules will otherwise not be blocked after switching to Lansweeper Sites.

## Asset cleanup rules

To manage asset cleanup rules:

1. In your Lansweeper Site, go to your **Inventory.**
2. Select **Manage cleanup rules**.
3. After managing your asset cleanup rules, select **Save changes**.

Below is an overview of currently available asset cleanup rules.

### All assets

- **Set non-active assets as active when they are rescanned**

  Automatically set any “non-active” asset to "active" when it is rescanned.
- **Set assets to non-active if not seen in the last X days**  
  Sets the state of assets to "non-active" if they have not been detected within the last X days. This setting only affects assets that have been successfully scanned at least once.

  "Non-active" assets are excluded from most reports.
- **Permanently delete assets not seen in the last X days**Deletes any assets from your Lansweeper inventory if they have not been detected in the last X days. This setting only affects assets that have been successfully scanned at least once.  

  Deleting assets cannot be undone without restoring a database backup.

### Network visibility (Asset radar)

- **Set passively detected assets to non-active if not seen in the last X days**  
  Sets the state of passively detected assets to "non-active" if they have not been detected within the last X days. This setting only affects assets that have been successfully scanned at least once.
- **Permanently delete passively detected assets not seen in the last X days**  
  Deletes any passively detected assets from your Lansweeper inventory if they have not been detected in the last X days. This setting only affects assets that have been successfully scanned at least once.
- **Set passively detected****assets** **of the types “Unknown” and “Network device” to non-active if not seen in the last X days**  
  Sets the state of “Unknown” and “Network device” assets to "non-active" if they have not been detected within the last X days. This setting only affects assets that have been successfully scanned at least once.
- **Permanently delete passively detected assets of the types “Unknown” and “Network device” if not seen in the last X days**  
  Deletes “Unknown” and “Network device” assets from your Lansweeper inventory if they have not been detected in the last X days. This setting only affects assets that have been successfully scanned at least once.

### Active Directory

- **Permanently delete computers disabled in Active Directory**Deletes any computers from your Lansweeper inventory if they are disabled in Active Directory. This setting only affects assets that have been successfully scanned at least once.
- **Set computers to non-active if disabled in Active Directory**Sets the state of computers to "non-active" if they are disabled in Active Directory. This setting only affects assets that have been successfully scanned at least once.

## User cleanup rules

To manage user cleanup rules:

1. In your Lansweeper Site, go to **Users**.
2. Select **Manage cleanup rules**.
3. After managing your user cleanup rules, select **Save changes**.

Below is an overview of currently available user cleanup rules.

### All users

- **Permanently delete users disabled in Active Directory**  
  Removes any users from your Lansweeper inventory if they are disabled in Active Directory. This setting only affects users that have been successfully scanned at least once.
