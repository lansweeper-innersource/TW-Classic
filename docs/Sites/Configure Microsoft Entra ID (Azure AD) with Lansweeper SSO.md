<!-- # Configure Microsoft Entra ID (Azure AD) with Lansweeper SSO -->
There are two main ways to log into Lansweeper Sites: using a login/password created in Sites itself or using SSO. Logging in with SSO is supported for identity providers that offer SAML (Security Assertion Markup Language) or OIDC (OpenID Connect). Azure Active Directory is such an identity provider or IdP.

This article explains how to do the necessary SSO setup in Microsoft Entra ID (Azure AD) to then complete an SSO configuration in Lansweeper Sites. Note that for these Microsoft Entra ID (Azure AD) instructions we're using SAML as an SSO connection type.

This article explains where in Microsoft Entra ID (Azure AD) to gather the SSO connection details that you need to submit in the **Add SSO Connection** pop-up in Sites. Make sure to read [the general Lansweeper SSO instructions](/classic/docs/set-up-lansweeper-sso) first before reading this article, as it only explains where in Microsoft Entra ID (Azure AD) to find and input the details of the SSO connection. For more information about how to improve security with Lansweeper, check out [5 Features of Lansweeper Cloud that Strengthen Security](https://www.lansweeper.com/updates/5-features-of-lansweeper-cloud-that-strengthen-security/).

## Create an application in Microsoft Entra ID (Azure AD)

1. Log into the Azure portal and browse to the Azure Active Directory resource.
2. Go to the **Enterprise applications** menu and select **New application**.  
   
3. Select **Create your own application**.  
   
4. In the resulting pop-up, enter a descriptive name for your application and select **Integrate any other application you don't find in the gallery (Non-Gallery)**.  
   
5. Finally, select **Create**.

## Configure your SSO app

1. In the **Single sign-on** menu of your newly created app, select SAML.  
   
2. Copy the Entity ID from the **Add SSO Connection** pop-up in Lansweeper and paste it in your SAML settings.
3. Select **Edit** under **Basic SAML Configuration**.  
   
4. Enter the Entity ID into the **Identifier (Entity ID)** field and set the new ID as default.
5. Copy the Assertion Consumer Service (ACS) URL from the **Add SSO Connection** pop-up in Lansweeper and paste it into the **Reply URL (Assertion Consumer Service URL)**field.
6. Copy the SingleLogout Service (SLO) URL from the **Add SSO Connection** pop-up in Lansweeper and paste it into the **Logout Url** field.  
   
7. Select **Save**.
8. In the **SAML Signing Certificate** section of your app's SSO config, download the Base64 certificate. Upload it in the **Add SSO Connection** pop-up in Lansweeper.  
   
9. In the **Set up <Your App Name>** section of your app's SSO config, copy the Login URL.  
   
10. Paste it into the **Add SSO Connection** pop-up in Lansweeper. The field you need to paste the value into in Lansweeper is called **Sign in URL**. Optionally, you can also copy the Logout URL from Microsoft Entra ID (Azure AD) to Lansweeper.
11. In the **Attributes & Claims** section of your app's SSO config, select **Edit**.   
    
12. Choose **Add new claim**, configure the new claim as mentioned below and select **Save**.  
    For the source attribute, enter `true` and select it. Your submission will automatically be surrounded by quotes.
    - Name: `email_verified`
    - Source: Attribute
    - Source attribute: `true`

    Do not skip this step. Adding this attribute is important as it is required by Lansweeper Sites' underlying SSO login process.
13. In the **Users and groups** menu of your app, select **Add user/group**.  
    
14. Select the users and/or groups that will be able to log into Sites using SSO. As an Microsoft Entra ID (Azure AD) admin, you will be able to monitor your users' SSO logins in Microsoft Entra ID (Azure AD).
