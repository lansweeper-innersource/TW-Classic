<!-- # Could not load type System.ServiceModel.Activation. HttpModule -->
If ASP.NET is not properly enabled (anymore) on the server hosting your Lansweeper web console, your console may become inaccessible and you may encounter the error below.

Could not load type 'System.ServiceModel.Activation.HttpModule' from assembly 'System.ServiceModel, Version=3.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089'.

This article explains how to resolve this issue. The exact instructions you should follow depend on which operating system you are using.

## Windows 8 and more recent operating systems

To resolve this issue if you are running Windows 8 or a more recent operating system, follow the steps below. Alternatively, you can access **Turn Windows Features On/Off** on the computer and register ASP.NET there. On Server operating systems, you can use Server Manager for ASP.NET registration.

1. On the machine hosting your Lansweeper web console, run Command Prompt as an administrator.

   ![could-not-load-type-system_servicemodel_activation-1.jpg](/docs/.document360/assets/article_281/image_001.jpg)
2. Type the following command and press **Enter** to enable ASP.NET:  
     

   ```
   dism /online /enable-feature /featurename:IIS-ASPNET45 /all
   ```

   ![could-not-load-type-system_servicemodel_activation-4.jpg](/docs/.document360/assets/article_281/image_002.jpg)
3. Reboot the machine hosting your Lansweeper web console.

## Operating systems below Windows 8

To resolve this issue if you are running an operating system version below Windows 8, follow these steps:

1. On the machine hosting your Lansweeper web console, run Command Prompt as an administrator.

   ![could-not-load-type-system_servicemodel_activation-1.jpg](/docs/.document360/assets/article_281/image_003.jpg)
2. Type the following command and press **Enter** to navigate to the appropriate folder:  

   ```
   cd\Windows\Microsoft.NET\Framework64\v4.0.30319
   ```

   ![could-not-load-type-system_servicemodel_activation-2.jpg](/docs/.document360/assets/article_281/image_004.jpg)
3. Type the following command and press **Enter** to enable ASP.NET:  
     

   ```
   aspnet_regiis.exe -I
   ```

   ![could-not-load-type-system_servicemodel_activation-3.jpg](/docs/.document360/assets/article_281/image_005.jpg)
4. Reboot the machine hosting your Lansweeper web console.
