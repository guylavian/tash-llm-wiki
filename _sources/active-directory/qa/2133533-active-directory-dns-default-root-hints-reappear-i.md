---
title: "Active Directory/DNS: Default Root Hints Reappear (in PowerShell only) After Removal on Some DCs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2133533/active-directory-dns-default-root-hints-reappear-i
question_id: 2133533
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Active Directory/DNS: Default Root Hints Reappear (in PowerShell only) After Removal on Some DCs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2133533/active-directory-dns-default-root-hints-reappear-i (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Background:

We have an Active Directory environment where all external DNS queries are strictly controlled. The configuration is as follows:

-  Domain Controllers (DCs) forward DNS queries to a central internal DNS server, which then forwards traffic to an external provider.

-  As a failsafe, we removed all default root hints and added custom root hints pointing to a specific external DNS server (e.g., OpenDNS).

In this setup, DCs should only send DNS traffic to:

-  The central internal DNS server (preferred path), or

-  The custom root hint server if the forwarder becomes unavailable.

Problem:

Our InfoSec team flagged that some DCs are sending DNS queries to external servers that are not part of our intended configuration. Upon investigation, I observed an unexpected behavior:

-  DNS Manager GUI: Shows only the manually configured custom root hints (correct).

-  PowerShell (`Get-DnsServerRootHint`): Shows both the custom root hints and the default root hints that were previously removed.

-  Restarting the DNS Server service does not resolve the issue.

-  If I use `Remove-DnsServerRootHint` to delete the default root hints, PowerShell reflects only the custom root hints. However, after restarting the DNS Server service, the default root hints reappear, again, only in PowerShell, not in the GUI.

-  This behavior occurs only on some DCs. Other DCs behave correctly, where both the GUI and PowerShell show only the custom root hints and all DCs have the cache.dns file present.

Questions:

-  What mechanism is causing the default root hints to return?

-  Are these default root hints being used and , even though they do not appear in the GUI?

-  Why do the default root hints only show in PowerShell (`Get-DnsServerRootHint`) and not in the GUI?

-  Why does this behavior occur on only some DCs and not all? 

-  Ultimately, how do I fix this and ensure only the custom root hints are active?

Additional Notes:

According to the official documentation, replacing root hints should be permanent. Note, the article is about root hints returning when all are removed, but that is a different issue.  I'm trying to replace them with others.

"When you replace root hints, the change is permanent, and the old root hints do not reappear." Reference: Root Hints Reappear After Removal

I found a similar unresolved issue from 2020 but without a resolution.

Environment:

-  Active Directory-integrated DNS

-  Custom root hints configured via DNS Manager GUI

-  Default `cache.dns` file exists on all DCs

Thank you in advance for your insights and guidance!

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-05-08*

My configuration has changed so this post is no longer relevant.  No correct answer could be determined to original question.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-12-20*

Hello,

 

Thank you for posting in Q&A forum.

To further troubleshoot this issue, please kindly try below steps:

1.Check if the domain replication service is running and the configuration change is replicated to all DCs in the domain.

2.The default root hints could be restored by the cache.dns file. Please check the contents of the cache.dns file located in C:\Windows\System32\dns on each DC and ensure that it doesn't contain any old root hints.

3.Check if there's any registry settings that could impact the DNS setting under path: HKLM\System\CurrentControlSet\Services\DNS\Parameters

HKLM\System\CurrentControlSet\Services\DNS\RootHints

 

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

 

Best regards，

Jill Zhou

 

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-12-19*

Hi,

Have you tried a configuration as covered in here?  

https://learn.microsoft.com/en-us/windows-server/networking/dns/quickstart-install-configure-dns-server?tabs=gui

Configure forwarder instead of custom root hint(s)

Configure forwarder clear "Use root hints if no forwarders are available" in the Forwarders tab

Make sure your forwarder targets are HA/redundant/always accessible 

HTH.
