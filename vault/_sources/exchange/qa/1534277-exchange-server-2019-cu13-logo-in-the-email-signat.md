---
title: "Exchange Server 2019 CU13 - Logo in the Email signature added as an attachment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1534277/exchange-server-2019-cu13-logo-in-the-email-signat
question_id: 1534277
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
---
# Exchange Server 2019 CU13 - Logo in the Email signature added as an attachment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1534277/exchange-server-2019-cu13-logo-in-the-email-signat (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All, 

We are testing Code Two signature solutions in Exchange server 2019 CU13, what we have noticed the mails sent from the outlook for IOS and Owa client to any external recipients (Gmail and other external domains) , received the mail which has signature applied on it, but the Logo in the Email signature was being added as an attachment in the received mail

Please note this is not happening when we use the outlook for IOS and Owa client to send mail to any internal recipient (the mailbox from the same senders domain)

I initially suspect, the Email gateway solutions is doing some changes in the mail sent to the External recipients, So i enabled transport pipeline logs, then verified the routing0001.XML logs, these logs confirms the logo is added as an attachment when the mail is processed in the Exchange server itself.

I verified the headers of the mails sent to external recipients, found the below.

Content-Type: multipart/related;

boundary="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
	type="text/plain"
There are two things i need to understand

-  Why this is not happening when the mail is sent to the internal recipient ?

-  How can i fix this behavior for the external recipients ?  please share your thoughts and notice me if i am missing anything here

I am planning to add one of the external domain in the remote domain list, then set the TNEFEnabled to false to see if that helps me.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-20*

Hi @Nithyanandham Singaravadivelu  ,
This is a common email signature-related problem, regardless if you use an email signature management software or not. This article shows possible reasons for such behavior and explains how to solve the problem.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-19*

Hi @Kai Yao  , Any suggestions that you have on the above mentioned issues, We are not using Code Two solutions, which is already removed from the exchange servers.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-16*

Hi  @Kai Yao  
Thank you for your response, I have removed the Code two solutions from the Exchange servers, then i did the very simple test.I have manually added the signature along with the logo in the owa through settings ->Options -> Layout-> Email signature 

Then i did two different tests

-  Sent one mail to internal recipient, where i don't see the logo being added as as an attachment in the mail received by the internal recipient.  

-  Sent one mail to the external recipient, I have seen the logo being, where i see the logo being added as as an attachment in the mail received by the external recipient.

Could you please let me know if you have any ideas on this ?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-02-16*

Hi @Nithyanandham Singaravadivelu  

Kindly note that since Code Two signature is a third-party solution, we may not be very familiar with it.

For further investigation please contact Code Two support for help.

Thanks for your understanding.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
