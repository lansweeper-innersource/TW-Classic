<!-- # Introduction to the help desk -->

This article provides an introduction to the Lansweeper help desk. From version 6.0 onward, the Lansweeper software includes a fully functional help desk. At its core, the help desk is a resource for sharing knowledge with people inside or outside of your company. It boasts a robust ticketing system that allows people to ask each other questions and request support. It also includes a knowledge base to share articles on a variety of topics, a company news widget and a calendar to keep track of meetings, vacation days and more! In this article, we'll mainly focus on the ticketing part of the help desk. The purpose of this article is to familiarize you with some important concepts and terminology related to the help desk and to give you a sense of what is possible. Though it is by no means a full feature list, this overview is definitely the place to start if you've never used the Lansweeper help desk before. We recommend reading it in its entirety and then clicking through to some of the other knowledge base articles linked within. Before you get started, be aware that hosting the Lansweeper database in Microsoft SQL LocalDB or Microsoft SQL Server is required when using the help desk. Microsoft SQL Compact is no longer a supported database server for hosting Lansweeper. If you are still using SQL Compact as your Lansweeper database server, you should [convert your database to SQL LocalDB or SQL Server](/docs/convert-a-deprecated-sql-compact-database).

## Users, agents and teams

The ticketing system included in Lansweeper allows people inside or outside of your company to ask questions and request support from your employees on a variety of issues. A common way to use the help desk would be for employees that are having issues with their computers and require support from your IT department.

- In the context of the help desk, a **user** is someone who can only ask questions and request support, but not answer questions. A user can only see his own questions, not questions other people have asked.
- A help desk **agent** is someone who can both ask and answer questions. **An agent is part of at least one team**, which is a group of agents, and can see all questions asked of that team. The teams an agent is in are only visible to other agents.
- The help desk part of Lansweeper is licensed on a per agent basis. An unlimited number of users can ask questions, but you pay a fee per agent that replies to them. One free agent license is included in all existing and newly purchased Lansweeper licenses and additional agent licenses can be purchased through our online store.
- In the example below, Susan (a user) reported an issue with her monitor that was assigned to Daniel (an agent). Daniel is a member of the company's IT Technicians team, which encompasses all IT personnel, and will respond to Susan's question.

  ![illustration-users-agents-teams.jpg](/docs/.document360/assets/article_025/image_002.jpg)

## Roles and permissions

What agents can do within the help desk is governed by a system of roles and permissions.

- A **permission** is a right, a specific action an agent is allowed to perform on a question that is asked of him. There is a permission that gives agents the ability to pass questions along to other agents for instance.
- Each agent is assigned a **role**, which is a collection of permissions. A role can be assigned to multiple agents. You could create one role for the IT department for instance that gives them permissions A, B and C, and another role for the human resources department that gives them permissions D, E and F.
- In the example below, agent Daniel was assigned the role Agent 2nd line, which includes a variety of permissions.

  ![illustration-roles-permissions.jpg](/docs/.document360/assets/article_025/image_003.jpg)

## Tickets, public replies and internal notes

**A ticket is a conversation**, a back and forth between a user and an agent. A user asks a question or reports an issue and an agent responds. If the question or issue is unresolved, the user can reply again and so on. There are two types of responses to a question or issue: public replies and internal notes.

- A **public reply** can be posted by both the user and the agent and is visible to both the user and the agent.
- An **internal note** can only be posted by an agent and is only visible to agents.
- The example below shows the same ticket as seen by user Susan and as seen by agent Daniel. The yellow note in the ticket is internal and only visible to Daniel and other agents. The rest of the conversation is visible to both Daniel and Susan.

  ![illustration-tickets-public-replies-internal-notes-agent.jpg](/docs/.document360/assets/article_025/image_004.jpg)

  ![illustration-tickets-public-replies-internal-notes-user.jpg](/docs/.document360/assets/article_025/image_005.jpg)

## Ticket sources

Tickets can come from various sources.

- Tickets can of course be created in the Lansweeper **web console** itself, but can also be **imported**, sent via **email** or generated through an **API**.
- If you allow users to send in questions via email, the emails are automatically imported as tickets and made visible to agents in the help desk. Agents can respond within the help desk and their (public) replies are automatically sent back to the users via email. Any subsequent user responses are automatically added to the users' existing tickets.
- The icon in the example below shows that user Susan submitted her ticket directly in the web console.

  ![illustration-ticket-sources.jpg](/docs/.document360/assets/article_025/image_006.jpg)

  ![lightbulb.png](/docs/.document360/assets/article_025/image_007.jpg) Learn how to configure ticket sources in [this knowledge base article](/docs/receive-tickets-through-the-web-console-email-api-import).

## Ticket types, states and priorities

Each ticket has a type, a state and a priority. There are a number of built-in types, states and priorities, but you can create your own as well.

- A ticket's **type** indicates what kind of question is being asked. You may have ticket types for IT support, IT purchases and human resources for instance. A user submitting a question in the help desk can specify the ticket type, but a ticket's type can also be changed by an agent or set through rules. Ticket types are linked to agent teams. A user submitting a question doesn't assign his ticket directly to a team. Instead, he specifies the ticket type. As a ticket type is linked to a specific team, the ticket is automatically assigned to the appropriate team.
- A ticket's **state** indicates what phase of the ticket resolution process the ticket is in and what needs to happen with the ticket. Newly created tickets are automatically set to Open. State changes occur as responses are sent, but can also be made by agents or through rules. By looking at the ticket state, both user and agent know whether the ticket has been responded to and whether further action is required. A ticket's considered fully resolved when it's set to Closed, either manually by the agent or user or through auto close rules.
- A ticket's **priority** indicates how urgently the ticket needs to be responded to. Priorities are by default only configurable by and visible to agents, as a way for them to know which tickets they need to work on first.
- In the example below, agent Daniel responded to an IT Support ticket submitted by Susan. Daniel changed the ticket state to Pending, as he'll only be following up on the ticket next week. The color code of the ticket indicates that the ticket has medium priority.

  ![illustration-ticket-types-states-priorities.jpg](/docs/.document360/assets/article_025/image_008.jpg)

  ![lightbulb.png](/docs/.document360/assets/article_025/image_009.jpg) Learn how to configure types, states and priorities in [this knowledge base article](/docs/configure-ticket-types-states-and-priorities).

