<!-- # Configure, use and create articles in the knowledge base -->
The Lansweeper Classic software includes a fully functional helpdesk. One of the many features included in the helpdesk, apart from a ticketing system, is a knowledge base.

The Lansweeper knowledge base allows you to create articles, categorize them and then share them with people in your company. This facilitates the resolution of support tickets and the centralization of information. Per category, you can configure who can see and edit articles.



## Configure the knowledge base

1. Browse to the **Knowledgebase > Knowledgebase Options**section of the web console.
2. Choose who will be able to see the Lansweeper knowledge base menu and the articles contained within.
   - Ticking the first checkbox will allow anyone with access to the Lansweeper web console to view the knowledge base.
   - Ticking the second checkbox will disable the knowledge base for non-agents, users who cannot see or respond to other people's helpdesk tickets.
   - By default, the first checkbox is ticked and the second is not, allowing anyone with access to the console to view the knowledge base. Further down the page, you are able to customize view and edit rights more, per article category.
3. Choose whether images that are part of a knowledge base article's contents are displayed as attachments in the article as well and, if so, where these attachments are displayed.
4. Optionally, adjust the **Number of articles shown per category** setting to increase or decrease the number of articles that are displayed per category in the category overview directly under the **Knowledgebase** menu. Users are still able to see all articles in a category by selecting the category or by clicking the More links in the category overview. They are also able to find articles by performing a search.
5. Optionally, adjust the **Sort articles on** setting to change the way articles are sorted in article overviews. Available options are:
   - Default: same sort order as seen under Knowledgebase Options. You can change the order of articles using the green arrows next to each article.
   - Alphabetically: alphabetical sorting (from A to Z) based on article title.
   - Creation date: recently created articles are listed at the top.
   - Last changed date: recently altered articles are listed at the top.
6. Select **Add category** to create a new category of knowledge base articles. The resulting pop-up asks for a name and color for the category. The color is used for bullets in front of category names and for category frames in the **Knowledgebase** menu. There are two built-in categories as well, which you may want to delete with the red delete buttons next to the categories.
7. Choose who can see and edit the knowledge base category. Ticking **User Access** gives everyone the ability to see articles in the knowledge base category. You can also specify which agent teams can see and add/edit articles in the category. An agent is a user who can respond to other people's helpdesk tickets. An agent is only able to edit articles in a knowledge base category if at least one of his teams has been granted the necessary permissions to the category.   
   In the example below, everyone can see articles in the Lansweeper category, but only the IT Support and IT Management teams are able to edit them.  

   An agent's role also needs to include the Alter Knowledgebase Articles or Access Configuration permission in order for the agent to be able to add or edit knowledge base articles. Info on restricting web console access can be found in [this knowledge base article](/docs/restrict-access-to-the-web-console).

   If you make changes to knowledge base permissions, have users restart their web browsers to make the changes take effect.
8. Select the category and click **Add article** to create a new article in the category.  

   Lansweeper knowledge base articles can be imported from a .csv file as well, under **Knowledgebase > Import Articles**.
9. Enter a name for your article into the Title field of the pop-up window and the article contents into the Text box. All of the usual formatting tools are available. You can make text bold or italic, underline, change the font size and color, highlight, create bulleted lists, add images and hyperlinks and more. You can also add attachments with the **Add attachment** button. Once you're done composing your article, select **Ok**.
10. Optionally, submit translations for your article by selecting the blue **A** button next to the article. In the resulting pop-up, select the language you want to submit and then enter your translation into the Title and Text boxes. By default, available languages in the dropdown are English, Dutch, French and German. Additional languages can be made available in the **Configuration > Translations** section of the console. When someone selects an article for viewing, the article is automatically displayed in the language chosen by the user as his preferred helpdesk language.
11. To allow agents responding to helpdesk tickets to insert links to knowledge base articles into their responses, make sure **Allow adding knowledgebase links** is ticked under **Configuration > General Settings**, and that your Lansweeper web console URL is correctly submitted in the Hostname field. 

      
    Agents can then insert a knowledge base link into a ticket reply by using the available button, selecting the knowledge base category in the resulting pop-up and then the specific article.

    
