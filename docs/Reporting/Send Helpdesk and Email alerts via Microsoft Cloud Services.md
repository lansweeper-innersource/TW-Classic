<!-- # Send Helpdesk and Email alerts via Microsoft Cloud Services -->

Lansweeper allows you to send emails in the context of both the [helpdesk module](/classic/docs/introduction-to-the-help-desk) and to send [report and event alerts](/classic/docs/send-report-and-event-log-alerts). To use Microsoft 365 with modern authentication as a mail provider, a Microsoft Cloud Services application is required.

This article explains what is required to set this up, which permissions to add to your Microsoft Cloud Services application and how to configure your email account in the helpdesk email configuration or email alert configuration.

## Prerequisites

To use a Microsoft 365 email account to send or receive emails in Lansweeper, make sure that:

- You have already [set up your Microsoft Cloud Services application](/classic/docs/create-a-microsoft-cloud-services-application).
- You have the **Application (client) ID**, **Directory (tenant) ID**, and **Client secret** for your Microsoft Cloud Services application.
- The email account is an individual user licensed for email via the Microsoft Graph API. Shared or group mailboxes are not supported, as application permissions cannot be authenticated with these account types.

## Add permissions to the Microsoft Graph application to send and receive emails

1. Open your company's Azure portal and navigate to **App registrations**.
2. Select the **API permissions** tab in the left-hand menu.  
   
3. On the **API permissions** page, click **Add permission** and select **Microsoft Graph** from the API list.  
4. As we are setting up the Microsoft Graph API to enforce modern authentication, you will need to add Application permissions. Start by selecting **Application permissions**.
5. Add the API permissions listed in the table below. These are all required to send and receive emails.  

   |  |  |
   | --- | --- |
   | Mail.ReadWrite | Read and write mail in all mailboxes |
   | Mail.Send | Send mail as any user |
   | User.Read.All | Read all users' full profiles |
6. Once the permissions are added, select **Save**and double-check that the permissions that are listed.
7. Admin consent must still be granted. Select **Grant admin consent for <organization>** and click **Grant**in the resulting pop-up.  
     
   All added permissions should now show **Granted for <organization>**

By default, when using the settings above, your application will have access to all mailboxes in your M365 tenant. You can restrict this further by configuring ["ApplicationAccessPolicy"](https://learn.microsoft.com/en-us/graph/auth-limit-mailbox-access "https://docs.microsoft.com/en-us/graph/auth-limit-mailbox-access").

## Configure your email account in the helpdesk email configuration

1. Browse to the **Configuration > Email Settings** section of the Lansweeper Classic web console.
2. Select **Add E-mail account**. You can also change an existing configuration by selecting **Edit**.
3. Fill out DisplayName and E-mail address in the General Settings tab.  

   The email address entered in the General Settings tab will be the email address used for sending and receiving email.
4. Select the Incoming tab and select **Microsoft Graph (REST API)** as protocol.
5. Fill in the Client ID, Tenant ID, and Client Secret. These values can be gathered when [creating the Microsoft Cloud Services application](/classic/docs/create-a-microsoft-cloud-services-application).  
   
6. Select the outgoing tab and select the Microsoft Graph (REST API) as protocol. Fill out the Client ID, Tenant ID, and Client Secret, and select **OK** to save your helpdesk email account.  
     

   The **Client Secret** entered in the **Incoming** and **Outgoing** tabs should contain the **Secret Value** and not the **Secret ID**.

## Configure your email account to send Email Alerts

1. Browse to the **Configuration > Email Alerts** section of the Lansweeper Classic web console.
2. Select **Microsoft Graph (REST API)** as protocol in the **E-mail Server** section.
3. Fill in the From address, Client ID, Tenant ID, and Client Secret. These values can be gathered when [creating the Microsoft Cloud Services application](/classic/docs/create-a-microsoft-cloud-services-application).  
     

   The email address entered in the From address field will be used to send the Email alerts.
