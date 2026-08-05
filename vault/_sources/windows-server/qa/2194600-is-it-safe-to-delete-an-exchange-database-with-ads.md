---
title: "Is it safe to delete an exchange database with ADSI edit?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2194600/is-it-safe-to-delete-an-exchange-database-with-ads
question_id: 2194600
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-other"]
---
# Is it safe to delete an exchange database with ADSI edit?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2194600/is-it-safe-to-delete-an-exchange-database-with-ads (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

At some point in the past a database called Arbitration was created in our Exchange environment.  Our current installation is Exchange 2016.  If we go to the Exchange Amin Center and go to Sever, then databases, the list is blank.  If we run Get-MailboxDatabase in the Exchange Management Shell we get an error...

"The Exchange server for the database object "Arbitration" wasn't found in Active Directory Domain Services. The object may be corrupted."

I can find this Arbitration database in ADSI Edit, but it is pointing to an old server that was decommissioned and recycled.  Is it safe to delete it in ADSI or to change the sever it's pointing to in ADSI, to one of our current servers?  Is it better to delete something like this or try to get it working again.  I'm assuming with the errors and the fact that it has been pointing to a server that is not in service for years that the database isn't working or doing it's job.  And help or advice would be appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-24*

I tried submitting the question again, but this time I used Firefox.  I was able to complete the process.  Thanks!

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-24*

Thanks Yanhong.  I followed the link and filled out the information.  When I clicked to post it, I got a robot challenge, which I successfully passed, and then I got a 404 Page not found error message.  I'll check it a little later and see if my question is there or not.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-12-23*

Hello,

Thank you for posting in Microsoft Community forum.

From the description above, I understand your question is related to Microsoft Exchange.

Since there are no engineers dedicated to Microsoft Exchange in this forum. In order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.

Ask a question - Microsoft Q&A

Click the "Ask a Question" button in the upper right corner to post your question and type "Microsoft Exchange" tag and select any tags related to your productions.

I hope the information above is helpful.

Best Regards,

Yanhong Liu
