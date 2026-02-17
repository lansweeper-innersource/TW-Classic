<!-- # Password hash errors -->
Scanning and other credentials submitted in the Lansweeper web console have always been encrypted prior to being added to the Lansweeper database. From Lansweeper 6.0 onward, [an added layer of security](/docs/credential-and-database-security-in-lansweeper) protects your passwords.

Credentials can no longer be encrypted or decrypted without an encryption key file on your Lansweeper server. A unique **Encryption.txt** key file is automatically generated and added to the `Program Files (x86)\Lansweeper\Key` folder on your Lansweeper server when you install Lansweeper 6.0 or a more recent Lansweeper release.   
If you spread out your Lansweeper installation over several machines, you need to manually copy one key file to all of your servers, so all servers use the same key. If all servers do not use the same key file or if your key file is changed after submitting credentials, you may see errors similar to the ones below in the Lansweeper web console. These errors indicate that the key file that was used to encrypt your credentials is not (or no longer) the same key file present on your Lansweeper server(s).

Cannot decrypt credential.

Credential and website hashes don't match.

Incorrect scanning credentials password hash.

Mismatch between website and server's password hash.

No valid credentials found. Check encryption file.



To resolve these errors, follow these steps:

1. If your Lansweeper installation has multiple scanning servers, make sure the **Use key file on disk to encrypt passwords** option is checked under **Configuration > Server Options**. This ensures that your installation uses the new, more secure method of encrypting credentials with an **Encryption.txt** file.  

   If you only have one scanning server, there is no **Use Key File** checkbox to change the method of encrypting credentials. With one scanning server, your Lansweeper installation will always use the new method of encrypting credentials with an Encryption file.
2. If your Lansweeper installation is spread out over several machines, grab the file below from one of those machines. In most cases, the **Encryption.txt** found on the server hosting the web console is the correct one, i.e. the one used to originally encrypt your credentials.

   `Program Files (x86)\Lansweeper\Key\Encryption.txt`

     
     

   If you cannot find an Encryption.txt file on any of your Lansweeper servers, restart the Lansweeper Server service (scanning service) on one of the servers to generate one.
3. Copy the **Encryption.txt** file to the folder found at `Program Files (x86)\Lansweeper\Key` on any server hosting a Lansweeper component, overwriting any other **Encryption.txt** files that may already be present on the servers. The Encryption file on all servers hosting a Lansweeper component must be the same.
4. Double-check that the contents of the **Encryption.txt** files on all of your Lansweeper servers are the same.
5. Restart the **Lansweeper Server** service in **Windows Services** on any scanning servers you have.

   
6. Restart the web server service in **Windows Services** on the machine hosting your web console. Keep in mind that this will log everyone out of the console. Your web server service is either IIS Express or World Wide Web Publishing Service (IIS).

   
7. If the password hash errors persist, resubmit your credentials in the web console as well, so they're re-encrypted with the key file stored on your web server. Credentials can be submitted in various sections of the web console.
   - Scanning credentials can be submitted under **Scanning > Scanning Credentials**.
   - Report and event log alert credentials can be submitted under **Configuration > Email Alerts**.
   - Deployment package share credentials can be submitted under **Deployment > Security Options**.
   - Proxy server credentials for warranty scanning, cloud scanning and cloud relay server access can be submitted under **Configuration > Server Options**.
   - Help desk email credentials can be submitted under **Configuration > E-mail Settings**.
   - Help desk file share credentials for distributed Lansweeper installations can be submitted under **Configuration > General Settings**.
