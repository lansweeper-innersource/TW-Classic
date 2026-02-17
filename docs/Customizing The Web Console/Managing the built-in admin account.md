<!-- # Managing the built-in admin account -->
To access Lansweeper's web console, you can use a local account or a Windows domain account. Additionally, a built-in admin can be used to log in and perform the initial configuration of the application. Once the configuration is complete and the necessary accounts have been provided access to the web console, it is recommended to disable the built-in admin account. The credentials for the built-in admin account can be set with the First Run Wizard when doing the initial installation of Lansweeper. After providing your license key, you can fill the username and password for this account. These credentials can be used the next time you access the web console if the built-in admin is still enabled.



Optionally, you can also give one of your Windows accounts or a local account full access to the web console. Access to other accounts can be provided later. 

After configuring these accounts, you can complete the First Run Wizard, and you will be logged in automatically to complete the configuration of Lansweeper. With the next logon, you need to use either the built-in admin or the configured Windows account to get access. Leaving the built-in account activated will put your Lansweeper web console at risk. As long as the account remains enabled, a notification will be shown in the web console.



The built-in admin account can be disabled under Configuration\Website Settings, if you're logged in with any account other than the built-in admin itself. 

If required, the built-in admin account can be enabled again using the tool `Program Files (x86)\Lansweeper\Tools\ResetWebUserRoles.exe` on your Lansweeper server. Click on `Enable Built-in Administrator` to enable the account. You will also be asked to provide the account with a new username and password when enabling it.



The same tool can also be used to edit the built-in administrator's username and password. 
