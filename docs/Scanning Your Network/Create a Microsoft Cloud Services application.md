<!-- # Create a Microsoft Cloud Services application -->
Microsoft Cloud Services scanning is a feature introduced in Lansweeper 8.3. You must [update your installation](http://lansweeper.com/knowledgebase/updating-your-installation/ "updating your installation") if you are running a lower Lansweeper version.

You can configure a Microsoft Cloud Services application with the Azure portal. The application uses Microsoft Graph API to perform scanning.

## How does Lansweeper use Microsoft Cloud Services applications?

Microsoft Cloud Services applications can be used to accomplish a variety of tasks.

Lansweeper:

- [Scan Intune V2 targets](/docs/scan-intune-v2-targets)

Lansweeper Classic:

- [Scan Intune targets](/docs/scan-mobile-devices-through-microsoft-intune)
- [Scan Microsoft 365 targets](/docs/scan-microsoft-365-targets)
- [Scan Microsoft Entra ID (Azure Active Directory) users and groups](/docs/scan-microsoft-entra-id-azure-ad-users-and-groups)
- [Send Helpdesk and email alerts with a Microsoft Cloud Services application](/docs/send-helpdesk-and-email-alerts-via-microsoft-cloud-services)

## Prerequisites

- The scanning service can reach the following URLs:
  - For retrieving data: [https://graph.microsoft.com](https://graph.microsoft.com/) and [https://graph.microsoft.net](https://graph.microsoft.com/)
  - For generating an authentication token: [https://login.microsoftonline.com](https://login.microsoftonline.com/)
- TLS 1.2 or higher is enabled on the device hosting the Lansweeper scanning service

## Register an application

1. Log in to your company's [Azure Portal](https://portal.azure.com/).

![sophie_0-1680175610239.png](/docs/.document360/assets/article_179/image_002.jpg)

2. Navigate to the **App Registrations** service.
3. Select **New registration**.

![sophie_1-1680175610241.png](/docs/.document360/assets/article_179/image_003.jpg)

4. Name your application, select a supported account type, then select **Register**.

![sophie_2-1680175610242.png](/docs/.document360/assets/article_179/image_004.jpg)

5. In the Overview tab, copy the **Application (client) ID** and the **Directory (tenant) ID** and save them for later.

![sophie_3-1680175610243.png](/docs/.document360/assets/article_179/image_005.jpg)

## Add a client secret

You must add a client secret if you want to [send Helpdesk and email alerts with a Microsoft Cloud Services application](/docs/send-helpdesk-and-email-alerts-via-microsoft-cloud-services).

1. Navigate to your app in the portal, then go to **Certificates & Secrets > Client Secrets > New client secret.**
2. Give the client secret a **Description** and choose when it should **Expire**. Select **Add**.
3. Copy the client secret **Value** and save it in a secure location.

![sophie_4-1680175610246.png](/docs/.document360/assets/article_179/image_006.jpg)

Do not leave this page before copying the Value. It cannot be retrieved afterward.

## Add a certificate

If your application is used for scanning, we recommend adding a certificate.

Generate or purchase a certificate and add it to the root certificate store of your Lansweeper scanning server that will be used to scan this target before completing the steps below.

1. Navigate to your app in the portal, then go to **Certificates & Secrets > Certificate > Upload certificate.**
2. Upload a certificate. This should be the same certificate you installed on your scanning server.
3. Enter a description. Select **Add**.
4. Copy the certificate **Thumbprint** and save it in a secure location.

![sophie_5-1680175610259.png](/docs/.document360/assets/article_179/image_007.jpg)

To use the application, see the list of possible tasks you can complete in How does Lansweeper use Microsoft Cloud Services applications? and follow the instructions in the related article.
