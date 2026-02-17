<!-- # Set up automated warranty checks -->
This page is for Lansweeper On-premises. For Lansweeper Sites, see [Enable warranty tracking](/docs/enable-warranty-tracking).

Lansweeper performs automated warranty checks and scans for assets manufactured by Dell, Fujitsu, IBM, Lenovo, Toshiba/Dynabook, and HP. Specifically, we attempt to retrieve key warranty details such as the purchase date, warranty expiration date, ship date, purchase country, and any purchased warranty products.

To do this, Lansweeper gathers data like the manufacturer, model, serial number, and, in some cases, the system SKU directly from the asset. This information is then submitted to the respective manufacturer's warranty service.

Scanned warranty information is listed in the **Summary** tab of individual asset pages and is also available in the built-in warranty reports within the **Reports** section of the web console.   
When Lansweeper first scans an asset, it automatically attempts to retrieve the warranty details from the manufacturer's site. Warranty information is then refreshed automatically every 4 months, or every 2 days if a previous scan attempt failed. You can also manually trigger a warranty scan for supported manufacturers at any time.

The current implementation of IBM warranty scanning relies on the IBM Support Portal which was retired in late June 2021. Due to this IBM warranty retrieval is currently non-functional while we search for a solution.

![automated-warranty-check-dell-fujitsu-hp-ibm-lenovo-toshiba-1.jpg](/docs/.document360/assets/article_242/image_002.jpg)

## Set up a warranty check

To trigger a warranty check for Dell, Fujitsu, IBM, Lenovo or Toshiba/Dynabook, follow the below steps. To set up a warranty check for HP, see [Enable HP warranty tracking](#HP).

1. If you have not already done so, update to the latest Lansweeper release by following the instructions in [this knowledge base article](/docs/update-lansweeper-on-premises). You can verify whether you are on the latest release by selecting **Check for updates now** in the **Configuration > Your Lansweeper license**section of the web console.  

   Don't skip this step. As the supported manufacturers change their websites on a regular basis, our warranty scanning procedures are updated on a regular basis as well.
2. Ensure all fields required for submission on the manufacturers' websites are filled in when looking at your assets' Lansweeper webpages. The assets' manufacturers should be set to Dell, Fujitsu, IBM, Lenovo or Toshiba and their serial numbers should be filled in.   
   For IBM assets, the model is required and for Lenovo assets the system SKU is required.
3. Select **Edit asset** in the left pane of an individual asset page, under **Asset options**, and make sure the checkboxes next to the **Purchased** and **Warranty** fields are unchecked.   
   The fields should be unlocked by default. Locked fields will prevent the data from being overwritten during scanning.

   ![automated-warranty-check-dell-fujitsu-hp-ibm-lenovo-toshiba-2.jpg](/docs/.document360/assets/article_242/image_003.jpg)
4. In the **Scanning > Scanned item interval**section of the web console, ensure the **WARRANTY** and **WARRANTYRETRY** items are set to **Scan Server And LsAgent**, though this is the default option.  
   ![Set up automated warranty checks 2.png](/docs/.document360/assets/article_242/image_004.jpg)
5. Ensure your Lansweeper scanning server can access the internet, as warranty information is retrieved online from the manufacturers' websites.
6. If you are using a proxy server to access the internet, add your proxy settings in the **Proxy Server** section of the **Configuration > Server options** page in the web console.   
   Your proxy server should allow access to the URLs below. Sub-links of these URLs are used to retrieve warranty information.

   <https://api.dell.com/support/assetinfo/>

   <https://apigtwb2c.us.dell.com/>

   <https://support.ts.fujitsu.com/>

   <https://www-947.ibm.com/support/entry/>

   <https://csp.lenovo.com/>

   <https://pcsupport.lenovo.com/>

   <https://support.dynabook.com/support/> (for Toshiba, which rebranded to Dynabook)  
   <https://warranty.api.hp.com/>   

   The links used by warranty scanning are hard coded into the scanning service and cannot be customized. If a manufacturer's website changes, Lansweeper is updated to include a new warranty scanning procedure.
7. Ensure you've selected **Enable warranty tracking on this server** in the **Warranty Tracking** section of the same page.   
   If you have multiple scanning servers, you only need to enable warranty scanning on one server. That server will retrieve the warranties of all assets in your database.
8. Select **Rescan all assets warranties now** or select **Refresh Warranty** in the left pane of individual asset pages, under **Asset options**.  
   ![Warranty tracking 1.png](/docs/.document360/assets/article_242/image_005.jpg)

   If you're scanning a lot of warranties, we recommend waiting at least an hour for all scans to complete, as the manufacturers' websites may take a while to respond. Refresh any previously opened asset pages afterwards to see updated information. Warranty scans do not show up in your scanning queue, as they're processed silently in the background.
9. If warranty information still doesn't appear in the **Summary** tab of individual asset pages, run [this report](https://www.lansweeper.com/Forum/yaf_postsm45562_Warranty-scanning-errors.aspx) to look for warranty scanning errors. You can add this report to your installation by following [these instructions](/docs/add-a-report-to-your-lansweeper-installation).   
   A common cause of warranty scanning errors is that your server is not able to reach the internet to retrieve the information. This must be resolved within your network itself by checking proxy and firewall configurations.

## Enable HP warranty tracking

To retrieve HP warranty information in Lansweeper On-premises, you need to perform a few additional steps due to HP’s strict access policies.

### Register on the HP developers portal

1. Navigate to the [HP developers portal](https://developers.hp.com/).
2. Create an account and complete the registration process.

You will receive an email confirming your registration.

HP currently does not accept registrations from Lansweeper directly. Access is granted on a per-customer basis and subject to HP’s approval.

### Enroll for the HP Warranty API

1. Once your account is approved, log in and navigate to the [HP warranty API page](https://developers.hp.com/hp-warranty-api-hp-warranty-api-pilot-companies/hp-warranty-api).
2. Complete the enrollment process. Steps include completing and submitting the enrollment form, and agreeing to the Warranty API EULA.  

   If you have any questions about the enrollment process, you can send an email to [warrantyapi.customers@hp.com](mailto:warrantyapi.customers@hp.com).
3. Once enrolled, go to <https://developers.hp.com/hp-warranty-api> and create your API Key and API Secret.   
   API credentials are valid for **90 days**, and need to be renewed in the HP Warranty API portal.

### Add the HP API Key and Secret

1. In your web console, go to **Configuration** > **Server options**.
2. In the **Warranty Tracking** section, select **Edit warranty keys** for the blank HP API key.   
   ![Warranty tracking 2.png](/docs/.document360/assets/article_242/image_006.jpg)
3. In the popup, enter the API Key and API Secret you received from HP.
4. Finally, select **Ok**.

Once the key and secret are configured, HP warranty scanning will be re-enabled and start returning warranty results for your HP assets.
