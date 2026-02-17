<!-- # Introduction to BI Dashboards -->
The new BI Dashboards in Lansweeper Sites are designed to empower you with flexible, fully integrated tools that transform your data into actionable insights. Built with a modern, intuitive interface, these dashboards allow seamless navigation and customization to spotlight the metrics that matter most.

With advanced filtering capabilities, you can quickly refine your data to uncover precise insights, while alert features let you stay on top of key metrics through timely email notifications. For sharing and analysis, the dashboards offer versatile export options and powerful tools for in-depth data exploration, enabling a deeper understanding of your analytics than ever before.

- [Create a new dashboard](#create)
- [Modify a dashboard](#modify)
- [Share dashboards](#share)
- [Datasets](#datasets)
- [Static and dynamic filters](#filters)

## Create a new dashboard

1. In your Lansweeper Site, navigate to **Dashboards**.
2. Select **Create dashboard**.
3. Select **Add item**, and drag and drop an item on your new dashboard.
4. In **Available datasets**, select which data you want to display in the dashboard item.
5. Drag and drop the selected data into the dashboard item.
6. Select **Close edit mode**.

---

## Modify a dashboard

If you want to modify dashboard items, you’ll first need to enter ![edit2.png](/docs/.document360/assets/article_367/image_002.jpg)**Edit mode**.

### Customize dashboard items

To customize the entirety of a dashboard item:

1. Select the dashboard item you want to modify.
2. Select ![settings.png](/docs/.document360/assets/article_367/image_003.jpg) **Settings**.
3. Customize the dashboard item in style, data display, or interactivity options.

If you want to customize how specific data fields are displayed instead:

1. Select the dashboard item you want to modify.
2. Select ![data.png](/docs/.document360/assets/article_367/image_004.jpg) **Data**.
3. Select ![settings2.png](/docs/.document360/assets/article_367/image_005.jpg) **Settings** for the field you want to customize.

### Duplicate dashboard items

1. Select the dashboard item you want to modify.
2. Select ![clone.png](/docs/.document360/assets/article_367/image_006.jpg) **Clone**.

If you want to duplicate the entire dashboard instead, select ![duplicate.png](/docs/.document360/assets/article_367/image_007.jpg) **Duplicate dashboard**.

### Add alerts to dashboard items

1. Hover over the dashboard item you want to add an alert for, and select ![alert.png](/docs/.document360/assets/article_367/image_008.jpg) **Set an alert**.
2. In the popup, customize the **Trigger** and **Category**.
3. Optionally, add a filter for your alert.
4. Select **Next**.
5. Choose the frequency for your alert.
6. Select **Create new channel** to configure a channel for your alert.
7. Select and configure a channel type.
8. Select **Create** to create the channel.
9. Select **Create** and **Close** to add your alert.

### Delete dashboard items

1. Select the dashboard item you want to modify.
2. Select ![delete2.png](/docs/.document360/assets/article_367/image_009.jpg) **Delete**.

If you want to delete the entire dashboard instead, select ![delete.png](/docs/.document360/assets/article_367/image_010.jpg) **Delete dashboard**.

---

## Share dashboards

You can share any dashboards you’ve created with other members of your Lansweeper Site, or save the dashboard items themselves to share externally.

### Share an entire dashboard

You can share your dashboards with other users in your Lansweeper Site.

1. Select ![share2.png](/docs/.document360/assets/article_367/image_011.jpg) **Share**.
2. Choose the site accounts you want to share the dashboard with.
3. Select **Share dashboard**.

### Share dashboard items

You can download the data displayed in dashboard items as either a CSV or XLSX file, or save the entire dashboard item as PNG.

1. Hover over the dashboard item you want to save, and select ![download.png](/docs/.document360/assets/article_367/image_012.jpg) **Download**.
2. Select how you want to save the dashboard item.

## Datasets

Datasets are collections of fields gathered from various Lansweeper Sites modules. These fields are taken from custom views, making it easy to include the exact data points you need for detailed analysis.

Currently, four datasets are available:

- **Vulnerabilities**: contains Risk insights information, including fields like Risk score and CVE, to help assess potential vulnerabilities
- **Inventory**: contains asset data, featuring details such as Manufacturer, IP address, and Last scan attempt
- **Software**: contains software-related data, such as Publisher and Install date, useful for tracking applications
- **Users**: contains user information fields, like Display name and Employee ID, which are ideal for linking users with assets or software

Have suggestions for new fields? [Let us know](https://az5krgaymnz.typeform.com/to/FAHhxLxc) which fields you’d like to see added to your datasets!

You can combine fields from different datasets to create more detailed items:

- The **Inventory** and **Software** datasets are linked through the assetKey field, connecting asset data with software details.
- The **Inventory** and **Vulnerabilities** datasets are linked through the assetKey field, allowing you to view vulnerabilities with asset details.
- The **Inventory** and **Users** datasets are linked through the Last user field, connecting asset data with user information.

Currently, not all datasets can be linked, so certain combinations aren’t yet possible. Upcoming enhancements will allow:

- The **Vulnerabilities** and **Software** datasets to be linked through the Affected product field.

## Static and dynamic filters

There are two types of filters: static filters and dynamic filters. You can use static filters to keep consistent views in your dashboard, or dynamic filters to interactively explore data in real-time, adjusting insights on demand.

### Static filters

Static filters are permanently applied to your dashboard, ensuring that each time you open it, your dashboard items will automatically display with these filters in place.

To add static filters to dashboard items:

1. Select the dashboard item you want to modify.
2. Select ![data.png](/docs/.document360/assets/article_367/image_013.jpg) **Data**.
3. Select **Add filter**.
4. In the popup, select **Add filter**.
5. Create your filter, and select **Apply filters**.

### Dynamic filters

Dynamic filters let you interact with your data. To add dynamic filters to dashboard items, simply click on a specific bar or figure. Connected widgets will be updated in real time, meaning you can explore specific data throughout your dashboard.

Dynamic filters are not saved. Closing a dashboard will reset your dashboard items.  
Additionally, dynamic filters are not visible to other users in shared dashboards.
