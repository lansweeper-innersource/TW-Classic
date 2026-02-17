<!-- # Configure ticket types, states and priorities -->
From version 6.0 onward, the Lansweeper software includes a fully functional helpdesk. The helpdesk boasts a robust ticketing system that allows people to ask each other questions and request support. Each helpdesk ticket has a type, a state and a priority. There are several built-in types, states and priorities, but you can create your own as well.

## Ticket type

A ticket's type indicates what kind of question is being asked. You may have ticket types for IT support, IT purchases and human resources for instance. A user submitting a question in the helpdesk can specify the ticket type, but a ticket's type can also be changed by an agent or set through rules. Ticket types are linked to agent teams. A user submitting a question doesn't assign his ticket directly to a team. Instead, he specifies the ticket type. As a ticket type is linked to a specific team, the ticket is automatically assigned to the appropriate team.

### Configuring ticket types

1. Browse to the **Configuration > Ticket Content**section of the web console.

   
2. To create your own ticket type, select **Add Ticket Type** in the **Ticket types** section of the page. You'll see several built-in ticket types here as well.

   

   - **Name**: ticket type name.
   - **Default agent**: optionally, have tickets of the specified ticket type automatically assigned to a specific agent.
   - **Icon**: ticket type icon. You can add your own icons to the `Program Files (x86)\Lansweeper\Website\helpdesk\icons` folder on your Lansweeper server.
   - **Agent team**: agent team that will be handling tickets of the specified ticket type. You can create teams at the top of the **Configuration > Ticket Content** page.
   - **Default note type**: determines which note type will automatically be selected when an agent responds to tickets of the specified ticket type, either public reply (visible to user and agents) or internal note (visible to agents only).
   - **Custom fields**: optionally, custom fields that are linked to the specified ticket type. Instructions for setting up ticket custom fields can be found in [this knowledge base article](/docs/create-and-add-custom-fields-to-ticket-types).
   - **Ticket description**: determines whether submitting a description for the ticket is required, optional or not possible. When choosing **Required**, users must submit their tickets with a description. When choosing **Optional**, users can submit their tickets with or without a description. When choosing Invisible, users must submit their tickets without a description.
   - **Extra new ticket options**: determines who can see and configure the options when creating new tickets in the web console, e.g. who can configure **Assets Concerning** and **Source**. You can either show these ticket options to everyone, hide them from everyone or only show them to agents handling tickets.
   - **User may add CC users**: if checked, the user submitting the ticket can add CC users to the ticket.
   - **User sets initial priority**: if checked, the user submitting the ticket can select the initial ticket priority himself. The ticket priority can still be changed by the agent handling the ticket.
   - **Ignore default state**: if checked, the ticket state marked as default in the **Ticket States** section of the **Configuration > Ticket Content** page will not be selected when an agent responds to tickets of the specified ticket type. Instead, the tickets' current state is selected.
   - **Input worktime**: if checked, the agent handling the ticket can input the time he worked on the ticket, by using the hammer icon in the upper right corner of ticket replies.
   - **Enabled**: check/uncheck this box to show/hide the ticket type when creating new tickets.
   - **Show different type to users**: if checked, the ticket type will be displayed as another ticket type of your choice to users without agent permissions.
3. Repeat the previous step for any additional ticket types you want to create. When you're done, you may want to change the default ticket type as well. This setting determines which ticket type is automatically selected when creating a new ticket through the web console or via email.

   

## Ticket state

A ticket's state indicates what phase of the ticket resolution process the ticket is in and what needs to happen with the ticket. Newly created tickets are automatically set to Open. State changes occur as responses are sent, but can also be made by agents or through rules. By looking at the ticket state, both user and agent know whether the ticket has been responded to and whether further action is required. A ticket's considered fully resolved when it's set to Closed, either manually by the agent or user or through auto close rules.

### Configuring ticket states

1. Browse to the **Configuration > Ticket Content**section of the web console.

   
2. To create your own ticket state, select **Add Ticket State** in the **Ticket states** section of the page. You'll see several built-in ticket states here as well.

   

   - **Name**: ticket state name.
   - **Color**: color of the ticket state.
   - **Description**: state description. This is just an informational message for your own benefit and will not be displayed to users creating tickets.
   - **Default**: if checked, this state will automatically be selected when an agent responds to a ticket through the web console. You can only select one default state.
   - **Set state when user replies**: if checked, this state will automatically be selected when a user responds to a ticket he created. You can only check this option for a single state.
   - **Track as work**: if checked, the agent will considered to be working on a ticket if the ticket's set to this state. For statistical purposes, it is important to only check this box for states where the agent is actively working on getting the ticket resolved. You can then see how long an agent worked on a ticket in the ticket's History tab.
   - **Show different state to users**: if checked, the ticket state will be displayed as another ticket state of your choice to users without agent permissions.
3. Repeat the previous step for any additional ticket states you want to create. Optionally, use the green arrows to change the order in which ticket states are displayed in all state dropdowns within the web console.

## Ticket priority

A ticket's priority indicates how urgently the ticket needs to be responded to. Priorities are by default only configurable by and visible to agents, as a way for them to know which tickets they need to work on first.

In the example below, agent Daniel responded to an IT Support ticket submitted by Susan. Daniel changed the ticket state to Pending 3rd party, as he'll only be following up on the ticket next week when Susan's replacement monitor arrives. The color code of the ticket indicates that the ticket has medium priority.



### Configuring ticket priorities

To create and configure ticket priorities, do the following:

1. Browse to the **Configuration > Ticket Content**section of the web console.

   
2. To create your own ticket priority, select **Add Ticket Priority** in the **Ticket priorities** section of the page. You'll see several built-in ticket priorities here as well.

   
3. Repeat the previous step for any additional ticket priorities you want to create. When you're done, you may want to change the default ticket priority as well. This setting determines which ticket priority is automatically selected when creating a new ticket through the web console or via email. Optionally, you can also use the green arrows to change the order in which ticket priorities are displayed in all priority dropdowns within the web console.

   
