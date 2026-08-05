---
title: "MSOL versus ExchangeOnlineManagement versus AzureAD versus AZ"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/204236/msol-versus-exchangeonlinemanagement-versus-azurea
question_id: 204236
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-online"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# MSOL versus ExchangeOnlineManagement versus AzureAD versus AZ

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/204236/msol-versus-exchangeonlinemanagement-versus-azurea (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Good evening,    

Looked on the forums here and plenty of other sites which I think has only confused things even more.  That said, I did come across a reference (these forums) where someone responded and stated that the MSOL module/cmdlets were replaced with the AzureAD (aka Connect-AzureAD).  Based on everything I have read, I believe the following is accurate.  Am I wrong?    

GOALS:    

Managing AzureAD    

Recommended module/cmdlets are AZ (aka Connect-AZAccount)    

Managing O365    

Recommended module/cmdlets are ExchangeOnlineManagement (aka Connect-ExchangeOnline)    

-   Wasn't the MSOL module/cmdlets replaced by ExchangeOnlineManagement?    

-   Wasn't the AzureAD module/cmdlets replaced by AZ?    

-   If the MSOL commands were replaced with ExchangeOnline, then what are the correct commands for all the articles that discuss Hybrid configurations, Modern Authentication, and Teams integration?  Lots of these sites refer to MSOL commands only.  How does everyone get around this?    

Example sites:    

https://learn.microsoft.com/en-us/microsoft-365/enterprise/configure-exchange-server-for-hybrid-modern-authentication?view=o365-worldwide#add-on-premises-web-service-urls-as-spns-in-azure-ad    

https://learn.microsoft.com/en-us/exchange/configure-oauth-authentication-between-exchange-and-exchange-online-organizations-exchange-2013-help    

In closing,  if I could get the MSOL commands to run or actually import I'd be golden, but after  installing the module my get-module command doesn't list it so I could then import them.  Maybe this is where my attention needs to be?    

Thanks all for any thoughts on this.    

CWT    

Also, there are a lot of references to MSOL commands related to this.  Did the ExchangeOnlineManagement module replace that?  If so, are the

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-28*

Just a quick follow up.  

After diving into my MSOL & AzureAD import issues I discovered something that I cannot recall ever running into.  For whatever reason the default module location was not used meaning that when I installed these two modules, it did not place them C:\Windows\System32\WindowsPowerShell\v1.0\Modules or C:\Program Files\WindowsPowerShell\Modules.  Feeling foolish I did not catch this, but for anyone that has issues importing these two modules, just use the following command to target the module directly.  

Import-Module "C:\PATH*.psd1"    

I still do not understand why the AZ and ExchangeOnlineManagement modules installed to a different location that powershell could just use so the import-module worked by default, but now at least I understand exactly what happened.  

Thanks again.  

CWT

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-21*

@Vasil Michev   & KyleXU    

So let me restate to confirm my understanding.    

3 module breakdown.    

-   The AZ module (Connect-AZAccount) allows us to manage Azure resources (vms, storage, subscriptoins etc) correct?    

-   The  Exchange Online module (Connect-ExchangeOnline) allows us to manage mailboxes, configurations, connectors etc correct?    

-   AzureAD module (Connect-AzureAD) is a combination that can be used to manage Azure resources (VMs etc) along with O365 (Exchange related commands).  Is this accurate?    

Thanks for the assistance with this.    

CWT

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2020-12-19*

The Az module is for Azure management, if you are planning to manage Azure AD as part of Office 365, stick to the Azure AD module. The MSOL module is the older version of the Azure AD module, sort of. It's not a direct replacement as some operations can still only be performed via MSOL.  

Exchange Online is totally separate from this, in no way it replaces any of the Azure AD related modules.
