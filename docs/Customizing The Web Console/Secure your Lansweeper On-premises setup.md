<!-- # Secure your Lansweeper On-premises setup -->

As part of our ongoing commitment to enhancing security for Lansweeper installations, we’ve implemented several important measures for Lansweeper On-premises. These changes are designed to protect your data and ensure a secure environment for managing your IT assets.

These security settings are available starting from Lansweeper On-prem version 11.1. If you haven't already, [update your installation](/classic/docs/update-lansweeper-on-premises) to access the latest features.

In this article, we'll explore key security settings, guide you through updating the settings, and we'll share some best practices to improve your Lansweeper installation.

## Update the AllowedContentDomains appsetting

One of the security measures we have introduced involves restricting content domains that can be accessed by the Lansweeper On-prem application. This helps prevent the injection of potentially harmful content from unauthorized sources.

To accommodate legitimate content, such as fetching JavaScript files, you may need to update the `AllowedContentDomains` appsetting. This setting is space-delimited, meaning you should separate each domain with a space.

1. Open the Lansweeper ConfigEditor found at `Program Files (x86)\Lansweeper\Tools\ConfigEditor.exe` on your Lansweeper server.
2. Go to the **Website** tab.
3. In **appSettings**, select **Add**.
4. In the **Key** field, enter `AllowedContentDomains`.
5. In the **Value** field, enter your domain.
6. Select **Add**.
7. Select **Save**.

You may need to add the necessary domains to this appsetting when creating custom widgets or using the iFrame widget.

## Key security settings

In addition to the `AllowedContentDomains` setting, Lansweeper has enforced several HTTP headers to enhance security:

- `X-Frame-Options`: This is set to `SAMEORIGIN` by default, which prevents other sites from embedding your Lansweeper console within an iFrame widget. If necessary, this can be changed to `ALLOW` using the `x-frame-options` appsetting, although this is generally not recommended as it could expose your site to clickjacking attacks.
- `X-XSS-Protection`: When set to `1`, this setting enables the browser's XSS filter, providing an additional layer of defense against cross-site scripting attacks. This setting cannot be altered.
- `X-Content-Type-Options`: When set to `nosniff`, this setting prevents browsers from interpreting files as a different MIME type than what is specified, helping to avoid certain types of attacks. This setting cannot be changed.

## Best practices: Disable HTTP

For enhanced security, we strongly recommend disabling HTTP and configuring your Lansweeper On-premises installation to use HTTPS exclusively. This ensures that all communications between your browser and Lansweeper are encrypted, protecting sensitive data from interception. For in-depth guidance on configuring SSL in IIS, take a look at [Configure SSL in IIS](/classic/docs/configure-ssl-in-iis) or [Configure SSL in IIS Express](/classic/docs/configure-ssl-in-iis-express).
