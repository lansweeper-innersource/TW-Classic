<!-- # Cloud requirement: sync server internet access -->

When you start setting up a link with your [Lansweeper](https://www.lansweeper.com/) Site, some prerequisite checks are performed to ensure your installation is ready to link. When you select **Link with Cloud site** in your local web console, a pop-up is presented with a pass/fail indication for a number of prerequisite checks. One of the checks is whether your sync server has internet access.

## Why is sync server internet access checked?

Cloud is accessed over the internet. Your sync server, the machine selected to sync with your site, must therefore be able to reach the internet to successfully link. More specifically, your sync server must be able to make outbound connections to all of the URLs below and their sub-URLs.

Ensure that your firewall allows traffic to the following URLs (port 443), based on where your site is hosted.

|  |  |
| --- | --- |
| **Europe** | **United States** |
| edge.eu.lansweeper.com | edge.us.lansweeper.com |
| https://id.eu.lansweeper.com | https://id.us.lansweeper.com |
| https://eu.lansweeper.com | https://us.lansweeper.com |
| [discovery-gateway.lansweeper.com](http://discovery-gateway.eu.lansweeper.com/ "http://discovery-gateway.eu.lansweeper.com/") | [discovery-gateway.lansweeper.com](http://discovery-gateway.eu.lansweeper.com/ "http://discovery-gateway.eu.lansweeper.com/") |
| \*.aws.amazon.com | \*.aws.amazon.com |
| \*.amazonaws.com | \*.amazonaws.com |
| [\*.cloudfront.net](http://cloudfront.net/) | [\*.cloudfront.net](http://cloudfront.net/) |

If it's your first time creating a U.S.-based Lansweeper Site from the Lansweeper On-premises console, you must whitelist [https://eu.lansweeper.com](http://app.lansweeper.com/ "http://app.lansweeper.com/") (or [http://app.lansweeper.com](http://app.lansweeper.com/ "http://app.lansweeper.com/") for an older agent version) when you initially create your site. Once you create the site, you can unlist the URL.

## What do I do if the sync server internet access check fails?

If the sync server internet access fails in the prerequisite pop-up, double-check that your sync server can make outbound connections to the aforementioned URLs and their sub-URLs. If it cannot, your network admin should check the settings of anti-virus software, proxy servers, software firewalls, hardware firewalls and other components in your network. One of these components may be blocking the sync server's internet access.

Syncing with Cloud requires an almost constant stream of data between your on-prem sync server and Cloud. To limit bottlenecks and ensure future readiness, Lansweeper chooses to only allow syncing to Cloud using HTTP2 enabled proxies. If your Lansweeper installation uses a proxy connection for outbound traffic, make sure HTTP2 is enabled or create an exception rule to bypass the proxy for the endpoint `edge.eu.lansweeper.com` or `edge.us.lansweeper.com` (depending on your data hosting region).
