<!-- # Enable warranty tracking -->
This page is for Lansweeper Sites. For Lansweeper On-premises, see [Warranty check for Dell, Fujitsu, IBM, Lenovo, Toshiba, and HP](/docs/set-up-automated-warranty-checks).

Lansweeper Sites can track warranty information for assets from the following manufacturers:

- Dell
- Fujitsu
- IBM
- Lenovo
- Toshiba
- HP

When warranty tracking is enabled, Lansweeper scans your assets to determine the manufacturer, model, serial number, and in some cases, the system SKU. It then connects to the manufacturer’s website to download the asset warranty information, such as:

- Purchase date
- Warranty expiration date
- Ship date
- Purchase country
- Purchased warranty products

Warranty tracking can only be enabled on one scan server in your installation.

## Set up a warranty check

To trigger a warranty check for Dell, Fujitsu, IBM, Lenovo or Toshiba/Dynabook, follow the below steps. To set up a warranty check for HP, see Enable HP warranty tracking.

1. Ensure your server has internet connection to the following URLs:  
   - <https://api.dell.com/support/assetinfo>
   - <https://apigtwb2c.us.dell.com/>
   - <https://support.ts.fujitsu.com/>
   - <https://www-947.ibm.com/support/entry/>
   - <https://csp.lenovo.com/>
   - <https://pcsupport.lenovo.com/>
   - <https://support.dynabook.com/support/>
   - <https://warranty.api.hp.com/>   

     If your scanning server does not have a direct internet connection, configure a proxy server.
2. In your Lansweeper Site, go to **Configuration > Server options**.
3. Select the scan server that you want to enable warranty tracking on.
4. Navigate to the **Warranty tracking** section.
5. Under **Enable warranty tracking on the server**, select the toggle to turn it to **Yes**.
6. Select **Save changes**.
7. To scan your asset warranties automatically, select **Rescan all asset warranties now**.

Assets that have warranty tracking available are added to the scanning queue.

## Enable HP warranty tracking

To retrieve HP warranty information in Lansweeper Sites, you need to perform a few additional steps due to HP’s strict access policies.

### Register for HP warranty API access

1. Navigate to the [HP developer portal](https://developers.hp.com/).
2. Create an account and complete the registration process.

You will receive an email to verify your email address.

HP currently does not accept registrations from Lansweeper directly. Access is granted on a per-customer basis and subject to HP’s approval.

### Create a new application

1. Once your email has been verified, send an email to [warrantyapi.customers@hp.com](mailto:warrantyapi.customers@hp.com) confirming your registered email address. Copy your HP account manager or contact as well.
2. Wait for a reply email with further instructions.
3. After enrollment, go to <https://developers.hp.com/hp-warranty-api> and create your API Key and API Secret.

### Add the HP API Key and Secret

1. In your web console, go to **Configuration** > **Server options**.  

   If you haven't enabled your web console yet, see [Enable the Lansweeper On-premises web console](/docs/enable-the-lansweeper-on-premises-web-console).
2. In the **Warranty Tracking** section, select **Edit warranty keys** for the blank HP API key.   
   
3. In the popup, enter the API Key and API Secret you received from HP.
4. Finally, select **Ok**.

Once the key and secret are configured, HP warranty scanning will be re-enabled and start returning warranty results for your HP assets.
