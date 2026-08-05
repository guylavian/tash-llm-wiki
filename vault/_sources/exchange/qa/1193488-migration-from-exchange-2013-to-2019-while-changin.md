---
title: "Migration from Exchange 2013 to 2019 while changing virtual directories URL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1193488/migration-from-exchange-2013-to-2019-while-changin
question_id: 1193488
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-exchange-other-l1"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Migration from Exchange 2013 to 2019 while changing virtual directories URL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1193488/migration-from-exchange-2013-to-2019-while-changin (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi, we are assisting one of our clients to migrate from Exchange 2013 to Exchange 2019.

Usually I would just install a new server, point DNS to the new server and move mailboxes then decommission the old server, like I've done before. The situation I have now is a bit unique and annoying. 

Server configuration: (as an example)

servername:  DCEX.company.com   (Primary Domain Controller AND Exchange 2013 on the same server)

Internal AND external virtual directory URLs for Outlook and mobile devices    dcex.company.com

servername:  DC02.company.com  (Second Domain Controller)

Plan on setting up new server:

servername:  MAIL.company.com  (Dedicated 2022 server with Exchange 2019 only)

The problem here is that I don't think I will be able to preserve the FQDN for exchange as all existing devices point to "dcex.company.com".   I cannot point the internal DNS records of "DCEX" to the new mailserver using that same name as I think this will break all sort of stuff domain related (authentication/dns).

Is there any way to add a second mailserver and just setup a completely different URL (mail.company.com) and have that coexist with the current Exchange 2013 server? I'm not sure this is possible.

I have never seen such a setup so I'm a little lost on what would be the best practice here. Any advice?

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-03-27*

Yep, that will work as well!:

https://techcommunity.microsoft.com/t5/exchange-team-blog/client-connectivity-in-an-exchange-2016-coexistence-environment/ba-p/603925

as far as the mobile devices, if you can't point to the new Exchange Server, then yes, users will need to update their profiles to access the new servers. Not elegant but it will work.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 1 · updated: 2023-03-27*

Sure, absolutely. 

For the new server, just ensure you have a valid trusted certificate applied with subject names that reflect the URLs on the 2019 client virtual directories and the Autodiscover SCP. 

Clients will find that new server and use it and as long as the cert is trusted, with no errors.

Ensure the new remote FQDNs are reachable externally as well
