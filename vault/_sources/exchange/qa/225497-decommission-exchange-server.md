---
title: "Decommission Exchange Server"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/225497/decommission-exchange-server
question_id: 225497
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Decommission Exchange Server

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/225497/decommission-exchange-server (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can I decommission Exchange Server with MailUsers in it and without disabling mailusers? If yes, what would happen to attributes of those mail users after decommissioning Exchange Server?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-11*

Thanks for the reply.   

I was working on decommissioning last Exchange Server after migrating all users to Exchange Online.  I converted Remote users mailbox to Mail users.  

I confirmed that we do not need to disable MailUsers and Mail Contacts to decommission the Exchange on-premises server. The mail attributes for Mail users and mail contacts stay "as-is" after clean decommissioning of Exchange server.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-11*

Sorry, not sure I am following your question, as logically what your saying doesn't make sense.  If you have mailboxes operational on the Exchange server and decommission the exchange server those mailboxes are not going to be accessible.  

Search, Recover, & Extract Mailboxes, Folders, & Email Items from Offline Exchange Mailbox and Public Folder EDB's and Live Exchange Servers or Import/Migrate direct from Offline EDB to Any Production Exchange Server, even cross version i.e. 2003 --> 2007 --> 2010 --> 2013 --> 2016 --> 2019 --> Exchange Online with Lucid8's DigiScope
