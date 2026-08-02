---
title: "How to GPO synchronization setting in domain controller windows"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1391452/how-to-gpo-synchronization-setting-in-domain-contr
question_id: 1391452
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to GPO synchronization setting in domain controller windows

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1391452/how-to-gpo-synchronization-setting-in-domain-contr (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello Team,

I have create a new group policy in domain controller.

Before going to execute gpupdate /force command in domain member server,  where to check  synchronize setting for that policy in the domain controller server .

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-10-30*

Hello

To check the synchronization setting for a Group Policy Object (GPO) in the domain controller server, you can follow these steps:

Open Group Policy Management: This tool is typically found in the Administrative Tools folder.

Find your GPO: In the left pane, navigate to your GPO. This is typically located under “Group Policy Objects” in the forest and domain containing your GPO.

Check the Status tab: Select your GPO, right-click and choose Properties. Then, go to the Status tab. This tab shows whether the GPO is in sync between the Group Policy container and the Group Policy template.

Check Details tab: The Details tab shows the User/Computer versioning information for the GPO. If there’s a mismatch between the domain controller’s version and the version on the client, it may indicate a replication issue.

Use repadmin tool: You can use repadmin /showrepl command to check replication status.

Remember, you need to have necessary permissions to perform these actions.

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/jj134176%28v=ws.11%29
