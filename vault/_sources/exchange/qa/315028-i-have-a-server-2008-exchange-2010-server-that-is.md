---
title: "I have a Server 2008 exchange 2010 server that is also a domain controller how can I get past this catch 22?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/315028/i-have-a-server-2008-exchange-2010-server-that-is
question_id: 315028
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# I have a Server 2008 exchange 2010 server that is also a domain controller how can I get past this catch 22?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/315028/i-have-a-server-2008-exchange-2010-server-that-is (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Server 1: Server 2008 exchange 2010 AD 2008 DC Attempting to add Server 2 Server2016 Exchange 2016 Member Server of 2008 AD How can I install Exchange 2016 and move my 2010 databases when Since CU 6 I need the domain level to be 2008r2 to install Exchange 2016 CU 16 which is all I have. I either need Exchange 2016 cu5 or some other solution? Can anyone help? I would be very grateful. The 2010 server is very busy and cannot be down u till the new server is up and running.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-16*

Hi @GiantProblems  ,    

Considering that you are still running Windows Server 2008, according to the supportability matrix, you would need Exchange 2016 CU 6 or earlier:    

    

That being said, please also make sure the following co-existence requirements are met before Exchange 2016 is introduced into the existing environment:    

-  The Exchange 2010 server has been updated to at least SP3 with Update Rollup 11 installed. It's recommended to install the latest Update Rollup 30 for SP3 and apply the latest security update KB5000978.    

-  The Outlook clients are upgraded to Outlook 2010 or above on Windows and Outlook 2011 or higher on the Mac.    

For step-by-step guidance to install Exchange 2016 in Exchange 2010 coexistence, here are some articles for your reference:    

Install Exchange 2016 in Exchange 2010 Co-existence    

EXCHANGE 2010 TO EXCHANGE 2016 MIGRATION     

Please Note: Since the second web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Additionally, the Exchange Deployment Assistant tool is highly recommended for the migration. The web-based tool asks you a few questions about your current environment and then generates a custom step-by-step checklist for you to deploy Exchange server. Hopefully you can find it be of help.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
