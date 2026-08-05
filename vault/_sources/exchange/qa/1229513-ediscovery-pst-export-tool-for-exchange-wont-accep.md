---
title: "eDiscovery PST Export Tool for exchange wont accept credentials"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1229513/ediscovery-pst-export-tool-for-exchange-wont-accep
question_id: 1229513
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Microsoft Moderator"]
---
# eDiscovery PST Export Tool for exchange wont accept credentials

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1229513/ediscovery-pst-export-tool-for-exchange-wont-accep (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,
I have been trying to run the ediscovery pst  export tool but I am continually prompted fro credentials to my organization's OWA environment. I have followed the solution of copying the Microsoft.Exchange.Diagnostics.dll from my exchange server to the root of C:\Users%USERNAME%\AppData\Local\Apps\2.0\4QXQH749.K77\AAQ29PXR.1G2\micr..tion_1f16bd4ec4c2bb19_000f.0001_75a3b5c8b7e14190. This is the folder with all the language folders. This is not working and I am still prompted for credentials.
My client machine is Windows11. Is there anything that I need to do in particular on this version of windows to get my export running?
Thanks

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2023-04-14*

Hi @02611269,
Based on my experience, this issue could be caused by permissions, so please make sure the account you used is a member of Discovery Management role group, see Export eDiscovery search results to a PST file.  

Also make sure it's not an account that require multi-factor authentication (MFA), which is not supported to use this tool. Below is a similar thread for reference:  

eDiscovery PST Export Tool for exchange wont accept credentials

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment". 
Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
