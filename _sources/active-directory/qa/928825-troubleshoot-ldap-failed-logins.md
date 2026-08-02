---
title: "Troubleshoot LDAP failed logins"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/928825/troubleshoot-ldap-failed-logins
question_id: 928825
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Troubleshoot LDAP failed logins

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/928825/troubleshoot-ldap-failed-logins (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

our company has purchased custom intranet site on VPS remote server, they have our one domain user configured for LDAP queries, because we should login to this site using domain credentials, they synced every of our domain users without problem but we cannot login.    

I see on central router logs that queries are hit our domain controller on 636 port (LDAPS) but we getting credentials failed when trying to login using AD credentials.    

Is any way on domain controller in event viewer to see if there are ldap failed logins, because I see many events like 4625, or 4771 but none of them incoming from remove VPN intranet server?    

Thanks for any help.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-07-18*

Hi @Tutek   Try this    

Enable LDAP auditing    

Open Registry Editor. Go to HKEY_LOCAL_MACHINE → SYSTEM → CurrentControlSet → Services → NTDS → Diagnostics. Note: Set '15 Field Engineering' to '5'. This enables Expensive and Inefficient LDAP calls to be logged in Event Viewer.    

Error from LDAP server     

Go to Event Viewer → Filter Directory Service logs to locate the event ID 1535 (Windows Server 2003 to 2012)    

Time-out LDAP connection     

Go to Event Viewer → Filter Directory Service logs to locate the event ID 1317 (Windows Server 2003 to 2012)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-16*

We have allowed 636 LDAP traffic from remove VPS to domain controller, I don't think we need to allow any traffic from AD do VPN. Routers are stateful so it recognize that receiving packets are part of existing and permitted connections.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-16*

By any chance is any return traffic getting blocked in your router / firewall?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-07-16*

Hi,    

Have a look at this post on troubleshooting LDAPS connectivity issues.    

https://nettools.net/howto-troubleshoot-ad-ldaps-connection-issues/    

Gary.
