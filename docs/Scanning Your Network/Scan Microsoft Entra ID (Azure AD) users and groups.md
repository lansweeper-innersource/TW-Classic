<!-- # Scan Microsoft Entra ID (Azure AD) users and groups -->
Lansweeper is capable of scanning Microsoft Entra ID (Azure Active Directory) users and groups using a scanning target. This scanning target makes use of the Microsoft Cloud Service credential type, which can also be used to scan your [Intune assets](/docs/scan-mobile-devices-through-microsoft-intune) or [Microsoft 365 tenant](/docs/scan-microsoft-365-targets). This credential makes use of Modern Authentication and the Microsoft Graph API, using application permissions.

## Prerequisites

To scan your Microsoft Entra ID (Azure AD) make sure that:

- You've already [set up your Microsoft Cloud Services application](/docs/create-a-microsoft-cloud-services-application "Creating a Microsoft Cloud Services application for scanning and email").
- You're in possession of your Microsoft Cloud Services application's Application (client) ID, Directory (tenant) ID, and Client secret or certificate. These are obtained when creating the application.

## Add permissions to the Microsoft Graph application

1. Open your company's Azure portal and go to **App registrations**.
2. Select the [the app you've already created](/docs/create-a-microsoft-cloud-services-application "Creating a Microsoft Cloud Services application for scanning and email"), then select the **API permissions** tab.  
   ![Scanning_with_a_Microsoft_cloud_credential_5.jpg](/docs/.document360/assets/article_222/image_001.jpg)
3. Select **Add permission** then select **Microsoft Graph** from the API list.  
   ![Scanning_M365_with_a_Microsoft_cloud_credential_6.jpg](/docs/.document360/assets/article_222/image_002.jpg)
4. As you're setting up the Microsoft Graph API to enforce modern authentication, you will need to add Application permissions. Select **Application permissions**.  
   ![Scanning_with_a_Microsoft_cloud_credential_6.jpg](/docs/.document360/assets/article_222/image_003.jpg)
5. Add the **Group.Read.All**, **GroupMember.Read.All** and **User.Read.All** API permissions. These are required to be able to scan all Microsoft Entra ID (Azure Active Directory) data. Once the permissions are added, select **Save** button and double-check the permissions listed.
6. Select **Grant admin consent for <organization>** and select **Grant** in the resulting pop-up. The added permissions should now show **Granted for <organization>**.

![AzureAdAdminConsentGranted.png](/docs/.document360/assets/article_222/image_004.jpg)

## Add a Microsoft Cloud Service credential

1. In Lansweeper, navigate to **Scanning > Scanning Credentials.**
2. Select **Add New Credential**.
3. In the Type dropdown, select **Microsoft Cloud Service**.
4. Enter a name for your credential.
5. Enter the Application ID and Directory ID that were created when you [created a Microsoft Cloud Services application](/docs/create-a-microsoft-cloud-services-application "Create a Microsoft Cloud Services application").
6. For **Authentication type**, select either **Client secret** or **Certificate thumbprint**.
7. Enter the client secret or certificate thumbprint that was created when you [created a Microsoft Cloud Services application](/docs/create-a-microsoft-cloud-services-application "Create a Microsoft Cloud Services application").
8. If you'd like a Microsoft Entra ID scan target to be automatically created, select **Microsoft Entra ID (Azure Active Directory)**. If you plan to use the same credentials for multiple scan targets, you can select those as well.
9. Select **OK**.  

   If you're using the Microsoft Cloud Service credential for multiple scan targets, ensure that the app has sufficient [API permissions](/docs/create-a-microsoft-cloud-services-application#HowToScanAndMail "Creating a Microsoft Cloud Services application for scanning and email") to scan the selected scanning targets. If you'd like to use the credential for both Microsoft 365 and Microsoft Entra ID (Azure Active Directory) scanning for example, make sure application permissions are set for both.

If you already have a Microsoft Cloud Services credential, you can add a new Microsoft Entra ID (Azure Active Directory) Scanning target to it via **Scanning > Scanning Targets**. During the creation of your Microsoft Entra ID (Azure Active Directory) scanning target, you can select a pre-existing credential.
