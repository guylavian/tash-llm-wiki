---
title: "ECP/OWA Broken After CU18 (not the usual problems)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/272376/ecp-owa-broken-after-cu18-not-the-usual-problems
question_id: 272376
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# ECP/OWA Broken After CU18 (not the usual problems)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/272376/ecp-owa-broken-after-cu18-not-the-usual-problems (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Installed Exchange 2016 CU18.  Afterwords OWA/ECP were not working.  I know this is a common issue and i've gone through all the following steps to resolve but I still have portions of ECP not working.    

The OWA logon page loads fine and works correctly now.  The ECP page logon screen loads fine HOWEVER once credentials are put in the page takes 10-20 seconds to load then looks like this:    

    

It looks like that in every browser (Edge, IE11, Firefox, Chrome) and none of the links work.    

I have already done the following:    

Checked to make sure the correct SSL certificate is bound to the ECP web port - It had switched back to the default but I corrected this.    

Removed and Recreated the virtual directories for OWA as well as ECP.    

Removed and recreated the web applications for OWA as well as ECP.    

Looked in all the web.config files and changed all the directory references with %ExchangeInstallDir% to static paths (there were a few)    

Fixed the application settings for the BinSearchFiles in ECP in IIS.  It was using %ExchangeInstallDir% as well I changed all those to static paths.    

Somebody suggested just installing CU19 but I don't want to make the problem worse.  I need it back up and working properly before I install anything else!

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-02-15*

Hi, @Gedruspax       

Did the problem occur just after you finished upgrading to CU18? Have you installed some security updates?    

Please try running the UpdateCas.ps1 and UpdateConfigFiles.ps1 script under C:\Program Files\Microsoft\Exchange Server\V15\Bin and see if it can help with your problem.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
