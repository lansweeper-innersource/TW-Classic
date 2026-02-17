<!-- # Integrate with the Lansweeper App for Jira Service Management Ticket Enrichment -->

Lansweeper App for JSM Ticket Enrichment allows the JSM user to enrich JSM issues with related Lansweeper assets as listed below:

- The app allows users to search the assets from Lansweeper directly based on IP, MAC, Asset Name, User Name, Manufacturer, Type, or All.
- It also fetches assets automatically that have been retrieved based on the IP addresses or MAC addresses from the issue summary or description.
- The app attempts to match the reporter’s email address in Jira with the last logged-in user on a Windows PC in Lansweeper.
- Users can select/deselect assets from these assets to associate them with the Jira issue.
- The Lansweeper app also provides a Jira issue linking feature, that would link all the Jira issues which have one or more than one selected assets matching the selected assets in the current Jira issue.
- Users can view the list of Software installed on the asset

On this page:

- Compatibility matrix
- Prerequisites
- Installation
- Get a Lansweeper API token
- Configure Lansweeper App for JSM
- Ticket enrichment
- Issue linking
- Known behavior
- Troubleshooting

## Compatibility matrix

|  |  |
| --- | --- |
| **Supported Browsers** | Google Chrome, Microsoft Edge, Safari |
| **Lansweeper REST API Version** | v2 |
| **Development Platform** | Atlassian Forge |
| **Jira REST API Version** | v3 |
| **Forge CLI Version** | v5.2.1 |
| **Supported Lansweeper Platform** | Lansweeper Sites |
| **App Hosting Type** | Cloud |
| **Supported Products** | Jira Software  Jira Service Management  Jira Work Management |

## Prerequisites

- A properly configured Jira Cloud instance with the Lansweeper App installed.
- Lansweeper instance appropriately configured and populated with assets (that can be synced with Jira).
- Only Jira admin users can configure the App.

## Installation

1. Log in to your Atlassian Jira site. Select **Apps** > **Explore more apps**. Only Jira administrators can access this menu.
2. In the search bar, enter **Lansweeper**.
3. Select the **Lansweeper App for Jira** app.
4. Select **Get it now > Get it now**. The installation process begins. Once installed, a message will appear on the bottom left, indicating that installation has been successful.  
   
5. Select **Apps > Manage your apps**. You can view the **Lansweeper App for Jira** in the Apps section on the left.

If you don’t get the success notification for the installation, create an Atlassian support ticket, explain the issue, and attach a screenshot of the message.

### Uninstallation

1. Select **Apps >** **Manage your apps**.  
   
2. Select **Lansweeper App for Jira Service Management**.
3. Select **Uninstall** **>** **Uninstall app**.

## Integration

### Get a Lansweeper API token

