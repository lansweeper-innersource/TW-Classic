<!-- # LsPush vs. LsAgent scanning agent -->
Lansweeper includes several agentless scanning methods to scan the assets in your network. You can scan the Linux, Unix, Mac and Windows computers, VMware servers and other devices in your network without installing any Lansweeper software on the machines you're scanning. Optionally, you can scan your computers with a scanning agent instead.

Lansweeper includes two agents for scanning computers, LsPush and LsAgent. Both LsPush and LsAgent gather data locally on the client computer and can send it back to your Lansweeper installation for import.

Though both are agents, LsAgent is superior to LsPush in many ways, making it the overall preferred scanning agent. LsAgent is cross-platform for instance and ideally suitable for scanning laptops that are on the road. It does not require machines to be present in your network, as it can pull their data over the Internet instead.   
The only reason you may want to use the old LsPush agent is for integration in logon scripts or group policies, for the purpose of user logon tracking.

The overview below compares LsPush to LsAgent. More detailed information on LsPush can be found in [this knowledge base article](/classic/docs/introduction-to-the-lspush-scanning-agent-for-windows), while more detailed information on LsAgent can be found in [this knowledge base article](/classic/docs/introduction-to-lsagent-for-windows-linux-and-mac).

|  | [LsPush](/classic/docs/introduction-to-the-lspush-scanning-agent-for-windows) | [LsAgent](/classic/docs/introduction-to-lsagent-for-windows-linux-and-mac) |
| --- | --- | --- |
| Introduced in | Lansweeper 4.2 | Lansweeper 7.0 |
| Scan Windows computers | ✔ (Windows 2000 and higher) | ✔ (Windows 7, SP1 and higher) |
| Scan Linux computers | ✘ | ✔ |
| Scan Mac computers | ✘ | ✔ |
| Scan computers where inbound traffic is blocked | ✔ | ✔ |
| Send scanned data directly to your Lansweeper installation | ✔ | ✔ |
| Send scanned data to your Lansweeper installation securely over the Internet (HTTPS and TLS 1.2) | ✘ | ✔ |
| Permanently installed as a software on the computer | ✘ | ✔ |
| Scanning schedule automatically configured | ✘ | ✔ |
| Option for automatic import of scanned data | ✔ | ✔ |
| Option for manual import of scanned data | ✔ | ✘ |
| Integrate in logon scripts or group policies | ✔ | ✘ |
| Automatic agent updates (on Windows computers) | ✘ | ✔ |
