---
title: "Unable to demote Domain Controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/387676/unable-to-demote-domain-controller
question_id: 387676
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# Unable to demote Domain Controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/387676/unable-to-demote-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Team,    

I am trying to demote a Domain Controller running on OS Windows Server 2012 R2 but getting error.    

Screen shot attached.    

Please advise on how to fix the issue.    

Thanks,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-12*

Any progress or updates?  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-05-10*

Hi,  

Based on the error screenshot you shared above, it seems you want to demote the DC with the FSMO roles, right?  

Also, it seems it can't find another DC to transfer the roles.  

Before the demotion, we need to check the status of all the DCs in your domain, you can run the command provided by Dspatric to confirm the situation.  

If there is a good DC, you can try size the roles from the one you want to demote, and then done a metadata cleanup.  

Best Regards,

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-09*

Any progress or updates?  

--please don't forget to `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-05-08*

I'd check the health of other domain controllers and role holders as first step.    

netdom query fsmo    

also dcdiag, repadmin tools may be helpful. If all checks out then the other option is to remove from network then seize roles (if necessary)    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

then do metadata clean up.    

https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/ad-ds-metadata-cleanup    

https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-manually-removing-a-domain-controller-server/ba-p/280564    

If you needed further assistance then please run;    

`Dcdiag /v /c /d /e /s:%computername% >c:\dcdiag.log`    

`repadmin /showrepl >C:\repl.txt`    

`ipconfig /all > C:\dc1.txt`    

`ipconfig /all > C:\dc2.txt`    

then put `unzipped` text files up on OneDrive and share a link.    

--please don't forget to Accept as answer if the reply is helpful--
