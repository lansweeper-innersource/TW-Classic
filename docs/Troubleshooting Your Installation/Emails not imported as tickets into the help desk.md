<!-- # Emails not imported as tickets into the help desk -->
From version 6.0 onward, the Lansweeper software includes a help desk and ticketing system. Tickets can be created in several ways: in the web console, by importing emails, by importing .csv files and through the ticket API. More information on how help desk tickets are created can be found in [this knowledge base article](/docs/receive-tickets-through-the-web-console-email-api-import).

Having users send in emails is a common way to create help desk tickets. It is convenient for the users and allows you to have external companies or email addresses create tickets as well. Ticket creation via email requires you to submit an email account configuration in the following section of the web console: **Configuration > E-mail Settings**.

If you've already configured a help desk email account, but your users' emails are not appearing as tickets in the help desk, this can have several possible explanations.   
The first thing to keep in mind is that this can simply be a permissions issue, i.e. the emails being imported but not visible in ticket filters due to lack of permissions.   
It can also be a functional issue, i.e. the emails not being imported or added to your Lansweeper database at all. The troubleshooting steps below help you determine whether you are experiencing a permissions or functional issue, as well as provide solutions for both.

If you've configured a help desk email account, but your users' emails are not appearing as tickets, follow these steps:

1. Make sure you are waiting 5 minutes for an email that arrived on your help desk mail server to be imported by Lansweeper. Emails are not imported instantaneously.   
   For performance reasons, Lansweeper checks every so often whether there are new emails that require import and then imports them in bulk. A delay of a few minutes between the arrival on the mail server and the creation of the ticket is normal.
2. Double-check whether tickets exist by performing a search for the subject of one of the emails. Click the **New Tab** button to the right of your existing ticket tabs and use the **Search** option in the left pane.
3. If you have not already done so, update to the latest Lansweeper release by following the instructions in [this knowledge base article](/docs/update-lansweeper-on-premises). You can verify whether you are on the latest release by selecting **Check for Updates now** in the following section of the web console: **Configuration > Your Lansweeper License**.
4. Start the **Lansweeper Server** service in **Windows Services** on your Lansweeper server, if not already started. The Lansweeper service processes both incoming and outgoing mail. If this service isn't running, no tickets can be imported via email. By default, the Lansweeper service is automatically running, but someone may have manually stopped it.

   
5. For troubleshooting purposes, log into the web console with the built-in admin or with a user whose role includes the **View Reports Containing Helpdesk Tables** permission.   
   If you've disabled the built-in admin, you can re-enable it by following the instructions in [this knowledge base article](https://www.lansweeper.com/kb/198/locked-out-of-the-web-console.html). Information on assigning roles and permissions to other users can be found in [this knowledge base article](/docs/restrict-access-to-the-web-console).

   
6. Verify whether you can see the missing tickets in either of the below built-in reports in the **Reports** tab of the web console.

   - Helpdesk: All ignored tickets
   - Helpdesk: All tickets that have been created

   
7. If you can see all missing tickets in one of the aforementioned reports, but receive an access error when clicking on any of them, stop at this step. You've now determined that what you're experiencing is a permissions issue. The tickets have actually been imported, but are not visible to you in ticket filters because you don't have rights to them.   
   You will need to add yourself to the appropriate agent teams to ensure you can see the tickets in ticket filters. Information on configuring teams and permissions can be found in [this knowledge base article](/docs/restrict-access-to-the-web-console).
8. If you cannot see the missing tickets in either of the aforementioned reports, you're experiencing a functional issue, where the tickets have not been imported at all. The first thing we recommend doing in this case, if you are using a Gmail address as your help desk email account, is to ensure that access by external apps has been allowed in your Gmail configuration.   
   Log into the Gmail account you are using as your help desk email address, browse to [this section of your Gmail settings](https://www.google.com/settings/security/lesssecureapps) and configure it as shown below.

   
9. Ensure that the incoming and outgoing status checks are green for your help desk email account in the **Configuration > E-mail Settings** section of the Lansweeper web console. These checks indicate whether a connection to the incoming and outgoing mail server can successfully be established with the login details provided.

   

   

   Status check errors are usually due to incorrect mail server details being submitted, e.g. an incorrect server name, username or password. They can also be due to firewalls blocking access to the mail server. Refer to documentation for your mail server or consult with whoever is managing the server to ensure you have the correct login information.   
   You can also test your mail settings using the following tool on your Lansweeper server: `Program Files (x86)\Lansweeper\Tools\MailTester.exe`
10. Click the **Edit** button next to your help desk email account and, in the **Incoming** tab, verify what you have configured as Inbox, Archive and Ignored folders. Lansweeper will only import emails that arrive in the Inbox folder(s) on the mail server specified by you. It will then move the imported emails to the Archive folder or, if you've configured Lansweeper to ignore certain emails, Ignored folder.   
    The Inbox, Archive and Ignored folders submitted in Lansweeper must exist on your mail server itself and the emails you want to import into Lansweeper must arrive in the Inbox folder(s) specified by you.

    
11. For troubleshooting purposes, configure the Incoming mail section of the **Configuration > E-mail Settings** menu as shown below. It ensures that any email that arrives in the configured Inbox folder(s) and that was not sent by the help desk email address itself is imported into Lansweeper. If reverting to the below settings resolves the email import issue, someone previously put a rule in place that ignores certain emails during import.

    

    Emails sent by the help desk email address or by the aliases configured under Configuration\E-mail Settings are automatically ignored during import. In other words, the help desk won't import emails that it sent to itself. This is to prevent email loops.
12. Log directly into your mail server itself. As an example, we are importing emails from a Gmail account and have logged into Gmail directly with our email account and password.
13. Ensure that emails you want to import are in fact arriving in the Inbox folder(s) configured under **Configuration > E-mail Settings** in Lansweeper.   
    In the example below, we configured Lansweeper to import emails from "FolderA". When logging into Gmail directly, we can see that two emails arrived in FolderA, one in a subfolder called "SubFolder" and another in "FolderB". This is due to email routing rules we configured in Gmail itself. Only the emails that arrived directly in FolderA will be imported as tickets by Lansweeper. The emails that arrived in SubFolder and FolderB will not be imported.

    

    
14. Check whether the emails you want to import were moved to the "Helpdesk\_archive" or "Helpdesk\_ignore" folder on your mail server. If they were and if there are no rules configured on the mail server itself that explain this behavior, this indicates that the emails were imported by a Lansweeper installation.   
    If you are still not seeing tickets for them, there is likely a second Lansweeper installation present in your network that is importing the mails. You may have set up a test installation at some point, which is still running. An email that was imported by one Lansweeper installation will not be imported again by another Lansweeper installation with the same help desk email account configuration. Depending on the situation, decommission your second Lansweeper installation or change its help desk email setup.

    
