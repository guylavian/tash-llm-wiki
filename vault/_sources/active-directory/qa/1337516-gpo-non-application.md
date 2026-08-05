---
title: "GPO - Non-application"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1337516/gpo-non-application
question_id: 1337516
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO - Non-application

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1337516/gpo-non-application (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Inherited AD network and need to convince some admins.  I believe I know why but I would like it confirmed because I cannot find any official reference

Issue

-  Created a new GPO but it doesn't apply the settings.

-  Some older GPOs seem to be working but changed a minor setting in one of them and it didn't change the setting.

Background

-  Functional AD level: W2008

-  Domain controllers: W2012

-  Majority of servers: W2016

Troubleshooting

-  No effect - I created a test OU and linked the GPO there.

-  No effect - Tried enforcing the GPO to the OU

-  RSOP says that the policy applied properly but when I check the local policy, I can change it, disable it.

-  I've tried forcing it with gpupdate /force and a restart to no avail

-  Tried modifying an existing GPO and it didn't take effect

-  Replication is working

-  There's no apparent GPO higher in the tree that's overwriting my setting

Yes I know that:

-  Domain controllers should ideally be equal or higher than your servers

-  Functional level should be at least the level of your most modern DC

Can anyone please confirm or give me a sanity check that the solution is that:

We need to raise our functional level because its causing issues with GPO inheritance? Is there a reference that I haven't found?  I want my ammo to convince the admins.  I believe that this is why but I would like a second opinion because I cannot find any official reference

Thanks in advance

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-14*

Hello Will,  

Thank you for posting in Q&A forum.    

How many DCs and sites are there in the domain?

Do you mean no matter what gpo settings in new GPO will not work (user configuration or computer configuration)?  

1.Please check the health of all DCs in the domain by running Dcdiag /v on each DC.  

2.Please check if AD replication is working fine.  

3.Please check SYSVOL replication engine is FRS or DFSR.  

4.Please check SYSVOL replication is working fine.  

5.For check if gpo setting is applied, I recommend gpresult instead of rsop.  

For computer configurations:  

1.Logon this machine using administrator account.

2.Open CMD (run as Administrator).

3.Type gpresult /h C:\gpo.html and click Enter.

4.Open gpo.html and check gpo setting under "Computer Details".

For user configurations:  

1.Logon one domain client machine using one domain user account in the OU.  

2.Create a folder in C drive(such as Folder1).  

3.Open CMD (do not run as Administrator).  

4.Type gpresult /h C:\Folder\gpo.html and click Enter.  

5.Open gpo.html and check gpo setting under "User Details".

Hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.
