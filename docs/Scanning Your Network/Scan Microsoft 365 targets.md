<!-- # Scan Microsoft 365 targets -->
Microsoft Cloud Service scanning is a feature introduced in Lansweeper 8.3. You must [update your installation](http://lansweeper.com/knowledgebase/updating-your-installation/) if you are running a lower Lansweeper version.

With a Microsoft 365 scanning target, you can scan your Microsoft 365 data, mailbox, and ActiveSync data.

## Prerequisites

- You've [created a Microsoft Cloud Services application](/docs/create-a-microsoft-cloud-services-application).
- You have the following Microsoft Cloud Services application information available:
  - Application (client) ID
  - Directory (tenant) ID
  - Client secret or certificate

## Add API permissions

1. Go to the Azure portal and navigate to **App registration**.
2. Find the app that you've previously created.
3. Go to **API permissions**.

![sophie_0-1680283780919.png](/docs/.document360/assets/article_221/image_002.jpg)

4. Go to **Add a permission > Microsoft Graph**.

![sophie_1-1680283780923.png](/docs/.document360/assets/article_221/image_003.jpg)

5. Select **Application permissions**.
6. Add the following API permissions:
   - Directory > Directory.Read.All
   - Domain > Domain.Read.All
   - Group > Group.Read.All
   - GroupMember > GroupMember.Read.All
   - Organization > Organization.Read.All
   - OrgContact > OrgContact.Read.All
   - User > User.Read.All
7. Select **Add permissions**.
8. Select **Grant admin consent for <organization>**.

## Configure PowerShell Online

To access mailbox information and ActiveSync data, enable PowerShell Online.

If you only want to scan Microsoft 365, you can skip this configuration and exclusively use the API.

To enable PowerShell Online, your Lansweeper scanning server must fulfill the following prerequisites:

- Operating system: Windows 7 or newer.
- Architecture: 64-bit architecture.
- PowerShell version: 7.1.   
  If you only just installed this PowerShell version, reboot your machine. Your scanning server can not have pending reboots.
- Scripts: To allow scripts that a trusted publisher signs, run the following command via an elevated PowerShell window on the scanning server: `Set-ExecutionPolicy RemoteSigned`.

You must use a certificate thumbprint for PowerShell Online scanning. Client secrets can not be used.

To enable PowerShell online:

1. Install the latest public version of Exchange Online PowerShell by entering the following command in an elevated PowerShell terminal: `Install-Module -Name ExchangeOnlineManagement`.
2. Go to the Azure portal and navigate to **App registration**.
3. Locate the app you created to scan Microsoft 365.
4. Copy the **Application (client) ID** to your clipboard.
5. Go to **Azure Active Directory** **> Roles and administrators.**
6. Select the **Exchange administrator** role.  
   ![sophie_0-1680529031689.png](/docs/.document360/assets/article_221/image_004.jpg)
7. Select **Add assignments**.
8. Click **No members selected**.  
   ![sophie_1-1680529116947.png](/docs/.document360/assets/article_221/image_005.jpg)
9. In the search bar, enter the Application (client) ID, select your app, then click **Select**.
10. Select **Next**, then fill in the assignment settings and click **Assign**.
11. Navigate back to the **App registration** and find the app that you created to scan Microsoft 365.
12. Go to **API permissions > Add a permission > APIs my organization uses > Office 365 Exchange Online**.
13. Select **Application permissions > Exchange > Exchange.ManageAsApp** **> Add permissions.**
14. Select ****Grant admin consent for <organization>****.![sophie_2-1680529285415.png](/docs/.document360/assets/article_221/image_006.jpg)

## Configure Lansweeper to scan Microsoft 365

1. In the web console, go to **Scanning > Scanning Credentials**.
2. Select **Add new credential**.
3. Fill in the following fields:
   - Type: Microsoft Cloud Service
   - Name: Name of your application
   - Application (client) ID: Copy from **Azure portal > App registration > <your application> > Overview**
   - Directory (tenant) ID: Copy from **Azure portal > App registration > <your application> > Overview**
   - Authentication type: Select either:
     - Client secret: Copy from **Azure portal > App registration > <your application> Certificates & secrets > Secret ID**
     - Certificate thumbprint: Copy from **Azure portal > App registration > <your application> Certificates & secrets > Thumbprint**  
       To scan mailbox and ActiveSync information using PowerShell you must use the certificate thumbprint authentication type.

4. Select **Microsoft 365** then **Ok**.

![sophie_3-1680283780925.png](/docs/.document360/assets/article_221/image_007.jpg)

Lansweeper can now scan your Microsoft 365 targets.
