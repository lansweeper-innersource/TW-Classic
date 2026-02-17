<!-- # Deploy a package manually or based on a schedule -->
A package can be deployed [manually](#heading1) or [based on a schedule](#heading2). When a deployment is initiated, Lansweeper uses your scanning credentials to access the Task Scheduler on your machines, creates a task on your computers that will run the deployment steps, and ends the connection. The task is then run under your computer's system account, the scanning credential mapped to the computer or the user currently logged into the computer.

It is generally recommended that you use the system account to run the task, which is the most secure. However, the other two options may be useful if your deployment requires special permissions or is meant to make changes to a specific user's installed software or registry keys.

The default run mode is configured in the **Deployment > Security options**section of the web console, but you can specify another run mode when manually initiating or scheduling a deployment as well.

![deploying-a-package-manually-or-based-on-a-schedule-1.jpg](/docs/.document360/assets/article_059/image_001.jpg)

Three credentials come into play when performing a deployment:

- Your scanning credentials will be used to create tasks on your machines that will run the deployment.
- Your [share credentials](/docs/deployment-requirements) are used by the tasks to access files stored in your package shares and referenced in your deployment package.
- The tasks are run under your system accounts, scanning credentials, or currently logged-on users, depending on which run mode you choose.

Deployments are performed in batches. The number of concurrent deployments is determined by the **Deployment Threads** value configured in the **Configuration > Server Options >****Service Options** section of the web console.

![menu-configuration-server-options.jpg](/docs/.document360/assets/article_059/image_002.jpg)  

Deployment thread changes won't take effect until you restart the Lansweeper Server service on your Lansweeper server.

## Deploying a package manually

To deploy a package manually, choose either of the options listed below. A pop-up will confirm which package you would like to deploy. Optionally, you can choose to perform a Wake-on-LAN of offline computers before deployment, in which case you'll need to specify an estimated boot time per asset. You can also have the deployment automatically retried for offline machines.

- Go to the Assets section of the web console, tick the checkboxes of the target computers of your choice and select **Deploy Package**.

  ![deploying-a-package-manually-or-based-on-a-schedule-2.jpg](/docs/.document360/assets/article_059/image_003.jpg)

  - You can search through the columns to find specific assets easily.
  - You can tick the top checkbox to select all assets in the current search results.
- Select a computer report under **Reports > View All Reports** and select **Deploy Package**. Remember that the deployment button only appears in asset reports, i.e., reports that include the tblAssets.AssetID field.  
  ![menu-reports-view-all-reports.jpg](/docs/.document360/assets/article_059/image_004.jpg)
- Hover over the **Assets**section at the top of the web console, select an entry in one of the available asset overviews and select **Deploy Package**.![procedure-selecting-domain-in-assets-menu.jpg](/docs/.document360/assets/article_059/image_005.jpg)
- Browse to the **Deployment > Deployment packages** section of the console, select your package on the left and select **Deploy Now**. This will also allow you to manually select assets or run a deployment on computers included in a specific (static or dynamic) group or report.![deploying-a-package-manually-or-based-on-a-schedule-3.jpg](/docs/.document360/assets/article_059/image_006.jpg)

## Deploying a package based on a schedule

To deploy a package based on a schedule, follow the steps below. Optionally, you can perform a Wake-on-LAN of offline computers before deployment, wherein you'll need to specify an estimated boot time per asset. You can also have the deployment automatically retried for offline machines or triggered by a successful scan.

1. Browse to the **Deployment > Scheduled deployments**section of the web console.![menu-deployment-scheduled-deployments.jpg](/docs/.document360/assets/article_059/image_007.jpg)
2. Select **New Schedule** in the **Schedules** section of the page. Specify a name for your schedule, start date and time, and schedule type. You can run your deployment once, based on an interval (every X number of minutes, hours, days), daily, weekly, or monthly. Daily, weekly and monthly deployments can be run once or every X hours as well.![deploying-a-package-manually-or-based-on-a-schedule-4.jpg](/docs/.document360/assets/article_059/image_008.jpg)
3. Select **New Deployment Configuration** in the **Configurations** section of the page. Select your schedule, select your package and choose either a (static or dynamic) asset group, a report or an individual selection of assets to run the deployment on.![deploying-a-package-manually-or-based-on-a-schedule-5.jpg](/docs/.document360/assets/article_059/image_009.jpg)
