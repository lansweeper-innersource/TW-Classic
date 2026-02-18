<!-- # Scan a Windows computer with AD LAPS -->
Lansweeper currently supports only the legacy Microsoft LAPS. Support for Windows LAPS is not available at this time.

Lansweeper On-premises supports legacy Microsoft Local Administrator Password Solution (LAPS), a Microsoft solution for Active Directory, allowing centralized password management. You can provide one credential to retrieve many other credentials managed by AD LAPS. AD LAPS allows you to fetch the built-in password of each Windows computer, using just one central credential.

You can also [scan a Windows computer](/classic/docs/how-to-scan-a-windows-computer) without AD LAPS if it isn't configured.

## Prerequisites

To scan a Windows computer using AD LAPS, make sure that:

- AD LAPS is enabled on your domain.
- You're in possession of an account with admin rights for managing AD LAPS.
- The admin account must have the rights to run Remote PowerShell on the AD LAPS server.

## Test an AD LAPS credential

Before adding an AD LAPS credential, you can test whether the credentials are correct and whether the scan will be successful.

1. On your Lansweeper Classic installation, browse to `Program Files (x86)\Lansweeper\Service`.
2. Run the Lansweeper.TestTools.App executable.
3. In the Scan Test Tool, select **Local Administrator Password Solution**, and fill in the fields:
   1. Username: username of the AD LAPS admin account.
   2. Password: password of the AD LAPS admin account.
   3. Domain Controller: address of the Domain Controller with AD LAPS file.
   4. Laps GPO: name of the Group Policy Object (GPO).
   5. Target Machine: FQDN or hostname.  
      
4. Select **Execute**. Once executed, the tool will display detailed logs of the process. When your connection is successful, your credentials have been validated for scanning.

## Add an AD LAPS credential

1. In the Lansweeper web console, navigate to the **Scanning > Scanning credentials**.
2. In the**Credentials** tab, select **Add new Credential**.
3. Select **Local Administrator Password Solution**as a credential type, and fill in the fields:
   1. Name: name for the credential.
   2. Username: username of the AD LAPS admin account.
   3. Password: password of the AD LAPS admin account.
   4. Domain Controller: address of the Domain Controller with LAPS file.
   5. LAPS GPO Name: name of the Group Policy Object (GPO).  
      
4. Select **Ok**.

## Map an AD LAPS credential

1. In the Lansweeper web console, navigate to the **Scanning > Scanning credentials**.
2. In the**Credential Mapping** tab, select **Map Credential**.
3. Map the AD LAPS credential to one of the following mapping types: 
   - IP Address: specify the exact IP address as well.
   - IP Range: specify the IP range.
   - Windows Computer: enter the Domain\Computername path.
   - Workgroup or Domain: enter the Workgroup or Domain.
4. Select **Add**.   
   
