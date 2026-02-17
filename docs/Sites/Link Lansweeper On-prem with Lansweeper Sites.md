<!-- # Link Lansweeper On-prem with Lansweeper Sites -->
[Lansweeper Sites](/docs/introduction-to-lansweeper-sites) offers a new way for you to use and access [Lansweeper](https://www.lansweeper.com/). This cloud-hosted platform not only provides existing Lansweeper functionalities but introduces many new features as well.

This page is for Lansweeper On-prem. For Lansweeper Sites, see [Link Lansweeper Sites with Lansweeper On-prem](/docs/link-lansweeper-sites-with-lansweeper-on-prem).

Depending on your situation, you might require a different installation experience.  
If you're a new customer and do not have a Lansweeper On-prem installation, [install the Lansweeper Cloud-first trial](/docs/install-the-lansweeper-trial "Install the Lansweeper Cloud-first trial").  
If you're an existing customer with a Lansweeper On-prem installation, [link your installation with a Lansweeper Site](/docs/link-lansweeper-on-prem-with-lansweeper-sites "Link your cloud site").  
If you're an existing customer and want to create a new Lansweeper installation that's linked with cloud, [Install Lansweeper Sites](/docs/install-lansweeper-sites "Install Lansweeper Cloud").  
If you're only interested in on-premises installations, [install Lansweeper On-prem](/docs/install-lansweeper-on-prem "Install Lansweeper Classic").

## Prerequisites

You need an existing, up-to-date Lansweeper On-prem installation to link with Lansweeper Sites. Install or update Lansweeper On-prem using the latest available installer, if you haven't already. Follow the [installation instructions](/docs/install-lansweeper-on-prem) and [update instructions](/docs/update-lansweeper-on-premises) to ensure full compatibility with Lansweeper Sites.

## Link with Lansweeper Sites

Once you've set up your Lansweeper installation and scanned your data, you can start the process of linking the installation with the site.

1. On the server hosting your local Lansweeper installation, go to the web console and select**Link with Cloud site**.  

   Every 12 hours, [prerequisite checks](/docs/cloud-linking-requirements) are performed in the background of your system to ensure your installation can be linked to a cloud site.
2. Select **Link with Cloud site**. If you have multiple scan servers, you will be asked which one should be responsible for syncing with Lansweeper Sites. This server will be the sync server.  

   If any prerequisite checks have failed, follow the provided instructions to resolve them and select **Retry** when you're ready. For more information, see [Lansweeper Sites linking requirements](/docs/cloud-linking-requirements "Cloud linking requirements").

     

   You only need one sync server for your entire local installation.
3. Enter your email address and select **Confirm**.   
   If you have not created a Lansweeper account yet, select **Register**.  
   If you aren't logged in yet, you will be redirected to a login page.  
   
4. Either select an existing site in the list to link to, or create a new site. If you select **Create new site**, Lansweeper Sites will create a site for you.  

   To link an installation with Lansweeper Sites, you must create at least one site in your account. You can create multiple sites to further group and separate your local installations. For more information, see [Create a site in Lansweeper Sites](/docs/create-a-lansweeper-cloud-site).

     

   If a site appears to be locked, you might not have permission to link to that site.
5. Select **Copy linking code**.
6. Enter your site's linking code in the local web console and select **Submit**.  
   
7. After Lansweeper has verified the site's linking code, your local installation will perform an initial sync with Lansweeper Sites. Depending on how much data is in your local Lansweeper installation, this process might take a while.  
   
8. Your Lansweeper Site will display your installation's data in the **Inventory** module. More information on the **Inventory** module can be found in [View assets](/docs/view-assets).  
   
9. Browse to **Configuration > Installations**to view the details of your linked installations. If you have multiple local installations linked to the same site, all of these installations will be listed there.   

   You can switch between sites using the **Change site** menu in the top left corner of the interface.
