<!-- # Set up Lansweeper SSO -->
There are two main ways to log into your Lansweeper Site: using a login/password created in Lansweeper Sites itself or using SSO.

Where possible, using single sign-on (SSO) is recommended, as it has a number of benefits. SSO allows you to centrally manage accounts in a third-party system you're already using. This simplifies management tasks, eliminates the need for each user to have multiple login/password combinations and allows you to enforce your own security policies, among other things. For more information about how to improve security, check out [5 Features of Lansweeper Cloud that Strengthen Security](https://www.lansweeper.com/updates/5-features-of-lansweeper-cloud-that-strengthen-security/).

Lansweeper Sites supports both OpenID Connect (OIDC) and SAML for setting up SSO. Any identity provider (IdP) that supports at least one of these options is a suitable candidate for use with Sites. Azure Active Directory, Google and Okta are just a few examples of identity providers that you can use to log into your site. SSO can be set up quickly and easily, as explained in the below steps.

For more information on configuring SSO, check out [Manage Lansweeper SSO](/docs/manage-lansweeper-cloud-sso).

## Add an SSO connection

1. Log into your site using your regular Lansweeper login/password combination.
2. Choose a site and select the **Settings** module.  
   ![lansweeper sso 3.png](/docs/.document360/assets/article_304/image_002.jpg)
3. Go to the **Single Sign-On** menu and select **Add SSO Connection**.  
   **![cloud-sso-menu.jpg](/docs/.document360/assets/article_304/image_003.jpg)**
4. In the resulting pop-up, select the type of SSO connection you want to set up and select **Continue**.   

   Lansweeper Sites supports two types of SSO connections, SAML (Security Assertion Markup Language) and OIDC (OpenID Connect). Which one you choose will depend on the identity provider you're using and the type(s) it supports. If you're using Azure AD as your IdP for instance, SAML is a suitable SSO connection type.
5. Enter a descriptive name for the connection, and several pieces of information regarding the connection. This is information you'll gather from your identity provider (IdP).  

   To log in to Lansweeper directly from your IdP with SSO, toggle **Enable IdP-Initiated Single Sign-On**to **On**.   
   Leaving the toggle **Off** will result in errors when logging in from your IdP.

   ![lansweeper sso 1.png](/docs/.document360/assets/article_304/image_004.jpg)

## Configure the SSO connection on the IdP side

1. You'll need to take some of the info provided in the pop-up and input it in your IdP configuration. The location to input the necessary info for the SSO connection will differ depending on the IdP you are using.  
   Only Azure AD and Okta are currently supported by the Lansweeper Support team, but there are many more identity providers you can use.
   - [How to use Azure AD with SSO](/docs/configure-microsoft-entra-id-azure-ad-with-lansweeper-sso)
   - [How to use Okta with SSO](/docs/configure-okta-with-lansweeper-sso)

   Consult the website and documentation of your specific identity provider (IdP) for up-to-date instructions on how to configure SAML or OIDC in that IdP. For SAML, make sure the certificate you're providing in the SSO pop-up is a Base64-encoded CER or PEM.
2. In the attribute setup of your SSO connection on the IdP side, make sure your IdP is configured to send both the user's email and an `email_verified` attribute to the Site.  
   Our knowledge base contains more specific attribute setup instructions for Azure AD and Okta, but the process is similar for other identity providers.  

   Do not skip this step. Adding these attributes is important as it's required by Lansweeper Site's underlying SSO login process that a user has an email address, and for that email address to be verified.

## Add, verify and enable your domain

1. Select **Continue** in the pop-up after exchanging necessary details between your Site and your IdP.
2. Select **Add Domain** and submit your domain name with the format `yourdomain.com`.  
   ![cloud-sso-add-domain-url.jpg](/docs/.document360/assets/article_304/image_005.jpg)
3. Copy the code presented in the pop-up.   
   You will need to add this code as a TXT record to your domain's DNS provider to verify the domain. If necessary, consult the website and documentation of your specific DNS provider for up-to-date instructions on how to set up the TXT record.  

   Adding the TXT record in DNS is an added security measure to verify that you own the domain. Once the domain has been verified, you can remove the TXT record from your DNS configuration.

   ![cloud-domain-verification-code.jpg](/docs/.document360/assets/article_304/image_006.jpg)
4. Select **Got it** and wait a few minutes for the DNS verification to automatically happen. Alternatively, select **Verify Domain**.
5. Select **Enable domain** once your domain is verified.

## Log in using SSO

Once you've set up your SSO connection new and existing Lansweeper Site users in your domain should be able to log in by selecting **Log in with Single Sign-On**. They will be asked for their email address prior to starting the SSO login process.

- Users who already created a login/password in Lansweeper Sites, prior to SSO being enabled for their domain, are by default able to log in with either their old login details or SSO. When they log in with SSO for the first time, they will be asked to link their old Sites account with their new SSO one.
- Users who did not already create a login/password in Lansweeper Sites will only be able to log in with SSO if SSO is configured for their domain. They will not be able to create another user account in Sites itself.

![cloud-sso-login-button.jpg](/docs/.document360/assets/article_304/image_007.jpg)

To log in to Lansweeper directly from your IdP with SSO, toggle **Enable IdP-Initiated Single Sign-On**to **On**when [adding or editing your SSO connection](#addsso).

You can combine SSO either with Sites-configured MFA (Multi-Factor Authentication) or the MFA of your IdP. That way, you can add an extra layer of security to the login process. If you already have MFA set up or enforced in your IdP, it will automatically be part of the Lansweeper Sites SSO login process for your domain users.

If you enabled both SSO for your domain, and MFA through Lansweeper Sites, you will not be asked to provide a one-time password generated by your authenticator app when using SSO to log in.  
However, users logging in using Lansweeper credentials will be asked to provide a one-time password.

## Enforce SSO

You can optionally enforce the use of SSO by all users in your site.

1. Go to **Configuration**.
2. In the **Site settings** menu, enable **Force login with SSO to access this site**.

If a user subsequently tries to log into your site with a Sites-created login/password, they will be denied site access. Site owners will still be able to log in using the Sites-created login/password in case of issues with your domain's SSO setup.

Make sure SSO is working for all domains that have access to your site, prior to enforcing SSO in your site settings. Otherwise, some users may inadvertently be locked out. You can use the test button next to your SSO connection to validate that the connection is working.

## Add SSO connection managers

Optionally, you can [add managers to your SSO connection](/docs/add-managers-to-an-sso-connection) for redundancy and security purposes. This means you are not dependent on a single person to manage the SSO connection.
