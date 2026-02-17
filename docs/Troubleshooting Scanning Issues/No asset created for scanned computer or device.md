<!-- # No asset created for scanned computer or device -->

If you have attempted to scan a computer or device, but no asset was created for it in the web console, it may be related to a variety of issues.

Work through the following steps to ensure an asset is created for your scanned computer or device:

1. [Confirm the asset does not exist](#assetnoexist "Confirm the asset does not exist")
2. [Update Lansweeper](#update "Update Lansweeper")
3. [Ensure Lansweeper Server service is running](#serverrunning "Ensure Lansweeper Server service is running")
4. [Ensure the number of assets does not exceed your license limit](#number "Ensure the number of assets does not exceed your license limit")
5. [Ensure your database is not too large](#database "Ensure your database is not too large")
6. [Ensure the hosting server has sufficient disk space](#disk "Ensure the hosting server has sufficient disk space")
7. [Verify the client machine is online](#client "Verify the client machine is online")
8. [Add the IP range as a scanning target](#IPrange "Add the IP range as a scanning target")
9. [Ensure the machine is not excluded from scanning](#exclude "Ensure the machine is not excluded from scanning")
10. [Submit appropriate scanning credentials](#credentials "Submit appropriate scanning credentials")
11. [Verify scanning requirements](#requirements "Verify scanning requirements")

Once you've completed the above steps, [rescan your machine](#h_539106825951680707669206 "Rescan your machine").

## Confirm the asset does not exist

In the web console's search bar, enter your machine's following information:

- Name
- IP adress
- MAC address

![search-bar.png](/docs/.document360/assets/article_259/image_002.jpg)

If an asset with your machine's information does not appear, continue with the following troubleshooting steps.

## Update Lansweeper

1. In the web console, go to **Configuration > Your Lansweeper license**.
2. Select **Check for updates now**.
3. If your Lansweeper installation is out of date, select **Download now** to update your installation.

## Ensure the Lansweeper Server service is running

By default, the Lansweeper Server service automatically starts and scans your data. However, it may have been manually stopped, which would stop scanning and not allow new assets to be created.

1. Navigate to **Windows Services**.
2. Locate and right-click **Lansweeper Server** from the list.
3. If the server has stopped, select **Start**.  

   ![procedure-starting-the-lansweeper-service.jpg](/docs/.document360/assets/article_259/image_003.jpg)

## Ensure the number of assets does not exceed your license limit

1. In the Lansweeper Classic web console, go to **Configuration > Your Lansweeper license**.
2. Ensure the **Licensed assets** count does not exceed the **Asset limit**.

   Most Lansweeper licenses limit the number of assets you can scan. Once you've reached [your licensed asset limit](/docs/assets-that-count-toward-your-licensed-asset-limit), you can not scan new or existing assets until you [delete assets](/docs/delete-assets "Delete assets") or [upgrade your license](https://www.lansweeper.com/pricing/ "Pricing & Plans").

## Ensure your database is not too large

1. In the Lansweeper Classic web console, go to **Dashboard > Main page**.
2. Locate the **Scanning Status** widget and confirm the database has not reached its limit.
3. If you've reached your size limit, the scanning service cannot write additional assets to the database. [Perform a database cleanup](/docs/clear-tables-to-free-up-space-and-improve-performance) to continue scanning.

   ![no-asset-created-for-scanned-computer-or-device-3.jpg](/docs/.document360/assets/article_259/image_004.jpg)

   For more information about available databases and their size limitations, see [Compatible SQL database servers for hosting the Lansweeper database](/docs/compatible-sql-database-servers-for-hosting-the-lansweeper-database "Compatible SQL database servers for hosting the Lansweeper database").

## Ensure the hosting server has sufficient disk space

In your machine, locate your Devices and drives file and check the Local disk has sufficient space.

![sophie_1-1680701720366.png](/docs/.document360/assets/article_259/image_005.jpg)

## Verify the client machine is online

1. Open a Command Prompt window on your Lansweeper server.
2. Ping the client machine to ensure it is online.

![no-asset-created-for-scanned-computer-or-device-5.jpg](/docs/.document360/assets/article_259/image_006.jpg)

## Add the IP range as a scanning target

1. In Lansweeper Classic's web console, go to **Scanning > Scanning targets**.
2. Select **Add scanning target**.
3. Set the **Target Type** to **IP Range**.
4. Enter the machine's IP range.
5. Select the **Save pinged IP**checkbox.
6. If the machine is Linux, Unix, Mac, or Windows computer, ensure the **Ignore Windows** and **No SSH** are unchecked.  
   ![sophie_2-1680702657653.png](/docs/.document360/assets/article_259/image_007.jpg)
7. Select **OK**.  

   For more information, see [Scanning with an IP Range scanning target](/docs/scanning-with-an-ip-range-scanning-target).

## Ensure the machine is not excluded from scanning

1. In Lansweeper Classic's web console, go to Scanning > Scanning targets.
2. Navigate to the **Scanning exclusions** section of the page.
3. Check the machine has not been excluded based on name, domain, IP address, IP range or asset type. No assets are created for machines that are excluded from scanning.![no-asset-created-for-scanned-computer-or-device-7.jpg](/docs/.document360/assets/article_259/image_008.jpg)

Pay attention to wildcards used in Windows Computer exclusions. In the example above, any Windows computer whose name contains the word "LAN" will not be scanned.

## Submit appropriate scanning credentials

Submit a scanning credential if your machine is one of the following:

- Linux
- Unix
- Mac
- Windows
- VMware server
- SNMP enabled network device

For more information on adding scanning credentials and the information required, see [Creating and mapping scanning credentials](/docs/create-and-map-scanning-credentials).

Once the scanning credential is created:

1. In **Scanning > Scanning credentials**.
2. In the **Credential mapping** section of the page, find your machine's IP range and select **Credential**.   
   ![no-asset-created-for-scanned-computer-or-device-9.jpg](/docs/.document360/assets/article_259/image_009.jpg)
3. Select the credential you created, then **Add**.

## Verify scanning requirements

Verify your machine fulfills the necessary scanning requirements. Review the following articles for more information:

- [Windows domain scanning requirements](/docs/windows-domain-scanning-requirements)
- [Windows workgroup scanning requirements](/docs/windows-workgroup-scanning-requirements)
- [Linux and Unix scanning requirements](/docs/linux-and-unix-agentless-scanning-requirements)
- [Apple Mac scanning requirements](/docs/apple-mac-scanning-requirements)
- [VMware server scanning requirements](/docs/vmware-server-scanning-requirements)
- [Network device scanning requirements](/docs/network-device-scanning-requirements)

## Rescan your machine

1. In Lansweeper Classic's web console, go to **Scanning > Scanning targets**.
2. Find your machine's IP range in the list.
3. Select **Scan now**.  
   ![no-asset-created-for-scanned-computer-or-device-10.jpg](/docs/.document360/assets/article_259/image_010.jpg)
4. Once the scan is complete, [search for the machine](#assetnoexist "Confirm the asset does not exist").
