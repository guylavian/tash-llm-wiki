---
title: "Exchange Online GAL Membership using Dynamic Groups in Azure"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/246847/exchange-online-gal-membership-using-dynamic-group
question_id: 246847
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# Exchange Online GAL Membership using Dynamic Groups in Azure

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/246847/exchange-online-gal-membership-using-dynamic-group (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Morning,  

I'm currently trying segregate GAL's but struggling with that I'm trying to achieve.  

I've created dynamic groups within Azure and these are populating correctly as I'm using them to licence users / teams policies etc.  

I've been looking at GAL segregation and getting as far as creating a new global address list in PowerShell  

Blockquote New-GlobalAddressList -Name "Test" -RecipientFilter "MemberOfGroup -eq 'POL_TEST_Staff'"  

Blockquote  

This creates the filter but then on the output it says  

Name RecipientFilter  

TEST MemberOfGroup -e 'DC=POL_TEST_Staff'  

This looks like its trying to look on prem (DC=) for the security group, am I missing something or are you not able to use groups based in Microsoft Azure and if so can anyone advise me of the syntax?  

Note: I don't have a hybrid exchange server setup & haven't extended the AD schema for exchange attributes, i wanted to try and use the groups I already have setup and working.  

Cheers  

Rob

## Answer (community) — community member

*upvotes: 1 · updated: 2021-02-01*

Set or change an attribute for all users in the local installation of Active Directory Domain Services (AD DS) who correspond to the filter objects Sure enough that worked, I change one users UPN and then changed it back and its now appeared in the GAL almost instantly. Not sure how I feel about changing 10k+ UPN's just so they appear in GAL's, it may be easier for me to extend the schema with exchange attributes and go down a more conventional approach. Thanks for the assistance in learning and discovering the pitfalls of (G)AL's. ![62502-forum1.jpg][1] [1]: /api/attachments/62502-forum1.jpg?platform=QnA

## Answer (community) — community member

*upvotes: 0 · updated: 2021-02-01*

Morning, Thanks for the posts, so I had a read through what was posted and I tried to be smart and filter using the format of the UPN. > New-GlobalAddressList -Name "TEST-GAL" -RecipientFilter ((UserPrincipalName -like '@sub  .sub.domain.co.uk') -or (UserPrincipalName -like '@sub  .domain.co.uk')) I can run the command and see users listed as part of this GAL ![62360-forum.png][1] I've created the ABP and linked this new GAL as you can see along with other bits but once I've assigned the ABP to the user there are no entries in their GAL at all. ![62340-forum1.png][2] Regards Rob [1]: /api/attachments/62360-forum.png?platform=QnA [2]: /api/attachments/62340-forum1.png?platform=QnA

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-01-28*

Hi anonymous user,    

According to the comments in this official link, the MemberOfGroup filter requires the distinguished name or canonical distinguished name of the distribution group or mail-enabled security group, so agree with michev that it won't work against the Dynamic group in Azure:    

    

As regards to the dynamic distribution list in Exchange, it's not mentioned in the description above and also didn't work when I tested in lab using the full DistinguishedName, hence it seems to me that dynamic distribution list isn't supported with the MemberOfGroup filter either.    

Given this, aside from the information barrier policies as mentioned by michev, you can also try creating the new global address list using the equivalent filter as what you used when creating the dynamic Azure group. For example, if the dynamic group in Azure is created based on the department:    

    

We can create a global address list using the command below:    

```
New-GlobalAddressList -Name "TEST" -RecipientFilter {(department -eq "Sales")}
```

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-01-27*

The MemberOfGroup filter requires you to specify the full DistinguishedName of the group, and it will not work against Dynamic Azure AD groups. I would suggest recreating this as an Exchange (dynamic) group. Alternatively you can explore the newer "information barrier policies", as they cover additional workloads: https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers?view=o365-worldwide
