---
title: "Changed Exchange 2019 DNS MX Records for Spam Filter Service and Exchange Active Sync Now Fails"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2191614/changed-exchange-2019-dns-mx-records-for-spam-filt
question_id: 2191614
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-networking-networking-other"]
---
# Changed Exchange 2019 DNS MX Records for Spam Filter Service and Exchange Active Sync Now Fails

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2191614/changed-exchange-2019-dns-mx-records-for-spam-filt (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We have an on-premises Exchange Server 2019.  Everything was working fine until we got an external spam filtering service.  We changed our MX records to point to the spam filtering service, and then the filtering service sends the emails to the Exchange Server.  That part works great.

The problem is when we try to add an account to Outlook or a smartphone, it won't connect to the Exchange Server to setup the account.  The only records changed were the MX records.  Autodiscover, mail.{domain].com, and autodiscover records still point to the Exchange server.

Here are the error messages I get.

If I manually setup the Outlook profile putting in the mail server name (mail.{domain}.com, domain\username, password, etc., then I get this.

I ran the Microsoft Remote Connectivity Analyzer for Activesync, and it passed.

Anyone have any ideas or workarounds?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-08-03*

I did all that.  There is nobody on the Microsoft forums anymore to answer any questions.  People don't like the forum layout with no categories.  Tags are not enough.  Microsoft needs to bring back Technet.  It's gone from a thriving forum (Technet) to dead (Microsoft Q&A).

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-30*

Hi Michael1000,

If you don't get a response on Microsoft Q&A, here are some suggestions that may help:

1.Make sure your question description is clear and detailed. You can attach error messages, screenshots, etc. to help others understand your problem.

2.Use tags correctly to make your question more discoverable by experts in related fields.

Regards,

Zunhui

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-26*

I posted on Microsoft Q&A, and never got a response there either.  I don't know where to post anymore.  Microsoft shut down the Technet forum.  Why?  That was a big mistake.  Now we can't get answers to anything.  Technet was great.  There was lots of expertise on there.  Tech Community and Q&A forums are dead.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-07-26*

Hello ，

Thank you for posting in Microsoft Community forum.

From the description above, I understand your question is related to Exchange Server. 

Since there are no engineers dedicated to this topic in this forum. To be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.

Questions - Microsoft Q&A

Click the "Ask a Question" button in the upper right corner to post your question and select tags related to your products.

I hope the information above is helpful.

If you have any questions or concerns, please feel free to let us know.

Regards,

Zunhui
