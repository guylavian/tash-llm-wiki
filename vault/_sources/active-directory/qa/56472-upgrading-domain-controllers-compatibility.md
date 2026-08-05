---
title: "Upgrading domain controllers - compatibility"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/56472/upgrading-domain-controllers-compatibility
question_id: 56472
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee", "Mvp"]
---
# Upgrading domain controllers - compatibility

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/56472/upgrading-domain-controllers-compatibility (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to track down official documentation for domain controller compatibility.  We are behind the ball and still have some 2008R2 DC's, I want to make sure that i can go to 2019 both with just the OS compatibility and also the functional level upgrade, what are the oldest client OS for workstations and servers that each functional level can support.  We have some applications that vendors are still requiring older OS's so I need to make sure i don't end up kicking anything off the domain as we upgrade.    

I have been trying to find a document that shows each functional level with the oldest OS each one supports but my searches have not tracked something down yet.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-08-01*

Hi @ThomasSzilagyi-1653

Let's go back one step to avoid confusion. There is a big difference between:  

Having a Server 2016 as a DC

and

Having a Server 2016 as a DC and have your Domain Functional level to 2016

So what is your Forest and Domain Functional level?

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-07-31*

It should be fine to use these OSs but may be riskier going forward if extended updates have not been applied.      

https://techcommunity.microsoft.com/t5/windows-it-pro-blog/archived-how-to-get-extended-security-updates-for-eligible/ba-p/917807    

The highest DFL for 2019 is also 2016. No new functional level features for Server 2019      

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels#windows-server-2019      

--please don't forget to Accept as answer if the reply is helpful--

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-31*

Unfortunately we still have some OS's that are not on the current supported still in the wild, both workstation and servers.  We are still trying to get them upgraded but its still taking time.  

Yes I am aware that it is a security issue as they will not get patches.    

We go back as far as Windows 7 for desktops and Server 2008 and 2008R2 for servers.    

with that said, can we still use 2019 as a domain controller OS or would we have to stop at say 2016.  Also what would be the highest domain functional level i could go to until we get these older systems upgraded or off the domain.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-07-31*

Hi @Thomas Szilagyi       

I believe the documents you are looking for are these ones:    

-  Forest and Domain Functional Levels: As you can see there is no new Windows Server 2019 Functional level    

-  Identifying Your Functional Level Upgrade    

--I hope this helps. Please Accept it as an answer and "Up-Vote" the answer or message(s) that helped you so that it can help others in the community looking for help on similar topics    

Regards,    

Didier3001

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2020-07-31*

The two prerequisites to introducing the first 2019 domain controller are that domain functional level needs to be 2008 or higher      

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-functional-levels      

 and older sysvol FRS replication needs to have been migrated to DFSR      

https://techcommunity.microsoft.com/t5/Storage-at-Microsoft/Streamlined-Migration-of-FRS-to-DFSR-SYSVOL/ba-p/425405     

I'd use dcdiag / repadmin tools to verify health correcting all errors found before starting. Then stand up the new 2019, patch it fully, license it, join existing domain, add active directory domain services, promote it also making it a GC (recommended), transfer FSMO roles over (optional), transfer pdc emulator role (optional), use dcdiag / repadmin tools to again verify health, when all is good you can decommission / demote old one and move on to next one.    

Any currently supported operating systems for member servers and desktops are fine to use.    

--please don't forget to Accept as answer if the reply is helpful--
