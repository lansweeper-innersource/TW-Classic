<!-- # Silently install, uninstall, or update Lansweeper -->

You can perform a silent install, uninstall or update of Lansweeper via Windows Command Prompt (CMD). This can be done attended or unattended and can be very useful when setting up large environments with multiple scanning servers in an automated way.   
To use the silent install feature, open a Windows Command Prompt with elevated permissions. You can find an example CMD below:



As of version 10.5 the parameter `/classic` is no longer required to install the classic version of Lansweeper. However, you will still need to select your management type in the first run wizard. You can still use `/classic` to skip the selection screen and go straight to on-premise management

## Lansweeper silent install parameters

The following parameters can be used:

- /classic: install Lansweeper in the Classic way, which means without linking to Cloud in the first run wizard.
- /silent or /verysilent: with /silent, the installation progress is still shown and the cancel button is available. With /verysilent, the progress is not shown and all warning messages are suppressed.
- /accepteula: to accept the Lansweeper terms of use.
- /upgrade: to update a Lansweeper installation.
- /install: to perform a new Lansweeper installation.
- /parts: to specify which components to install (e.g. /parts ="SCAN,DB,WEB").
- /dbserver: to choose either SQLLocalDB or SQLServer (e.g. /dbserver="SQLServer").
- /dbinstance: to choose the SQL Server instance to connect to (e.g. /dbinstance="localhost\sqlexpress").
- /dbuser: to specify the database username that creates the database during installation.
- /dbpassword: to specify the database password of the user that creates the database during installation.
- /dbuserconfig: adds an optional password for the "lansweeperuser" database user, useful when installing multiple scanning servers.
- /allowdboverwrite: forces the installer to overwrite an existing database found during a new Lansweeper installation.
- /webserver: to choose either IIS or IISExpress.
- /httpport: to specify the web console's HTTP port (e.g. httpport=81).
- /httpsport: to specify the web console's HTTPS port (e.g. httpsport=82).
- /folder: to specify the Lansweeper installation folder.
- /credkeyfile: to specify the encryption key file (**Encryption.txt**) to be used.
- /noDCOMReset: to prevent the Lansweeper installer from making [DCOM changes](/docs/dcom-and-other-changes-made-by-the-lansweeper-installer) on the Lansweeper server.
- /SkipNpCapDriver: to prevent the Lansweeper installer from installing the Npcap driver, used by [Asset Radar](/docs/introduction-to-asset-radar).
- /ConfigurationFile: to perform the installation by pointing to a config file that contains the necessary parameters.

All parameters and values are case-insensitive, except the values provided for /dbuserconfig and /dbpassword.   
If a specific parameter is not provided, a default value is assumed. For instance, if you don't specify which components to install, the assumption is made that you want to install all of them.   
If the installation stops unexpectedly, its log file can be found by typing "%temp%" in the path of Windows Explorer. The log file is a .txt and will start with "Setup Log...". The final installation log file can be also found in `Program Files (x86)\Lansweeper\Install` on your Lansweeper server once the installation has fully completed. Below you can find some example commands that can be used for different installation scenarios:

## Example 1

The below example will perform an Easy, silent installation of all Lansweeper components. The Lansweeper scanning service, database (SQL LocalDB) and web console will be installed on the same machine.

```
LansweeperSetup.exe /silent /accepteula /install
```

## Example 2

The below example will silently install all Lansweeper components with a Lansweeper database hosted in SQL Server and a web console hosted in IIS.

```
LansweeperSetup.exe /silent /accepteula /dbserver="SQLServer" /dbinstance="localhost\SQLEXPRESS" /webserver=IIS /httpport=81 /install /parts=scan,db,web
```

## Example 3

The below example will install an additional scanning server, with the Lansweeper database being hosted on a remote database instance "REMOTE\_SERVER\SQLEXPRESS".

```
LansweeperSetup.exe /verysilent /accepteula /dbserver="SQLServer" /dbinstance="REMOTE_SERVER\SQLEXPRESS" /dbuserconfig="your_db_password" /install /parts=scan
```

## Example 4

The install parameters to use can also be stored in a config file. With the below contents in **InstallConfig.ini**, an installation will be performed of all Lansweeper components, with the Lansweeper database being hosted in SQL Server. The Lansweeper web console will be hosted in IIS Express using HTTP port 81.

```
[GENERAL]
ACCEPTEULA="True"
ACTION="INSTALL"
PARTS="SCAN,DB,WEB"
[DATABASE]
DBSERVER="SQLServer"
DBINSTANCE="REMOTE_SERVER\SQLEXPRESS"
DBUSERCONFIG="your_db_password"
ALLOWDBOVERWRITE="True"
[WEBSERVER]
WEBSERVER="IISExpress"
HTTPPORT="81"
```

The below command can be used to point the Lansweeper installer to your config file.

```
LansweeperSetup.exe /silent /ConfigurationFile="C:\install_files\InstallConfig.ini"
```

The /silent or /verysilent parameters always need to be provided in the command itself. They cannot be included in the config file. H

## Example 5

To install Lansweeper using an Easy, silent installation, but without installing the Npcap driver, the following command can be used.

```
LansweeperSetup.exe /silent /accepteula /install /SkipNpCapDriver
```

## Example 6

To update Lansweeper the following command can be used.

```
LansweeperSetup.exe /silent /upgrade /accepteula
```

## Example 7

To uninstall all Lansweeper components the following command can be used.

```
"C:\Program Files (x86)\Lansweeper\unins000.exe" /silent
```
