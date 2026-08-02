---
title: "Restricted  RDP GPO for domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1029366/restricted-rdp-gpo-for-domain-controllers
question_id: 1029366
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Restricted  RDP GPO for domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1029366/restricted-rdp-gpo-for-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Guys,    

Would you pls advise is there any possibility to apply restricted RDP GPO only on domain controllers .We would like to control Domain controller via GPO instead of manually adding users into "Remote Desktop Users"    

Requirement is only users which is the part of certain groups they can only access Domain controllers if somebody has added users manually into Built-In "Remote Desktop users" it will be remove automatically.    

Pls let me know if this is possible i have tested with Restricted groups but things not working as expected      

Regards

## Answer (community) — community member

*upvotes: 0 · updated: 2022-10-03*

Hello there,    

You can try the security groups. Security groups can provide an efficient way to assign access to resources on your network.    

You can also configure the "Deny logon locally" user right on the local computer to eliminate the option of logging on one or a few computers.    

Group Policy Objects can be configured to restrict privileged access on Domain Controllers. To do this, navigate to Computer Configuration\Policies\Windows Settings\Security Settings\Local Settings\User Rights Assignments. To manage privilege access in GPOs, you must do the following:    

Deny network access to the computer    

Deny logon as a batch job    

Deny logon as a service    

Deny logon through Remote Desktop Services    

Active Directory security groups https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups    

How to restrict use of a computer to one domain user only https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/restrict-use-one-domain-user-only    

---------------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-10-01*

Hi,    

Here is an article that explains how to configure remote desktop access for non-admins.  This approach is not using restricted groups, as membership is controlled in the AD group which can only be changed by users that have been granted access.    

http://woshub.com/allow-non-administrators-rdp-access-to-domain-controller    

This didn't work as documented in my test environment, but mine is not really standard any more.  If this doesn't work for you let me know and I can provide the details I used to get it working in my environment.    

Gary.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-09-29*

Hi,     

Restricted groups are an ideal solution for this scenario, what was the issue you experienced?    

You could also look at GPP group management to do the same thing.    

Gary.
