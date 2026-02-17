<!-- # Configure service-level agreements -->
Service-level agreements (SLAs) help you ensure that tickets are responded to by agents in a timely manner. They allow you to set company standards for the handling and resolution of tickets, to ensure user satisfaction.

You can create specific SLAs for specific ticket types, priorities, sources or users. An SLA specifies how quickly an agent should respond to a ticket and how quickly a ticket should be resolved, i.e. set to the Closed state. Built-in or custom filters, reports or widgets can be used to find tickets where SLAs are not respected.

In the example below, agent Daniel has another 8 days to get the ticket that was assigned to him resolved.  


## Configure SLAs

1. Browse to the **Configuration > General Settings**section of the web console.  
   
2. Submit your company's opening hours in the **Business hours** section of the page. SLAs can be made to take these office hours into account.  
   
3. Delete the built-in SLA and select **Add SLA** in the **Service-level agreement** section of the page to create your own SLA. Alternatively, adjust the built-in SLA to suit your needs. If you create multiple SLAs and a ticket meets the criteria of all of them, the first SLA in the list will be applied to the ticket. The SLA list can be rearranged using the green arrows.
   - **Name**: SLA name.
   - **Initial response time**: how quickly an agent should send an initial public reply to a ticket. If a ticket was created by a user, the initial response time will stop running as soon as an agent posts a public reply to the ticket. If a ticket was created by an agent, the initial response time will only stop running if another agent posts a public reply to the ticket.
   - **Resolve time**: how quickly a ticket should be resolved, i.e. set to the Closed state.
   - **Hours**: determines whether the SLA will run during calendar hours or only during business hours. Consider a scenario where your offices are open Monday through Friday, 8 AM to 6 PM, and your initial response time is 3 hours. A ticket that is created at 5 PM on a Monday will need to be responded to by 8 PM on Monday if you choose calendar hours, by 10 AM on Tuesday if you choose business hours.  

     SLAs only run during workdays, even if you choose calendar hours. If your offices are open Monday through Friday, 8 AM to 6 PM, and your initial response time is 3 hours, a ticket that is created at 11 PM on a Friday will need to be responded to by 2 AM on Monday if you choose calendar hours. If you choose business hours, the ticket will need to be responded to by 11 AM on Monday.
   - **Enabled**: check/uncheck this box to enable/disable the SLA.
   - **Targets**: the ticket types, priorities, sources, users, Active Directory user departments, Active Directory user companies the SLA should be applied to. The SLA will only be applied to tickets that meet all of the specified criteria.
4. Select **Ok**. Whenever a ticket is created that meets the criteria you've specified, a countdown timer visible only to agents starts running on the ticket page. First, the initial response time starts running. When an agent's sent his first public reply, the initial response timer stops and the resolve timer starts. You can open the built-in **SLA Overtime** filter to find tickets where SLAs are not respected. Built-in or custom reports and widgets can be used as well.
