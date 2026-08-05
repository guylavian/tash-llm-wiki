---
title: "Active Directory Domain naming"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2198435/active-directory-domain-naming
question_id: 2198435
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Active Directory Domain naming

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2198435/active-directory-domain-naming (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,

I'm trying to understand the naming best practices when deploying Active Directory Domain Services. Say, I have an organization company .com has their services hosted publicly under the name company.com.

The requirement is the company is planning to have new ADDS structure which include Two child domains, as below.

hq.company.com

br1. company.com

br2.company.com

From few searches on the Internet for naming best practices, I have seen people advising that avoid company.com as your domain name and use like ad.company.com.

in my case, as mentioned above in the naming requirements, can I create my root domain as company.com, which is the tree root domain having forest wide FSMO roles held in it and create hq, br1 and br2 as child domains under company.com? Is this approach advised? The company is also planning to have office 365 licenses to be allocated for some its members. The company has office 365 accounts exists under the name company.com

Could someone please help to clear the confusions.

Regards

JG

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-16*

Hello   

Greetings!  

Yes, based on the official document it is. Usually, if your organization does not have a domain name registered on the internet (like domain.com), you can name domain as domain.com.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-16*

Hello Daizy,

Thanks for the detailed explanation.

So, assume that my domain name contoso.com and it has internet presence. according to your example if I choose my root domain (internal domain) as corp.contoso.com, then the child domain names will be hq.corp.contoso.com, br1.corp.contoso.com and br2.corp.contoso.com. Is it so?

Regards,

JG

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-15*

Hello，

Greetings!  

This statement provides guidance for naming the internal (intranet) domain of an organization in a way that is consistent with its external (internet) domain name. 

Here's what it means in simpler terms: 

-  Internet Presence: 

If your organization has a domain name registered on the internet (like contoso.com), use that as a basis. 

-  Consistency: 

To keep things organized and easily identifiable, your internal network's domain name should relate to your external domain name. 

-  Example: 

If your company's internet domain is contoso.com, you should name your internal network something like corp.contoso.com or internal.contoso.com. This way, it's clear that the intranet domain is part of the same organization as the external domain.

In essence, it’s about maintaining a clear and consistent naming convention for both your external and internal domains to avoid confusion and ensure easy management.

If your organization does not have a domain name registered on the internet (like contoso.com), you can name domain as domain.com.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-15*

Dear Daizy,

Thanks for your quick and detailed explanation.

We have company.com (used as an example) domain is already registered with DNS registrar and has Internet presence. 

My question is: company.com being a public domain and having Internet presence, would you be advising to use as default tree root domain name.

"

-  If the organization has an internet presence, use names that are relative to the registered internet DNS domain name. For example, if you've registered the internet DNS domain name `contoso.com`, use a DNS domain name such as `corp.contoso.com` for the intranet domain name."

As quoted above from the earlier shared article, it says to use corp.contoso.com, in the case where contoso.com has Internet presence. If I follow, this, I assume that your First: option applies. If we go with this, we have long domain name for the users. 

Your Second: option proposed has domain name which is company.com, has Internet presence. I would personally like to choose this naming convention, as this has more meaningful and structured naming convention.  On the other hand, surprisingly, it contradicts with what MS says in their above article, that is to use either ad.company.com or corp.contoso.com, in the case the parent domain name has Internet presence. This is the confusing part for me. Could you please enlighten me on this?

Regards,

JG

## Answer (community) — community member

*upvotes: 0 · updated: 2025-01-14*

Hello Jobish George,

Thank you for posting in Microsoft Community forum.

Do you want to know which domain name you should set? If so, I think domain name looks like second one.

First:

ad.company.com (domain name)

hq.ad.company.com (child domain name)

br1.ad. company.com (child domain name)

br2.ad.company.com (child domain name)

Second:

company.com (domain name)

hq.company.com (child domain name)

br1. company.com (child domain name)

br2.company.com (child domain name)

  

Name computers, domains, sites, and OUs - Windows Server | Microsoft Learn

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
