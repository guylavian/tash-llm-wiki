---
title: "unable to delegate exchange online to exchange onpremises mailbox in hybrid enviornment."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/220648/unable-to-delegate-exchange-online-to-exchange-onp
question_id: 220648
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management", "office-exchange-online"]
answer_author_roles: ["Q&A User"]
---
# unable to delegate exchange online to exchange onpremises mailbox in hybrid enviornment.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/220648/unable-to-delegate-exchange-online-to-exchange-onp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

we have an Exchange hybrid environment, we are facing an issue while trying to delegates exchange online users to exchange on-premises mailbox.  

Example: User A is an exchange online user (migrated from on-premises) and user B is an exchange on-premises user.  

Now we want delegate user A to user B for send on behalf/full access but user A is unable to send mail on be half of user B.  

Any idea?  

Thank You  

Nur

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-07*

Hi @Nur Hossain   ,    

I agree with what AshokM-8240 said.    

-  What’s the on-premises Exchange version? You could follow the "Configuring your on-premises Exchange servers to support hybrid mailbox permissions" section in the first link provided by AshokM-8240 to check your on-premises Exchange version.    

-  Please make sure that your Azure Active Directory (Azure AD) Connect version to 1.1.553 or a later.    

-  After you have assigned permissions, it may take a while to work, please wait 30 minutes and try again.    

Here is an official document about delegation settings in the Exchange hybrid environment: Overview of delegation in an Office 365 hybrid environment    

Below screens is the test in my lab environment, User1 is the mailbox migrated to Exchange Online. Assign the send on behalf of permission of on-premises mailbox user2 to user1. Then user1 can send mail on behalf of user2 successfully    

    

    

----------    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation  to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-06*

Hi,    

Could you please let us know how the mailbox permission has been assigned?     

Exchange hybrid deployments support the use of some delegated permissions in on-premise Exchange, but not all.    

https://learn.microsoft.com/en-us/exchange/permissions#delegate-mailbox-permissions    

In order for this permission to work, you may need to upgrade Azure AD connect  to at least version 1.1.553.0. Also Enable Exchange Hybrid to writeback the permissions.    

https://learn.microsoft.com/en-us/exchange/troubleshoot/send-emails/delegate-cannot-send-on-behalf-of-after-migration    

If the above suggestion helps, please click on "Accept Answer" and upvote it
