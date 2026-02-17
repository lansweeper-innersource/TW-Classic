<!-- # Install IIS (Internet Information Services) -->
The Lansweeper web console can be run under the Internet Information Services (IIS) Express or IIS web server, both developed by Microsoft. IIS Express is the default web server used by [Lansweeper](https://www.lansweeper.com/ "Lansweeper"), but you can choose to install Lansweeper in IIS.

IIS or Internet Information Services is available in most editions of Windows, though disabled by default. If you choose to host the Lansweeper console under IIS, you first must enable the IIS feature on your machine before running the Lansweeper installer.

If IIS is not installed by default, you can download and install the latest version of IIS Express for your Windows 10 or Windows 11 OS from [the Microsoft website](https://www.microsoft.com/en-US/download/details.aspx?id=48264). IIS versions later than 7.0 include the new IIS Manager user interface.

## Enable Internet Information Services (IIS) on a Windows 10 or Windows 11 computer

1. Open the **Start** menu.
2. Type "features" and select **Turn Windows features on or off**.

   ![menu-turn-windows-features-on-or-off.jpg](/docs/.document360/assets/article_077/image_002.jpg)
3. Tick the **Internet Information Services** checkbox and select **OK**.

   ![how-to-install-iis-internet-information-services-1.jpg](/docs/.document360/assets/article_077/image_003.jpg)
4. Wait for the installation to complete and select **Close**.
5. If you plan on using integrated Windows authentication in Lansweeper or another website hosted in IIS, tick the **Windows Authentication** option under **Internet Information Services > World Wide Web Services > Security** as well and select **OK**.

   ![how-to-install-iis-internet-information-services-4.jpg](/docs/.document360/assets/article_077/image_004.jpg)
6. You can now install Lansweeper and choose IIS as your web server by following [this installation guide](/docs/install-lansweeper-on-prem#heading2 "Advanced Lansweeper installation"). After installation, you will see your Lansweeper web console listed in IIS Manager (inetmgr), along with a default website generated when you enabled IIS.

   ![menu-iis-manager.jpg](/docs/.document360/assets/article_077/image_005.jpg)

   ![how-to-install-iis-internet-information-services-5.jpg](/docs/.document360/assets/article_077/image_006.jpg)
7. If you already are running Lansweeper with IIS Express, you can now migrate your existing Lansweeper web console running under IIS Express to IIS Server.   
   To do so, reinstall the web console by following these instructions to [install your Lansweeper web console](/docs/reinstalling-the-web-console) in IIS. When you get to step 11, choose the Advanced (IIS) option.
