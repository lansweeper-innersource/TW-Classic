<!-- # Check the status of a deployment -->
Lansweeper includes a deployment module that allows you to deploy changes on Windows computers. You can [create deployment packages](/docs/create-a-deployment-package), series of conditions and commands, to remotely make changes to the Windows computers in your network. Packages can be [deployed manually or based on a schedule](/docs/deploy-a-package-manually-or-based-on-a-schedule) and allow you to: install and uninstall software, make command-line changes (e.g. registry changes) to your machines, kill processes and run custom scripts.

## Where to check deployment statuses

- In the **Deployments** tab of individual computer webpages. This tab is only displayed if at least one deployment has been run on the computer.
- In the **Deployment > Deployment logs** section of the web console, if you have just one scanning server.  
  
- If you have multiple scanning servers, in the **<server name>** section of the web console under **Deployment**. Each scanning server has its own log page.

## What is included in deployment statuses

The following information is included in deployment statuses:

- Log Date: date and time of the completion of the deployment package.
- Asset Name: name of the target computer.
- Package: name of the deployment package.
- Executor: name of the user or schedule that initiated the deployment.
- Return: code returned by the last step in the deployment package.
- Last Step: last step that was executed in the deployment package.
- Run Mode: account the deployment task that was pushed to the computer was run under. This is either the system account, scanning credential or currently logged on user.
- Message: feedback returned by the deployment package.
- Deployer Version: version number of the deployment executable that ran the deployment. When a deployment is initiated, this executable is copied from the `Program Files (x86)\Lansweeper\Service\Deployers` folder on your Lansweeper server to the `C:\Windows\LSDeployment` folder on the target computer.
- Server Name: name of the scanning server that ran the deployment package.
