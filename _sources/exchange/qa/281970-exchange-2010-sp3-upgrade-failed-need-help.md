---
title: "exchange 2010 sp3 upgrade failed need help"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/281970/exchange-2010-sp3-upgrade-failed-need-help
question_id: 281970
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# exchange 2010 sp3 upgrade failed need help

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/281970/exchange-2010-sp3-upgrade-failed-need-help (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All I tried to do a Exchange 2010 SP3 upgrade on an old SBS2011 Standard box so I can move user mailboxes to 365 but it failed during the upgrade   

It gets to the Language files install ( one before restoring services) and it keeps failing with errors about not finding different 521e6064-b4b1-4cbc-0401-25ad697801fa   

 tried to install all the language files for the sp2 and sp3 language pack download but both say that i am not allowed to install please use add remove programs exchange install, if i run that it just goes back to the sp3 install  

I think a previous admin removed the windows\installer folder contents which this install is looking for been trying to resolve this for 14 hours flat with no success I just seem to be going around in one big circle   

any advice would be great Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-22*

Hi, @Rob Andrews      

I think a previous admin removed the windows\installer folder contents    

According to this document: Missing Windows Installer cache requires a computer rebuild    

I suppose you may have to reinstall the operation system of the server or use some third-party tools to recover the windows\installer folder caches.    

Since the Exchange server should be working fine, I think you may install exchange 2010 SP3 on a new device and migrate the mailboxes (including system mailboxes) to the new server.    

You may also need to configure the virtual directories, DNS records to point to the new server.    

It is suggested to turn off the old server for a few days to check if everything is working fine.    

After that you may decommission the old server and prepare to move to Office 365.    

Besides, you may also restore the databases from windows server backup on a new exchange 2010 server or use /Mode:RecoverServer to recover the server on a new device.    

If there aren't many user mailboxes, export/import pst files would also work fine.    

Anyway, I suppose a new device is needed (to install a new Exchange 2010 server or recover the old server)     

Here are some related documents for your reference:     

Using Windows Server Backup to back up and restore Exchange data    

Use Windows Server Backup to restore a backup of Exchange    

Recover Exchange servers    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
