<!-- # Create ticket templates -->
From version 6.0 onward, the Lansweeper software includes a fully functional helpdesk. At its core, the Lansweeper helpdesk is a resource for sharing knowledge with people inside or outside of your company. It boasts a robust ticketing system that allows people to ask each other questions and request support. It also includes a knowledge base to share articles on a variety of topics.

**Helpdesk** users may at times ask similar questions or there may be helpdesk tickets that require similar responses. To improve efficiency and decrease the average response time for frequently asked questions, agents can send replies that are partially or completely preformatted, so-called ticket templates. Parameters can be used to automatically insert user or agent details into the responses, giving the users customized answers that are both quick and efficient. If a particular question is asked often enough, you may also want to consider [creating a knowledge base article](/classic/docs/configure-use-and-create-articles-in-the-knowledge-base) on the subject.

## Create ticket templates

1. Browse to the **Configuration > Ticket Content**section of the web console.

   
2. Select **Add category** in the **Ticket templates** section of the page and enter a category name for the template you'll be creating into the resulting pop-up window.
3. Select your template category and select **Add Template** on the right to add a ticket template to the category.

   
4. Enter a name for your template into the Name field of the pop-up window and the template contents into the Text box. All of the usual formatting tools are available to create optimal templates. You can also add attachments with the **Add attachment** button, as well as include one or more parameters. Once you're done composing your message, select **Ok**. Templates with attached files are displayed with a paperclip icon in template overviews.  
   The available parameters are:
   - %USERNAME% : name of the user who created the ticket.
   - %USERCOMPANY% : company name of the user who created the ticket.
   - %USEREMAIL% : email address of the user who created the ticket.
   - %AGENTNAME% : name of the agent responding to the ticket and sending the ticket template.
   - %AGENTEMAIL% : email address of the agent responding to the ticket and sending the ticket template.

     
5. Optionally, submit translations for your template by clicking the blue **A** button next to the template. In the resulting pop-up, select the language you want to submit and then enter your translation into the Name and Text boxes. By default, available languages in the dropdown are English, Dutch, French and German. Additional languages can be made available in the **Configuration > Translations** section of the console. When an agent inserts a template into a ticket reply, the template language is automatically set based on what the agent configured as his preferred helpdesk language.

   
6. To use the template in a reply to a ticket, open the ticket, select **Template**, select the category of the template, then the template itself and click **Ok**. The template is added to your reply. Optionally, you can add more text to your response before sending it off. Only agents can add templates to replies. Users that can only create tickets don't see and cannot use ticket templates.

   
