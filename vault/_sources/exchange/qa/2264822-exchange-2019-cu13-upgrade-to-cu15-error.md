---
title: "Exchange 2019 CU13 upgrade to CU15 error...."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2264822/exchange-2019-cu13-upgrade-to-cu15-error
question_id: 2264822
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange 2019 CU13 upgrade to CU15 error....

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2264822/exchange-2019-cu13-upgrade-to-cu15-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We currently have two exchange servers 2019 on CU13. I am trying to upgrade to CU15 so we can prepare to migrate to Exchange Online in a hybrid mode. 

My user that is installing it, is part of the Enterprise Admins and part of the Scheme Admins.

I am running it from the command line as to not enable extended protection. So the command i am using is  E:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataON /Mode:Upgrade /DoNotEnableEP

And it starts the process and then errors out. I ran the setup.exe /PrepareAd and it errors out at the same location.

Below is end of the error log. I only pasted the part from where the error starts, if need more let me know. It appears that it has an issue with our Organization Management Security group. This group was created when we setup exchange last year in this new domain. The groups were not moved and are in the default location, Domain>Microsoft Exchange Security Groups>Organization Management

So need some help. 

Start of Log:

[05/09/2025 02:29:22.0708] [2] [ERROR] Active Directory operation failed on DomainController.AdDomainName.registereddomainname.xyz. One or more attribute entries of the object 'CN=Organization Management,OU=Microsoft Exchange Security Groups,DC=AdDomainName,DC=registereddomainname,DC=xyz' already exists.

[05/09/2025 02:29:22.0709] [2] [ERROR] The object exists.

[05/09/2025 02:29:22.0716] [2] Ending processing initialize-ExchangeUniversalGroups

[05/09/2025 02:29:22.0719] [1] The following 1 error(s) occurred during task execution:

[05/09/2025 02:29:22.0719] [1] 0.  ErrorRecord: Active Directory operation failed on DomainController.AdDomainName.registereddomainname.xyz. One or more attribute entries of the object 'CN=Organization Management,OU=Microsoft Exchange Security Groups,DC=AdDomainName,DC=registereddomainname,DC=xyz' already exists.

[05/09/2025 02:29:22.0720] [1] 0.  ErrorRecord: Microsoft.Exchange.Data.Directory.ADObjectEntryAlreadyExistsException: Active Directory operation failed on DomainController.AdDomainName.registereddomainname.xyz. One or more attribute entries of the object 'CN=Organization Management,OU=Microsoft Exchange Security Groups,DC=AdDomainName,DC=registereddomainname,DC=xyz' already exists. ---> System.DirectoryServices.Protocols.DirectoryOperationException: The object exists.

I have more of the log if needed later to view or discuss. 

Thank you all in advance

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2025-05-09*

Is the ""Microsoft Exchange Security Groups" OU in a different spot? Did you move it at some point?
