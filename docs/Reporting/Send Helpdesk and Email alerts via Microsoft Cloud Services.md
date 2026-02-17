<!-- # Send Helpdesk and Email alerts via Microsoft Cloud Services -->
![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_151/image_001.jpg) **This page provides instructions on configuring Lansweeper to send emails using Microsoft 365 with modern authentication and a Microsoft Cloud Services application.**

Lansweeper allows you to send emails in the context of both the [helpdesk module](/docs/introduction-to-the-help-desk) and to send [report and event alerts](/docs/send-report-and-event-log-alerts). To use Microsoft 365 with modern authentication as a mail provider, a Microsoft Cloud Services application is required.

This article explains what is [required](#heading1) to set this up, which [permissions to add](#api-permissions) to your Microsoft Cloud Services application and how to [configure your email account in the helpdesk email configuration](#helpdeskemail) or [email alert configuration](#emailalerts).

## Prerequisites

To use a Microsoft 365 email account to send or receive emails in Lansweeper, make sure that:

- You have already [set up your Microsoft Cloud Services application](/docs/create-a-microsoft-cloud-services-application).
- You have the **Application (client) ID**, **Directory (tenant) ID**, and **Client secret** for your Microsoft Cloud Services application.
- The email account is an individual user licensed for email via the Microsoft Graph API. Shared or group mailboxes are not supported, as application permissions cannot be authenticated with these account types.

## Add permissions to the Microsoft Graph application to send and receive emails

1. Open your company's Azure portal and navigate to **App registrations**.
2. Select the **API permissions** tab in the left-hand menu.  
   ![Scanning_with_a_Microsoft_cloud_credential_5.jpg](/docs/.document360/assets/article_151/image_002.jpg)
3. On the **API permissions** page, click **Add permission** and select **Microsoft Graph** from the API list.  ![Scanning_M365_with_a_Microsoft_cloud_credential_6.jpg](/docs/.document360/assets/article_151/image_003.jpg)
4. As we are setting up the Microsoft Graph API to enforce modern authentication, you will need to add Application permissions. Start by selecting **Application permissions**.![Scanning_with_a_Microsoft_cloud_credential_6.jpg](/docs/.document360/assets/article_151/image_004.jpg)
5. Add the API permissions listed in the table below. These are all required to send and receive emails.  

   |  |  |
   | --- | --- |
   | Mail.ReadWrite | Read and write mail in all mailboxes |
   | Mail.Send | Send mail as any user |
   | User.Read.All | Read all users' full profiles |
6. Once the permissions are added, select **Save**and double-check that the permissions that are listed.![How-to-setup-a-MS-graph-email-configuration-4.jpg](/docs/.document360/assets/article_151/image_005.jpg)
7. Admin consent must still be granted. Select **Grant admin consent for <organization>** and click **Grant**in the resulting pop-up.  
   ![How-to-setup-a-MS-graph-email-configuration-5.jpg](/docs/.document360/assets/article_151/image_006.jpg)  
   All added permissions should now show **Granted for <organization>**![How-to-setup-a-MS-graph-email-configuration-6.jpg](/docs/.document360/assets/article_151/image_007.jpg)

By default, when using the settings above, your application will have access to all mailboxes in your M365 tenant. You can restrict this further by configuring ["ApplicationAccessPolicy"](https://learn.microsoft.com/en-us/graph/auth-limit-mailbox-access "https://docs.microsoft.com/en-us/graph/auth-limit-mailbox-access").

## Configure your email account in the helpdesk email configuration

1. Browse to the **Configuration > Email Settings** section of the Lansweeper Classic web console.
2. Select **Add E-mail account**. You can also change an existing configuration by selecting **Edit**.
3. Fill out DisplayName and E-mail address in the General Settings tab.  

   The email address entered in the General Settings tab will be the email address used for sending and receiving email.
4. Select the Incoming tab and select **Microsoft Graph (REST API)** as protocol.
5. Fill in the Client ID, Tenant ID, and Client Secret. These values can be gathered when [creating the Microsoft Cloud Services application](/docs/create-a-microsoft-cloud-services-application).  
   ![How_to_setup_a_MS_graph_email_configuration_1.jpg](/docs/.document360/assets/article_151/image_008.jpg)
6. Select the outgoing tab and select the Microsoft Graph (REST API) as protocol. Fill out the Client ID, Tenant ID, and Client Secret, and select **OK** to save your helpdesk email account.  
   ![How_to_setup_a_MS_graph_email_configuration_2.jpg](/docs/.document360/assets/article_151/image_009.jpg)  

   The **Client Secret** entered in the **Incoming** and **Outgoing** tabs should contain the **Secret Value** and not the **Secret ID**.

## Configure your email account to send Email Alerts

1. Browse to the **Configuration > Email Alerts** section of the Lansweeper Classic web console.
2. Select **Microsoft Graph (REST API)** as protocol in the **E-mail Server** section.
3. Fill in the From address, Client ID, Tenant ID, and Client Secret. These values can be gathered when [creating the Microsoft Cloud Services application](/docs/create-a-microsoft-cloud-services-application).  
   ![How_to_setup_a_MS_graph_email_configuration_3.jpg](/docs/.document360/assets/article_151/image_010.jpg)  

   The email address entered in the From address field will be used to send the Email alerts.
