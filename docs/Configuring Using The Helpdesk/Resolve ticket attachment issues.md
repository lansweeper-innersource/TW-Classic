<!-- # Resolve ticket attachment issues -->
In [the helpdesk module](/docs/introduction-to-the-help-desk), tickets can contain images and other attachments. Attachments can come from emails that were imported as tickets or can be added through the web console.

Attachments are stored in a folder on your Lansweeper server, not in your database. If a ticket comes in via email, its attachments are processed by the scanning server that is configured as your helpdesk mail server. If a ticket is created or viewed via the web console, its attachments are processed by your web server service, which is either IIS or IIS Express. In other words, both the Lansweeper and web server service need to be able to access the folder that stores your ticket attachments.

If your Lansweeper and web server service are hosted on the same machine, both services automatically have access to your attachment folder and you don't need to do anything to ensure correct functioning of attachments. If your Lansweeper and web server service are hosted on different machines though, both services do not automatically have access and ticket attachments can by default fail to load or return errors. With your services spread across different machines, you need to manually share the attachment folder on your web server, to ensure the scanning server can access it. The connection details of the shared folder must be submitted in Lansweeper as well.

## Sharing the attachment folder

1. On the machine hosting your Lansweeper web console, browse to `Program Files (x86)\Lansweeper\Website\helpdesk`.
2. Right-click the "files" folder, and go to **Properties >** **Sharing**and select **Advanced Sharing...**.   

   You must share the `Program Files (x86)\Lansweeper\Website\helpdesk\files` folder specifically on the machine hosting your web console.
3. Tick the **Share this folder** checkbox and give the share a name. 
4. Select **Permissions**, then **Add...** and select a user account to grant access to the share. This user account will be used by the scanning server to access the share.
5. Tick the Full Control checkbox for the share and click **Apply** and **Ok** until you've closed all pop-ups.  
     

   For optimal security we recommend creating a new, dedicated user account just for accessing the helpdesk share.
6. Right-click the "files" folder, and go to **Properties >** **Security**and select **Edit**. Give the same share user full control to the folder.   
   
7. Browse to the **Configuration > General Settings** section of the Lansweeper web console. 
8. Tick the **Service requires shared folder for attachments** checkbox and enter the information of the share and share user account you created earlier.   
   
9. Go to the scanning server you are using as your helpdesk mail server. If there are files in the `Program Files (x86)\Lansweeper\Website\helpdesk\files` folder of this scanning server, move them to the same folder on your web console server. If you have multiple scanning servers, you can verify which one is configured as your helpdesk mail server by browsing to **Configuration > E-mail Settings** in the web console and reviewing the **E-mail settings** section.  

2.11.0.0
