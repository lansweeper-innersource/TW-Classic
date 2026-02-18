<!-- # Add manufacturer support links -->
The serial number of Dell and HP assets is clickable in the **Summary**tab, for assets whose asset serial was scanned. The serial link takes you to the page on Dell or HP's website that lists that specific asset's warranty information, so you don't need to manually look up warranty details.

These manufacturer support links are customizable, and you can add your own for additional vendors.



Manufacturer support links are only used to make asset serials on individual asset pages clickable and to link them to warranty pages on the vendors' websites. They are not used to automatically scan or add warranty information to Lansweeper.   
Lansweeper includes a [warranty scanning](/classic/docs/set-up-automated-warranty-checks) feature as well, but it is a separate feature that uses its own URLs and APIs to retrieve data. The links used by warranty scanning to retrieve data are hard coded into the scanning service and cannot be customized.

## Add custom support links

1. Browse to the **Configuration > Asset Pages**section of the web console.
2. Select **Add Manufacturer support link** in the **Asset Manufacturer support links** section of the page.
3. Enter the name of the manufacturer the support link will be used for into the Vendor field of the pop-up window. The name you submit in the pop-up window should match the manufacturer that is listed on your asset pages.
4. Enter the URL the asset serial should link to into the Support Link field of the pop-up window and select **Ok**.   

   You need to research which page on the manufacturer's website can be used to view warranty information and copy that link. Ideally, the manufacturer should allow for direct linking to a specific asset's warranty details by including the asset serial in the URL.   
   If the manufacturer allows this, you can use the {assettag} parameter as a placeholder for the asset serial when submitting the URL in Lansweeper. On an individual asset page, the parameter will automatically be replaced with that specific asset's serial. {model} and {systemsku} are available parameters as well, which are placeholders for the asset model and system SKU.

   

   
