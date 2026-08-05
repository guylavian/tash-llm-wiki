---
title: "Exchange 2016 mailbox user can not use Outlook client."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1011926/exchange-2016-mailbox-user-can-not-use-outlook-cli
question_id: 1011926
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 mailbox user can not use Outlook client.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1011926/exchange-2016-mailbox-user-can-not-use-outlook-cli (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a Exchange Server 2016. My mailbox user access their mail via web. but recently I want to let them use Outlook client(outlook 2016,2013) but when the user create a new profile it always asking for a password or if somehow it connect he outlook window appear loading stage but not open.    

I have tried many solution like changing outlook anywhere settings from Exchange Admin center , installing different version of outlook ,changing device. But the issue remain same for all of the tried action.     

What is your expertise opinion on that. please suggest me what workaround should I follow on this.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-19*

Check this MS article for help - https://learn.microsoft.com/en-us/previous-versions/office/exchange-server-2007/gg263433(v=exchg.80)?redirectedfrom=MSDN

## Answer (community) — community member

*upvotes: 0 · updated: 2022-09-19*

Hi @Hriday Saha  ,    

Is there any error returned when unable to open Outlook?    

Please use ExRCA to test the Outlook connection and check if there are any errors.    

Or use Test-OutlookConnectivity to test the connection between client and Exchange server.    

Try editing the authentication settings for the mapi virtual directory in the EAC.    

And please enable windows Authentication-NTLM, Negotiate and Basic    

I found the following questions similar to yours and hope to help you.    

outlook-2016-connect-to-exchange-2016-failed-via-mapi-over-https-autodiscovery    

outlook-clients-cannot-connect-to-exchange-2016    

If none of the above suggestions work, we recommend that you delete the profile completely and create a new profile again.    

In addition, you can configure outlook connection according to the content of this article.    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-17*

Hi @Hriday Saha  ,    

Hopefully, this points you to the right direction.    

https://learn.microsoft.com/en-us/answers/questions/380168/outlook-2016-can39t-connect-to-exchange-2016.html

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-17*

Hi @Hriday Saha  ,    

Hopefully, this points you to the right direction.    

https://learn.microsoft.com/en-us/answers/questions/380168/outlook-2016-can39t-connect-to-exchange-2016.html
