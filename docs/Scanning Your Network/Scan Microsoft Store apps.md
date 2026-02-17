<!-- # Scan Microsoft Store apps -->

Microsoft Store app scanning was introduced in Lansweeper 9.3 and further optimized in Lansweeper 9.5. You will need to [update your installation](http://lansweeper.com/knowledgebase/updating-your-installation/ "updating your installation") if you are running a lower Lansweeper version.

For many years, Lansweeper has scanned desktop software seen in Add/Remove Programs on Windows client machines, as well as software found on Linux and Mac computers. From version 9.3 onward, Lansweeper is also capable of scanning apps installed through the Microsoft Store, formerly known as Windows Store, on Windows computers. These Store apps are also called UWP apps or Universal Windows Platform apps.

Lansweeper now scans the name, version number, publisher and install date of Store apps installed under a Windows computer's last logged on user.   
This article explains how to set up Store app scanning and how to view the app data in Lansweeper.

## Configure client machines for scanning

Like other software, Lansweeper retrieves Store apps through a combination of WMI (Windows Management Instrumentation) and the registry of the client machine. To scan the Store apps of a Windows computer, make sure the machine meets [the general Windows scanning requirements](/docs/windows-domain-scanning-requirements). If you can successfully scan the machine, the Store apps will be successfully retrieved as well.

## Enable Store app scanning

Store app scanning is disabled by default in new Lansweeper installations and installations updated from a version older than 9.3.   
To enable Store app scanning, browse to the **Scanning > Scanned Item Interval** menu of the web console. Here, tick the **Enable** checkbox for the SOFTWAREMSSTOREAPPS item. The default [refresh interval](/docs/manage-scanned-item-intervals) of the item is 1 day.

![menu-scanning-scanned-item-interval.png](/docs/.document360/assets/article_223/image_002.jpg)

## Scan Store app data

Once you've completed the previous steps, fully rescan your client machines to immediately retrieve the Store app data.   
For instance, click the **Assets**menu at the top of the web console, filter the **Type** column for Windows computers, tick the upper checkbox to select all assets and click **Rescan asset(s)**. Note that you must use an agentless scanning method or LsAgent to scan your client machines, as the older LsPush agent does not scan drivers.

If you rescan your computers with one of the **Rescan** buttons found throughout the web console, the apps of each computer's currently logged on user will immediately be retrieved as part of the rescan. If you use another scanning method like an IP range target, the app data being refreshed will depend on how you configured the SOFTWAREMSSTOREAPPS item interval. With a default SOFTWAREMSSTOREAPPS interval of 1 day for instance, an IP range scan will only refresh app data every 24 hours at most.

![rescan-windows-computers.png](/docs/.document360/assets/article_223/image_003.jpg)

## View Store app data

Scanned Store apps can be viewed in the **Software > Software** tab of individual Windows asset pages. At the top of the tab, a drop-down menu is available that allows you to filter the listed software. To view Store apps, choose either **Show All Software** or **Show Microsoft Store apps**. Store apps are marked with a blue Store app icon in the software list.

![scanned-microsoft-store-apps.png](/docs/.document360/assets/article_223/image_004.jpg)

You can search for apps using [the web console search bar](/docs/search-through-assets-with-the-web-console-search-bar), as is the case for other software. You can also use built-in or custom reports to view app data. Perform a search for "software" in the **Reports** menu of the web console to find built-in software reports. There is a built-in report listing only apps, called "Windows: Installed Microsoft Store apps by computer". There are also reports listing both apps and desktop software, which usually have a Type column so you can differentiate between the two software types.   
If you want to build a custom report, an easy way to do so is by editing a built-in report and choosing **Save As** from the report builder. This creates a copy of the report that you can customize further.

Like other software found on Windows computers, Store apps can be [marked as authorized, unauthorized or unrated](/docs/mark-software-and-add-ons-as-authorized). This can be done in the **Software > Authorization** menu of the web console. Unlike the software authorization module, the software license compliance module does not include Store apps, due to their user-specific nature.
