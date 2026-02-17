<!-- # Migrate your SSO connections -->

Starting June 16th, we will begin migrating our authentication provider. This migration process will impact all Lansweeper Sites users.
Although your current SSO login will be supported during phase 1, we recommend switching as soon as possible. If you hold off migrating until phase 2, you will not be able to use SSO to log in, until you update your Identity Provider.

If your Lansweeper Sites has SSO enabled, your SSO connection will need to be migrated, and your SSO admin will need to update the connection parameters in your Identity Provider (IdP).

## Add required URLs to your allowlist before June 16th 2025

To ensure a successful migration, make sure the following URLs are accessible from your environment before June 16th:

- <https://ls.auth.lansweeper.com/> – Enables the migration process
- <https://login.auth.lansweeper.com/> – New authentication endpoint URL

If these URLs are not reachable, you will not be able to log in or start the migration.

While the URLs listed above must be reachable for the migration and login process to function, you will still log in via [app.lansweeper.com](https://app.lansweeper.com) as usual.

## Manually migrate SSO connections

In the first phase of the authentication migration, starting from June 16th, SSO admins can freely decide when to migrate to the new authentication provider.

Before proceeding with the migration, make sure that you are ready to make **immediate** changes to the connection parameters in your IdP to maintain SSO functionality.

To manually migrate your SSO connection:

1. Ensure the URLs `https://ls.auth.lansweeper.com/` and `https://login.auth.lansweeper.com/`  have been added to your allowlist.
2. In your Lansweeper Site, go to **Settings > Single Sign-On**.
3. Select **Migrate connection**.  
   

Your SSO connection will be migrated in the background.

In the second phase of the authentication migration, your SSO connection will automatically be migrated to the new authentication provider if your SSO admin hasn’t migrated manually yet.

SSO users will not be able to access Lansweeper Sites until the SSO admin updates the IdP parameters.

## Update your Identity Provider (IdP)

After migrating to the new authentication provider, your SSO admin will need to update the connection parameters in your IdP. Depending on the type of SSO connection, these parameters will differ.

To find the most recent connection parameters for your Lansweeper Site, go to **Settings > Single Sign-On**, and select **Edit connection** for the SSO connection.

Although regular SSO users briefly won’t be able to access Lansweeper Sites, SSO admins can still log in by providing their username and password. They can then check the SSO configuration and modify the IdP parameters.

### SAML

If your Site has a SAML SSO connection, your SSO/IdP admin will need to copy the following connection parameters, and update them in the IdP:

- Entity ID
- Assertion Consumer Service (ACS) URL
- Verification certificate (optional): only if a certificate was configured before

### OIDC

If your Site has an OIDC SSO connection, your SSO/IdP admin will need to copy the following connection parameter, and update it in the IdP:

- Callback URL

## Troubleshoot login issues

If you're experiencing issues logging in after the authentication provider migration, our Support team will be happy to help.

To get assistance:

1. Go to our [Contact Sales & Customer Service](https://www.lansweeper.com/contact/contact-sales/) page.
2. Fill out your contact information.
3. In the **How can we help you today?** dropdown, select **I have a question about the Support Portal**.
4. In the description, provide more details about your login issue.

Once submitted, our Support team will review your request and get back to you as soon as possible.
