<!-- # Troubleshoot a failed initial push to Cloud -->
When you [link your local Lansweeper installation with Cloud](/classic/docs/link-lansweeper-on-prem-with-lansweeper-sites), a number of prerequisite checks are performed to ensure your installation is ready to link. Normally, after the prerequisite checks are successful, the initial push of your [Lansweeper](https://www.lansweeper.com/) installation to Cloud will succeed. However, sync errors can still occur under certain conditions.  
For instance, if your Lansweeper server loses internet access after the completion of the prerequisite checks and the submission of your Cloud details, your initial push will fail.

## Before you begin

- To ensure full compatibility with Cloud, make sure your Lansweeper installation is up to date. [Update instructions](/classic/docs/update-lansweeper-on-premises) can be found in the knowledge base.
- Pay close attention to any potential failures in [the Cloud prerequisite checks](/classic/docs/cloud-linking-requirements). Review the details of the failure and resolve it by following the instructions in the prerequisite check tooltip.

## Resolve initial push failure

1. If your initial push failed for a reason that could be resolved with a retry, the Lansweeper web console may offer you the **Retry initial push now** button. If available, this button is displayed in the **Troubleshooting** column of the **Configuration > Link With Cloud Site** menu.   
   If your internet connection was lost after submitting your Cloud link settings for instance, you can use the button to retry the sync.  
   
2. If no retry button is offered in the Cloud menu or if the sync still fails after a retry, you can try removing the link to Cloud and adding it again.   
   Select **Unlink from Cloud site** and wait for the unlink to complete. Afterward, you can select **Link with Cloud site** to try the link again.  
   
3. If the initial push to Cloud continues to fail and the cause is unclear, the log files below may contain additional info on the failure. These logs can be found on your Lansweeper server.   
   `Program Files (x86)\Lansweeper\Service\errorlog.txt`  `Program Files (x86)\Lansweeper\Service\sync_errorlog.txt` `Program Files (x86)\Lansweeper\Website\App_Data\web_errorlog.txt`  

   The sync\_errorlog.txt and web\_errorlog.txt will only exist if errors actually occurred in your Cloud sync or web console, respectively.
4. Syncing with Cloud requires an almost constant data stream between your on-prem sync server and Cloud. To limit bottlenecks and ensure future readiness, Lansweeper chooses to only allow syncing to Cloud using HTTP2-enabled proxies.   
   If your Lansweeper installation uses a proxy connection for outbound traffic, make sure HTTP2 is enabled or create an exception rule to bypass the proxy for the endpoint `edge.lansweeper.com`.
