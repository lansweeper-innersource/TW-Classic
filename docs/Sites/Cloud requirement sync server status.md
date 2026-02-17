<!-- # Cloud requirement: sync server status -->
When you start setting up a link with your [Lansweeper](https://www.lansweeper.com/) cloud site, some prerequisite checks are performed to ensure your installation is ready to link. When you select **Link with Cloud site** in your local web console, a pop-up is presented with a pass/fail indication for a number of prerequisite checks. One of the checks is whether the Lansweeper Server service on your sync server is up or down.

## Why is sync server status checked?

Your sync server is the machine you selected to sync with Cloud. The Lansweeper Server service on your sync server is what connects and syncs your local Lansweeper database with your Cloud site. If this service is not running or successfully connecting to your local Lansweeper database, the sync with Cloud cannot work.

## What do I do if the sync server status check fails?

If the sync server status check fails, this indicates that the Lansweeper Server service on the server isn't successfully connecting to your local Lansweeper database. Open **Windows Services** on your sync server and start the Lansweeper Server service, if it is not already running. If the service fails to start, you can check the **Errorlog.txt** file on the server for possible database connection issues. The error log can be found in the following location: `Program Files (x86)\Lansweeper\Service\Errorlog.txt`

![procedure-starting-the-lansweeper-service.jpg](/docs/.document360/assets/article_363/image_002.jpg)