1. This app requires an API token from Lansweeper, which is used to make API calls from Jira to Lansweeper.
2. The API token is required after installation to configure the app.
3. [Generate an API token.](https://developer.lansweeper.com/docs/data-api/get-started/quickstart/#personal-access-token-pat) Ensure that you choose the API client type as PAT (Personal Access Token).
4. We recommended that you keep a long period of expiration time or no expiration time for the token to allow the app to function seamlessly.

### Configure Lansweeper App for JSM

1. Select **Apps > Manage your apps**.
2. Select **Lansweeper App for Jira Service Management**.
3. The first time, you might be asked to allow the app to access Atlassian products on your behalf. Select **Allow access** to open the authorization window. After validating the permission, select **Accept**.
4. Enter the API token that you generated in the above step.
5. Select which apps projects you want the app to function in using the **Projects** dropdown.
6. Select **Validate and Save**. The configuration parameters are validated, and the Lansweeper credentials are authenticated. Upon successful validation and authentication, a success message will appear.  
   

![](https://files.document360.io/21d5935c-1b73-44fa-bf5a-a8b0f5c67f25/Images/Documentation/lansweeper-app-for-jira---release-documentation-and-user-guide-new-image-6c3gf8ft.png)

### Ticket enrichment

Navigate to any Jira issue to see a **Lansweeper** field on the right side of the **Details** tab. Select **View Associated Assets** will open the Asset Details view.

You can see the assets in the following tabs:

**Search Results**

This tab displays the assets fetched from the Lansweeper using the **LS search** (a.k.a. Lansweeper Search) functionality. LS search can be done based on IP, MAC, Asset Name, User Name, Manufacturer and Type, and ALL.

For example, in the image below, four assets were fetched from the Lansweeper based on the **Asset Name** search that contains **AP0**. One is a Network Device, and the other three are Windows machines.

![](https://files.document360.io/21d5935c-1b73-44fa-bf5a-a8b0f5c67f25/Images/Documentation/lansweeper-app-for-jira---release-documentation-and-user-guide-new-image-erpfdcwt.png)

Select the ones needed for the ticket by selecting the checkbox.

**Matched**

This tab displays the assets that have been fetched automatically based on the IP addresses or MAC addresses from the issue summary or description. Additionally, the app attempts to match the reporter’s email address in Jira with the last logged-in user on a Windows PC in Lansweeper.

For example, in the image below, one asset seen in the Matched tab has been fetched based on the IP address present in the Jira Issue summary field.



Select the ones needed for the ticket by selecting the checkbox.

**Selected**

This tab displays the assets that have been selected for the particular Jira issue previously on the other Tabs, namely Matched and Search Results. These details are saved in the Jira Cloud storage issue-wise. For each Jira issue, information like asset ID, site ID, and company name is stored for each of the selected assets.

In the image below, one asset has been selected each from the Matched and Search Results tab and is now visible in the Selected tab.



If the asset has software installed, a computer icon appears in the **Info** column. Clicking on this icon pops up a table and lists the installed software, including the versions.

If the asset has active vulnerabilities, a red bug icon will appear in the **Info** column, allowing you to view the number of vulnerabilities and their CVE numbers. It is possible to view the details of the asset vulnerabilities by clicking on the related **Link**.

### Issue linking

In a complex Jira environment, there may be multiple issues/tickets related to the same asset. For example, if a database server is down, there is a high chance that multiple people will create tickets to report the issue to the IT Operations team. Solving each issue without having an overall view is time-consuming and complicated.

Lansweeper App for Jira solves this complexity with the Link Related Issue feature. The use case is as follows:

1. For each ticket, you can search and relate the assets as described in the previous step.
2. After selecting the assets, select **Link Related Issue**. This will link all the Jira issues having any of the selected assets matching the selected assets in the current Jira issue. Refresh the page to see the linked issues.

This will only link issues that do not have the Jira status **Done** which includes the statuses: Resolved, Closed, Declined, Canceled, Completed, Failed, Done, Published, Approved, Canceled, and Rejected.

## Known behavior

- If the API token provided does not have any site selected, then it will display an error message.
- If the process of linking is initiated in two issues with the same selected assets at the same time then duplication may occur for a few linked issues.
- The IP and MAC provided in the summary and description of the issue should be in plaintext. If IP or MAC is provided in the format of a link in the summary or description, then assets related to it may not be displayed in Asset Details.
- To view the linked Assets, the user needs to refresh the page after clicking the **Link Related Issue** button.

## Troubleshooting

- In case you don’t get the success notification for the installation, please create a ticket to Atlassian, explain the issue and attach a screenshot of the message. The installation process of our application is managed by Atlassian in an automated way. They will be able to help.
- Check application logs whenever any error/issue is observed. To see the application logs, follow the below steps. It would require the role of a system administrator.
  1. Go to <https://admin.atlassian.com/>.
  2. Select **Products**.
  3. Select **SITES AND PRODUCTS**.
  4. Navigate to **Connected Apps**.
  5. Select the 3 dots, then Download logs.
- Manage users, groups, permissions, and roles in Jira Cloud
- To manage users, groups, permissions and roles in Jira Cloud, review the following link and execute the steps  
  [https://support.atlassian.com/jira-cloud-administration/docs/manage-users-groups-permissions-and-rol...](https://support.atlassian.com/jira-cloud-administration/docs/manage-users-groups-permissions-and-roles-in-jira-cloud/)
- Unable to install/activate the app on Jira Cloud: If any issue is faced during installation/activation of the app on the Jira Cloud, review the following link and execute the steps.  
  <https://confluence.atlassian.com/upm/installing-marketplace-apps-273875715.html>
- Issue encountered in Issue Enrichment UI: If any issue is faced while viewing the asset details, selecting/deselecting the assets or viewing the updated asset data, a refresh button has been provided on the right side of the Asset Details page. Click on the refresh button or hard refresh the page.

Lansweeper’s APIs allow you to develop apps that seamlessly integrate our market-leading IT discovery and inventory platform. Find everything you need to get started in our [Developer Portal](https://developer.lansweeper.com/?utm_source=referral&utm_medium=website&utm_campaign=ls-dev_portal-global-q4-2024&utm_content=kb_article-sentence_cta%20or%20Developer%20Portal).
