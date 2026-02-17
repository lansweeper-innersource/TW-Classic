<!-- # Perform actions on new tickets using dispatching rules -->
When new tickets are [sent via email to the helpdesk and imported](/docs/receive-tickets-through-the-web-console-email-api-import), dispatching rules can be used to perform automated actions on those tickets. A dispatching rule allows you to automatically change type, state, priority and other properties of incoming emails based on whether those tickets meet certain criteria specified by you.



## Create dispatching rules

1. Browse to the **Configuration > E-mail Settings**section of the web console.

   
2. Select **Add rule** in the **Ticket dispatching** section of the page and submit a name and description for your rule in the resulting pop-up. The name and description just serve as reference so you can easily identify your dispatching rules.
3. In the **Conditions** section of the pop-up, submit the criteria that tickets must meet to be changed by your dispatching rule. You can submit multiple criteria using the **+** button.   
   Conditions can look for matches in an email's subject (title), description (initial note), from email (sender email address) and to email (recipient email address). These matches can be exact (Equal or Not Equal) or partial (Like or Not Like). If you add multiple types of conditions, an email must meet all conditions to be affected by the dispatching rule. If you add multiple of the same type of condition, an email must meet just one of the conditions to be affected by the dispatching rule.
4. In the **Actions** section of the pop-up, submit the actions that must be performed on the tickets. You can submit multiple actions using the green + button. All of the specified actions will be performed on tickets that meet your conditions. Dispatching rules can set type and other properties of tickets, assign to an agent or team, add a follow-up or calendar event and set tickets to personal.  

   Agent replies on personal tickets show the agent's name and can be sent from the agent's personal email address and with his personal signature, depending on your setup.

   
5. If you create multiple rules, use the green arrow buttons to change their order if required. Lansweeper will run through the rules from top to bottom in the order you see them. To know which specific rules were applied to a ticket, you can check the ticket's **History** tab.
6. If you create multiple rules, optionally tick the **Stop processing** checkbox for one or more rules. If this checkbox is ticked for a rule and that rule is applied to a ticket, Lansweeper will not run through any following rules. If this checkbox is not ticked for a rule and that rule is applied to a ticket, Lansweeper will still run through other rules in the order you see them.   
   In the example below, Lansweeper will not process the Blue Screen rule for a ticket if the Susan Hemoco rule was already applied to that ticket.

   

## Ticket dispatching rule examples

Below are some examples illustrating the use of ticket dispatching rules in the helpdesk. If you're familiar with the use of regular expressions, you can make the conditions even more specific and search for patterns. Dispatching rule conditions use regex in the background.

- In the example below, any emails whose contents contain "blue screen" or "BSoD" will be set to the ticket type IT Support, assigned to the team IT Support and set to priority High.
- In the example below, emails that both have "invoice" in the title and were sent to the purchasing department's email address will be set to the ticket type IT Purchase and assigned to the Purchase team. A calendar event will also be added for the ticket, which starts 10 minutes after receiving the email (minimum delay) and lasts 15 minutes.
- In the example below, any emails sent by Susan Hemoco will be assigned to agent Dave, made personal and set to priority High.  
  
