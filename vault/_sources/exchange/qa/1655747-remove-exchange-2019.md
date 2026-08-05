---
title: "Remove Exchange 2019"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1655747/remove-exchange-2019
question_id: 1655747
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-other-l1", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Remove Exchange 2019

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1655747/remove-exchange-2019 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I had exchange 2019 in my network, but for some reason, I had to install a new exchange 2019 in my network and all mailboxes moved from the previous exchange to the new exchange. the previous exchange has been powered off for some months. so how can I delete the previous exchange from my network and AD without destroying my new exchange?

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2024-04-15*

Hi @Hossein Zakeri  ,

Since you have powered off the previous exchange for some months. Then there are some steps you should do next to remove your previous exchange:

-Start by reviewing the Best Practices section of Upgrade Exchange to the latest Cumulative Update, as they also apply when uninstalling Exchange (e.g., reboot the server before and after running Setup, disable antivirus, etc.).

-Remove health mailboxes

-Uninstall Previous Exchange 

Before you begin the uninstall process, close EMS and any other programs that might delay the uninstall process (e.g., programs using .NET assemblies, antivirus, and backup agents). The uninstall Exchange using either of these recommended methods (we do not recommend using Control Panel):

-  Use the unattended setup mode: Setup.exe /mode:Uninstall

-  Run Setup.exe from the setup file location.

-Perform post-uninstallation tasks:

-  Removing the previous Exchange computer accounts from Active Directory (including the DAG’s Cluster Name Object and Kerberos ASA object).

-  Removing the previous Exchange servers as targets to other services (e.g., backup software, antivirus/security agents, network monitoring).

-  Removing previous Exchange name records from DNS.

-  Ensuring the folder on the DAG’s file share witness (FSW) servers were successfully removed.

-  Removing the Exchange Trusted Subsystem from the FSW servers’ local Administrators group unless these servers are witnesses for other DAGs.

-  Removing old firewall rules that open ports to previous Exchange environment.

-  Removing and disposing of the previous Exchange environment’s physical equipment.

-  Deleting any previous Exchange virtual machines.

You can refer to the documentation linked below for more information: https://techcommunity.microsoft.com/t5/exchange-team-blog/decommissioning-exchange-server-2013/ba-p/3613793.If you have any questions, please feel free to contact me.
