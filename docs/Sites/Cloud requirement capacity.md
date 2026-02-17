<!-- # Cloud requirement: capacity -->
When you start setting up a link with your Cloud site, some prerequisite checks are performed to ensure your installation is ready to link. When you select **Link with Cloud site** in your local web console, a pop-up is presented with a pass/fail indication for a number of prerequisite checks. One of the checks is whether Cloud has enough capacity available to service your sync request.

## Why is capacity checked?

Cloud and its back-end resources are scaled according to how many users are using it. Under normal circumstances, enough capacity is available in Cloud to allow you to set up your initial sync. At extraordinarily busy times though, we may temporarily block further pushes to Cloud. This temporary block gives our back-end systems the time to scale appropriately.

## What do I do if the capacity check fails?

If the capacity check fails, this indicates that new pushes have temporarily been blocked by Cloud itself. This failure is not related to any issue within your local Lansweeper installation and hence cannot be resolved locally. You can simply try the push at a later time, once capacity has stabilized.
