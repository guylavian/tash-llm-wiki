---
title: "ADFS & HRD sign in page"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/44721/adfs-hrd-sign-in-page
question_id: 44721
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# ADFS & HRD sign in page

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/44721/adfs-hrd-sign-in-page (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,

We are facing an issue when applying HRD on lab &amp; prod environement. We have 2 directories for authentication.  

We use ADFS installed on Windows Server 2019.  

We use OrganizationalSuffix (Set-AdfsLocalClaimsProviderTrust -TargetName &#34;Active Directory&#34; -OrganizationalAccountSuffix @(&#34;mydomain.com&#34;), for HRD.  

We configured HRD Cookie with &#34;set-adfswebconfig&#34;:

HRDCookieLifetime : 30  

HRDCookieEnabled : True  

ContextCookieEnabled : True

I&#39;m connect to RP, and I&#39;m redirected on ADFS login page  

The logon page show only login form without password  

I enter @mail, and on the second page, I enter password, and everything is working fine.

I close my session (logout).

On the lab Environment

I reconnect to the RP,  

ADFS shows the Signin page with Login and password on the same page.  

This is due to HRD cookie lifetime, very good.

One the prod environment

I reconnect to the RP  

ADFS shows the signin page with login only. I must click &#34;next&#34;.  

First, I did believe that que HRD cookie was deleted, but if I choose login which is in the other directory (different from the first login), authentication failed. I&#39;m sure that HRD works fine, but I don&#39;t understand this page.

I tested with our custom theme, and I re-activate default ADFS 2019 theme.

What I missed?

Thanks,

Jean-Luc

## Answers

_No answers on this thread._
