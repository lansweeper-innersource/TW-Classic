<!-- # LsPush fallback scanning -->
Lansweeper includes several agentless scanning methods to scan the assets in your network. You can scan the Linux, Unix, Mac and Windows computers, VMware servers and other devices in your network without installing any Lansweeper software on the machines you're scanning.

Optionally, you can scan your computers with a scanning agent instead. Lansweeper includes two agents for scanning computers, LsPush and LsAgent. [This knowledge base article](/docs/lspush-vs-lsagent-scanning-agent) explains the difference between the two agents and links to setup instructions for both.

While LsPush is generally deployed by you using a group policy, Lansweeper also has a feature that automatically tries to scan Windows computers using LsPush. This feature is called fallback scanning.

## What fallback scanning is

Fallback scanning is a feature that places the LsPush agent on a Windows client machine and runs it as a scheduled task, so scanned data can be sent back to your Lansweeper installation. The path of the LsPush executable as pushed to the client machine is `C:\Windows\LSDeployment\LsPush.exe`.   
A fallback scan only occurs if all of the following requirements are met:

- You submitted the client machine for agentless scanning in the following section of the Lansweeper web console: **Scanning > Scanning Targets**.
- The client machine's agentless scan is failing with an RPC (firewall) error due to required ports not being open on the machine.
- Port 135 is open on the client machine.
- The Task Scheduler service is running and Task Scheduler is accessible on the client machine.
- The administrative share C$ is accessible on the client machine.

## How to disable this feature

Fallback scanning is enabled by default. If you do not want fallback scans to occur for your Windows computers, do either of the following options:

- Resolve the scanning errors your computers are generating during agentless scanning, as fallback scanning only takes place if agentless scanning fails. A troubleshooting guide for RPC errors can be found in [this knowledge base article](/docs/the-rpc-server-is-unavailable-0x800706ba).
- Uncheck the **Enable fallback scanning** box in the **Configuration > Server Options**section of the web console.

  

  
