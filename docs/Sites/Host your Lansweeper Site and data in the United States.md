<!-- # Host your Lansweeper Site and data in the United States -->

Lansweeper Sites can be hosted in the United States, giving you greater control over data residency. By choosing U.S. hosting, your Inventory data will be securely stored in our AWS cloud instance in Ohio (us-east-2).

## Considerations

- **No migration path**: You cannot migrate your existing Lansweeper Site from Europe to the U.S. To host your site in the U.S., you must [create a new site](#site).
- **Data transiting to Europe**: Certain processes, like Credential-free Device Recognition, may still transit data to Europe. 
- **Centrally stored data**: Essential data is stored in a central European region for service performance and reliability. This data is strictly managed under our data protection protocols.

## Requirements

- **Minimum Lansweeper On-premises version**: If you're using an On-premises scanner, Lansweeper On-premises 11.4 or a newer version is required.
- **Web server access**: Review the [web server internet requirements](/docs/cloud-requirement-web-server-internet-access) for U.S.-hosted sites.  

  If it's your first time creating a U.S.-based Lansweeper Site from the Lansweeper On-premises console, you must whitelist <http://app.lansweeper.com> when you initially create your site. Once you create the site, you can unlist the URL.

## Which region is right for me?

The U.S. East (Ohio) region might be right for you if:

- You’re based in the United States.
- Your organization must adhere to specific federal, state, or industry-specific data protection standards that require your inventory data to be stored (or hosted) within the U.S.

If neither of the above points applies to you, the European (Ireland) region might be a better fit.

## Create a Lansweeper Site in the U.S.

1. Create a new Lansweeper Site. You can do this from [your Lansweeper Site](/docs/create-a-lansweeper-cloud-site), or [your Lansweeper On-Premises console](/docs/link-lansweeper-on-prem-with-lansweeper-sites).
2. When you’re prompted to pick a name for your site, next to **Select data hosting region**, select **US East (Ohio)** from the dropdown.  
   ![create-new-site.png](/docs/.document360/assets/article_312/image_002.jpg)
3. Continue with the steps to create a new site.
