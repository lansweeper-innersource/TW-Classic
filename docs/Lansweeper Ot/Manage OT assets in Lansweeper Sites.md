<!-- # Manage OT assets in Lansweeper Sites -->

This page is for Lansweeper Sites. For Lansweeper On-premises, see [Manage OT assets in Lansweeper On-premises](/docs/manage-ot-assets-in-lansweeper-on-premises).

Once you’ve installed Lansweeper, [scanned your OT environment](/docs/scan-your-ot) you can manage your OT assets from your Lansweeper Site.

There are a variety of options available to manage your OT assets. You can:

- [View OT assets](#viewOT)
- [Create OT assets](#createOT)
- [Edit OT assets](#editOT)
- [Create asset relationships](#relations)
- [Add OT assets to groups](#groups)
- [Add attachments or comments to OT assets](#attach)
- [Delete OT assets](#deleteOT)

Your OT installation needs at least version 3.4.0 to manage OT assets on your site.

## View OT assets

To view your OT assets in Lansweeper Sites, go to **Inventory > Asset types > OT**.

OT assets can also be viewed by creating [custom dashboards](/docs/manage-dashboards) or [reports](/docs/manage-reports).

From the **OT** view, you can sort your OT assets by [multiple columns](/docs/view-assets#sort) or [create advanced filters and custom views](/docs/view-assets#filter).

Select the OT asset and go to its Summary page to learn more about a specific asset. The summary page includes information such as its manufacturer, model, scan protocol, and more.

If the OT asset you’re viewing is a child module, the summary page will include information about the related main module.

You can visually identify your modules depending on their bus type by selecting **Bus Config**. You can find more information about the module, such as bus type, position, and name. The bus types are identified by their colour:

- DeviceNet is red
- ControlNet is blue
- BACnet is purple
- Backplane is grey

## Create OT assets

If the scanning service hasn't discovered a particular asset yet, or if an asset hasn't connected to your network yet, you can manually create OT assets.

If you create an OT asset in Lansweeper Sites, that asset will only be available in your site and will not sync to your OT Hub. The created asset will not be scanned.

1. In your Lansweeper Site, go to your **Inventory**.
2. Select **Add new asset**.
3. In the **Asset type** dropdown, select **OT**.
4. Enter the asset’s information in the various fields.  

   After selecting an installation to link to the asset and saving the changes, you can no longer change the associated installation.
5. Select **Save changes**.

## Edit OT assets

You can edit the details of individual OT assets from your site.

1. In your Lansweeper Site, go to **Inventory > Asset types > OT**. You can also search or [create an advanced filter](/docs/view-assets#h54067037961674828386919) to locate your OT assets.
2. Click the asset that you want to edit.
3. Select **Edit asset**.
4. Edit the assets' information in the various fields.
5. Select **Save changes**.

You can use the bulk edit feature to edit the details of multiple OT assets from your site.

1. In your Lansweeper Site, go to **Inventory > Asset types > OT**. You can also search or [create an advanced filter](/docs/view-assets#h54067037961674828386919) to locate your OT assets.
2. Select the assets that you want to edit.
3. Select **Bulk edit**.
4. In the pop-up, select a field to bulk edit, and enter a value.
5. Select **Add more fields** to continue editing, or **Save and apply**.

[Custom fields](/docs/edit-assets#customfield) can also be created and added to OT assets.
