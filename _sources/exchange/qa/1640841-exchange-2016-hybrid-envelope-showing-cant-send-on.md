---
title: "Exchange 2016 hybrid, envelope showing, can't send on behalf with full rights"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1640841/exchange-2016-hybrid-envelope-showing-cant-send-on
question_id: 1640841
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2016 hybrid, envelope showing, can't send on behalf with full rights

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1640841/exchange-2016-hybrid-envelope-showing-cant-send-on (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good morning,

Starting last week, yellow envelopes started showing up on some emails.  Had an exchange issue with patch Tuesday security update, but reinstalled the update and that seemed to resolve the issues.  Haven't had any more issues until mid-week last week, where the envelopes showed up, can't set up a user in the Outlook app on android and ios(native mail app works fine) and now, some users can't send on behalf of a shared mailbox, even with full delegation.  

Error that's returning is: The following recipient(s) cannot be reached:

            This message could not be sent. Try sending the message again later, or contact your network administrator. You do not have the permission to send the message on behalf of the specified user. Error is [0x80070005-0x0004dc-0x000524].

Any assistance would be appreciated.

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2024-04-03*

Hi @Asker  ,

Are the affected users all hosted on Exchange 2016?  

And by "patch Tuesday security update", are you referring to the March 2024 Exchange Server Security Updates?

If so, the yellow envelope icon in Outlook client is a known issue according to the blog:  

As regards to the issue that "can't set up a user in the Outlook app on android and ios", while it's completely unrelated to on-premises patch level, there are also some discussions in the comment section of the aforementioned blog. According to the comments there, "the service team was working to address this ASAP but was not sure of the exact timeframe". But some others reported that it's working for them again without any changes. Please have a try again on your end to see how it goes. If it still fails, you can try the workaround shared under the blog, adding the user account using settings below:

-  Email Address: ******@contoso.com <required>

-  Password: *********** <required>

-  Description: <Optional>

-  Server: mail.contoso.com <required>

-  Domain: <LEAVE EMPTY>

-  Username: ******@contoso.com <Use email address used for email address field>

Concerning the "can't send on behalf of a shared mailbox" issue, was it working fine previously? Despite of the full access permission, it's also suggested to check if the Send as permission has been granted to the delegate user:  

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
