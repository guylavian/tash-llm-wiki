---
title: "Is safe to install or upgrade exchange online powershell v2 or higher on exchange 2013 server itself to run Sync-ModernMailPublicFolders.ps1?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1282198/is-safe-to-install-or-upgrade-exchange-online-powe
question_id: 1282198
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online"]
answer_author_roles: ["Microsoft Moderator"]
---
# Is safe to install or upgrade exchange online powershell v2 or higher on exchange 2013 server itself to run Sync-ModernMailPublicFolders.ps1?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1282198/is-safe-to-install-or-upgrade-exchange-online-powe (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

During migration from exchange 2013 last CU. (I know, I know I'm trying to hurry) to EO, I need to run Sync-ModernMailPublicFolders.ps1 to support PFs temporarily as I migrate the remaining mailboxes. The script requires I run it in exchange management shell on the server itself. It also appears this should just work out of the box, but it doesn't.

https://learn.microsoft.com/en-us/exchange/hybrid-deployment/set-up-modern-hybrid-public-folders#step-3-configure-exchange-online-users-to-access-exchange-server-on-premises-public-folders

```
Checking for mail-enabled System folders...

Getting all public folders. This might take a while...

Found 18 public folders.

17 of those are mail-enabled.

0 folders are mail-enabled with no AD object.

17 folders are mail-enabled and are properly linked to an existing AD object.

No folders need to be mail-disabled.

No orphaned MailPublicFolders were found.

No duplicate MailPublicFolders were found.

No mail-disabled public folders with proxy GUIDs were found.

No disconnected MailPublicFolders were found.

Done!
```

I get this error with a typo (authenticaion).

WARNING: [5/10/2023 7:21:12 AM] This script uses modern authenticaion to connect to Exchange Online and requires EXO V2 module to be installed. Please follow the instructions at

https://docs.microsoft.com/powershell/exchange/exchange-online-powershell-v2?view=exchange-ps#install-the-exo-v2-module to install EXO V2 module.

This url conflicts with other information microsoft provides about which module can be installed with which PSVersion:

"All versions of the module are supported in Windows PowerShell 5.1."

ExchangeOnlineManagement 3.1.0
Minimum PowerShell version
3.0

$psversiontable

Name                           Value

PSVersion                      4.0

WSManStackVersion              3.0

SerializationVersion           1.1.0.1

CLRVersion                     4.0.30319.42000

BuildVersion                   6.3.9600.20713

PSCompatibleVersions           {1.0, 2.0, 3.0, 4.0}

PSRemotingProtocolVersion      2.2

```

```

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-05-11*

Hi @Dee Bukkus  ，

Is safe to install or upgrade exchange online powershell v2 or higher on exchange 2013 server itself to run Sync-ModernMailPublicFolders.ps1?

Yes, you can go ahead.

I haven't seen that it will do any harm to install or upgrade Exchange Online PowerShell module on Exchange server 2013. And you can always choose to uninstall the module if necessary. See About the Exchange Online PowerShell module.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
