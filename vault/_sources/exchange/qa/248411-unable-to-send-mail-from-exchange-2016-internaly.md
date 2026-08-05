---
title: "Unable to send mail from exchange 2016 internaly"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/248411/unable-to-send-mail-from-exchange-2016-internaly
question_id: 248411
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Unable to send mail from exchange 2016 internaly

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/248411/unable-to-send-mail-from-exchange-2016-internaly (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,    

Installed Exchange server 2016 on windows ,The emails sent(internally) are saved in to drafts folder instead of inbox/sent items.    

Kindly assist me on this issue.    

Thanks,    

Manoj    

manojr023@Stuff  .com

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-04*

Hi,    

Have you changed internal URL and external URL for owa via Exchange Admin Center?    

By default the internal URL is https://macinename.domain.com/owa, and the external URL is null.    

If you would like to use https://domainname/owa instead, you may need to configure the internal URL and external URL for owa,ecp and other virtual directories.    

And you may also need to configure split-dns:     

Set internal DNS records on your internal DNS server to point the URL to the internal ip address of your exchange server    

Set external DNS records on public DNS server to point to the public ip address of your exchange server    

For more detailed information, please refer to the steps in this Microsoft document:    

Step 4: Configure external URLs    

Step 5: Configure internal URLs    

Configure internal and external URLs to be the same    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-29*

Hi, Manoj.    

Sorry I need to ask a few questions in order to get some more information:    

-  Does the problem happen when you send emails via OWA? Or are you using Outlook?    

-  Have you modified the default receive connectors on the Exchange server?    

Please make sure the "Microsoft Exchange Transport" and "Microsoft Exchange Mailbox Transport Submission" services are running on your Exchange server.    

If they are running, you may also restart the services and see if the problem perists.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
