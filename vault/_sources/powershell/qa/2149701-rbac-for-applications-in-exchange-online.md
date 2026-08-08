---
title: "RBAC for Applications in Exchange Online."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2149701/rbac-for-applications-in-exchange-online
question_id: 2149701
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-ms-graph", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# RBAC for Applications in Exchange Online.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2149701/rbac-for-applications-in-exchange-online (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello

With the RBAC for application in exchange online coming to EOL this February I have been tasked with finding the apps that are using it and either re-creating them or changing the permissions to the relevant Microsoft graph permissions. 

Could someone please point me in the direction of a script that I could run to list the apps that are using the permission in question? 

As a side note can someone point me as well to a PowerShell I can use to remove/ delete application beginning with a certain name on mass from azure? 

Regards,

Marek

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2025-01-22*

Hello @Marek K,

I'm glad that you were able to resolve your issue and thank you for posting your solution so that others experiencing the same thing can easily reference this! Since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others ", I'll repost your solution in case you'd like to "Accept " the answer.

Issue: Could someone please point me in the direction of a script that I could run to list the apps that are using the permission in question?

Solution: Resolved by @Marek K,

I have found the answer to my question for those that may struggle.
This script https://stackoverflow.com/questions/77064801/retrieve-complete-api-permissions-of-azure-ad-application-via-powershell allowed me to list every app registration we have with all the permission it uses.
As it exports to CSV I was then able to filter by permissions and find the EWS permission that is being retired. I now just need to work at replacing it with the graph permission.
If anyone has PowerShell to list all azure app registrations beginning with a name and then delete them I would be grateful.

If you have any other questions or are still running into more issues, please let me know. Thank you again for your time and patience throughout this issue.

Please remember to "Accept Answer" if any answer/reply helped, so that others in the community facing similar issues can easily find the solution.

Thanks,  

Raja Pothuraju.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-01-21*

Hi all again

I have found the answer to my question for those that may struggle. 

This script https://stackoverflow.com/questions/77064801/retrieve-complete-api-permissions-of-azure-ad-application-via-powershell allowed me to list every app registration we have with all the permission it uses.

As it exports to CSV I was then able to filter by permissions and find the EWS permission that is being retired. I now just need to work at replacing it with the graph permission. 

If anyone has PowerShell to list all azure app registrations beginning with a name and then delete them I would be grateful. 

Regards,

Marek
