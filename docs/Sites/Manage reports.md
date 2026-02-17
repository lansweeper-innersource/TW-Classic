<!-- # Manage reports -->
Lansweeper Sites includes a new, intuitive reporting engine. All reports can be found in the Reports module of Lansweeper Sites and are split up into 4 main categories: Hardware, Security, Software, and Users.   
By selecting one of these categories, you can view the reports in that specific category.

While there are built-in reports, you can modify or create your own as well using the report builder. Lansweeper Sites uses MongoDB to store your data and leverages GraphQL to query your data.  
![Export Report 4.png](/docs/.document360/assets/article_322/image_002.jpg)

## Viewing, running, and exporting reports

### Report state

Reports may take some time to run if your organization has a large number of assets, or many users accessing reports simultaneously. To ensure the health, scalability, speed, and availability of the reporting service, you can run and schedule your reports according to your needs.

Instead of constantly accessing the data in real-time, the execution of reports can be ad-hoc or at a scheduled time. You can track the status of your reports in the **Report > Status** column.

There are four different report states: scheduled, non-scheduled, queued, and errored.

#### Scheduled report

Report schedules can be paused if the reports are not actively used over a defined period. For more information, see Disabled reports.

This indicates the report is scheduled to run at a user-configured interval. The scheduling information is shown when hovering over the report status icon.  
![reporting_18.jpg](/docs/.document360/assets/article_322/image_003.jpg)

#### Non-scheduled report

A non-scheduled report will not run automatically and can be run ad-hoc by selecting **Run report now**.  
![reporting_19.jpg](/docs/.document360/assets/article_322/image_004.jpg)

#### Queued report

When a report is triggered, either through its schedule or ad-hoc, it is added to the report queue that is running in the background. Queued reports are indicated as below.  
![reporting_20.jpg](/docs/.document360/assets/article_322/image_005.jpg)

#### Execution error

When a report is not executed properly, an error icon will appear. This indicates the report was not run successfully. This can be resolved by running the report again using the **Run report now** button.  
![reporting_25.jpg](/docs/.document360/assets/article_322/image_006.jpg)

#### Disabled reports

Scheduled reports will be paused automatically if the reports are not actively used.

For reports scheduled as **Everyday** or **On specific days**:

- The system evaluates the consumption percentage of the specific report over the past **7 days** during each scheduled execution.
- If the consumption percentage falls below **50%**, the report schedule will be automatically disabled.

A report is considered consumed when:

- A user opens the report results page.
- A dashboard uses the data from the report widget.

Reports with no executions during the evaluation period will not be disabled.

### Run reports ad-hoc

You can run any report in real-time with the click of a button.

1. Hover over the status icon of the report in the **Status**column.
2. Select **Run report now**.  
   ![Export Report 2.png](/docs/.document360/assets/article_322/image_007.jpg)

Alternatively, you can run multiple reports at once by selecting all reports you want to run, and selecting **Run report now**.

### Schedule reports

You can schedule your reports to run at a certain day and time or at a given interval.

1. Select the reports you want to schedule.
2. Select **Schedule Report**.  
   ![Export Report 3.png](/docs/.document360/assets/article_322/image_008.jpg)
3. In the pop-up, select how often you want the reports to run.
4. Select **Schedule report**.

### Export report results

1. Select the report whose results you want to export.
2. In the results view, select **Export**.   
   ![Export report 1.png](/docs/.document360/assets/article_322/image_009.jpg)
3. In the resulting pop-up, you can choose whether to export the first 10,000 results of the report (Standard export), or all results (Full export). You can also select the export format, CSV or XLSX.  
   ![Export report 2.png](/docs/.document360/assets/article_322/image_010.jpg)  
   If you choose **Standard export**, you will be offered the export file immediately upon confirming the operation.  
   If you choose **Full export**, the export file will be prepared for you upon confirming the operation and sent to you via email. The download link in the email remains valid for 3 days.

## Report builder

The report builder allows you to visually build or modify your own reports. For a complete overview of the report builder menu, check out [Introduction to the report builder](/docs/introduction-to-the-report-builder).
