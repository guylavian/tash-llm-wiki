---
title: "Exchange 2019 Sporadically Sends and Receives"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1366602/exchange-2019-sporadically-sends-and-receives
question_id: 1366602
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 Sporadically Sends and Receives

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1366602/exchange-2019-sporadically-sends-and-receives (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello everyone and thanks for the help in advance.  I have a stand-alone Exchange 2019 server running on Windows Server 2022.  The server has been operating fine until a few days ago when mail flow began sporadically stopping then restarting.  There have been no changes to hardware, nor has there been any system updates.  I have restarted the FrontEnd Transport service, however, this does not correct the problem.  The mail flow problems are system wide and are not domain specific.  Internal emails are not delivered.  However, after a few hours, the mails flow miraculously begins until the next stoppage.  I not an Exchange expert, so I am not sure where to go form here.  Any help would be appreciated.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-10-23*

OK.  After a lot of sifting through documentation, it appears Exchange doesn't like external DNS servers being used on the Exchange box.  I found the DNS servers on the Exchange server were both pointing to external DNS servers and not to the domain  controller.  Once I changed this, mail flow began working  perfectly.  I guess my only question  is why this would have become an intermittent problem after the server had been working correctly, and then only an intermittent issue.  But in any event, problem solved.  Thanks to everyone for their help.  I appreciate it.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-13*

Hi @Kmcnet    

1.Are all your exchange services up and running?

Check with this command: `Get-Service | Where-Object {$_.Name -Like ‘MSExchange*’ -and $_.Status -eq ‘Stopped’}`

2.Does the database space have at least 10 percent free space? You can use the following command to view:

`Get-MailboxDatabase -Status | select Name, DatabaseSize, AvailableNewMailboxSpace`

3.Check the event log or message tracking log for clues.

You mentioned that the internal email was not delivered, check if the sender received a non-delivery report?

Regards

Shaofan

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".   

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
