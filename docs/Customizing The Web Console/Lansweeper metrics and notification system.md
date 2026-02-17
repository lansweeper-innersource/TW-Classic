<!-- # Lansweeper metrics and notification system -->
The metrics and notification system within the Lansweeper Classic web console provides a notification service to Lansweeper users, which can be personalized.

With notifications, you can be notified of the latest vulnerabilities, blog posts, news or reports we publish. You can personalize which types of notifications you wish to receive, or turn them off altogether.

## Notifications

### User interface

Lansweeper notifications are shown in an overlay at the bottom of the web console. Depending on the notification categories you've enabled, you can get notifications about Lansweeper news, blog posts, published reports and more.   
![Metrics-and-notifications-1.jpg](/docs/.document360/assets/article_038/image_001.jpg)  
Notifications can be cycled through or dismissed by using the navigational buttons in the bottom right-hand corner.  
![Metrics-and-notifications-2.jpg](/docs/.document360/assets/article_038/image_002.jpg)

### Configuration

To choose which categories to receive notifications for, navigate to **Configuration > In-app Notifications** in the web console. Uncheck the categories you no longer wish to receive notifications about.  
![Metrics-and-notifications-7.jpg](/docs/.document360/assets/article_038/image_003.jpg)

Notification settings are configured globally for your Lansweeper installation. However, when notifications are sent, they may in some cases be filtered so they are only shown to specific users. For instance, a notification regarding a Lansweeper update may only be presented to Lansweeper administrators and not to other console users.

Notifications are sent to your Lansweeper installation via an API created for the notification and metric features. Notification data, along with the display criteria, are sent to your Lansweeper installation. The Lansweeper service interprets the data and displays the notification to users who match the given criteria.

## Metrics

Metrics are aggregated data collected from your Lansweeper installation. Aggregated metrics are used to provide relevant, personalized notifications and content. They allow us to determine which vulnerabilities or topics are most relevant to our customer base and to you specifically. That way, we can provide content that is not only interesting but also useful and actionable.

### Configuration

The configuration page allows you to view which metrics have been collected, which scanning server is the primary scanning server used for metrics, and disable the collection of metrics if wanted.

- You can change the metrics configuration by navigating to **Configuration > Privacy Settings**. You can view the last data set collected by selecting **Show last collected metrics**.   
  ![Metrics-and-notifications-4.jpg](/docs/.document360/assets/article_038/image_004.jpg)
- To change which scanning server is the primary scanning server used for metrics, select your desired scanning server from the drop-down menu.   
  If the selected scanning server is not currently running, Lansweeper checks if another scanning server can connect to the API. If another scanning server is found, that server makes the API connection.   
  ![Metrics-and-notifications-5.jpg](/docs/.document360/assets/article_038/image_005.jpg)
- To disable metrics collection, uncheck **Allow Lansweeper to gather metrics**. ![Metrics-and-notifications-6-e1562253268704.jpg](/docs/.document360/assets/article_038/image_006.jpg)  

  Disabling metrics will make it impossible for Lansweeper to present you with personalized notifications on certain topics. For instance, we will no longer be able to inform you about vulnerabilities that were detected in your network.

### Security

To guarantee full security of the gathered metrics, data is sent via HTTPS and is also encrypted with symmetric encryption using an on-the-fly generated key. Only our cloud API has the private key in order to decrypt the data.
