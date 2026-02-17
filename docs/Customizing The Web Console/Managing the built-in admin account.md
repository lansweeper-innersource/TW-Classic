<!-- # Managing the built-in admin account -->
To access Lansweeper's web console, you can use a local account or a Windows domain account. Additionally, a built-in admin can be used to log in and perform the initial configuration of the application. Once the configuration is complete and the necessary accounts have been provided access to the web console, it is recommended to disable the built-in admin account. The credentials for the built-in admin account can be set with the First Run Wizard when doing the initial installation of Lansweeper. After providing your license key, you can fill the username and password for this account. These credentials can be used the next time you access the web console if the built-in admin is still enabled.

![Disabling-built-in-admin-1.png](/docs/.document360/assets/article_041/image_001.jpg)

Optionally, you can also give one of your Windows accounts or a local account full access to the web console. Access to other accounts can be provided later. ![Disabling-built-in-admin-2.png](/docs/.document360/assets/article_041/image_002.jpg)

After configuring these accounts, you can complete the First Run Wizard, and you will be logged in automatically to complete the configuration of Lansweeper. With the next logon, you need to use either the built-in admin or the configured Windows account to get access. Leaving the built-in account activated will put your Lansweeper web console at risk. As long as the account remains enabled, a notification will be shown in the web console.

![Disabling-built-in-admin2-3.png](/docs/.document360/assets/article_041/image_003.jpg)

The built-in admin account can be disabled under Configuration\Website Settings, if you're logged in with any account other than the built-in admin itself. ![Disabling-built-in-admin2-4.png](/docs/.document360/assets/article_041/image_004.jpg)

If required, the built-in admin account can be enabled again using the tool `Program Files (x86)\Lansweeper\Tools\ResetWebUserRoles.exe` on your Lansweeper server. Click on `Enable Built-in Administrator` to enable the account. You will also be asked to provide the account with a new username and password when enabling it.

![Disabling-built-in-admin-5.png](/docs/.document360/assets/article_041/image_005.jpg)

The same tool can also be used to edit the built-in administrator's username and password. ![Disabling-built-in-admin-6.png](/docs/.document360/assets/article_041/image_006.jpg)
