<!-- # Software on Windows computer not being scanned -->

Lansweeper scans Windows computers in your network for installed software. Software information scanned by Lansweeper for Windows computers mimics Windows' Programs and Features on the computer itself.

For more information, see [View and scan software installations on Windows computers](/docs/view-and-scan-software-installations-on-windows-computers).

If there is software installed on a Windows computer that you do not see listed in Lansweeper:

## Ensure the hosting server has sufficient disk space

In your machine, locate your Devices and drives file and check the Local disk has sufficient space.



## Ensure your database is not too large

1. In the Lansweeper Classic web console, go to **Dashboard > Main page**.
2. Locate the **Scanning Status** widget and confirm the database has not reached its limit.
3. If you've reached your size limit, the scanning service cannot write additional assets to the database. [Perform a database cleanup](/docs/clear-tables-to-free-up-space-and-improve-performance) to continue scanning.

   

   For more information about available databases and their size limitations, see [Compatible SQL database servers for hosting the Lansweeper database](/docs/compatible-sql-database-servers-for-hosting-the-lansweeper-database "Compatible SQL database servers for hosting the Lansweeper database").

## Ensure the number of assets does not exceed your license limit

1. In the Lansweeper Classic web console, go to **Configuration > Your Lansweeper license**.
2. Ensure the **Licensed assets** count does not exceed the **Asset limit**.

   Most Lansweeper licenses limit the number of assets you can scan. Once you've reached [your licensed asset limit](/docs/assets-that-count-toward-your-licensed-asset-limit), you can not scan new or existing assets until you [delete assets](/docs/delete-assets "Delete assets") or [upgrade your license](https://www.lansweeper.com/pricing/ "Pricing & Plans").

## Update Lansweeper

1. In the web console, go to **Configuration > Your Lansweeper license**.
2. Select **Check for updates now**.
3. If your Lansweeper installation is out of date, select **Download now** to update your installation.

For more information, see [Update Lansweeper Classic](/docs/update-lansweeper-on-premises).

## Use the latest LsPush executable

When you update your Lansweeper installation, the latest version of the LsPush executable is also updated. If you are using a logon script, group policy, or scheduled task:

1. In **File explorer**, navigate to **Program Files (x86)\Lansweeper\Client**.
2. Copy **lspush.exe** to your clipboard.
3. Paste the executable to the folder referenced by your script, policy, or task.



## **Ensure software is listed in Programs and Features**

1. In your Windows system, go to **Control Panel > Programs > Programs and Features**.
2. Search through the list of programs to ensure the software is listed. If the software is not listed, it will not be scanned, as Lansweeper recreates this software list to scan.   
   To scan the software, try using the [file scanning](/docs/windows-custom-file-scanning) or [registry scanning](/docs/scan-registry-values-with-custom-registry-scanning) features instead.

## Rescan the machine's software

If software information was not recently rescanned, this can explain why the scanned software list is not up-to-date.

1. In the web console, go to **Assets**.
2. Find your machine and select the checkbox for it, then select **Rescan asset(s)**.

Most scanning methods respect item intervals and will by default only scan software information once every 24 hours at most. More info on configuring intervals can be found in [Managing how often specific data is scanned](/docs/manage-scanned-item-intervals).   
The Rescan button ignores intervals and rescans all of a Windows computer's data, including software.

## Ensure software is installed for each user

In your Windows computer, log into each user profile and verify the software is installed for each user. Some software packages allow you to install them for specific user profiles on a computer. If software is only installed for a specific user on a computer:

- It will not be listed in the computer's Software tab if that user was not logged into the computer when the machine was last rescanned.
- It will be listed in the computer's Software tab if that user was logged into the computer when the machine was last rescanned. The software will then have a little icon accompanying it to indicate that it's user-specific.


