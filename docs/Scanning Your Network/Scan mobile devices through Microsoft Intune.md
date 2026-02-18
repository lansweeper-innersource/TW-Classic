<!-- # Scan mobile devices through Microsoft Intune -->

This page is for Lansweeper On-prem. For Lansweeper Sites, see [Scan Intune V2 targets](/classic/docs/scan-intune-v2-targets).

The Microsoft Cloud Service credential can be used to scan Intune, and makes full use of Modern Authentication and the Microsoft Graph API, using application permissions.

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

1. In the Lansweeper web console, navigate to the **Scanning > Scanning credentials**.
2. In the**Credentials** tab, select **Add new Credential**.
3. Select **Microsoft Cloud Service** as a credential type, and fill in the name, Application ID and Directory ID. Application ID and Directory ID are obtained when [creating the Microsoft Cloud Services application](/classic/docs/create-a-microsoft-cloud-services-application).
4. If a *Client secret* is selected, add the client secret (obtained when creating the MS Graph app in Azure).  
   If a *Certificate thumbprint* is selected, add the certificate thumbprint which is obtained when creating the MS Graph app in Azure.
5. Optionally, add a new scanning target from this pop-up. Select the designated checkboxes and click **OK**. The corresponding scanning target will be created.  
     

   When multiple scanning targets are selected, ensure that the app has sufficient [API permissions](/classic/docs/create-a-microsoft-cloud-services-application#HowToScanAndMail "Creating a Microsoft Cloud Services application for scanning and email") to scan the selected scanning targets.

### Add an Intune scanning target

1. In the Lansweeper web console, navigate to the **Scanning > Scanning targets**.
2. In the**Scanning Targets**tab, select **Add Scanning Target**.
3. Select **Intune**as a target type.  
   
4. Enter a target name, and select a credential to assign to the scanning target.  
   Alternatively, create a new Microsoft Cloud Service credential.
5. Enter a description, and select the scanning schedule for the target.
6. Select **Ok**.
