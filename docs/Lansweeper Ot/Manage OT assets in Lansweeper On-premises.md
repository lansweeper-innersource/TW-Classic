<!-- # Manage OT assets in Lansweeper On-premises -->

This page is for Lansweeper On-premises. For Lansweeper Sites, see [Manage OT assets in Lansweeper Sites](/classic/docs/manage-ot-assets-in-lansweeper-sites).

Once you’ve installed Lansweeper, [scanned your OT environment](/classic/docs/scan-your-ot), and [linked your OT installation to On-prem](/classic/docs/link-network-discovery-hub-with-lansweeper-on-premises), you can manage your OT assets from your local web console.

Your OT installation needs at least version 3.4.0 to manage OT assets from the local web console.

## View OT assets

To view your OT assets in Lansweeper On-prem, go to **Assets > OT assets**.

Select any OT asset to display more detailed information about a specific asset. The summary page includes information such as its manufacturer, model, scan protocol, and more.

If the OT asset you’re viewing is a child module, the summary page will include information about the related main module.

You can visually identify your modules depending on their bus type by selecting **Bus Config**. You can find more information about the module, such as bus type, position, and name. The bus types are identified by their colour:

- DeviceNet is red
- ControlNet is blue
- BACnet is purple
- Backplane is grey

## Create OT assets

If the scanning service hasn't discovered a particular asset yet, or if an asset hasn't connected to your network yet, you can manually create OT assets.

If you create an OT asset in Lansweeper On-prem, that asset will only be available locally and will not sync to your OT Hub. The created asset will not be scanned.

1. In your web console, go to **Assets**.
2. Select **New asset**.
3. In the **Asset Type** dropdown, select **OT**.
4. Enter the asset’s information in the various fields.
5. Select **Save asset**.

## Edit OT assets

You can edit the details of your OT assets from the web console.

1. In your web console, go to **Assets > OT assets**. You can also enter “OT” in the **Type**field to display all OT assets.
2. Select the asset that you want to edit.
3. Select **Edit asset**.
4. Edit the asset’s information in the various fields.
5. Select **Save asset**.

Custom fields can also be added to OT assets.

OT assets cannot currently be bulk edited.
