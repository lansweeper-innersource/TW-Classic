<!-- # Create a deployment package -->
[Lansweeper](https://www.lansweeper.com/ "Lansweeper") Classic includes a deployment module that allows you to deploy changes on Windows computers. You can create deployment packages, which are series of conditions and commands, to remotely make changes to the Windows computers in your network. Packages can be deployed manually, based on a schedule or after scanning. They allow you to: install and uninstall software, make command-line changes (e.g. registry changes) to your machines, kill processes and run custom scripts.

A good place to find and share deployment packages is [our community forum](https://lansweeper.com/forum/yaf_topics28.aspx).

## Create a deployment package

1. Make sure any command you plan on adding to your deployment package works when executed directly in Command Prompt on a client machine. If a command generates an error when executed in Command Prompt, it will also fail to execute as part of a deployment package as well.
2. Browse to the **Deployment > Deployment packages**section of the web console.
3. Select **New package** to create a new package. Alternatively, to create a new package based on an existing one, click the file icon next to the package you want to duplicate.
4. Enter a name and more detailed description for the package in the resulting pop-up.
5. Configure the deployment package's options.
   - Maximum Duration Per Asset: when the specified time has elapsed, Lansweeper will stop the deployment. This will ensure that unnecessary processes or failing deployments do not continue to run. Don't set your max duration lower than the expected execution time or your deployment package will be interrupted.
   - Final Action: optionally, which action Lansweeper should take once the deployment has completed and how long Lansweeper should wait before taking said action. In the example below, the target machines will be rebooted 5 minutes after the deployment has completed. Your deployment is considered completed if it ended in a Stop (Success), Stop (Failure), or if your maximum duration has expired.  
     
   - Rescan Assets: whether or not Lansweeper should rescan the target machines once the deployment has completed. Your deployment is considered completed if it ended in a Stop (Success) or Stop (Failure) or if your max duration expired.
6. Select your deployment package's run mode and click **Ok** to submit your initial configuration. When Lansweeper runs a deployment on a Windows computer, it creates a scheduled task on the computer to execute the deployment steps. Your run mode determines which user this scheduled task runs under once it's been created.
   - Select On Deployment: the package will ask which run mode to use when it is deployed.
   - System Account: the scheduled task is run under the computer's local system account. This is generally the most secure and the best option for most deployments. The local system account should be able to do most things on the local computer.
   - Scanning Credentials: the scheduled task is run under the scanning credential submitted in Lansweeper for the computer. This run mode may be required if your deployment requires special permissions or access to certain resources that are not on the local computer.
   - Currently Logged On: the scheduled task is run under the account of the user currently logged into the computer. This run mode may be required if your deployment is meant to make changes to a specific user's installed software, settings or registry keys.
7. Select your package and click **Add step** to start adding steps. You can now specify what your package will actually do. A deployment package consists of one or more steps, with each step leading to either another step or a success or failure message.
   - You can rearrange, edit and delete steps using the available buttons.
   - For each step, you must specify which return codes signify successful execution of the step. When you execute a command on a computer, a code is returned in the background signifying whether or not the command was successful. Codes signifying success must be submitted in your deployment step, so Lansweeper can correctly assess whether a step ran successfully. 0, 1641 and 3010 are the default codes added to each step, as these are common success codes. However, your specific command may have other success codes, in which case you must manually submit them.
   - For each step, you must specify a step name and what will happen upon success or failure of the step. The success or failure of a step can lead to the next step, a specific step of your choice or the completion of your deployment with a Stop (Success) or Stop (Failure) message.

## Available types of deployment steps

There are 6 types of deployment steps:

- Installer: allows you to run installers on the target computer and specify parameters. Don't forget to store your installers in your package share(s). The installers referenced by the built-in deployment packages are stored in DefaultPackageShare$ on your Lansweeper server, in the Installers subfolder.  

  To reference [your package share(s)](/docs/deployment-requirements) in your deployment package, include the {PackageShare} parameter in your file path.
- Command: allows you to run Command Prompt (CMD) commands on the target computer.
- KillProcess: allows you to kill processes running on the target computer. Optionally, you can forcefully kill the process and/or kill its child processes as well.
- Script: allows you to run a VBS or other type of script on the target computer. Don't forget to store your scripts in your package share(s). The scripts referenced by the built-in deployment packages are stored in DefaultPackageShare$ on your Lansweeper server, in the Scripts subfolder.  

  To reference [your package share(s)](/docs/deployment-requirements) in your deployment package, include the {PackageShare} parameter in your file path.
- Condition: allows you to verify the existence or version of specific files on the computer, the existing or value of specific registry keys, the computer's OS architecture (32-bit or 64-bit) or OS. If all of the criteria you specify are met, the deployment step will be considered successful. If not all criteria are met, the deployment step will be considered unsuccessful.   
  In the example below, the deployment will end in a Stop (Success) if LansweeperService.exe exists and if it has a file version lower than 5.2.0.4. The deployment will end in a Stop (Failure) if LansweeperService.exe does not exist or if LansweeperService.exe has a file version greater than or equal to 5.2.0.4.  

  The Condition step can check files, registry keys, OS and OS architecture. However, you can also target specific computers with your deployment by running the package on a specific (static or dynamic) asset group or report.
- MSIUninstaller: allows you to silently uninstall MSI software packages from the target computer by selecting from a list of scanned software. Non-MSI packages can be uninstalled using deployments as well, but then you must choose a different type of step and specify the exact uninstall command as found on the software vendor's website.
