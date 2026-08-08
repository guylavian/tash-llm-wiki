---
title: "Version 2004 GPO Deployed Printers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/181971/version-2004-gpo-deployed-printers
question_id: 181971
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-print-jobs"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Version 2004 GPO Deployed Printers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/181971/version-2004-gpo-deployed-printers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

My GPO deployed printers show as "unknown devices" after updating workstations to Version 2004. I've been able to defer updates for 180 days through GP, but now workstations are starting to update and it breaks all GPO deployed printers. I've seen posts where others have this issue, but there is no resolution.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-12-02*

Hello @Luke Moffitt       

Would it due to the printer drivers?  Have you update them?    

Did you check from the event log , any errors?    

Maybe you can use  group policy preferences instead.    

If it is a known issue , we probably  need to wait for the patch released.    

----------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.    

Best Regards    

Karlie

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-01*

I'm having a similar issue. Windows 2004 feature update was delayed for 180, but after getting the 2004 update our deployed printers have disappeared completely instead of showing as unknown. We have had some luck with redeploying the printers using the FQDN or IP of the print server. Starting to think this has something to do with DNS. Hope this helps.
