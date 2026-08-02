---
title: "Exchange 2016 to 2019 internal mail wont flow under if ...."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1013444/exchange-2016-to-2019-internal-mail-wont-flow-unde
question_id: 1013444
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
---
# Exchange 2016 to 2019 internal mail wont flow under if ....

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1013444/exchange-2016-to-2019-internal-mail-wont-flow-unde (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Have Exchange 2016 servers and now 2 (so far) 2019 servers, all up to date, with most things pointing to mail.domain    

I have 2 MB's now moved to the 19 servers and both MB's now have the same symptom. All the below is internal to internal    

when users send to the 19 mailboxes, some emails show and some dont, when they dont come through I have asked the user to send it to me directly from the GAL and then it comes through.     

the 2 19 MB's can send to each other except if they reply to an email that was before the move to the 19 server and then it doesnt come through (yes we do have X400 addresses but they dont appear to have been changed)    

Think i would prefer no mail to come through than some mail as its really hard now to understand why, but obviously i'm missing something that will explain this.    

Anyone have any ideas?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-30*

It turned out It was the antimalware bug, and as such getting stuck in the Queue    

Turning it off instantly fixed the problem, just really bad timing getting caught with this during a migration, which had me heading in the wrong direction.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-20*

Hi @Daryl Davis  ,    

Thanks for your sharing!    

Great to know that you've already thought of a solution and really appreciate it for your sharing!    

By the way, since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others." and according to the scenario introduced here: Answering your own questions on Microsoft Q&A    

I would make a brief summary of this thread:    

[Exchange 2016 to 2019 internal mail wont flow under if ....]    

Issue Symptom:    

There are Exchange 2016 servers and now 2 (so far) 2019 servers, all up to date.    

I moved 2 mailboxes to Exchange Server 2019, and the internal mails in these two mailboxes have the following symptoms:    

- 	When users use GAL to send messages from Outlook to my Exchange 2019 mailbox, the emails will never come through. (User not using cache mode).    

- 	The 2 19 MB's can send to each other.     

However, if the user replies to an old email that was moved to the 19 server before, the email never come through.    

The Solution:    

For symptom one, the user created a new profile and sent email using GAL, then the email worked.    

For symptom two, had user reply to the same email and remove my name and replace it from GAL,  then the email worked.    

Besides, here are some of my thoughts and troubleshooting, hoping to help you:    

When sending a message to a user, if there is a copy of the email in the sender's "Outbox", it means that Outlook is not configured to send correctly, or Exchange is not configured to accept correctly. There may be a problem with the Receive connector, and it is recommended that you check the Receive connectors on Exchange Server 2019.    

exchange-2016-internal-mail-flow-not-working    

exchange-2016-emails-not-sending    

After you move mailboxes, you might still try to access the mailbox from the old server. Therefore, when you recreate the profile, it works.    

In addition, you can refer to the following articles to learn more about it.    

impact-of-deleting-x500-and-x400-address-in-mailbox-profile    

1642182-can-t-send-email-to-address-in-gal    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-19*

More info.  Just had someone when sending from Outlook to my 19 Mailbox and using the GAL, email never come through. (User not using cache mode)    

User created a new profile and sent email using GAL and it now worked.    

Got user to reply to an old email and email never come through    

Had user reply to the same email and remove my name and replace it from GAL and it then come through    

Hope this helps someone
