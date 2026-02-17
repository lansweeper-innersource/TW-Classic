<!-- # Cloud sync speed issue -->
When you link your local [Lansweeper](https://www.lansweeper.com/) installation to a cloud site, the scan server you choose as sync server becomes responsible for syncing scanned and other data with Lansweeper Cloud. The cloud sync process is optimized to ensure data is sent in an efficient and timely way.   
However, under certain circumstances, your data may not be synced to Cloud quickly enough, and you may see a warning notification in your local web console as a result.

This article explains some steps you can take to resolve the sync speed issue.

## Verify sync server status

If your sync server is down, data cannot be synced to and from Cloud. In case of a Cloud sync speed warning, the first thing you should verify is the status of your sync server. In an installation with multiple scan servers, verify which machine is your sync server.

You can do this by browsing to the **Configuration > Link With Cloud Site** menu of the local web console. This menu lists all of your scan servers and clearly indicates which one is the sync server.

Locally on the sync server, open **Windows Services** and verify the status of the Lansweeper Server service. This service is responsible for all of the scan server's activities, including the sync with Cloud. If the Lansweeper service is not currently running, start it. If the service was previously down and you've since restarted it, be aware that you should wait a while for the Cloud sync to catch up and for the sync speed warning to resolve itself.

![procedure-starting-the-lansweeper-service.jpg](/docs/.document360/assets/article_372/image_002.jpg)

## Verify internet connectivity and speed

The speed of your internet connection significantly impacts the speed at which your data can be synced with Cloud. Make sure your Lansweeper sync server has access to the internet, that you have sufficient bandwidth and that your speed is stable. If you recently resolved an internet connectivity or speed issue, you should wait a while for the Cloud sync to catch up and for the sync speed warning to resolve itself.

Syncing with Cloud requires an almost constant stream of data between your on prem sync server and Cloud. To limit bottlenecks and ensure future readiness, Lansweeper chooses to only allow syncing to Cloud using HTTP2 enabled proxies. If your Lansweeper installation uses a proxy connection for outbound traffic, make sure HTTP2 is enabled or create an exception rule to bypass the proxy for the endpoint `edge.lansweeper.com`.
