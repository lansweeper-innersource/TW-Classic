<!-- # Link Lansweeper Sites with Lansweeper On-prem -->
[Lansweeper Sites](/docs/introduction-to-lansweeper-sites) offers a new way for you to use and access [Lansweeper](https://www.lansweeper.com/). This cloud-hosted platform not only provides existing Lansweeper functionalities but introduces many new features as well.

This page is for Lansweeper Sites. For Lansweeper On-prem, see [Link Lansweeper On-prem with Lansweeper Sites](/docs/link-lansweeper-on-prem-with-lansweeper-sites).

Depending on your situation, you might require a different installation experience.  
If you're a new customer and do not have a Lansweeper On-prem installation, [install the Lansweeper Cloud-first trial](/docs/install-the-lansweeper-trial "Install the Lansweeper Cloud-first trial").  
If you're an existing customer with a Lansweeper On-prem installation, [link your installation with a cloud site](/docs/link-lansweeper-on-prem-with-lansweeper-sites "Link your cloud site").  
If you're an existing customer and want to create a new Lansweeper installation that's linked with cloud, [Install Lansweeper Sites](/docs/install-lansweeper-sites "Install Lansweeper Cloud").  
If you're only interested in on-premises installations, [install Lansweeper On-prem](/docs/install-lansweeper-on-prem "Install Lansweeper Classic").

## Prerequisites

You need an existing, up-to-date Lansweeper On-prem installation to link with Lansweeper Sites. Install or update Lansweeper On-prem using the latest available installer, if you haven't already. Follow the [installation instructions](/docs/install-lansweeper-on-prem) and [update instructions](/docs/update-lansweeper-on-premises) to ensure full compatibility with Lansweeper Sites.

## Link with Lansweeper On-prem

Once you've set up your Lansweeper installation and scanned your data, you can start the process of linking the installation with a Site.

1. Create an account for Lansweeper Sites at [app.lansweeper.com](https://app.lansweeper.com/ "http://app.lansweeper.com") by selecting **Register**.
2. Enter your email and password, or register with one of the available social login options.  

   Make sure to look for and follow the instructions in your account verification email. You must verify your email address within 24 hours.
3. Enter a name for your site and select **Create**.  

   Pick your site name carefully, as this name is used as part of your site URL. The display name of a site can be changed after creation, but the internal name used in the URL cannot. Your site name must be unique and may not contain spaces.

   ![Linking with cloud 1.png](/docs/.document360/assets/article_347/image_002.jpg)  

   To link an installation with Lansweeper Sites, you must create at least one site in your account. You can create multiple sites to further group and separate your local installations. For more information, see [Create a site in Lansweeper Sites](/docs/create-a-lansweeper-cloud-site).
4. Select **Get linking code**to be redirected to your new Lansweeper Site.  

   The linking code was introduced in Lansweeper 10.5. You will need to [update your installation](http://lansweeper.com/knowledgebase/updating-your-installation/ "updating your installation") if you are running a lower Lansweeper version.

   ![Linking with cloud 15.png](/docs/.document360/assets/article_347/image_003.jpg)  
   If you selected **Access empty site**instead, you can get your linking code from your site by going to **Configuration > Installations > Link an installation**.
5. In the pop-up, select **Copy code**. You will need to enter this code in your local web console later.
6. On the server hosting your local Lansweeper installation, go to the web console and select**Link with Cloud site**.  

   Every 12 hours, [prerequisite checks](/docs/cloud-linking-requirements) are performed in the background of your system to ensure your installation can be linked to a cloud site.
7. Select **I have a linking code**. If you have multiple scan servers, you will be asked which one should be responsible for syncing with Lansweeper Cloud. This server will be the sync server.  

   If any prerequisite checks have failed, follow the provided instructions to resolve them and select **Retry** when you're ready. For more information, see [Cloud linking requirements](/docs/cloud-linking-requirements "Cloud linking requirements").

   ![Linking with cloud 8.png](/docs/.document360/assets/article_347/image_004.jpg)  

   You only need one sync server for your entire local installation.
8. Enter your site's linking code in the local web console and select **Submit**.  
   ![Linking with cloud 12.png](/docs/.document360/assets/article_347/image_005.jpg)
9. After Lansweeper has verified the site's linking code, your local installation will perform an initial sync with Lansweeper Cloud. Depending on how much data is in your local Lansweeper installation, this process could take a while.  
   ![link-with-cloud-site4.png](/docs/.document360/assets/article_347/image_006.jpg)
10. Your Lansweeper Site will display your installation's data in the **Inventory** module. More information on the **Inventory** module can be found in [View assets](/docs/view-assets).  
    ![Linking with cloud 4.png](/docs/.document360/assets/article_347/image_007.jpg)
11. Browse to **Configuration > Installations**to view the details of your linked installations. If you have multiple local installations linked to the same site, all of these installations will be listed here.   

    You can switch between sites using the **Change site** menu in the top left corner of the interface.
