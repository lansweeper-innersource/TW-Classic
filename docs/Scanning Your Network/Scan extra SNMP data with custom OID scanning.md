<!-- # Scan extra SNMP data with custom OID scanning -->
Custom OID scanning is a feature introduced in Lansweeper 7.0. You will need to [update your installation](http://lansweeper.com/knowledgebase/updating-your-installation/ "updating your installation") if you are running a lower Lansweeper version.

SNMP is one of the protocols through which Lansweeper can retrieve data from network devices like printers, switches, routers etc. By default, Lansweeper retrieves various properties from these devices via SNMP. This includes basic details like serial number and description, but also more advanced details like interface and printer toner information.

A device that has been successfully scanned via SNMP can be identified by the device OID listed in its **Summary** tab. In addition to this, the custom OID scanning feature allows you to retrieve any other information that is stored in an SNMP OID on the device.

Custom OID scanning lets you specify one or more OIDs to be scanned for a specific group of devices, giving you the ability to gather even more device data. Any device that has been successfully scanned via SNMP can be scanned further via custom OID scanning.



## Custom OID scanning

To scan specific OIDs of an SNMP enabled device, follow these steps:

1. Gather the OIDs you'd like to scan. This can be done by finding OIDs online, through MIB browsers or through vendor documentation.
2. Make sure your user role includes the **Access Data Selection** permission. If it doesn't, you won't be able to access the custom OID scanning configuration. More information on configuring website access and specifying who has what permissions can be found in [this knowledge base article](/docs/restrict-access-to-the-web-console).
3. Browse to the **Scanning > Custom OID Scanning**section of the web console.

   
4. Click the **Add Target** button at the top of the page. Alternatively, from Lansweeper 7.1 onward, you can import OIDs from or export them to another Lansweeper installation. Import/export instructions can be found in [this knowledge base article](/docs/import-and-export-custom-oid-scanning-targets).

   
5. From the Type dropdown in the resulting pop-up, select the collection of assets you want to retrieve the OID data for. You can retrieve the OID data for a single asset, assets in a specific static or dynamic asset group, assets of a specific type, assets in a specific IP range or assets in a specific asset report from the **Reports** menu.
6. Depending on what you selected before, choose your specific asset, group, asset type, IP range or report.
7. You can submit manufacturer and/or model as well.

   If you leave these fields empty, the OIDs will be scanned for all assets specified as target. If you fill in one or both of these fields, OIDs will only be scanned for the specified manufacturer/model within the target.   
   Keep in mind that, if you fill in the fields, what you submit must match what is listed as manufacturer/model on the device's asset page. This can either be the scanned manufacturer/model or what was manually overwritten. What you see listed on the asset page is the correct value to submit in the OID scanning configuration. If the manufacturer/model submitted in your OID configuration does not match what is listed on the asset page, no data will be scanned.
8. Make sure the **Enabled** checkbox is ticked.
9. Optionally, tick **Delete On Rescan**. This is a cleanup option to prevent old OID data from being left behind on asset pages. If ticked, Lansweeper will first delete the OID data associated with the target upon rescanning a specific device. It will then rescan the OID data and add fresh data to the device.
10. You can submit a description for your OID scanning target. This can be anything you want and is only displayed in your OID scanning configuration.
11. Submit your label and OID. The label can be anything you want, and is displayed next to scanned data on asset pages.

    
12. Make sure your devices are submitted for scheduled scans under **Scanning > Scanning Targets**, as custom OID data will be retrieved the next time the assets are scanned. You can of course manually rescan assets as well by using the **Rescan** buttons in asset overviews or on individual asset pages.
13. View scanned data in the Scanned OIDs tab of individual asset pages, by clicking on a label of a submitted OID or through built-in or custom reports in the **Reports** menu.

    

    
