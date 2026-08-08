---
title: "adfs and exchange 2016"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/166124/adfs-and-exchange-2016
question_id: 166124
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "office-exchange-office-exchange-server-management"]
---
# adfs and exchange 2016

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/166124/adfs-and-exchange-2016 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Two wap and two adfs 3.0 in use with exchange 2013 for owa and ecp. It has been working fine.     

Exchange 2016 was added to the organization for migration. However, pointing the dns identifier to 2016 sso doesn't work. Only regular prompt is received.     

Since 2016 uses the same organization settings as 2013 not sure what is missing. Token signing cert thumbprint matches. Had adfs authentication set to true (with others false) on virtual directory as mentioned in the article below and that didn't work.     

https://learn.microsoft.com/en-us/exchange/clients/outlook-on-the-web/ad-fs-claims-based-auth?view=exchserver-2019    

Also, imported the cert to 2016 box root store. didn't work.     

Thanks.

## Answer (community) — community member

*upvotes: 1 · updated: 2020-11-18*

Hi,     

Can you post the result of  "  Get-OrganizationConfig |FL ADFS "?    

I just wonder if you add "/" at the end of each url:    

The inclusion of the trailing slash / in the URL examples shown below is intentional. It’s important to ensure that both the AD FS relying party trusts and Exchange Audience URI’s are identical. This means the AD FS relying party trusts and Exchange Audience URI’s should both have or both emit the trailing slashes in their URLs. The examples in this section contain the trailing /’s after any url ending with “owa” ( /owa/) or “ecp” (/ecp/).    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
