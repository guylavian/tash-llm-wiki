---
title: "OWA login using Windows Security dialog box"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/321076/owa-login-using-windows-security-dialog-box
question_id: 321076
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# OWA login using Windows Security dialog box

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/321076/owa-login-using-windows-security-dialog-box (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I recently migrated from a Exchange 2016 CU17 to a Exchange 2019 CU8.   

I had some issue with authentication to OWA and ECP but was able to resolve by using Basic and Windows authentication on the Virtual Directories.  

However, now my users are being prompted by a Windows Security box for credentials vs. the default ASPX login page from Exchange.   

We are able log into OWA and ECP but with Windows Security box only.  

How do I get my ASPX login page back?  

Please advise.  

thank you,

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-18*

If you set BasicAuthentication to $false, then it should just allow domain-joined users to access without any prompt, otherwise you will need to enable forms-based auth if you want them to get the web-based logon screen so they can enter their password or integrate with ADFS

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-18*

Did you disable Forms based auth on those virtaul directories?    

```
Get-OwaVirtualDirectory -Server exch3 | fl *auth*  
Get-EcpVirtualDirectory -Server exch3 | fl *auth*
```

If you want forms-based, you can enable:    

```
Set-OwaVirtualDirectory -Identity "EXCH3\owa (Default Web Site)" -FormsAuthentication $true -WindowsAuthentication $false  

Set-EcpVirtualDirectory -Identity "EXCH3\ECP (Default Web Site)" -FormsAuthentication $true -WindowsAuthentication $false
```

This doc sort of touches on the issue if you didnt want Forms Based:    

https://learn.microsoft.com/en-us/exchange/troubleshoot/client-connectivity/fba-page-shows-when-accessing-owa-or-eac
