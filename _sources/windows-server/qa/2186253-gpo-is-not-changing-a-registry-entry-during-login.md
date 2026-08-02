---
title: "GPO is not changing a registry entry during login but if I force it using gpupdate /force, it works."
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2186253/gpo-is-not-changing-a-registry-entry-during-login
question_id: 2186253
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-windows-cloud-windows-cloud-other"]
---
# GPO is not changing a registry entry during login but if I force it using gpupdate /force, it works.

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2186253/gpo-is-not-changing-a-registry-entry-during-login (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I created a GPO to update a registry entry, 3 to 0. We have 2 DCs and can see the GPO on both. If I sign in on my local computer, it's working normally and the GPO execute the task during the login but, when I'm trying to sign in into our AVDs (Virtual machine on Azure running Windows 10) it is not executed. I checked the GPOs applied using gpresult /r on MS-DOS and I can see the GPO there, applied to my user but the registry entry is still 3. If I force it using gpupdate /force, it works and the entry changes to 0. Is there anyone to help me troubleshoot this situation, where the GPO is not changing the registry entry during the login? 

Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-13*

Hello   

Good day!  

Is the AVDs (Virtual machine on Azure running Windows 10) in the same domain as your local machine?

Is the AVDs (Virtual machine on Azure running Windows 10) in the same domain as the user account that applied the registry entry?  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-12*

Thank you for your response Daisy.

It's under HKEY_CURRENT_USER. AVDs can see the DC because other polices are being applied. GPO is under the correct OU because I can see the police applied executing gpresult /r. 

The issue is it is not changing the registry entry from 3 to 0 during the login. I added a batch to the same police to execute gpupdate /force and it worked. But I don't see it as the right way to do that.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-12*

Hello Paulo Puhl,  

Thank you for posting in Microsoft Community forum.

1.What specific GPO setting did you configure? Is it under User Configurations or under Computer Configurations?  

2.Is the registry entry under HKEY_CURRENT_USER or HKEY_LOCAL_MACHINE?

If it is user configuration (registry entry under HKEY_CURRENT_USER), you should sign out and sign in the user account (that applies this GPO) to make GPO setting refresh or run gpupdate /force.  

If it is computer configuration (registry entry under HKEY_LOCAL_MACHINE), you should restart the machine (that applies this GPO) to make GPO setting refresh or run gpupdate /force.

It sounds like the GPO is not being applied during the initial login process on the AVDs. One possible reason for this could be that the AVDs are not able to communicate with the domain controllers during the login process.  

To troubleshoot this issue, you can try the following steps: 

1.Check the network connectivity between the AVDs and the domain controllers. Make sure that the AVDs are able to communicate with the domain controllers over the required ports and protocols. 

2.Check the event logs on the AVDs and the domain controllers for any errors related to Group Policy processing. This can give you an idea of what might be causing the issue. 

3.Check the Group Policy settings on the AVDs to make sure that they are configured correctly. You can use the Group Policy Results wizard in the Group Policy Management Console to check the settings that are being applied to the AVDs.

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zhou
