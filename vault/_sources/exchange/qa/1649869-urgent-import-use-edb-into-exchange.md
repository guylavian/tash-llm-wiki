---
title: "URGENT: Import/Use EDB into Exchange"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1649869/urgent-import-use-edb-into-exchange
question_id: 1649869
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# URGENT: Import/Use EDB into Exchange

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1649869/urgent-import-use-edb-into-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Due to catastrophic server damage, we have lost virtually all our data. Luckily, i recently backed up (just copied it to another drive that didnt fail) the edb file from our exchange server, so we only lost a few days of emails at best. The old Exchange server was running Exchange 2012 on a 2012 server iirc. Now i'd like to use exchange 2019 on Windows Server 2022.

Is it possible to "just" use the edb? How would i go about that? What precautions need to be taken?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-04-15*

Database would mount only on the Exchange server version it was created on. No “cross-version” mount possible. You would have to deploy Exchange server 2010 or 2013, restore database and only then migrate. Also check following link for the same.

Alternatively creating a new mail database on the new server in ECP and then convert offline edb file to pst. use 3rd party tools to extract data. 

Please Note: Since the web sites are not hosted by Microsoft, the links may change without notice. Microsoft does not guarantee the accuracy of this information.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2024-04-08*

You cant upgrade to 2019 using just the database. I assume you mean Exch 2013 or Exch 2010 is what you are running now?

If the database is in a clean shutdown state, you can recover the server running the same Exch Version and CU and same Windows O/S and drop the database in same drive structure and it should work:

https://learn.microsoft.com/en-us/exchange/recover-an-exchange-server-exchange-2013-help

Or you can use database portability and mount on another server running the same version of Exchange:

https://learn.microsoft.com/en-us/exchange/database-portability-exchange-2013-help

Or purchase 3rd party software to recover.

Once recovered, then you can upgrade.
