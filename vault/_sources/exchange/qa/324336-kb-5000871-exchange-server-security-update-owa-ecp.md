---
title: "KB 5000871 Exchange Server Security Update - OWA/ECP issue"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/324336/kb-5000871-exchange-server-security-update-owa-ecp
question_id: 324336
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# KB 5000871 Exchange Server Security Update - OWA/ECP issue

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/324336/kb-5000871-exchange-server-security-update-owa-ecp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I recently applied the KB5000871 on Exchange Server 2013 servers to patch the Exchange vulnerabilities of March 2021. After this application, I had an issue with the ECP and OWA, it was no longer accessible. I know now this is a known issue and that it happened because I didn't run the update via an elevated cmd prompt.  

Then, I ran the following scripts located in the Exchange installation folder : UpdateConfigFiles.ps1 and UpdateCAS.ps1. That solved the issue : the OWA and ECP were available again.  

However, I have a question : does the application of these two scripts remove the benefits of the KB (as vulnerabilities mainly affect the OWA and ECP) ?  

I need to be sure that the vulnerabilities are still fixed.  

Is there a Microsoft Exchange expert who could answer me ?  

Thank you a lot in advance,  

Sébastien

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-03-22*

Hi @Sébastien   ,    

No you don't have to worry about it. Since the SU has enhanced the defense of your server and the scripts won't break it.    

    

Also you could use the Test-ProxyLogon.ps1 to detect any potential attacker activity.    

Guidance for responders: Investigating and remediating on-premises Exchange Server vulnerabilities    

Regards,    

Lou    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-03-21*

This the known issue mentioned in the documentation here: description-of-the-security-update-for-microsoft-exchange-server-2019-2016-and-2013-march-2-2021-kb5000871-9800a6bb-0a21-4ee7-b9da-fa85b3e1d23b    

    

So, to install the fix successfully, Disabled UAC and ran de update as administrator.    

UpdateCas.ps1 script reverts the changes made with the failed updates from the back up directory
