<!-- # Scan Intune V2 targets -->
This page is for Lansweeper Sites. For Lansweeper On-prem, see [Scan Intune targets](/classic/docs/scan-mobile-devices-through-microsoft-intune).

[Lansweeper](https://www.lansweeper.com/) can be used to scan Android, iOS and Windows Phone mobile devices through Intune. To start scanning mobile devices, you'll first need to configure the appropriate credentials. These Microsoft Cloud Service credentials not only enable the scanning of Intune but also maximize the utilization of Modern Authentication and the Microsoft Graph API through application permissions.

With an Intune V2 scanning target you'll be able to scan Android, iOS (iPhone and iPad) and Windows Phone mobile devices enrolled in Intune.

## Prerequisites

To scan mobile devices from Intune with a Microsoft Cloud Services Credential, make sure that:

- You've already [set up your Microsoft Cloud Services application](/classic/docs/create-a-microsoft-cloud-services-application).
- You're in possession of your Microsoft Cloud Services application's Application (client) ID, Directory (tenant) ID, and Client secret or certificate. These are obtained when creating the application.

## Add permissions to the Microsoft Graph application to scan Intune data

1. Open your company's Azure portal and navigate to **App registrations**.
2. Select [the app you've already created](/classic/docs/create-a-microsoft-cloud-services-application) and select the **API permissions** tab in the left-hand menu.  
   
3. On the **API permissions** page, click **Add permission** and select **Microsoft Graph** from the API list.    
   
4. As we are setting up the Microsoft Graph API to enforce modern authentication, you will need to add Application permissions. Start by selecting **Application permissions**.   
   
5. Add the **DeviceManagementManagedDevices.Read.All** API permission and select **Save**. This permission is required to scan your Intune data.  
   
6. Admin consent must still be granted. Select **Grant admin consent for <organization>** and click **Grant**in the resulting pop-up.  
     
     
   The added permissions should now show **Granted for <organization>**.  
   

## Set up Lansweeper to scan your Intune data

### Add a Microsoft Cloud Service credential

1. In your Lansweeper Cloud environment, go to **Scanning > Credential vault > My credentials**.
2. Select **Add new credential**.  
   
3. In the pop-up, select **Microsoft Cloud Service** and continue.
4. Fill in the fields:
   1. Name: name for the credential.
   2. Directory (tenant) ID and Application (client) ID: these are obtained when [creating the Microsoft Cloud Services application](/classic/docs/create-a-microsoft-cloud-services-application).
   3. Authentication method: select either Client Secret or Certificate Thumbprint.
   4. Client Secret or Certificate Thumbprint: obtained when creating the MS Graph app in Azure.  
      

### Add an Intune V2 scanning target

1. In your Lansweeper Cloud environment, navigate to **Scanning > Targets**.
2. Select **Add scanning target**.   
   
3. In the pop-up, choose a scan server and select the **Intune V2** scanning target.
4. Enter a name and description for the new target, and select a scanning schedule.
5. Select a Microsoft Cloud Service credential to assign to the Intune V2 scanning target.  
   
6. Select **Save and exit**, or **Save target**.
