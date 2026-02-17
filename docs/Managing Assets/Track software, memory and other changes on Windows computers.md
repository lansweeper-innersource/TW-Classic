<!-- # Track software, memory and other changes on Windows computers -->
A Windows computer's Lansweeper Classic webpage lists the most recently scanned properties of the machine's software, OS, memory and other details. Details like software, OS and memory are called scan items.

It is possible to [enable or disable scanning of scan items](/docs/manage-scanned-item-intervals), as well as to specify the scanning schedule for each. Not only can you specify whether and how often scan items are scanned, but you can also enable history tracking for most of these. In other words, you can not only see the current status of a scan item, but also any changes that occurred. These changes can be major or minor.

By enabling tracking of software changes for instance, you can detect software updates, additions and removals. By enabling history tracking for the OS, you can detect both OS upgrades and reinstallations. In essence, if a change is detected in any aspect or column of a scan item, it is written as history into the Lansweeper database.

To conserve database space, history tracking is disabled by default for most scan items. It can be manually enabled, however.

## Enable tracking of changes

1. Browse to the **Scanning > Scanned Item Interval**section of the web console.![menu-scanning-scanned-item-interval.jpg](/docs/.document360/assets/article_139/image_001.jpg)
2. Tick the History checkbox for any scan item you want to keep a history of and whose History box isn't grayed out.![tracking-software-memory-and-other-changes-on-windows-computers-1.jpg](/docs/.document360/assets/article_139/image_002.jpg)  

   Lansweeper will start keeping a history of the specified scan item from the moment the History checkbox is ticked. History is not gathered retroactively.
3. Make sure your Windows computers are rescanned on a regular basis, so changes are detected. Scanning schedules can be configured in the **Scanning > Scanning Targets** section of the web console.

## Viewing tracked software and other changes

Once changes in the specified scan items have been detected, view them in the web console using any of these options:

- Browse to a specific Windows computer's Lansweeper webpage and open the **History** tab.![tracking-software-memory-and-other-changes-on-windows-computers-2.jpg](/docs/.document360/assets/article_139/image_003.jpg)
- Open the **Reports > Changes By Type** menu in the web console. This page categorizes detected changes by scan item, allowing you to pick a scan item on the left and then see related changes for all Windows computers.![menu-reports-changes-by-type.jpg](/docs/.document360/assets/article_139/image_004.jpg)
- Open the **Reports > Configuration History** menu in the web console. This page lists detected changes for all Windows computers, in descending chronological order.
- Open one of the other built-in reports in the **Reports** menu, e.g. one of the reports below.
  - Computer: Memory changes
  - Software: Changes in the last 24 hours
  - Software: Changes in the last 7 days
- Build a custom report under **Reports > Create New Report**. Historical Windows computer data is stored in database tables ending in Hist.  

  A Windows computer's current OS is stored in tblOperatingsystem, while OS changes are stored in tblOperatingsystemHist. Each history table has an Action column. An Action value of 1 means that the item was added, while a value of 2 means that the item was removed. Certain changes will cause both a 1 and 2 record to be generated. When a computer's software or OS is updated for instance, as it will show as a a removal of the old software/OS version (2) and an addition of the new software/OS version (1). Using Cases, the 1 and 2 values can be displayed as + and - within the report results.
