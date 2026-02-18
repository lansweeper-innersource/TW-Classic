<!-- # Chrome OS scanning requirements -->
To be able to scan your Chrome OS (e.g. Chromebook) devices with Lansweeper, you need to ensure that they meet the scanning requirements. This article describes these requirements, and how to set up the required project and credential.

## Chrome OS scanning requirements

To perform Chrome OS scans, the following requirements must be met:

- Your Lansweeper installation must be version 7.2 or higher.
- Your Lansweeper license must support Chrome OS scanning.
- Your Lansweeper scanning server must have access to the internet.
- You must have access to the Google admin console that manages your Chrome OS devices.
- You need a G Suite, educational or governmental license to configure and use the API.
- You need to have a project that has the Admin SDK enabled, and a credential that has access to the necessary scopes. Detailed instructions on how to configure this can be found below.

## Configuring your Google environment for scanning

The below steps help you set up a project and configure an account that has access to the resources Lansweeper queries. If you're already using Google APIs, you can choose to use existing projects, service accounts and/or credentials.

### Step 1: create a project

First, you'll need to create a project for the domain your Chrome OS devices are located in.

Browse to <https://console.developers.google.com/> and sign in as a super administrator. Open the navigation menu, select the **IAM & Admin** sub-menu and select **Manage Resources**.





From here, you can select **Create project**. Give your project a name, select the correct organization and location and select **Create**.



### Step 2: enable Admin SDK for your project

Next, enable the Admin SDK for the project you just created.

In the developer console, make sure you have your newly created project selected at the top. Open the navigation menu, select the **APIs & Services** sub-menu and select **Library**.



 Search for "Admin SDK", select the API in the search results and select **Enable**.

 

### Step 3: create service account

Next, create a service account with access to the Admin SDK API of your project.

In the developer console, make sure you have your project selected at the top. Open the navigation menu, select the **APIs & Services** sub-menu and select **Credentials**. Press **Create credentials** and then choose **Service account** from the available options.



Enter a name and description for your account, select**Create and continue** followed by **Done**.



### Step 4: copy service account ID and generate JSON key

On the resulting page, the **Credentials** sub-menu of the **APIs & Services** menu, select your newly created service account.



Copy the unique ID you see listed on the page, as you'll need it in step 5 of this article.



If you don't see your service account listed right away, refresh the webpage by pressing F5.

In the **Keys** tab of the service account, go to the **Add key** drop-down menu and select the **Create new key** option within.



In the resulting pop-up, select the JSON format. The key will be saved to your computer. Make sure to keep it somewhere safe. If you lose your key, you'll need to generate a new one.   
The JSON key will be used as part of your Chrome OS scanning target in Lansweeper.



### Step 5: grant service account scope access

Next, grant your service account access to the necessary scopes. Browse to <https://admin.google.com/> and sign in as a super administrator. Open the **Security** menu, **Access and data control** and finally **API controls**.

Only accounts with the super administrator role are able to see **Access and data control > API controls**.



Select **Manage domain wide delegation** and press **Add new**.



In the resulting pop-up, submit the service account ID you copied earlier. In the OAuth scopes input box, paste the following to grant the service account access to the necessary scopes, and select **Authorize**: https://www.googleapis.com/auth/admin.directory.orgunit.readonly, https://www.googleapis.com/auth/admin.directory.device.chromeos.readonly



### Step 6: Configure user with Services Admin role

Make sure you have a user with the Services Admin role. In your Google Admin console, go to **Account > Admin** roles. Point to the role and then **View privileges** or **View admins** to see the admins assigned to the role.

If no admins are assigned, see [Assign roles](https://support.google.com/a/answer/9807615?sjid=17086806967343551423-NA#single-user&multiple-users&group&service-account) to learn how to assign a role to a user.

You're now ready to start scanning your Chrome OS devices in Lansweeper, by following [this Chrome OS scanning guide](/classic/docs/how-to-scan-chrome-os-machines). As part of your Lansweeper scanning target, you'll need to submit the user account you configured or created, the one with the Services Admin role. You'll also need to provide the JSON key you generated.
