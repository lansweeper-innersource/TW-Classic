<!-- # View and clear your scanning queue -->

To see which assets are currently being scanned by your Lansweeper installation and which are queued for scanning, browse to the **Scanning > Scanning Queue**section of the web console. If you have multiple scanning servers, there will be multiple tabs within this menu, one for each server. Within each tab, you can view and clear the scanning queue of a specific scanning server.

![menu-scanning-scanning-queue.jpg](/docs/.document360/assets/article_246/image_002.jpg)

![viewing-and-clearing-your-scanning-queue-1.jpg](/docs/.document360/assets/article_246/image_003.jpg)

There is a queue for viewing scanned IP addresses and one for viewing scanned Windows computers. If a Windows computer is scanned based on IP address, it will first show up in the IP queue and then move to the Windows queue once it's been identified as a Windows computer.

The following types of scans are not visible in your scanning queue but are processed silently in the background: [Active Directory User/Group Path](/docs/scanning-with-an-active-directory-usergroup-path-scanning-target), [AirWatch](/docs/scan-mobile-devices-through-vmware-workspace-one-uem-powered-by-airwatch), [AWS](/docs/scan-an-aws-cloud-environment), [Azure](/docs/scan-an-azure-cloud-environment), [Chrome OS](/docs/how-to-scan-chrome-os-machines), [Intune](/docs/scan-mobile-devices-through-microsoft-intune), [SCCM](/docs/integrate-lansweeper-with-sccm), [event log](/docs/scanning-with-an-eventlog-only-scanning-target) and [warranty scans](/docs/set-up-automated-warranty-checks).

Scans are performed in batches. Scans with a spinning wheel icon are currently in progress. The remaining scans are queued for processing. The number of concurrent scans is determined by the Computer Threads and IP Threads values configured in the **Service Options** section of the **Configuration > Server Options**page.

Computer thread or IP thread changes won't take effect until you restart the Lansweeper Server service on your Lansweeper server.

In general, new scan requests are added at the end of the queue and are processed when all previously initiated scans have finished. However, event log scans and scan requests initiated with Batch Scanning or the **Rescan** buttons are moved to the top of the scanning queue, if the specified assets are not already in the queue. These scans receive priority, though event log scans are not actually visible in the queue.

There is a **Clear queue** button per scanning server that allows you to remove any queued scan requests from the scanning queue of that server. Scans already in progress will still be completed.
