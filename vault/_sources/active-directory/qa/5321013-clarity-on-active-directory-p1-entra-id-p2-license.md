---
title: "Clarity on Active Directory P1 & Entra ID P2 Licenses"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/5321013/clarity-on-active-directory-p1-entra-id-p2-license
question_id: 5321013
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 6
qa_tags: []
---
# Clarity on Active Directory P1 & Entra ID P2 Licenses

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/5321013/clarity-on-active-directory-p1-entra-id-p2-license (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Microsoft,

In recent, I have purchased Azure AD premium P1 licenses to apply location/IP based conditional access policy to our AD users.

Now I have assigned AD P1 license to each user and it works very well restricting users to access from out office IPs. Now I see

on my license portal  Entra ID P2 license of Qty:100 , So wanted to know does this Entra P2 comes along with P1 purchase or should i have bought it by mistake. Secondly since all 100 licenses are unassigned for now, so do I get billed for Entra P2 as well. In short can suggest, if I only need P1 license for location based conditional access policy not both P1 & P2? I afraid I get billed for P2 also (100 Qty) or P2 is free on cost of P1 buy? Please suggest.Refer the attached existing screenshot.

## Answer (community) — community member

*upvotes: 1 · updated: 2024-06-22*

Dear Mahendra Rane1,

Good day! Thank you for posting to Microsoft Community.

Recently, Azure Active Directory Premium renamed to Microsoft Entra ID and currently, we use these names interchangeably, but they are the same services. Therefore, Microsoft Entra ID P2 will not come along side of Azure Active Directory Premium P1(Microsoft Entra ID P1), Microsoft Entra ID P2 is an advanced upgrade license of Azure Active Directory Premium P1(Microsoft Entra ID P1).

Therefore, to answer your question, Microsoft Entra ID P2 includes all features that are in the Azure active directory P1(Microsoft Entra ID P1) and other additional features such as Identity protection (Risk-based Conditional Access, Token protection and soon), Basic entitlement management, privileged identity management and other advanced security features. However, if you only need location-based conditional access policy, then you only need the Azure Active Directory Premium P1(Microsoft Entra ID P1) license. To see which features are included in P2 but not in P1, you can refer to this article Microsoft Entra Plans and Pricing | Microsoft Security

```
**Tip:** when you check the article, you can click on expand all to see the detail.
```

In addition, Microsoft Entra ID P2 is not free, it is a paid license. 

Therefore, if you purchased licenses through the Microsoft 365 admin center, you can check the purchased licenses listed under the Billing -->Your Product section in the Microsoft 365 admin center. Therefore, if the Microsoft Entra ID P2 license is listed in the "Your Products" section, you may have purchased these licenses by mistake and you will be charged for those licenses regardless of whether you have assigned them or not.  

However, since the screenshot you have shared is not visible on my side I can't provide exact information, to check the screenshot and provide accurate information, could you please provide me with the screenshot of your "Your Product" page or the location that shows the number of Microsoft Entra ID P2 or where this license listed? Based on the information you will provide I can provide more suggestion and accurate information. 

I look forward to your updates, if you have any other questions or I have got you wrong, please feel free to let me know.

Thank you for your precious time. Have a nice day.

Sincerely,

Libeamlak | Microsoft Community Moderator
