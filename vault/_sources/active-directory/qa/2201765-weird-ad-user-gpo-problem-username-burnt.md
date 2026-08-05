---
title: "Weird AD User / GPO Problem (Username burnt?)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2201765/weird-ad-user-gpo-problem-username-burnt
question_id: 2201765
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Weird AD User / GPO Problem (Username burnt?)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2201765/weird-ad-user-gpo-problem-username-burnt (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

H Everyone,

i am facing a really really strange problem regarding GPO´s and an AD user account. I have several guest user accounts in my domain. (Guest1, Guest2, Guest3...) These users get a share connected via GPO wich works fine for all users except for one. Guest2. I already did all the troubleshooting and came to the following result:

running gpupdate ends up with the error "The Username can not be resolved" - this is strange, where would a username be resolved?

gpresult ends up in "No RSoP data for this User"

DNS works fine

Other User on same PC works fine

Same User on different PC -> same error

no roaming profiles

Local Profiles have been reset on both testing pc´s

User can access the share, the sysvol and netlogon direcory

DC replication shows no errors

I then deleted the user from AD and re-created it (I replicated my dc´s in between) - same error

I then created a User called "Guest2-1" and the share gets connected perfectly (guest2 was deleted at this point) afterwards i renamed "Guest2-1" to "Guest2" and the problem occured again

So i restored all my "Guest2" objects from AD recyclebin and removed them each with "remove-adobject" so they wont be put to recyclebin. But still the same problem.

It looks like the username "Guest2" still exists somewhere in AD even after deletion of the object. Search via AD console, get-adobject, get-aduser and get-mailbox have not shown any results.

I have never seen such behaviour in 18 Years of AD and GPO.

I also tried to use GPO tracing but could not get any useful info from there.

Maybe anyone has faced the same issue before.

Best regards

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-03-11*

I solved it, there is a group with almost the same name as the user. There are german letters used and AD does not see a difference in "A" and "Ä" there for the user gets mistaken for the group.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2025-03-07*

Hello Johannes Glenz,  

Thank you for posting in Q&A forum. 

Please confirm information below:

1.Would you please tell us what specific GPO setting you mean based on "get a share connected via GPO"?

2.Do you put this user Guest2 into on OU?

3.Do you configure Security filtering or WMI filter?

4.Have you ever renamed a domain user account to Guest2 OR rename Guest2 to another account?  

Also, please check the information below:

1.Check error via Event Viewer:

look under “Application” and “System” (or “Group Policy” if available) for any additional details surrounding the error. The event details may mention which GPO or setting is attempting to use the unresolved user name.

2.Review the Problematic Group Policy:

Using Group Policy Management Console (GPMC), inspect any recently modified or suspect GPOs.  Check if any User Rights Assignments, security filtering, WMI filters, or startup/logon scripts are referencing a specific user or SID that might not exist.  

For example, sometimes a “run as” task or scheduled task settings may list a domain user that was moved or deleted.

3.Please check if you have the local account named the same name Guest2 on the domain machine.

Make sure the policy isn’t mistakenly trying to apply user settings that are meant for a domain account onto a local account or vice versa.

4.Consider Recent Changes:  

If this error started after a change—like a domain restructure, renaming a user, or migrating accounts.

5.If it is group policy Preferences setting, please check if you have configured Item-Targeting level.

Preference Item-Level Targeting Using the GPMC

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789189(v=ws.11)

I hope the information above is helpful. 

If you have any questions or concerns, please feel free to let us know. 

Best Regards, 

Daisy Zhou 

============================================ 

If the Answer is helpful, please click "Accept Answer" and upvote it.
