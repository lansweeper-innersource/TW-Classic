<!-- # Configure Gmail to send alert and ticket emails -->

Lansweeper On-premises includes a helpdesk ticketing system that allows you to receive and respond to tickets via email. In addition, email can also be used in Lansweeper to send [report and event log alerts](/classic/docs/send-report-and-event-log-alerts).

From June 2022 onward, Google no longer allows applications like Lansweeper to sign into Gmail using your email account and account password. Instead, two-factor authentication and an app password should be set up in your Google account.

## Configure Gmail settings

1. Log into your Google account and browse to your security settings. You can do so directly by clicking this link: <https://myaccount.google.com/security>.
2. In the **Signing in to Google** section of the page, select **2-Step Verification** if not already enabled.
3. Select **Get started** button and enter your account password again as instructed.   
   Follow the on-screen instructions to link your phone to your email account as a second factor of authentication. Don't forget to enable two-factor authentication once your phone has been verified. 
4. Go back to your Google security settings. You can do so directly by going to <https://myaccount.google.com/security>.
5. In the **Signing in to Google** section of the page, select **App passwords**. You can do so directly by going to <https://myaccount.google.com/apppasswords>.
6. Enter your account password again as instructed.
7. In the **Select app** drop-down menu, choose **Other (Custom name)**.
8. Submit "Lansweeper" or another descriptive name for your app and select **Generate**. Copy the app password displayed in the resulting pop-up and select **Done**.
9. You are now ready to use your newly generated app password in Lansweeper. When setting up your helpdesk mail server under **Configuration > E-mail Settings** or your email alert server under **Configuration > E-mail Alerts**:
   - Choose Gmail from the **Select standard configuration** drop-down menu.
   - Submit your email address in the User field.
   - Submit your app password, not your Google account password, in the Password field.
   - Submit any other required settings.
