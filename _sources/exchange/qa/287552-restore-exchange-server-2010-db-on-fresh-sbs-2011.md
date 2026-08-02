---
title: "Restore Exchange Server 2010 DB on fresh SBS 2011 installation."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/287552/restore-exchange-server-2010-db-on-fresh-sbs-2011
question_id: 287552
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Restore Exchange Server 2010 DB on fresh SBS 2011 installation.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/287552/restore-exchange-server-2010-db-on-fresh-sbs-2011 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello. Yes, you read correctly. I have been asked to restore a client's mailbox from their old "Exchange 2010" database on Small Business Server, which yes, they are still using to this day. Their SBS 2011 crashed and their backups are corrupt. They have a separate backup that has the EDB on it. Search as I might, I can't find a way to do this without having the original server intact and available in the same forest. Any help would be greatly appreciated. Kind Regards Hentie

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-25*

Hi, Hentie.    

I would suggest recovering the server via using the Setup /m:RecoverServer command.    

It will use the information in the active directory.     

You may need a new hardware which runs the same operation system as the lost server.    

And the new hardware needs to be named the same name as the lost server and needs all the prerequisites installed on it.     

About more detailed information, please refer to these Microsoft documents:    

Recover an Exchange Server    

Exchange 2010 System Requirements    

Exchange 2010 Prerequisites    

After the recovery succeed, you may restore the database on the new server from the backup.    

About the detailed steps, please refer to this Microsoft document:    

Use Windows Server Backup to Restore a Backup of Exchange    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-02-24*

I actually found myself in that same situation but about 6 years ago ;-)  

Although you could try to repair the database and attempt to restore it in a clean environment (that matches the old one at some crucial levels), it is very labor intensive with quite a bit of trial and error involved. The chances of success are also not guaranteed so you could just be wasting a lot of time.  

I ended up purchasing a 3rd party recovery tool to export the mailboxes to pst-files which I then recovered to a new Exchange environment (in this case Exchange Online). Although these tools don't come cheap, for this case it actually was cheaper than putting in the work and the high risk of failing still. There also wasn't any real hardware around to construct a recovery environment either.  

FWIW: I ended up using Kernel for Exchange Server but there are also other tools such as Stellar Repair for Exchange. If you do go the 3rd party route, make sure you first try it out with the trial software first to make sure the tool is suited for your type of data corruption.
