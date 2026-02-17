<!-- # Deployment requirements -->
**This page explains which requirements you need to fulfil to start using Lansweeper deployment packages.**

---

Lansweeper includes a deployment module that allows you to deploy changes on Windows computers. You can [create deployment packages](/docs/create-a-deployment-package), series of conditions and commands, to remotely make changes to the Windows computers in your network.

Packages can be [deployed manually or based on a schedule](/docs/deploy-a-package-manually-or-based-on-a-schedule) and allow you to: install and uninstall software, make command-line changes (e.g. registry changes) to your machines, kill processes and run custom scripts. To deploy changes on Windows computers, certain deployment requirements must be met.

## Deployment requirements

- The target computer must be running a non-Home edition of Windows XP or a more recent Windows OS. Windows 2000 and older operating systems are not supported.
- The target computer's name must resolve to an IP address from your Lansweeper server. DNS resolution must be successful.
- The target computer must have an IPv4 IP address.
- The **Task Scheduler** service, found in Windows Services, must be running on the target computer, as the deployment package runs as a task. If the **Task Scheduler** service isn't running, Lansweeper will try to start it as part of the deployment requirements check.
- The **Remote Registry** service, found in Windows Services, must be running on the target computer, as the deployment steps are written into the computer's registry. If the **Remote Registry** service isn't running, Lansweeper will try to start it.
- The target computer's firewall must be properly configured to allow access to the machine. If you are using Windows Firewall and enabled the [remote administration exception](/docs/configure-windows-firewall-for-agentless-scanning-of-computers) for agentless scanning, deployments should ordinarily already be allowed through the firewall. However, in some Windows builds it is necessary to enable and allow the **Remote Scheduled Tasks Management** rule in Windows Firewall as well.
- A valid scanning credential, with administrative privileges on the target machine, must be used as a global Windows credential or must be mapped to the target machine's computer name, domain, IP address or IP range.  

  In this scenario, LAPS credentials cannot be used as scanning credentials.
- Your scanning credential must have access to administrative share C$ on the target computer, as an executable required for running the deployment is written into a `C:\Windows\LSDeployment` folder on the computer.
- Any installers, scripts or other files you plan on referencing in your deployment package must be added to the DefaultPackageShare$ folder on your Lansweeper server, or other share(s) of your choice. You must also provide a credential with Read & Execute permissions on the share. Shares can be managed in the **Deployment > Security options**section of the web console.
  - The Lansweeper installer shares `Program Files (x86)\Lansweeper\PackageShare` on your Lansweeper server as DefaultPackageShare$. By default, deployment packages look for files in this folder.
  - However, you can choose another share and specify additional shares for specific IP ranges in your network. The Default Package Share will be used for deployments on computers without an IP range specific share.![menu-deployment-security-options.jpg](/docs/.document360/assets/article_060/image_002.jpg)![deployment-requirements-1.jpg](/docs/.document360/assets/article_060/image_003.jpg)  

    Share credentials are stored in a reversible encrypted format in the registry of the computers you're deploying on. For security reasons it is recommended that you use accounts that only have (Read & Execute) permissions on your shares as your share credentials. Should these credentials ever be compromised, the only access they will have is to your package shares.

    It is recommended that you do not host your package share(s) on a Windows XP machine. Windows XP only allows for five concurrent share connections, which will limit the maximum number of concurrent deployments to five.
