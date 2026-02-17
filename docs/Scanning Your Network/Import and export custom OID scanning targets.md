<!-- # Import and export custom OID scanning targets -->
The ability to import/export OID scanning targets was introduced in Lansweeper 7.1. You will need to [update your installation](http://lansweeper.com/knowledgebase/updating-your-installation/ "updating your installation") if you are running a lower Lansweeper version.

From version 7.1 onward, Lansweeper allows you to import and export custom SNMP OID targets into and from other Lansweeper installations. This enables you to migrate your custom OID scanning targets between installations and to share targets with other Lansweeper users, e.g. through [our online forum](https://www.lansweeper.com/forum/yaf_topics35_Custom-OID-Sharing.aspx).

SNMP is one of the protocols through which Lansweeper can retrieve data from network devices like printers, switches, routers etc. By default, Lansweeper retrieves various properties from these devices via SNMP. This includes basic details like serial number and description, but also more advanced details like interface and printer toner information. A device that has been successfully scanned via SNMP can be identified by the device OID listed in its **Summary** tab.   
In addition to this, [the custom OID scanning feature](/docs/scan-extra-snmp-data-with-custom-oid-scanning) allows you to retrieve any other information that is stored in an SNMP OID on the device. Custom OID scanning targets can be manually created and from Lansweeper 7.1 onward imported.

## Exporting custom OID scanning targets

To export custom OID scanning targets, follow these steps:

1. Browse to the following section of the web console: **Scanning > Custom OID Scanning**.

   ![menu-scanning-custom-oid-scanning.jpg](/docs/.document360/assets/article_196/image_001.jpg)
2. Tick the checkboxes of any custom OID scanning targets you want to export. Alternatively, tick the checkbox at the top to select all targets.
3. Click **Export** at the top of the page.

   ![importing-and-exporting-custom-oid-scanning-targets-1.jpg](/docs/.document360/assets/article_196/image_002.jpg)
4. In the resulting pop-up, you can uncheck parts of the OID targets that you do not want to export.

   ![importing-and-exporting-custom-oid-scanning-targets-2.jpg](/docs/.document360/assets/article_196/image_003.jpg)
5. Click the **Export** button. The OID targets you've selected are exported in XML format and added to a file ending in .ls.oid. They can now be imported into another Lansweeper installation.

   ![importing-and-exporting-custom-oid-scanning-targets-3.jpg](/docs/.document360/assets/article_196/image_004.jpg)

## Importing custom OID scanning targets

To import custom OID scanning targets, follow these steps:

1. Find a .ls.oid file you want to import. Any OID target configuration that was exported from another Lansweeper installation to a .ls.oid file can be imported into yours.
2. Browse to the following section of the web console: **Scanning > Custom OID Scanning**.

   ![menu-scanning-custom-oid-scanning.jpg](/docs/.document360/assets/article_196/image_005.jpg)
3. Click **Import** at the top of the page.
4. Select **Browse...** or **Choose File** in the resulting pop-up, select your .ls.oid file and click **Open**.

   ![importing-and-exporting-custom-oid-scanning-targets-4.jpg](/docs/.document360/assets/article_196/image_006.jpg)
5. In the resulting pop-up, you can uncheck parts of the OID targets that you do not want to import.
6. You can change other settings of the OID targets to be imported: description, target type, target, manufacturer or model.
7. Click the **Import** button. The OID targets you've selected are now imported into your Lansweeper installation. The OID data will be retrieved for the specified assets once those assets are rescanned.

   ![importing-and-exporting-custom-oid-scanning-targets-5.jpg](/docs/.document360/assets/article_196/image_007.jpg)
