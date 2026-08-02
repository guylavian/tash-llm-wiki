---
title: "GPO Registry Behavior not as Expected"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1432539/gpo-registry-behavior-not-as-expected
question_id: 1432539
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# GPO Registry Behavior not as Expected

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1432539/gpo-registry-behavior-not-as-expected (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

So I need to write a registry key, and I want to do it with a GPO.

I configure my GPO with no issues at

Computer Configuration > Preferences > Windows Settings > Registry (using the registry wizard)

RSOP.msc and gpresult show that the GPO is 'Applied' with no error.  When I check the registry, the entry is NOT there, and it is also not in HKLM\Software\Policies\Microsoft...

BUT

When I search the registry, I DO find it under HKey_Users.Default\software\policies... and \S-1_5-18

-  Question 1: why is my GPO showing up here, and not in the normal spot in the registry?

-  Question 2: Is this policy in effect (the policy is for disabling ie11 NotifyDisableIEOptions)??  Because my security group is not seeing the registry key in the proper place, they are saying it is not working, even though IE11 is not starting.

-  Question 3: If the /.Delault HKey is merged with the normal profiles and is in effect, can I please have a MS reference to show my security people.

p.s. I am not interested in getting the separate admx files to load on my domain to avoid the reg keys.

PART 2

OK, so this is not working the way security wants, so lets just try to use the second GPO registry portion under:

Computer Configuration > Policies > Windows Settings > Security Settings > Registry 

but this only allows me to write the key and set permissions on the key.  it does not allow me to write values.

Question 4: why?  What is the GPO for if not creating registry keys and such?

Thank you all for your help and patience :)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-11-30*

OK, for the next poor sap who has a similar question, here is the best I can tell :(

-  Question 1: I don't know why, but i doubled down that it was happening and i was not seeing things

-  Question 2: No, I don't THINK so.  Because of the .DEFAULT profile is not "merged" only used to create a user.  So for existing users, it would be ignored.

-  Question 3: I have no Microsoft reference, only Google and ChatGPT

-  Question 4: The reg GPO settings in this location are mostly for permissions, not settings.  It will create folders, but that is it, by design.
