---
title: "Active directory administrative center password policy do not completly apply to WIndows 10"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/607649/active-directory-administrative-center-password-po
question_id: 607649
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Q&A User"]
---
# Active directory administrative center password policy do not completly apply to WIndows 10

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/607649/active-directory-administrative-center-password-po (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

DC is 2012r2  

Client is WIndows 10 21H1  

The current default domain policy has not enabled "password must meet complexity requirements" and has a short minimum length.  

In Active Directory Administrative Center i have made a new password policy which require "password must meet complexity requirements" plus it expires and has a minimum length. This policy is applied to a Group where i have added a test user.  

Everyting except the "password must meet complexity requirements" is getting applied to the Windows 10 machine. If i press Ctrl-Alt-Del i can set a new password without any special charecters.  

gpupdate /force and several reboots to the Win10 machine has been done.  

Any clue why password must meet complexity requirements is not applied to the machine?  

Regards  

Robert

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-29*

Hi @Robert Vilhelmsen       

I'm going to make a couple of assumptions from your question, please correct if these are wrong.    

-  You have a domain password policy with no complexity requirement    

-  You have created a FGPP which specifies complexity requirement and length and assigned to a user via a group     

The domain password policy is delivered by GPO normally in the Default Domain Policy and is applied to all the machines in the domain.  This policy must be applied to the domain controllers for the password policy to be applied.      

Fine Grain Password Policies are created using the Admin centre and are created in AD as an PSO object in the Password Settings container in the default naming context.  These are used by the DC to enforce the password policy when the user changes their password and has no dependency on the GPO delivery at the workstations or DCs.    

From your question, the domain password policy is working and the FGPP are not working as expected.    

Here are a few commands to confirm that settings of each of the password policy options:    

To check the configuration of the domain password policy    

```
Get-ADDefaultDomainPasswordPolicy -identity 
```

Then check if there is a FGPP applied to the user, which will take precedence over the domain password policy    

```
Get-ADUserResultantPasswordPolicy -Identity 
```

This will display which policy is applied to the user and the settings of the policy.  If a FGPP is not set on the user the command returns nothing.    

Gary.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-28*

Hello @Robert Vilhelmsen  ,    

This looks like it might be related to the DC's themselves. It turns out that previously this domain had the GPO setting "Turn off background refresh of Group Policy" enabled in the Domain Policy.    

With this setting enabled it means that a reboot is required to apply Computer Settings whereas normally this would occur whenever GPupdate ran silently in the background every 90 minutes.    

The DC's have not been rebooted since the "Turn off background refresh of Group Policy" policy was disabled so they are stuck with the old GPO setting applied which has Password Complexity disabled.    

Hope this helps with your query,    

------    

--If the reply is helpful, please Upvote and Accept as answer--
