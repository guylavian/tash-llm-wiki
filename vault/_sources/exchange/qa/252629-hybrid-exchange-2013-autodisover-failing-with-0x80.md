---
title: "Hybrid Exchange 2013 autodisover failing with 0x800C820F for 365 mailboxes"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/252629/hybrid-exchange-2013-autodisover-failing-with-0x80
question_id: 252629
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-hybrid-management", "office-exchange-office-exchange-server-management"]
---
# Hybrid Exchange 2013 autodisover failing with 0x800C820F for 365 mailboxes

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/252629/hybrid-exchange-2013-autodisover-failing-with-0x80 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have Exchange 2013 hybrid environment. I have mailboxes on-prem and in 365. Autodiscover record is pointed to on-prem. When I use outlook 2016 16.0.4266.1001 to set up a mailbox that is in 365, it fails.    

When I perform outlook autodiscover test from the same machine, I get autodiscover error 0x800C820F. Looking at autodiscover http proxy logs on the exchange server, I see "OrganizationMailboxNotFound" and "Unable to find organization mailbox for organization" errors during that autodiscover query.    

I did a lot of research on this before posting, and from what I understand, autodiscover should be responding with 0x800c8205, which means targetaddress was found. I have verified that targetaddress value exists in AD and in exchange admin center and is set to the onmicrosoft.com domain.    

On newer versions of outlook this error doesn't happen, but that's because newer versions first check 365 for the mailbox. I don't want to upgrade all 2016 users to the latest version of office.    

See the pictures below for results from outlook autodiscover test and exchange connectivity test from microsoft.    

    

    

Can anyone point me in the right direction on how to troubleshoot this issue further?

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-01*

Hi @BoBanHak   ,  

Is it normal to use Microsoft Remote Connectivity Analyzer to test on-premises user mailboxes?

1.Please run the following command to check whether the “RemoteRoutingAddress” of the user mailbox is correct:

```
Get-RemoteMailbox <> | fl RemoteRoutingAddress
```

2.Have you deployed the firewall? If so, please check the firewall settings to ensure that it will not block the on-premises Autodiscover service from being redirected to Exchange online.  

3.Please check the Authentication method in Autodiscover in IIS.  

  

In addition, upgrading Outlook to the latest version will give you a better experience, which is always recommended by Microsoft.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
