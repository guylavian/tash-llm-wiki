---
title: "Folder Permission via GPO"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2237041/folder-permission-via-gpo
question_id: 2237041
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Folder Permission via GPO

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2237041/folder-permission-via-gpo (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

We are trying to update folder permission of only "Downloads" folders of all the users folder under C:\Users. So we have created GPO and assign it to respective Computer OU. but it is not working, permission is not getting update.  

Below are setting made from GPO.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-21*

Hello,

Thank you for posting in Microsoft Q&A.

Based on the description, I understand your question is related to GPO.

Check the GPO is linked to the correct OU containing the target computers. Verify that the GPO is enabled and enforced. By default, the GPO should apply to "Authenticated Users". If you've modified this, ensure the correct groups or users are included.

Check the Event Viewer on the client machines for any Group Policy-related errors. Look for events under Windows Logs > System and Applications and Services Logs > Microsoft > Windows > GroupPolicy.

Have a nice day. 

Best Regards,

Molly

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it
