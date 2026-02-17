<!-- # Cloud requirement: web server internet access -->

When you start setting up a link with your [Lansweeper](https://www.lansweeper.com/) Site, some prerequisite checks are performed to ensure your installation is ready to link. When you select **Link with Cloud site** in your local web console, a pop-up is presented with a pass/fail indication for a number of prerequisite checks. One of the checks is whether the machine hosting your Lansweeper web console has internet access.

## Why is web server internet access checked?

Lansweeper Sites is accessed over the internet. Your web server must therefore be able to reach the internet to successfully link with a site.

Ensure that your firewall allows traffic to the following URLs (port 443), based on where your site is hosted.

|  |  |
| --- | --- |
| **Europe** | **United States** |
| edge.eu.lansweeper.com | edge.us.lansweeper.com |
| https://id.lansweeper.com | https://id.us.lansweeper.com |
| https://app.lansweeper.com | https://app.lansweeper.com |
| https://eu.lansweeper.com | https://us.lansweeper.com |
| installerapi.lansweeper.com | installerapi.lansweeper.com |
| \*.aws.amazon.com | \*.aws.amazon.com |
| \*.amazonaws.com | \*.amazonaws.com |
| https://discovery-gateway.lansweeper.com | https://discovery-gateway.lansweeper.com |
| [\*.authentication.lansweeper.com](http://*.authentication.lansweeper.com) | [\*.authentication.lansweeper.com](http://*.authentication.lansweeper.com) |

If it's your first time creating a U.S.-based Lansweeper Site from the Lansweeper On-premises console, you must whitelist <https://app.lansweeper.com> when you initially create your site. Once you create the site, you can unlist the URL.

## What do I do if the web server internet access check fails?

If the web server internet access fails in the prerequisite pop-up, double-check that your web server can make outbound connections to the aforementioned URLs and their sub-URLs. If it cannot, your network admin should check the settings of anti-virus software, proxy servers, software firewalls, hardware firewalls and other components in your network. One of these components may be blocking the web server's internet access.

Syncing with Cloud requires an almost constant stream of data between your on prem sync server and Cloud. To limit bottlenecks and ensure future readiness, Lansweeper chooses to only allow syncing to Cloud using HTTP2 enabled proxies. If your Lansweeper installation uses a proxy connection for outbound traffic, make sure HTTP2 is enabled or create an exception rule to bypass the proxy for the endpoint `edge.eu.lansweeper.com` or `edge.us.lansweeper.com`.
