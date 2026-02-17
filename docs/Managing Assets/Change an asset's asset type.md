<!-- # Change an asset's asset type -->
When Lansweeper scans an asset, it automatically tries to determine its type: Linux, Unix, Mac or Windows computer, VMware server, NAS, printer, switch, etc. It does this by looking at open ports and information pulled from the following protocols: Bonjour, DNS-SD, FTP, HTTP, HTTPS, JetDirect, DNS, SIP, SMTP, SNMP (SNMPv1, SNMPv2 or SNMPv3), SSDP, SSH, Telnet, UPnP, and WMI.

You may want to override scanned asset type information, however. There are two ways you can do this: by manually editing the asset or by remapping the asset's OID. Remapping is useful if you have many assets of the same model whose type you want to change.

You cannot change a Windows computer's type. An asset is automatically identified as Windows if port 135 is open on the asset and if you've submitted a valid credential. For Active Directory objects, the operating system attribute is also used to determine whether the asset is Windows or non-Windows. If the attribute includes the words "Windows" or "Hyper-V," the asset is deemed a Windows computer.

Many asset type names and icons are built-in. However, you can also [add your own](/docs/create-asset-types "Creating asset types").

## Manually changing asset types

To manually override the scanned asset type of one or more assets at once, try one of these three options:

- Browse to the asset's details and select **Edit asset** under **Asset options**. Select an asset type from the dropdown and ensure the box next to the dropdown is checked, indicating that your changes won't be overridden during scanning. Select **Save asset** to save your changes.
- Go to the **Assets** sections and select **Editing Mode** under **Options**. Place your cursor in the Type column, select an asset type from the dropdown, and select **Ok**.
- Go to the **Assets** section, tick the checkboxes in front of the assets of your choice, and select **Mass Edit Assets** under **Asset Actions**. In the resulting pop-up, select the Asset Type field, choose your preferred asset type for the assets you selected, and select **Change Field(s)**
  - You can search on one or more columns to easily find specific assets. In the example above, we filtered the Type column to only list music systems.
  - You could also tick the checkbox at the top to select all assets in the current search results.

## Changing asset types by remapping OIDs

To automatically have assets reassigned to your preferred asset type based on their OID, those assets must support SNMP.

1. Browse to an asset's detailed page and copy the OID listed on the page. If there is none, the asset either does not support SNMP or SNMP could not be scanned, e.g., due to the submitted SNMP community string being incorrect. If no OID exists, you could rescan the asset using a different community string or manually change the asset's type, as explained previously.
2. Browse to the **Configuration > Asset Mapping** section of the web console.  
   
3. Paste the OID into the SNMP OID search box found in the **Device SNMP OID lookup** section of the page. We want to verify whether the OID is already present in our database.
4. If there is a search result, the OID is present in your database, and you can change the asset type assigned to it by selecting a different option from the Type dropdown. You can change the model assigned to the OID by placing your cursor in the Model column, making the necessary change, and pressing **Enter** while your cursor is still in the line. Remember that the model name you submit here is only used for a device if one is not scanned from the device itself.
5. If there are no search results, the OID is not present in your database. You can add it by selecting **Add SNMP OID**. Paste the OID into the SNMP OID field of the pop-up window, select an option from the Device type dropdown, type the asset's model in the Model field, and select **Ok**. Remember that the model name you submit here is only used for a device if one is not scanned from the device itself.
6. Make sure your devices are submitted for scheduled scanning under **Scanning > Scanning Targets**. Any asset with a mapped OID will automatically be assigned the asset type of your choice when the asset is rescanned.
