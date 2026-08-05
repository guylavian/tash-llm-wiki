---
title: "ZEROLOGON - GPO - Active Directory"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/111661/zerologon-gpo-active-directory
question_id: 111661
fetched: 2026-07-25
answer_count: 9
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-config-app-groups"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# ZEROLOGON - GPO - Active Directory

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/111661/zerologon-gpo-active-directory (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi there Microsoft!  

I have an AD Domain running 2 x 2016 Domain Controllers (virtual) - FFL & DFL are both 2012R2 and were uplifted recently from 2008R2.  

The single domain in a single forest has recently been uplifted from 2008R2,   the old 2008r2 DCs were retired gracefully using DCPROMO.  

Schema version is 87.   

The 2016 DCs are both patched fully up to date too and the following reg key is present indicating that the patches have been applied successfully:-  

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters]  

"FullSecureChannelProtection"=dword:00000000  

My question is this:-  

In the Group Policy Console, within a brand new GPO - this configuration item is missing:-  

"Domain Controller: Allow vulnerable Netlogon secure channel connections"  

I can confirm that all ADMX Files are up to date.  

Any help would be fantastic - i need to set some exceptions using this GPO before i can fix the ZEROLOGON issue.

## Answer (community) — Q&A User

*upvotes: 2 · updated: 2020-10-02*

Hi guys - these has now been resolved for me - so thanks for the help.  

Theres a good learning point here which has only become apparent through this exercise:-  

As mentioned in the OP - The forest in question for 2008r2 and has been uplifted to FFL 2012R2.   At the start of the uplift - all DCs were fully patched.  

KB4577015 is a red herring and just complicated the situation - remove it if you have to until Microsoft resolve the issue.  

KB4571694 need to be installed manually on both 2016 DCs in order to reveal the - "Domain Controller: Allow vulnerable Netlogon secure channel connections" configuration item  

I think that KB4571694 wasnt showing as being needed in WSUS because there were 2008R2 Domain Controllers kicking around.   Even after the 2008R2 boxes were demoted,  and the FFL & DFL raised - the DCs still wouldnt pick this up in WSUS.  

Anyways - all is good now.   So thank you very much.  

Mike

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-09-30*

I'd look for it in local security policy `gpedit.msc` As mentioned if you have installed the September 8, 2020—KB4577015 then this dialog was broken by the update so for now the only option is to uninstall KB4577015.  

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-30*

Hiya,  

Local and Domain group policy editors both crash the MMC when trying to access that function since the Sep20 patch went on.  

I have built a spare 2012r2 server to access the Domain GP Console which works fine - BUT the features within the GPO are still missing and im not sure how to enable them.  

Any ideas?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-09-29*

I'd look for it in local security policy `gpedit.msc` Also note if you have installed the September 8, 2020—KB4577015 then this dialog was broken by the update.    

    

--please don't forget to Accept as answer if the reply is helpful--
