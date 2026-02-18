<!-- # Install Lansweeper On-prem -->
Depending on your situation, you might require a different installation experience.  
If you're a new customer and do not have a Lansweeper On-prem installation, [install the Lansweeper Cloud-first trial](/classic/docs/install-the-lansweeper-trial "Install the Lansweeper Cloud-first trial").  
If you're an existing customer with a Lansweeper On-prem installation, [link your installation with a cloud site](/classic/docs/link-lansweeper-on-prem-with-lansweeper-sites "Link your cloud site").  
If you're an existing customer and want to create a new Lansweeper installation that's linked with cloud, [install Lansweeper Cloud](/classic/docs/install-lansweeper-sites "Install Lansweeper Cloud").

If you don't have Lansweeper On-prem yet, you can always [download Lansweeper On-prem](https://www.lansweeper.com/download/).

You don't need a Lansweeper license key to try out Lansweeper On-prem, but your installation will be in freeware mode. To fully unlock Lansweeper's potential, request an on-prem trial key at [Start Your Lansweeper On-prem Trial](https://www.lansweeper.com/classic/) or take a look at our [pricing & plans](https://www.lansweeper.com/pricing/) to purchase a license key.

There are two main ways you can install the Lansweeper software, both of which are documented in this installation guide: you can choose an Easy or an Advanced install.  
Regardless of your installation type, the First Run Wizard will pop up after Lansweeper has finished installing.

To help you select the correct database server for your needs, we recommend reviewing the comparison list in [this knowledge base article](/classic/docs/compatible-sql-database-servers-for-hosting-the-lansweeper-database).

## Perform an Easy Install

The easy install process will install all Lansweeper components (Lansweeper scanning service, database and web console) on the same machine. The database will be installed under the SQL LocalDB database server, which is limited by Microsoft to 10 GB of data, and the web console under the IIS Express web server.

1. Download [the latest Lansweeper installer](https://www.lansweeper.com/install-lansweeper/) and run it on the Windows computer you want to install Lansweeper on.
2. Review the terms of use, click **Accept** to continue.  
   
3. Select the **Easy install** option.
4. You can choose a custom HTTP and HTTPS port used for the web console. If you don't choose custom ports, the installer will automatically install the web console under the first available ports.   
   
5. You can choose a custom folder to install under. Select **Install** to start the installation process.  
   - The Lansweeper service will be installed under Windows Services.
   - The Lansweeper database will be installed under SQL LocalDB, which is limited by Microsoft to 10 GB of data. The database will be called "lansweeperdb" and should not be renamed.
   - The Lansweeper web console will be installed under IIS Express, which is installed and configured automatically, and your preferred ports.
6. When you get to the screen that confirms the successful installation of Lansweeper, select **Finish** to close the installer.

## Perform an Advanced Install

The advanced install process allows you to choose which component (Lansweeper scanning service, database, web console) to install on which machine. The database can be installed under the SQL LocalDB or SQL Server database server, and the web console can be installed under the IIS or IIS Express web server.

1. If you want to host the database under SQL Server, make sure you manually install your SQL Server instance prior to running the Lansweeper installer. You'll need to point the Lansweeper installer to your existing SQL Server instance.
2. Download [the latest Lansweeper installer](https://www.lansweeper.com/install-lansweeper/) and run it on the Windows computer you want to install Lansweeper on.
3. Review the terms of use, click **Accept** to continue.  
   
4. Select the **Advanced install** option and select the components you want to install on the machine.  
   

   If you're spreading out database, service and website over several machines, keep in mind that:  
   - The database must be installed first, then the service and then the web console.
   - You need to reset the database password after installing all components, due to the installer adding a random password to the service and website configuration files. Instructions for resetting the database password can be found in [this knowledge base article](/classic/docs/change-the-lansweeper-database-password). If you don't reset the password, you'll see database login failures.
   - You need to copy the **Encryption.txt** file from the server hosting the web console to any servers hosting the Lansweeper service, replacing the default file generated on the servers. The **Encryption.txt** file is a key used to encrypt and decrypt credentials submitted in Lansweeper and must be the same on all servers hosting a Lansweeper component. If you're spreading out components over several machines, each server will have a unique file by default and you'll need to manually copy one of the files to all Lansweeper servers, so the encryption key is the same on all servers:    
     `Program Files (x86)\Lansweeper\Key\Encryption.txt`
5. Select the database server you want to use. If you're spreading out Lansweeper components over several machines, you need a SQL Server. For a more detailed comparison between database servers, review [this knowledge base article](/classic/docs/compatible-sql-database-servers-for-hosting-the-lansweeper-database).

   
6. If you selected a SQL Server as your database type, submit the name of the SQL Server instance you want to install the Lansweeper database under. This should be the same SQL Server instance name you use when logging into other SQL tools like SQL Server Management Studio.
7. If you selected a SQL Server as your database type, select the authentication method you want to use to connect to SQL Server from the **Authentication** dropdown. You can choose Windows authentication or SQL Server authentication. If you choose Windows authentication, the database installation is performed under the currently logged on Windows user. If you choose SQL authentication, you need to submit your SQL username and password.  
   

   The user performing the database installation must be a member of your SQL Server's sysadmin server role. When the installation has completed, the Lansweeper service and web console will connect to the database with a newly created SQL user called "lansweeperuser", which only has access to the Lansweeper database.
8. If you are installing the Lansweeper web console, select the web server you want to install the console under. Selecting **Recommended** will install the web console under IIS Express, selecting **Advanced** will install the web console under IIS. The **Advanced** option will only be available if IIS is already enabled on your computer.  
   
9. You can choose a custom HTTP and (if offered by the installer) HTTPS port used for the web console. If you don't choose custom ports, the installer will automatically install the web console under the first available ports.
10. If your web server's registry keys indicate that you have allowed insecure SSL renegotiation, you will be prompted to disable insecure SSL renegotiations.   
    Disabling insecure renegotiation is **optional**, but recommended for improved system security.  
    The registry key for this setting can be found at `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL`.  

    Disabling insecure SSL/TLS renegotiation configures the system to refuse renegotiation requests from clients, preventing potential abuse and reducing the attack surface of your server.  
    This setting applies system-wide and will affect **all SSL/TLS connections** on this system, not just Lansweeper.
11. You can choose a custom folder to install under. Select **Install** to start the installation process.
    - The Lansweeper service will be installed under Windows Services.
    - The Lansweeper database will be installed under the database server of your choice, will be called "lansweeperdb" and should not be renamed.
    - The Lansweeper web console will be installed under the web server of your choice and your preferred ports.
12. When you get to the screen that confirms the successful installation of Lansweeper, select **Finish** to close the installer.
13. If you did not perform a full installation (service, database and web console), run the installer on any other machine you want to use to host Lansweeper. Click through the opening and license agreement screens and once again select the **Advanced install** option.  
    
    - Select the components (service and/or web console) you want to install on the machine.
    - Tick the **SQL Server** checkbox.
    - Point the installer to your existing SQL Server instance and Lansweeper database when prompted.

## First Run Wizard

Once you've installed Lansweeper On-prem, the web console automatically opens in your default web browser. When you access the Lansweeper web console for the first time, you are presented with a First Run Wizard, which allows you to add an initial scanning setup and configure some basic options.

The First Run Wizard is only meant for submitting an initial configuration of a Lansweeper On-prem installation. You'll only see and need to configure this wizard once. You can make changes to your settings and submit additional network segments for scanning once you've completed the wizard.

### Select a management type

Select **Choose on-premise management**.  


If you have a license key to unlock your Lansweeper installation, see [Apply your Lansweeper license](/classic/docs/apply-your-lansweeper-license).

### Web console login configuration

Configure a basic access configuration for the web console. There are two options:

1. A built-in administrator account with full access to the console and whose username and password you can configure.
2. Giving an existing Windows user full access to the web console.  
   More users can be provided access and [your access configuration can be customized further](/classic/docs/restrict-access-to-the-web-console) after completion of the First Run Wizard.

For any subsequent access to the web console after completion of the First Run, you will be asked to log in first. You can do so with the built-in admin user/password or the Windows user you previously chose.

### Scanning configuration

Select the IP ranges you would like to scan. By default, the wizard will present you with the IP ranges of your local subnet(s), but you can submit other ranges in the available input boxes.   
Scanning assets with Asset Radar and Extended Display Scanning is enabled by default, but can be disabled if required.

Lansweeper will automatically scan the domain or workgroup your Lansweeper server is located in.

### Scanning starts

Lansweeper will start scanning your network. Select **Finish** to proceed to the web console, which will display scanned data. You can safely explore the console while scans are taking place in the background.

It is recommended to [submit scanning credentials](/classic/docs/create-and-map-scanning-credentials) after completion of the First Run Wizard. Lansweeper scans basic asset info without credentials, but having scanning credentials greatly increases the amount of detail that can be retrieved. If you want, you can also [submit additional network segments for scanning](https://www.lansweeper.com/kb-category/scanning-your-network/) after completion of the First Run.
