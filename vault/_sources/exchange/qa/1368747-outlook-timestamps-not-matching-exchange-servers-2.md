---
title: "Outlook timestamps not matching [Exchange servers:2010/2013]"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1368747/outlook-timestamps-not-matching-exchange-servers-2
question_id: 1368747
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Outlook timestamps not matching [Exchange servers:2010/2013]

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1368747/outlook-timestamps-not-matching-exchange-servers-2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

 

I was wondering if an Exchange engineer/expert can assist? Unless you have enterprise support, Microsoft's support has lost it's quality.

Details

Exchange servers:2010/2013

Shared mailbox

Email sent from Gmail to Outlook, same country, same time zone. 

 

Moving forward, question: Why sometimes Outlook timestamps do not match? In specific, an email's header timestamp is different from the opened email timestamp? Would the email's header timestamp indicate when it was opened or selected at that time?

 

Another question: Once an externally sent email reaches the Exchange server, is it technically in the inbox of the recipient? If so, which timestamp would be referenced if they did not match and there was a submission deadline?

 

Example: Deadline is 11:59; email's header timestamp is 12:00-past deadline, but when the email is opened the timestamp is 11:59-on time.

 

Which is technically correct? And how could something like this happen?

 

Also, how helpful would the email audit log for the email would be in a situation like this?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-09-15*

Hi @KL_99  ,

Moving forward, question: Why sometimes Outlook timestamps do not match? In specific, an email's header timestamp is different from the opened email timestamp? Would the email's header timestamp indicate when it was opened or selected at that time?

Do you mean the timestamp in the message list is different from the timestamp when you open the message? Like the image below?

If this is what you are talking about, it's actually the expected behavior as the timestamp shown in the message list pane is the "Received time" while the one in the opened mail is the "Sent time".  This can be told by switching to Preview view and adding the Sent item field:  

Add columns in Inbox  

Email's header timestamp wouldn‘t indicate the opened or selected time.

Another question: Once an externally sent email reaches the Exchange server, is it technically in the inbox of the recipient? If so, which timestamp would be referenced if they did not match and there was a submission deadline? 
Example: Deadline is 11:59; email's header timestamp is 12:00-past deadline, but when the email is opened the timestamp is 11:59-on time.

External mail reached the Exchange server doesn't mean it's in the Inbox. If you have the interest to learn more about the details of how an externally sent mail gets delivered to a user's Inbox, you can read the article below:  

Exchange 2013 Mail Flow Demystified…Hopefully!  

The purple lines in the following diagram give us a general idea of the whole procedure. The first line means it reaches your Exchange server, the last line means the mail is put into the user's mailbox.  

When it comes to the sample you provided, it really depends on how you define the "deadline", the time a message is sent or the time it's finally received. "when the email is opened the timestamp is 11:59-on time" means the sender sent the email on 11:59, so if the sent time counts, this mail has met the deadline : )

Also, how helpful would the email audit log for the email would be in a situation like this?

By "email audit log", are you referring to the message tracking log as described in this official document. Personally, I don't think it's necessary to utilize the message tracking logs in this scenario, but if you do want to check it, you can adapt the command below to fit your situation to see the timestamp of each event occurred in your Exchange servers:

```
Get-TransportServer | Get-MessageTrackingLog -MessageSubject  -Start "09/15/2023 10:00AM" -End "09/15/2021 11:00AM" | Sort-Object timestamp | ft timestamp,Sender,Recipients,EventID,MessageSubject -AutoSize
```

Hope the above can be helpful.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