## Ticket custom fields

Custom fields allow users and agents to add extra information to a ticket in an organized way.

- Custom fields are fields you create and assign a name, type and (optionally) list of possible values to. They can be combo boxes, date fields, text values and more.
- Adding information to custom fields can be made optional or required. Custom fields can be nested as well, with the completion of one field bringing up another field and so on. As different ticket types tend to require different kinds of fields, custom fields are configured per ticket type.
- In the example below, agent Daniel used custom fields to mark the ticket that was assigned to him as a hardware related issue.

  ![illustration-ticket-custom-fields.jpg](/docs/.document360/assets/article_025/image_010.jpg)

  ![lightbulb.png](/docs/.document360/assets/article_025/image_011.jpg) Learn how to create and configure custom fields in [this knowledge base article](/docs/create-and-add-custom-fields-to-ticket-types).

## Ticket filters, tabs and notifications

As agents tend to respond to many tickets, and potentially many different kinds of tickets, they need a way to organize those tickets into various overviews.

- A **filter** is a collection of tickets that meet certain criteria. Each agent can create his own filters and filters can be saved, so they can be referred back to and reopened at any time.
- Each agent can configure his own help desk layout, creating **tabs** and displaying a ticket filter in each tab. A count in the tab header indicates how many tickets are in each tab. This gives the agent an easy way to monitor and separate various kinds of tickets.
- To further assist agents in locating tickets that require action, **notifications** are displayed in the top right corner of the console, next to the agent's name. There are notifications for unassigned tickets (star icon) and notifications for changes made to tickets the agent's involved in (bell icon).
- In the example below, agent Daniel created and saved several filters. He's displaying the Related to me, SLA overtime and Unassigned filters in tabs, so he can easily monitor tickets that meet the filters' criteria.

  ![illustration-ticket-filters-tabs-notifications.jpg](/docs/.document360/assets/article_025/image_012.jpg)

  ![lightbulb.png](/docs/.document360/assets/article_025/image_013.jpg) Learn how to create and configure ticket filters in [this knowledge base article](/docs/configure-and-use-ticket-filters).

## Ticket templates and outgoing email templates (auto reply)

Templates are pre-configured messages that can be sent to users. There are two kinds of templates, ticket templates and outgoing email templates.

- A **ticket template** is a pre-configured message an agent can manually select when creating or responding to a ticket. Ticket templates allow agents to quickly respond to common questions. They are organized into categories and can include variables to automatically insert user or agent details.
- An **outgoing email template** is a pre-configured email that is automatically sent to the user when an action occurs on the user's ticket, e.g. when the ticket is assigned to an agent. This allows you to keep users up-to-date on what is happening with their support cases. Like ticket templates, outgoing email templates can include variables as well.

  ![illustration-ticket-templates-outgoing-email-templates.jpg](/docs/.document360/assets/article_025/image_014.jpg)

## Ticket dispatching, auto assign and auto close

By default, newly created tickets are not automatically assigned to a specific agent. They are assigned to a team based on the ticket type, but not to any particular agent within that team. Agents can then choose which tickets to pick up and respond to.

- **Auto assignment** lets you select a default agent for a specific ticket type. Any tickets of the specified type will automatically be assigned to the default agent. Auto assignment can also be used to have tickets assigned to agents in turn (round robin), so each agent has the same amount of tickets, or to have tickets assigned to the agent with the fewest non-closed tickets (load balancing).
- **Ticket dispatching** can also be used to assign tickets to agents or to set the ticket type, state, priority and more. Dispatching rules check whether certain conditions are met and, if so, change certain ticket properties. Ticket dispatching rules affect tickets created via email.
- **Auto close** lets you automatically close tickets with a specific type or state after X number of hours or days, which is useful if neither the agent nor user closes a resolved ticket. Optionally, the user can be warned prior to closing the ticket.
- In the example below, ticket dispatching is used to automatically assign ticket emails with shutdown in the title to agent Daniel.

  ![illustration-ticket-dispatching-auto-assign-auto-close.jpg](/docs/.document360/assets/article_025/image_015.jpg)

## Ticket SLAs

SLA stands for **service-level agreement** and is a way for you to ensure that tickets are responded to by agents in a timely manner. SLAs allow you to set company standards for the handling and resolution of tickets, to ensure user satisfaction.

- You can create specific SLAs for specific ticket types, priorities, sources or users.
- An SLA specifies how quickly an agent should respond to a ticket and how quickly a ticket should be resolved, i.e. closed. Built-in or custom filters, reports or widgets can be used to find tickets where SLAs are not respected.
- In the example below, agent Daniel has another 8 days to get the ticket that was assigned to him resolved.

  ![illustration-ticket-slas.jpg](/docs/.document360/assets/article_025/image_016.jpg)

  ![lightbulb.png](/docs/.document360/assets/article_025/image_017.jpg) Learn how to configure SLAs in [this knowledge base article](/docs/configure-service-level-agreements).
