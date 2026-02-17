<!-- # Cloud requirement: sync server TLS 1.2 -->
When you start setting up a link with your Cloud site, some prerequisite checks are performed to ensure your installation is ready to link. When you select **Link with Cloud site** in your local web console, a pop-up is presented with a pass/fail indication for a number of prerequisite checks. One of the checks is whether your sync server has TLS 1.2 enabled.

## Why is sync server TLS checked?

Your sync server is the machine selected to sync with Cloud. In order to secure the communication between your local Lansweeper installation and Cloud, Cloud is configured to use the TLS 1.2 cryptographic protocol. If your sync server does not also have this protocol enabled, communication with Cloud will fail as a result. Computers running a modern OS ordinarily have TLS 1.2 enabled by default.

## What do I do if the sync server TLS check fails?

If the sync server TLS check fails in the prerequisite pop-up, make sure TLS 1.2 is enabled on the machine hosting your sync server. Instructions for enabling TLS 1.2 can be found online and in Microsoft's knowledge base. Be careful editing TLS settings directly in the machine's registry, as incorrect changes may break the machine.
