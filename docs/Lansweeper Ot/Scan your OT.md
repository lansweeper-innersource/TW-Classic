<!-- # Scan your OT -->
![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_120/image_001.jpg) **This page explains how you can scan your industrial OT devices with Lansweeper.**

Operational technology (OT) is a category of hardware and software that monitors and controls physical assets. Industrial OT can be found on factory floors, e.g. in assembly lines and manufacturing plants. OT assets are becoming more and more network connected, allowing them to be scanned and analyzed.

[Lansweeper OT](https://www.lansweeper.com/use-cases/ot-asset-management/) is a new, standalone software designed to scan industrial OT. When installed and configured, it lets you retrieve data on your PLCs (Programmable Logic Controllers) and other industrial OT assets. Scanned properties include, among others: MAC address, manufacturer, model, serial number, firmware version and bus size info. Data retrieved by Lansweeper OT enables you to monitor the accessibility and security of your assets, prevent firmware vulnerabilities, plan maintenance and more.

You can scan your OT assets using one of two flows. The [default flow](#h85855550931675346298788) uses Lansweeper OT's smart scanning to detect both the IP range and the asset's protocol configuration. The [advanced flow](#h99593092371675346307360) allows you to customize this process, to cover your specific needs.

The advanced flow is only available when [linked to a Lansweeper On-premises installation](/docs/link-network-discovery-hub-with-lansweeper-on-premises).

## Supported protocols

Before you begin, review the list of [supported protocols](/docs/ot-supported-protocols "OT supported protocols") to ensure Lansweeper can scan your device.

## Scan your OT from Lansweeper Sites

Once you've set up your installation, you can start scanning your network.

You can create new Network Discovery actions in your Lansweeper Site. For detailed instructions on adding discovery actions, check out [Configure Network Discovery](/docs/configure-network-discovery).

Existing scanning targets can be [edited from your Lansweeper Site](/docs/configure-network-discovery), or locally in your Network Discovery hub. To edit your scan targets locally:

1. Use the **Lansweeper Network Discovery Hub** shortcut on your desktop to access the OT interface.
2. Select **Built-in Admin Login** to log in.
3. Go to **Scan targets**.
4. Select the scan target you want to edit.
5. Select **Save** to save your changes.

## Scan your OT from Lansweeper On-premises

Once you've set up your installation, you can start scanning your network. Use the **Lansweeper Network Discovery Hub** shortcut on your desktop to access the OT interface and select **Built-in Admin Login** to log in.

### Default flow

1. On the **Scan Targets** page, select **Default** to view your default scan targets.
2. Select **Add New**to create a new, default scan target.  
   ![add-scan-target.png](/docs/.document360/assets/article_120/image_002.jpg)
3. Optionally, if you have linked multiple sensors, select a sensor.  
   A default OT installation will only have one sensor. This field will only be visible if multiple sensors have been linked.
4. Enter a unique name for the new scan target.
5. Select the IP range you want to scan.   

   Lansweeper OT will automatically detect the network ranges based on information from the network interfaces linked to the selected sensor. If you want to change the proposed IP range, edit the IP range in the **Scan Targets** page.
6. Select a scan schedule. You can create custom scan schedules in the **Schedules** menu.
7. Optionally, you can enable or disable the scan target.
8. Select **Save**.

In the default flow, Lansweeper OT will detect the asset's protocol configuration using smart scanning.

Once you've added a new scan target, it will be scanned according to your chosen schedule. Alternatively, select the bullseye icon ![Scan your OT 1.png](/docs/.document360/assets/article_120/image_003.jpg) next to the target to start the scan.

If your OT installation can reach and pull data from the specified IP(s), assets will be generated and visible in the **Assets**menu. Click the eye icon ![Scan your OT 2.png](/docs/.document360/assets/article_120/image_004.jpg) next to an asset to view the asset details. In the case of a PLC, the entire PLC is considered one asset, with bus info being visible on the asset detail page.

Up to 10 assets can be viewed in your local OT installation. To view more assets, use the **Link With Cloud Site** option in your OT installation to link the installation with [Lansweeper Sites](https://app.lansweeper.com/). Your entire scanned OT inventory can be viewed in your Site.

### Advanced flow

1. On the **Scan Targets** page, select **Advanced** to view your advanced scan targets.
2. Select **Add New**to create a new, advanced scan target.
3. Optionally, if you have linked multiple sensors, select a sensor.  
   A default OT installation will only have one sensor. This field will only be visible if multiple sensors have been linked.
4. Enter a unique name for the new scan target.
5. Enter the IP address or IP range you want to scan.  

   Lansweeper OT will automatically detect the network ranges based on information from the network interfaces linked to the selected sensor.
6. Select a scan schedule. You can create custom scan schedules in the **Schedules** menu.
7. Select one or multiple protocol configurations you want to scan. You can create custom protocol configurations in the **Protocols** menu.
8. Optionally, you can enable or disable the scan target.
9. Select **Save**.

Once you've added a new scan target, it will be scanned according to your chosen schedule. Alternatively, select the bullseye icon ![Scan your OT 1.png](/docs/.document360/assets/article_120/image_005.jpg) next to the target to start the scan.

If your OT installation can reach and pull data from the specified IP(s), assets will be generated and visible in the **Assets**menu. Click the eye icon ![Scan your OT 2.png](/docs/.document360/assets/article_120/image_006.jpg) next to an asset to view the asset details. In the case of a PLC, the entire PLC is considered one asset, with bus info being visible on the asset detail page.

Up to 10 assets can be viewed in your local OT installation. To view more assets, use the **Link With Cloud Site** option in your OT installation to link the installation with [Lansweeper Sites](https://app.lansweeper.com/). Your entire scanned OT inventory can be viewed in your Site.
