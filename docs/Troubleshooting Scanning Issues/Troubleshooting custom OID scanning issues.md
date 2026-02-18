<!-- # Troubleshooting custom OID scanning issues -->
Lansweeper allows you to [scan extra SNMP data with custom OID scanning](/classic/docs/scan-extra-snmp-data-with-custom-oid-scanning).

If you've submitted custom OIDs for scanning but data is not being returned:

1. Make sure your Lansweeper license allows access to the custom OID scanning feature.
2. Make sure there is an OID listed in the device's Summary tab, indicating that Lansweeper is able to access the SNMP protocol on the device. If there isn't, [troubleshoot the SNMP access issue](/classic/docs/troubleshoot-snmp-scanning-issues "Troubleshooting SNMP scanning issues"). Custom OID scanning cannot retrieve data if the SNMP protocol in general is not accessible on the device.

   
3. Go to **Scanning > Custom OID** scanning and make sure the **Enabled** checkbox is selected.

   
4. Make sure your OID target is applied to the correct assets. If you choose Asset Type as your Target Type for instance, make sure the chosen asset type corresponds with the asset type of your device.  

   If you choose **Asset Type** as your **Target Type**, you must submit the asset type Lansweeper detects for your devices during scanning. If you manually edit a device's asset type, or if asset types are [automatically changed by remapping OIDs](/classic/docs/change-an-assets-asset-type#heading2), custom OID scanning will not take this into account.
5. Make sure your OID target's Manufacturer and Model are either empty or correspond exactly with what is listed on the device's Lansweeper webpage.

   

   
6. Make sure the OID submitted in your OID target is correct and contains data. You can use the tool below, found on your Lansweeper server, for troubleshooting. Run the tool from your Lansweeper server and submit your device's IP address and SNMP scanning credential. In the SNMP Custom OIDs field, submit the OIDs you'd like to test. Multiple OIDs can be submitted, separated with commas.

   Program Files (x86)\Lansweeper\Actions\Devicetester.exe

   
7. Rescan the network device be selecting **Rescan Asset** on the device's Lansweeper webpage.
8. Check the **Scanned OIDs** tab on individual asset pages or reports in the **Reports** tab for the retrieved data.

   
