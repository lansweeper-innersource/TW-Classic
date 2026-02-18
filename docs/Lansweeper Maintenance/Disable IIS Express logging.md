<!-- # Disable IIS Express logging -->
If your Lansweeper web console is hosted by [the IIS Express web server](/classic/docs/lansweeper-classic-components-and-architecture), the IIS Express log files below may be generated.

To preserve disk space and improve performance, it is generally recommended that you disable IIS Express logging and then delete the IIS Express logs.

`C:\Windows\SysWOW64\config\systemprofile\Documents\IISExpress\Logs\LANSWEEPER.log`

`C:\Windows\System32\config\systemprofile\Documents\IISExpress\Logs\LANSWEEPER.log`

`C:\Documents and Settings\<username>\My Documents\IISExpress\Logs\LANSWEEPER.log`

`C:\Users\<username>\Documents\IISExpress\Logs\LANSWEEPER.log`

## Disable IIS Express logging

1. Stop the **IIS Express service** in Windows Services.
2. Open the following file with Notepad or another text editor:

   `Program Files (x86)\Lansweeper\IISexpress\iisexpress.config`
3. Remove the following lines from the file, then close and save the edited file.  
   `<add name="HttpLoggingModule" image="%IIS_BIN%\loghttp.dll" />   
    <add name="HttpLoggingModule" lockItem="true" />`
4. Restart the **IIS Express service** in Windows Services
5. Once you've disabled logging, you can safely delete the log files below if they are present on your system.

   `C:\Windows\SysWOW64\config\systemprofile\Documents\IISExpress\Logs\LANSWEEPER.log``C:\Windows\System32\config\systemprofile\Documents\IISExpress\Logs\LANSWEEPER.log``C:\Documents and Settings\<username>\My Documents\IISExpress\Logs\LANSWEEPER.log``C:\Users\<username>\Documents\IISExpress\Logs\LANSWEEPER.log`
