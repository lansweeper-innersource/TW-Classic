<!-- # Delete tickets from the helpdesk -->
No one apart from the built-in admin has the ability to delete tickets by default, to avoid gaps in the ticket history. You can however manually give users the right to permanently delete tickets from the helpdesk and Lansweeper database.

1. Browse to the **Configuration > User Access & Roles**section of the web console.![menu-configuration-user-access-and-roles.jpg](/docs/.document360/assets/article_023/image_001.jpg)
2. Select **Make Agent** next to your user account in the **Users** section of the page to give the account a role, add it to one or more agent teams and assign an agent license. You are able to see tickets assigned to teams you're a member of and your role determines which actions you can perform on those tickets.![deleting-tickets-1.jpg](/docs/.document360/assets/article_023/image_002.jpg)
3. Select the pencil shaped edit button next to the role previously assigned to the user account in the **User Roles** section of the same page.  
   ![deleting-tickets-2.jpg](/docs/.document360/assets/article_023/image_003.jpg)  
   Add the **Delete Tickets** permission to the user role. Alternatively, you can create a new role that includes the permission and assign that to the user account.![deleting-tickets-3.jpg](/docs/.document360/assets/article_023/image_004.jpg)
4. Restart your web browser.
5. Remove tickets from the helpdesk by selecting the **Delete ticket(s)** option in the **Actions** menu, either from within an individual ticket or a ticket filter. Within a ticket filter, tick the checkboxes in front of the tickets you want to delete and then open the **Actions** menu. You could also tick the checkbox at the very top of the ticket filter to select and then delete all tickets in the filter.  
   ![deleting-tickets-4.jpg](/docs/.document360/assets/article_023/image_005.jpg)  

   Deleting a ticket removes it from the Lansweeper Classic web console and database. If the ticket was initially imported via email, the corresponding email is not removed from the mail server itself, however.
