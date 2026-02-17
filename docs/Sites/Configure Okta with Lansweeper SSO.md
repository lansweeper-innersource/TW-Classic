<!-- # Configure Okta with Lansweeper SSO -->
There are two main ways to log into Lansweeper Sites: using a login/password created in Sites itself or using SSO. Logging in with SSO is supported for identity providers that offer SAML (Security Assertion Markup Language) or OIDC (OpenID Connect). Okta is such an identity provider or IdP.

This article explains how to do the necessary SSO setup in Okta to then complete an SSO configuration in Lansweeper Sites. Note that for these Okta instructions we're using SAML as an SSO connection type.

This article explains where in Okta to gather the SSO connection details that you need to submit in the **Add SSO Connection** pop-up in Sites. Make sure to read [the general Lansweeper SSO instructions](/docs/set-up-lansweeper-sso) first, before reading this article, as it only explains where in Okta to find and input the details of the SSO connection. For more information about how to improve security with Lansweeper, check out [5 Features of Lansweeper Cloud that Strengthen Security](https://www.lansweeper.com/updates/5-features-of-lansweeper-cloud-that-strengthen-security/).

## Create a SAML app integration in Okta

1. In your Okta dashboard, go to the **Applications** menu.
2. Select **Create App Integration**, choose SAML 2.0 and select **Next**. ![okta-create-app-integration.jpg](/docs/.document360/assets/article_357/image_002.jpg)
3. Enter a descriptive name for your app integration and continue.

## Configure your SSO app

1. Select **Download Okta Certificate**.  
   ![okta-sso-certificate.jpg](/docs/.document360/assets/article_357/image_003.jpg)
2. Rename the resulting file so it ends in ".cer" instead of ".cert".
3. Upload the Okta certificate in the **Add SSO Connection** pop-up in your site.
4. Copy the Entity ID from the **Add SSO Connection** pop-up in your site and paste it into the **Audience URI (SP Entity ID)** field.   
   ![okta-sso-entity-id.jpg](/docs/.document360/assets/article_357/image_004.jpg)
5. Copy the Assertion Consumer Service (ACS) URL from the **Add SSO Connection** pop-up in your site and paste it into the **Single sign on URL** field.   
   ![okta-sso-acs-url.jpg](/docs/.document360/assets/article_357/image_005.jpg)
6. In the **Attribute Statements** section, add the following two attributes:
   - Name: email, value: user.email
   - Name: email\_verified, value: true

   ![okta-sso-attribute-statements.jpg](/docs/.document360/assets/article_357/image_006.jpg)

   Do not skip this step. Adding these attributes is important as they are required by Lansweeper Sites' underlying SSO login process.
7. In Okta, complete the remaining setup questions and select **Finish**
8. In the **Sign On** section of your newly created app, select **View Setup Instructions**.   
   ![okta-saml-setup-instructions.jpg](/docs/.document360/assets/article_357/image_007.jpg)
9. Copy the Identity Provider Single Sign-On URL seen on the resulting page and paste it into the **Sign in URL** field in the **Add SSO Connection** pop-up in your site.  
   ![okta-sso-url.jpg](/docs/.document360/assets/article_357/image_008.jpg)
