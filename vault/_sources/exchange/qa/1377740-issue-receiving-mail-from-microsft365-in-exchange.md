---
title: "Issue receiving mail from Microsft365 in Exchange 2016 Hybrid configuration"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1377740/issue-receiving-mail-from-microsft365-in-exchange
question_id: 1377740
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-online", "office-exchange-other-l1"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Issue receiving mail from Microsft365 in Exchange 2016 Hybrid configuration

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1377740/issue-receiving-mail-from-microsft365-in-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a onprem 2016 exchange server and have configured a hybrid connection to Microsoft365.  I am able to send and receive emails from the test migration account on M365 to a gmail address.  I can send an email from my onprem exchange to the M365 account and it is received.  However, I cannot send an email from M365 to the onprem.

The email goes into defer status according to message trace with the Reason: [{LED=450 4.4.316 Connection refused [Message=Socket error code 10061].

I suspect it has to do with the fact that our mx record points to a third party service that monitors for spam.  I don't want to change the mx record because I only want to migrate ~10 email accounts to M365 and leave the other 50+ users on the onprem exchange server.  I've read just about every article I could find on this issue but have not been able to get it to process.  I'm hoping someone here has other suggestions or experienced the same scenario and can offer assistance.  Thank you.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-29*

Hi @ Hwls，

Just want to confirm that your issue is solved?

If it has been resolved, please click "Accept answer" to mark this post or share your solution, your action would benefit others who have similar issues.

Here are some of my suggestions for this issue:

-  Check your firewall and make sure EXO can access your on-perm server （port 25）.

-  Temporarily turn off firewall and antivirus software to test mailflow.

-  Check the configuration of the connector that is used for message transport between your on-premises and Exchange Online organizations.

-  Make sure that the domain name you're using has also been successfully added to O365.

-   Check to make sure that a valid certificate purchased from a trusted CA is used for secure message transmission.

-  Check that you've correctly added an SPF record for your domain in Office 365.

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-28*

please disregard.  I tried to delete the question but wasn't able to find a way to do so.
