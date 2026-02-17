<!-- # Scanning Windows drivers -->

Lansweeper is capable of scanning system drivers, PnP (plug and play) drivers and printer drivers installed on Windows computers. Scanned data includes driver name, version, manufacturer, path, state, release date and more!

This knowledge base article explains how to set up driver scanning and how to view the driver data in Lansweeper:

1. [Configure client machines for scanning](#heading1)
2. [Enable driver scanning](#heading2)
3. [Scan driver data](#heading3)
4. [View driver data](#heading4)

![scanned-windows-drivers.png](/docs/.document360/assets/article_228/image_002.jpg)

## Configure client machines for scanning

Like other data, Lansweeper retrieves drivers through a combination of WMI (Windows Management Instrumentation) and the registry of the client machine. To scan the drivers of a Windows computer, make sure the machine meets [the general Windows scanning requirements](/docs/windows-domain-scanning-requirements). If you can successfully scan the machine, the drivers will be successfully retrieved as well.

## Enable driver scanning

To enable driver scanning, browse to the **Scanning > Scanned Item Interval** menu of the web console.   
Tick the **Enable** checkbox for the PNPSIGNEDDRIVERS, PRINTERDRIVERS and/or SYSTEMDRIVERS item. The default [refresh interval](/docs/manage-scanned-item-intervals) of each of these items is 6 days.

The WMI class storing system driver data is inherently heavy to read. Scanning system drivers can therefore impact client machine performance. It is recommended that you only enable system driver scanning if you have a specific need for it. Refresh the data as infrequently as possible as well, by increasing the SYSTEMDRIVERS refresh setting if possible.

![menu-scanning-scanned-item-interval.png](/docs/.document360/assets/article_228/image_003.jpg)

## Scan driver data

Once you've completed the previous steps, fully rescan your client machines to immediately retrieve the driver data.

For instance, click the **Assets** menu at the top of the web console, filter the **Type** column for Windows computers, tick the upper checkbox to select all assets and click **Rescan asset(s)**. Note that you must use an agentless scanning method or LsAgent to scan your client machines, as the older LsPush agent does not scan drivers.   
If you rescan your computers with one of the **Rescan** buttons found throughout the web console, the computers' drivers will immediately be retrieved as part of the rescan. If you use another scanning method like an IP range target, the driver data being refreshed will depend on how you configured your scanned item intervals. With default driver intervals of 6 days for instance, an IP range scan will only refresh driver data every 6 days at most.

![rescan-windows-computers.png](/docs/.document360/assets/article_228/image_004.jpg)

## View driver data

Scanned drivers can be viewed in the **Config> Windows > Drivers** tab of individual Windows asset pages. There are sub-tabs for system drivers, PnP signed drivers and printer drivers.

You can also use built-in or custom reports to view driver data. Perform a search for "driver" in the **Reports** menu of the web console to find built-in driver reports.   
If you want to build a custom report, an easy way to do so is by editing a built-in report and choosing **Save As** from the report builder. This creates a copy of the report that you can customize further.
