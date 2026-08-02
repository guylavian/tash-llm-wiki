---
title: "GPO Security Group"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/633659/gpo-security-group
question_id: 633659
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# GPO Security Group

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/633659/gpo-security-group (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,  

I was looking for specific information on Security Filtering and how it actually works.  

I need to create a GPO that populates PAC file address information. The GPO should only be distributed to Users or Computers in a specific group.  

Our OU Domain structure has users in one OU which consists of every Global Domain User in one Container. It has not been split into Regions or countries. It's too late to even think about creating Sub OU's.  

My first question is - can I distribute the PAC file address http link using Computer Configuration details. This would be much easier as the OU client structure is split between Countries, Regions, and Offices. I cant seem to find details of how to populate I.E. with the PAC details, I see them in User Configuration Preferences > Control Panel Settings > Internet Settings > Internet Explorer 10 1 > Connections > Lan Settings, the PAC file information is updated on the Address: field. Cant see where to configure the policies on Computer Configuration....!  

My second question is - could I create a Security Group with specific users in the group, Link the GPO to the Top Level users OU (where thousands of Users Reside). Remove Authenticated Users from Security Filtering, add the Security Group with specific users. Would that be a certain guarantee that ONLY the users in the Security Group would get the Pac File address in I.E. settings.   

I cannot be in a situation where ALL users pick up the Pac file entry in I.E. that would be a disaster.  

Any thoughts / suggestions / help / would be gratefully received.    

Regards.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-15*

Security filtering of a GPO allows you to limit what users or computers are hit by the GPO settings and allows you to delegate the administration of the GPO. To target a user or computer you must assign Read and Apply permissions to the user/computer or a group of which they are member.    

Yes you can create a Security Group with specific users in the group. Here is a link as well to help you out.    

Create, edit, or delete a security group in the Microsoft 365 admin center    

https://learn.microsoft.com/en-us/microsoft-365/admin/email/create-edit-or-delete-a-security-group?view=o365-worldwide    

Active Directory Security Groups    

https://learn.microsoft.com/en-us/windows/security/identity-protection/access-control/active-directory-security-groups    

---    

--If the reply is helpful, please Upvote and Accept it as an answer--

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-23*

It looks good, just confirm that no other group has the apply group policy permission.  You can leave the policy blank and apply the policy to the user or test OU. You can then confirm that it will be applied to the selected machines/users that are.members of the group, they will try to apply the policy but will failed with a filtered status, because the policy is empty.  

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-22*

Sorry Just thinking - one more question.  

Is it at all possible to edit the Users Configuration information and link the GPO directly at a computers OU?  

Create a Security Group to include Specific Users and change the permissions of the GPO under the delegation tag? This way i would avoid all contact with the Users OU at the top level. (would that work)?  

Just a thought...

## Answer (community) — community member

*upvotes: 0 · updated: 2021-11-22*

Hi Gary,  

Thank you very much. I believe this is exactly what i have been looking to achieve.  

Will let you know how it goes - i hope to put live next week,  

Once again regards.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-11-19*

Hi,  

Not all setting are available in both user and computer sections of GPOs and I think have found one that is not available in both.  

As for using groups to target specific users or workstations, yes this is an acceptable option and is intended functionality by design. You don't need to remove the existing groups, you just need to remove the 'Apply Policy' permission from the currently assigned groups, add your new group and assign 'Apply Policy' permission to it.  I would suggest you test the changes in a separate OU before applying the new GPO to your main user OU.  

Gary.  

Gary. .
