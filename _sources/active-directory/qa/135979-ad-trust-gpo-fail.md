---
title: "AD Trust, GPO Fail"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/135979/ad-trust-gpo-fail
question_id: 135979
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other"]
answer_author_roles: ["Microsoft Moderator"]
---
# AD Trust, GPO Fail

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/135979/ad-trust-gpo-fail (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Community  

We have a problem similar as described in the report:  

https://social.technet.microsoft.com/Forums/en-US/c7641c89-76d5-4f44-aced-e492638f7dea/oneway-crossforest-roaming-profile-and-gpo-processing-issues?forum=winservergen  

Scenario  

Two domains connected to each other via one way trust.  

In between is a firewall.  

Firewall --> Off, all computers can communicate  

• User 1 in domain A should log on to the computer in domain B. --> Works  

• User 1 is a member of a group (Global) in Domain A, this group (Global) in Domain A is a member of a group (Domain Local) in Domain B, Group (Domain Local) in Domain B Is linked to GPO via the Security Filter  

• If user 1 in domain A logs on to computer in domain B, the GPO should be used --> works  

Firewall --> On, only communication between DC A and DC B allowed.  

• User 1 account removed from computer in domain B  

• User 1 in domain A should log on to the computer in domain B. --> Works  

• If user 1 in domain A logs on to the computer in domain B, the GPO should be used --> does not work  

• Gpupdate / force fails  

C: \ Users \ 1> gpupdate / force  

Updating Policy ...  

User policy could not be updated successfully. The following errors were encountered:  

The processing of Group Policy failed. Windows could not resolve the user name. This could be caused by one of more of the following:  

a) Name resolution failure on the current domain controller.  

b) Active Directory Replication Latency (an account created on another domain controller has not replicated to the current domain controller).  

Computer Policy update has completed successfully.  

To diagnose the failure, review the event log or run GPRESULT / H GPReport.html from the command line to access information about Group Policy results.  

C: \ Users \ 1>  

The solution as shown in the description of the problem by opening the firewall is unfortunately not an option because the computers in domain B are not allowed to communicate directly with the DC in domain A.  

Question,  

Does computer in domain B have to communicate directly with DC in domain A?  

If not, is there a workaround for this? Unfortunately, the topic is not addressed in any of the explanations.  

Thank you in advance!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-26*

Hi,  

thanks for your answer.   

This is clear, and for a normal environment it makes sense if the Client can directly contact the DC in Domain A to request those Policy’s.  

However...the Access is restricted for good reason and not all the 300 clients in Domain B should contact the DC in Domain A directly.  

GPOs from Domain A are not relevant for B. Target would be that the GPOs from Domain B get rolled out when user from Domain A login.  

When I do an "whoamI /groups" i can see all group member ships   

So would it be possible to swap this GPO processing that he tries just to contact the Domain B DC to check for GPOs regardless what would be linked in Domain A.  

Many thanks for your help!

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-26*

Hi,  

   

Just checking in to see if the information provided was helpful. Please let us know if you would like further assistance.  

   

Best Regards,  

Vicky

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-10-22*

Hi,  

If you want apply a GPO on computer in domain B when a user in domain A try login, the computer from domain B need to contact one of domain controller in domain A to check user properties in order to apply user GPO settings.   

So if you want apply the GPO  successfully , you have to open network flows between computer in domain B and domain controllers in domain A.  

Please don't forget to mark this reply as answer if it help you to fix your issue
