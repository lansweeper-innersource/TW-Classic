<!-- # Resolve vulnerabilities -->

Resolving vulnerabilities is paramount to safeguarding your assets against potential threats. Lansweeper equips you with the tools to identify vulnerabilities across your network, but the next step is resolving those vulnerabilities. Lansweeper identifies three kinds of vulnerabilities: Software, Hardware, and OS.

Vulnerabilities may involve a combination of the Software, Hardware or OS categories. Read through the mitigation recommendations to learn how to resolve mixed vulnerabilities.   
Resolving vulnerabilities in one category might resolve the entire mixed vulnerability.

## Resolve software and OS vulnerabilities

1. Select the vulnerability you want to resolve.
2. In the **Summary**, check the **Patch info** tabs.

1. If the **Patch info** tabs contain links to external sources, follow the provided links and apply the necessary mitigation strategies.
2. If the **Patch info** tabs do not contain any information, check the **References** tab instead for mitigation recommendations.   
   Alternatively, you can wait until relevant patches or updates are detected by Lansweeper's sources.

If you don’t want to manually inspect each vulnerability in your systems, consider using a patch management tool instead. For more information on our cybersecurity integrations, check out [Lansweeper Integrates with your Tech Stack](https://www.lansweeper.com/product/integrations/).

### After resolution

After applying mitigation strategies, rescan the affected assets. During each rescan, Lansweeper re-evaluates the assets to check if the vulnerabilities have been resolved.

If a vulnerability has been mitigated, the asset will no longer be listed for that particular CVE.   
If it was the only affected asset, or if all affected assets have been fixed, Lansweeper will no longer show the CVE in your list of vulnerabilities, ensuring it remains accurate and current.

## Resolve hardware vulnerabilities

In the case of hardware vulnerabilities, the most effective solution may be to replace the affected hardware component entirely. Should the vulnerability be mixed, try resolving the other category first.

For example: a vulnerability can be categorized as both Hardware and OS at the same time. This indicates that the asset is vulnerable due to a specific OS version running on a particular hardware model. In such cases, patching the OS vulnerability could potentially resolve the entire vulnerability.

### After resolution

After applying mitigation strategies, rescan the affected assets. During each rescan, Lansweeper re-evaluates the assets to check if the vulnerabilities have been resolved.

If a vulnerability has been mitigated, the asset will no longer be listed for that particular CVE.   
If it was the only affected asset, or if all affected assets have been fixed, Lansweeper will no longer show the CVE in your list of vulnerabilities, ensuring it remains accurate and current.
