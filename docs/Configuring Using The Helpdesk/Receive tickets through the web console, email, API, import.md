<!-- # Receive tickets through the web console, email, API, import -->
![TL;DR-Sweepy-Icon (1).png](/docs/.document360/assets/article_027/image_001.jpg) **This page explains how to set up helpdesk tickets in Lansweeper, using either the web console, emails, an API or importing them manually.**

A helpdesk ticket is a conversation, a back and forth between a user and an agent. A user asks a question or reports an issue and an agent responds. If the question or issue is unresolved, the user can reply again and so on. Tickets can come from various sources.

- Tickets can be created in the Lansweeper Classic web console itself, but can also be imported, sent via email or generated through an API.
- If you allow users to send in questions via email, the emails are automatically imported as tickets and made visible to agents in the helpdesk. Agents can respond within the helpdesk and their (public) replies are automatically sent back to the users via email. Any subsequent user responses are automatically added to the users' existing tickets.
- The icon in the example below shows that user Susan submitted her ticket directly in the web console.

  ![illustration-ticket-sources.jpg](/docs/.document360/assets/article_027/image_002.jpg)

## Web console tickets

By default, everyone in your network has access to the web console and can log in as a helpdesk user to create tickets. All they have to do is submit a Windows username and password in the login screen. Everyone can also log in with full access to all Lansweeper features by selecting **Built-In Admin**.

To restrict access to the web console and disable the Built-in Admin button, check out [Restrict access to the web console](/docs/restrict-access-to-the-web-console).

## Email tickets

1. Browse to the **Configuration > E-mail Settings**section of the web console.

   ![menu-configuration-email-settings.jpg](/docs/.document360/assets/article_027/image_003.jpg)
2. Submit your preferred email prefix in the **E-mail settings** section of the page.

   ![receiving-tickets-through-the-web-console-email-api-and-import-1.jpg](/docs/.document360/assets/article_027/image_004.jpg)  
   This prefix, along with a ticket ID, will be added to the subject of outgoing emails. This way, Lansweeper can identify any subsequent user responses as belonging to an existing helpdesk ticket and add them to the existing conversation.  
   ![receiving-tickets-through-the-web-console-email-api-and-import-2.jpg](/docs/.document360/assets/article_027/image_005.jpg)
3. Select **Add E-mail account** in the **E-mail account** section of the page.  

   You can add multiple email accounts to your helpdesk. Note that you will have to mark one email account as your default email account.
4. Use the **Select standard configuration** button in the resulting pop-up to automatically insert the correct Gmail, Outlook or Yahoo SMTP and IMAP settings, or manually submit your settings in the available input boxes.

   ![receiving-tickets-through-the-web-console-email-api-and-import-3.jpg](/docs/.document360/assets/article_027/image_006.jpg)

   - SMTP server: your SMTP server and port
   - Incoming mail server: your IMAP server and port
   - E-mail address: your email address, which will be used to send and receive emails  

     We recommend using a dedicated email account. The email account you enter must have its own folder structure. E.g. an O365 account without an assigned license cannot be used.
   - Aliases: optionally, any aliases of your primary email address that you've configured in your mail server and that you want to use to send and receive emails from as well.  

     If an agent's email address is configured as an alias in your mail server and submitted as an alias in your helpdesk settings as well, that agent can mark tickets as personal and any responses they post will be sent to the user from their personal email address. By default, emails are sent from your primary email address and don't include individual agents' names.
   - Displayname: user display name to be used by the helpdesk when sending emails
   - Inbox folders: mail folders the helpdesk should import user emails from. You can separate multiple folders with semicolons.
   - Archive folder: folder user emails should be moved to once imported
   - Ignored folder: folder user emails should be moved to if marked as irrelevant by an agent
   - Use SSL connection: tick if SSL is required by the mail server.
   - User and password: your email address and password, if authentication is required by the mail server
5. Select **OK** to finish the configuration. Users can then send an email to the email address you've configured and the email will automatically be imported as a ticket into the helpdesk, where an agent can respond.  

   If an email is sent to a specific helpdesk account or alias and then replied to, the reply will be sent from the same account or alias. If a ticket is created in the web console and the agent has no alias, related emails are sent from the default email account.

## API tickets

1. Browse to the **Configuration > Ticket API**section of the web console.

   ![menu-configuration-ticket-api.jpg](/docs/.document360/assets/article_027/image_007.jpg)
2. Select **Add API key** to generate an API key for your application or custom helpdesk interface, submit a description in the resulting pop-up and select **Ok**.

   ![receiving-tickets-through-the-web-console-email-api-and-import-4.jpg](/docs/.document360/assets/article_027/image_008.jpg)
3. Follow the instructions in the **Documentation** section of the page. The web console itself contains a detailed API documentation, with a complete list of functions and parameters. Examples are included as well.

   ![receiving-tickets-through-the-web-console-email-api-and-import-5.jpg](/docs/.document360/assets/article_027/image_009.jpg)

## Importing tickets from a .csv

1. Browse to the **Configuration > Import Tickets**section of the web console.

   ![menu-configuration-import-tickets.jpg](/docs/.document360/assets/article_027/image_010.jpg)
2. Download the available template.

   ![receiving-tickets-through-the-web-console-email-api-and-import-6.jpg](/docs/.document360/assets/article_027/image_011.jpg)
3. Open your template, add tickets to it and save it as a .csv file. Each line represents one ticket.

   ![receiving-tickets-through-the-web-console-email-api-and-import-7.jpg](/docs/.document360/assets/article_027/image_012.jpg)

   - Subject: subject or title of the ticket
   - Description: ticket contents
   - Date: ticket creation date
   - Displayname: display name of the user submitting the ticket
   - UserDomain: NetBIOS domain name of the user submitting the ticket
   - Username: username of the user submitting the ticket
   - Email: email address of the user submitting the ticket
   - AgentDomain: NetBIOS domain name of the agent answering the ticket
   - AgentUsername: username of the agent answering the ticket
   - Priority: ticket priority
   - State: ticket state
   - Type: ticket type
   - Attachments: files to be attached to the ticket. Attachments must be separated with | , must have an absolute path (e.g. c:\temp\image.png) and must be in a directory accessible to Everyone on the server hosting the Lansweeper web console.
4. Select **Choose File** in the web console to launch Windows Explorer, select your .csv file, click **Open** and then **Import**.

   ![receiving-tickets-through-the-web-console-email-api-and-import-8.jpg](/docs/.document360/assets/article_027/image_013.jpg)

## In person and phone

When you create a ticket, you'll notice two more possible ticket sources, in person and phone. These can only be selected manually, through the API or during import.

![receiving-tickets-through-the-web-console-email-api-and-import-9.jpg](/docs/.document360/assets/article_027/image_014.jpg)
