<!-- # Azure scanning requirements -->

From version 7.1 onward, Lansweeper is capable of scanning resource groups and virtual machines hosted on the Microsoft Azure cloud computing platform. An asset is created for each resource group and for each virtual machine.

This article explains what the requirements are for Azure scanning and how to set up and gather the Azure parameters required for scanning.

## Requirements

To scan an Azure cloud environment, the following requirements must be met:

- Your Lansweeper installation must be version 7.1 or higher.
- Your Lansweeper license must support Azure scanning.
- Your Lansweeper scanning server must have access to the internet.
- You must provide Lansweeper with your Azure subscription ID, directory (tenant) ID and the application ID and key (password) of an application with read-only access to your subscription. Lansweeper uses the Azure Resource Manager (ARM) REST API to retrieve data.

## Setting up the Azure application

To set up an application with read-only access to your Azure subscription and to gather the Azure properties required for scanning, follow the steps below.

### Step 1: copy your subscription ID

Log into your Azure account and browse to your subscription. One way to do this is by clicking [this direct link](https://portal.azure.com/#blade/Microsoft_Azure_Billing/SubscriptionsBlade "Azure portal"). Copy the subscription ID that is listed on the page, as you'll need to submit this in Lansweeper.

![azure-scanning-requirements-1.jpg](/docs/.document360/assets/article_156/image_002.jpg)

### Step 2: copy your tenant ID

Select the portal menu button in the upper left corner of the screen, select **Azure Active Directory** and go the **Properties** section. Copy the tenant ID (directory ID) that is listed on the page, as you'll need to submit this in Lansweeper. ![azure-active-directory-tenant-id.jpg](/docs/.document360/assets/article_156/image_003.jpg)

### Step 3: create an app and copy the application ID

Select the **Azure Active Directory** menu and go to the **App registrations** section. Select the **New registration** button and submit a descriptive name for the application. Choose who can use the application and select **Register** at the bottom of the page.

![azure-active-directory-new-app-registration.jpg](/docs/.document360/assets/article_156/image_004.jpg)

Copy the application ID that is listed on the resulting page, as you'll need to submit this in Lansweeper.

![azure-active-directory-application-id.jpg](/docs/.document360/assets/article_156/image_005.jpg)

### Step 4: create an app secret

In the **Certificates & secrets** menu of your application, select the **New client secret** button.

![azure-active-directory-application-client-secret.jpg](/docs/.document360/assets/article_156/image_006.jpg)

Submit a description for your key, choose whether or when it expires and select **Add**.

Though having the key expire is more secure, keep in mind that this will require you to generate a new one at some point in the future. Copy the key that was generated and that is now visible in the Value field of the page. You'll need to submit this as your application password in Lansweeper.

![azure-active-directory-copy-application-client-secret.jpg](/docs/.document360/assets/article_156/image_007.jpg)

You will not be able to see your key again once you leave this page, so make sure you store it somewhere safe for future reference. If you do lose your key, you will need to generate a new one.

### Step 5: assign an app role

Go back to your subscription. One way to do this is by clicking [this direct link](https://portal.azure.com/#blade/Microsoft_Azure_Billing/SubscriptionsBlade "Azure portal"). Click on the name of your subscription and select the **Access control (IAM)** menu. Select **Add** at the top and then select **Add role assignment**.

![azure-add-role-assignment.jpg](/docs/.document360/assets/article_156/image_008.jpg)

Perform a search for the Reader role, select it and click **Next** at the bottom of the page. Click **Select members** , perform a search for the application you created earlier and hit **Select**. Finally, select **Review + assign** to assign the role to your app.  ![azure-role-assignment-members.jpg](/docs/.document360/assets/article_156/image_009.jpg)

### Step 6: set up Azure scanning in Lansweeper

You now have the 4 parameters required to set up Azure scanning in Lansweeper: a subscription ID, a directory (tenant) ID, an application ID and an application password. You can now [configure Azure scanning in Lansweeper](/docs/scan-an-azure-cloud-environment) by following the instructions in the knowledge base.
