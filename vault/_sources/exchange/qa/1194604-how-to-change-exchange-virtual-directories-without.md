---
title: "How to change Exchange Virtual Directories without reconfiguring Outlook clients?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1194604/how-to-change-exchange-virtual-directories-without
question_id: 1194604
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
---
# How to change Exchange Virtual Directories without reconfiguring Outlook clients?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1194604/how-to-change-exchange-virtual-directories-without (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm planning some changes to an exchange setup at one of our clients.

They want to migrate from Exchange 2013 to Exchange 2019.

The FQDN they use for Exchange 2013 internal and external has a wildcard SSL certificate, naming is  "server1.company.com"

The issue now is that the FQDN used for Exchange is also used for various other services as someone in the past installed all sort of other tools and services on the Exchange 2013 server itself.

This prevents me from simply pointing the FQDN to a new Exchange 2019 server and move mailboxes as this will break many other tools in the domain that also connect to "server1.company.com"

The plan we have for now is to first reconfigure Exchange 2013 to use a brand new URL like "mail.company.com"  I know how to change the Virtual Directories but I'm struggling to find how this will impact all existing connections from Outlook to "server1.company.com". Is there a way to trick Outlook to update to "**mail.**company.com" without me having to reconfigure all Outlook profiles?

The idea is that if this is successful, we can then install the new Exchange 2019 in the domain and point this new DNS record to the Exchange 2019 server.  The old "server1.company.com" will still work for services remaining there, and the email will be separate accessible using "mail.company.com"

The client wants me to find the least annoying for their existing users.. Any tips on this?

## Answers

_No answers on this thread._
