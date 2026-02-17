<!-- # Create and add custom fields to ticket types -->
From version 6.0 onward, the Lansweeper software includes a fully functional helpdesk. The Lansweeper helpdesk includes a robust ticketing system that allows people to ask each other questions and request support. Ticket custom fields allow users and agents to add extra information to a ticket in an organized way.

Custom fields are fields you create and assign a name, type and (optionally) list of possible values to. They can be combo boxes, date fields, text values and more.

Adding information to custom fields can be made optional or required. Custom fields can be nested as well, with the completion of one field bringing up another field and so on. As different ticket types tend to require different kinds of fields, custom fields are configured per ticket type.

In the example below, agent Daniel used custom fields to mark the ticket that was assigned to him as a hardware related issue.

![illustration-ticket-custom-fields.jpg](/docs/.document360/assets/article_021/image_001.jpg)

## Configuring ticket custom fields

1. Browse to the **Configuration > Ticket Content**section of the web console.![menu-configuration-ticket-content.jpg](/docs/.document360/assets/article_021/image_002.jpg)
2. Select **Add Custom Field** in the **Ticket custom fields** section of the page to create a field that you can add to a ticket type later. Repeat this step for any additional custom fields you may need.![creating-and-adding-custom-fields-to-ticket-types-1.jpg](/docs/.document360/assets/article_021/image_003.jpg)
   - **Name**: name of the ticket custom field.
   - **Info**: description of the custom field, which will be displayed as a tooltip next to the field on ticket pages.
   - **Type**: color combo box, combo box, currency, date, datetime, hyperlink, multiselect, numeric, radiobutton list, textarea, textbox, time or yes/no checkbox.
   - **Values**: for (color) combo boxes and multiselect and radiobutton lists, the list of possible values.
3. Select **Alter Custom Fields** next to the ticket type you want to add your fields to in the **Ticket types** section of the page.![creating-and-adding-custom-fields-to-ticket-types-2.jpg](/docs/.document360/assets/article_021/image_004.jpg)
4. Click and hold a field in the list on the left and drag it to the empty area to add the field to the ticket type.  
   ![creating-and-adding-custom-fields-to-ticket-types-3.jpg](/docs/.document360/assets/article_021/image_005.jpg)
   - **Agents Only**: if checked, this field will only be visible to agents.
   - **Required**: if checked, this field must be filled in when a ticket of the specified ticket type is created.
   - **Required for Closing**: if checked, this field must be filled in when a ticket of the specified ticket type is set to the Closed state.  
     ![creating-and-adding-custom-fields-to-ticket-types-4.jpg](/docs/.document360/assets/article_021/image_006.jpg)
5. Add additional fields on the same level as the initial one by dragging them into the area and placing them above or below the initial field. Fields will be displayed in this same order on ticket pages.![creating-and-adding-custom-fields-to-ticket-types-5.jpg](/docs/.document360/assets/article_021/image_007.jpg)

   ![creating-and-adding-custom-fields-to-ticket-types-6.jpg](/docs/.document360/assets/article_021/image_008.jpg)
6. Nest fields by dragging a field on the left into a field on the right. You can have field A bring up field B when field A is simply filled in. Alternatively, for certain field types, you can have the selection of a specific value in field A bring up field B. You can nest several levels deep.   
   In the example below, the First occurrence and Last occurrence fields will become available when the Occurrences field is filled in, the Root cause category field will become available when the Root cause known field is set to Yes.

   ![creating-and-adding-custom-fields-to-ticket-types-7.jpg](/docs/.document360/assets/article_021/image_009.jpg)

   ![creating-and-adding-custom-fields-to-ticket-types-8.jpg](/docs/.document360/assets/article_021/image_010.jpg)

   ![creating-and-adding-custom-fields-to-ticket-types-9.jpg](/docs/.document360/assets/article_021/image_011.jpg)
