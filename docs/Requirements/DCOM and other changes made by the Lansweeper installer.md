<!-- # DCOM and other changes made by the Lansweeper installer -->
When you [install](/classic/docs/install-lansweeper-on-prem) or subsequently [update](/classic/docs/update-lansweeper-on-premises) Lansweeper, the Lansweeper installer makes changes to the DCOM and a few other settings on your Lansweeper server. The purpose of these setting changes is to prevent Lansweeper installation and scanning failures.

Below is an overview of changes made by the Lansweeper installer to the server hosting your Lansweeper installation.

## DCOM is enabled

DCOM is enabled by modifying several registry values through the commands below. These DCOM setting changes are made to ensure agentless scanning of Windows computers works.

```
RegWriteStringValue(HKEY_LOCAL_MACHINE, 'SOFTWARE\Microsoft\Ole', 'EnableDCOM','Y');
RegWriteDWordValue(HKEY_LOCAL_MACHINE, 'SOFTWARE\Microsoft\Ole', 'LegacyAuthenticationLevel',2);
```



You can prevent DCOM changes by installing using the /noDCOMReset [silent install option](/classic/docs/silently-install-uninstall-or-update-lansweeper). Keep in mind that these changes may be necessary to ensure agentless scanning is functional

## Loopback checks are disabled

Loopback checks are disabled by modifying a registry value through the command below.

```
RegWriteDWordValue(HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Control\Lsa', 'DisableLoopbackCheck',1);
```

## Simple file sharing is disabled

Simple file sharing is disabled by modifying a registry value through the command below.

```
RegWriteDWordValue(HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Control\Lsa', 'forceguest',0);
```

## Npcap driver is installed

An Npcap driver is automatically installed. This driver is required for Lansweeper's [Asset Radar](/classic/docs/introduction-to-asset-radar) feature. Asset Radar is a credential-free scanning method that retrieves asset information based on captured network packets. Note that the automatic installation of the Npcap driver results in the addition of a loopback adapter on your Lansweeper server.

You can skip the installation of Npcap by adding the [silent install option](/classic/docs/silently-install-uninstall-or-update-lansweeper) /SkipNpCapDriver.
