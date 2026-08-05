---
title: "Best practice for upgrading Active Directory (AD) from Windows Server 2016 to windows 2022"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5930080/best-practice-for-upgrading-active-directory-ad-fr
question_id: 5930080
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
answer_author_roles: ["Independent Advisor"]
---
# Best practice for upgrading Active Directory (AD) from Windows Server 2016 to windows 2022

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5930080/best-practice-for-upgrading-active-directory-ad-fr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We plan to upgrade the OS of our 4 DC servers from win 2016 to win 2022, since there is no new functional level till win 2025, we remain on 2016 functional level.. 

We consider in-place OS upgrade and would like to know the absolute best practice for upgrading Active Directory (AD) from Win 2016 to Win 2022. We know Microsoft supports in-place upgrades, but we need your assessment for impact which include, least not to list, performance issues, TLS 1.3, Active Directory Certificate Services, FSMO, replication, LDAP, etc.

## Answer (community) — Independent Advisor

*upvotes: 0 · updated: 2026-06-25*

Hello Tarek Khalil,

It's recommended to avoid in-place operating system upgrades for Domain Controllers. The best practice is a swing migration, which involves deploying new Windows Server 2022 instances, transferring your Flexible Single Master Operations roles, and gracefully demoting the old 2016 servers. This demotion process safely removes the old server's metadata from the directory database at the CN=Configuration,DC=yourdomain,DC=com path, ensuring your topology remains free of orphaned replication partners. Promoting these new servers automatically updates your Active Directory blueprint, located at CN=Schema,CN=Configuration,DC=yourdomain,DC=com, to schema version 88. This happens seamlessly in the background to support modern attributes without altering your established 2016 functional level.

Transitioning to fresh 2022 servers inherently strengthens your environment by introducing native TLS 1.3 support. This protocol upgrade, managed within the system registry at HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols, ensures faster and highly secure LDAP communications by enforcing modern cryptographic standards. Additionally, deploying new servers guarantees that your SYSVOL directory, located at %SystemRoot%\SYSVOL which stores your Group Policy Objects, is synchronized using entirely uncorrupted Distributed File System Replication databases, completely bypassing the legacy bloat of an in-place upgrade.

If Active Directory Certificate Services currently resides on any of your domain controllers, you must separate this infrastructure during the transition. Upgrading the OS directly beneath a live Certificate Authority poses a severe risk of corrupting the database housed in the %SystemRoot%\System32\CertLog directory. You must back up this data and its configuration registry keys located at HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\CertSvc to safely migrate the role to a dedicated member server, keeping your directory identity services permanently isolated from your certificate infrastructure.

Domic
