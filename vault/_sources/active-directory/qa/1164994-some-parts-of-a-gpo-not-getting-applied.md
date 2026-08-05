---
title: "Some parts of a GPO not getting applied"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1164994/some-parts-of-a-gpo-not-getting-applied
question_id: 1164994
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Some parts of a GPO not getting applied

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1164994/some-parts-of-a-gpo-not-getting-applied (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have created a group policy to allow inbound remote administration exception and to copy a powershell script to C:\temp of domain computers and run it using scheduled task. I have linked the GPO to Workstations OU and added Domain computers to Security Filtering. When I run a group policy update from the domain controller, the only thing that gets applied is, allow inbound remote administration exception. Copying file and running the script through scheduled task is not working. I appreciate some help with this.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-01-30*

Hello @phantom2000,

Thank you for posting in our Q&A forum.  

Based on the description "I have linked the GPO to Workstations OU and added Domain computers to Security Filtering.", you can run gpupdate /force on one machine in the Workstations OU.  

And run gpresult /h C:\gpo.html and click Enter. Then check the gpo setting under "Computer Details".  

If it does not work, please tell us  

1.If all the gpo settings are Computer Configuration.  

2.And how did you configure Security Filtering?  

3.If you configure Preferences and Item-targeting level?

Hope the information above is helpful. If you have any question or concern, please feel free to let us know.

Best Regards, 

Daisy Zhou

=============================================== 

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2023-01-28*

Hi,

Can you check event logs and there could be permission issue with running the script remotely with the account. Did you tried manually running the script on the workstation from the remote path? Follow this link - https://woshub.com/copy-files-on-all-computers-group-policy/#:~:text=If%20you%20need%20to%20copy,to%20copy%20the%20file%20to.

Hope this helps.

JS

==

Please Accept the answer if the information helped you. This will help us and others in the community as well.
