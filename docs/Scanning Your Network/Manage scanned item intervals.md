<!-- # Manage scanned item intervals -->
To avoid unnecessary network traffic during agentless scanning, not all Windows and Linux computer data is rescanned all the time. As your computer's processor does not change on a regular basis for instance, it makes sense not to rescan this data during every scan attempt. By default, processor data is rescanned once every 50 days at most.

Each item scanned runs on its own schedule, which is called an "item interval" within Lansweeper Classic. Examples of other scan items are: BIOS, memory, OS, software and video card information. Though Lansweeper sets a default configuration for your item intervals, it is possible to customize these values to suit your needs.

Item intervals only exist for Windows data and a selection of Linux data, namely the Linux intervals starting with the word "Linux". There are no intervals for other types of assets. Other assets are always fully rescanned, during every successful scan attempt.

Item intervals only dictate which data is updated when a computer is actually rescanned. If a computer is no longer submitted for scanning, it will not be rescanned and its data will not be updated, regardless of what you set your intervals to.

To configure how often scan items are scanned:

1. Browse to the following section of the web console: **Scanning > Scanned Item Interval**.  
   
2. Click the **Enable**value of a particular scan item to select the scan mode.  
     
   - All Disabled: the scanned item is disabled and will never be scanned.
   - Scan Server and LsAgent: the scanned item will be scanned by the Scan Server and LsAgent.
   - LsAgent Only: the scanned item will be scanned by LsAgent, and the **Refresh**value cannot be set.
   - Scan Server Only: the scanned item will be scanned by the Scan Server.
3. Select the **Refresh**value of a particular scan item, make the desired change and press **Enter** to save the change.  
     
   - A value of 5 means that, when a computer is rescanned, the specified data will only be updated if it hasn't been updated in the last 5 days.
   - A value of 1 means that, when a computer is rescanned, the specified data will only be updated if it hasn't been updated in the last day.
   - A value of 0 means that, when a computer is rescanned, the specified data will always be updated.
   - Scan items marked in red are disabled and will never be scanned.
   - Scan items marked in gray cannot be disabled. Disabling these items would lead to unexpected scanning behavior.
4. The scanning targets and methods listed below respect item intervals. When Batch Scanning rescans a Windows computer for instance, it will (by default) only update OS information if that data hasn't been updated in the last 3 days.
   - Active Directory Domain
   - Workgroup
   - IP Range
   - Asset Group
   - Asset Type
   - Report
   - Windows Computer
   - Active Directory Computer Path
   - Batch Scanning
5. The scanning targets and methods listed below do not respect item intervals. When LsAgent rescans a Windows computer for instance, it will always update all (enabled) scan items, regardless of what their schedules are. All computer data will be refreshed.
   - Active Directory User/Group Path, as this only scans users and groups, not computers
   - Windows Computer (Eventlog only)
   - Active Directory Path (Eventlog only)
   - LsPush
   - Rescan buttons found on the left in asset overviews, reports and on webpages of individual computers
6. When you browse to a Windows computer's Lansweeper webpage and open the **Scan time** tab, you can see when a specific scan item was last rescanned for that computer.  
   
