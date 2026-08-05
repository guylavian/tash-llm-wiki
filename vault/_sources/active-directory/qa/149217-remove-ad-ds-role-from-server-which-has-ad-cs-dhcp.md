---
title: "Remove AD DS role from server which has (AD CS, DHCP, IIS)"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/149217/remove-ad-ds-role-from-server-which-has-ad-cs-dhcp
question_id: 149217
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Remove AD DS role from server which has (AD CS, DHCP, IIS)

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/149217/remove-ad-ds-role-from-server-which-has-ad-cs-dhcp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,  

I got a question.  

I have a domain controller server that has -> AD DS, AD CS, DHCP, IIS roles. I installed a new DC in this domain. IIS role is for certificate Authority.  

I need to remove AD DS role from old server that has AD CS and DHCP roles.  

My plan:  

On old DC:  

Backup AD CS - then remove AD CS role, but what to do with IIS ? Because it's related to CA.  

Remove AD DS role  

Restart server - add AD CS role and return it from backup.  

Is this will work?  

And what about DHCP? - could i remove AD DS without removing DHCP?  

Also i have domain trust and this server IP is figuring out there.. how could i be sure that after removing AD DS role from this server trust between domains will be working?  

Also i have installed new AD servers and promoted them to DC.  

How could i reconfigure DNS so workstations will be using new AD DC DNS not old ones that is now?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2020-11-05*

Hello @EduardsGrebezs  ,    

Thank you for update.    

Based on our experience, there is no effect for transferring FSMO roles.     

We can place them on one DC according to your needs and requirement.    

Usually, we recommend we can place them on a DC with better server hardware performance.    

References:    

Transfer or seize FSMO roles in Active Directory Domain Services    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/transfer-or-seize-fsmo-roles-in-ad-ds    

FSMO placement and optimization on Active Directory domain controllers    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/fsmo-placement-and-optimization-on-ad-dcs    

Hope the information above is helpful. If anything is unclear, please feel free to let us know.    

Best Regards,    

Daisy Zhou

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-04*

Hi,  

On this server where is DHCP - i also got configured PXE - after moving FSMO roles from old DC will this impact my DHCP settings on PXE and all other?  

Moving fsmo roles to another domain controller doesn't impact DHCP , PXE and others services.  

Or it could only impact in moment when i remove AD DS role on old DC?  

It can impact, if there is some servers or workstations use this DC as DNS resolver. I recommend you to plan the demotion outside of working hours.  

Please don't forget to mark this reply as answer if it help you to fix your issue

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-11-04*

Thank you for your answer! It will help me alot.    

I have last question. This server on which i want to remove AD DS role installed have all FSMO roles.    

I wand to move FSMO roles to my new AD DC server.     

On this server where is DHCP - i also got configured PXE - after moving FSMO roles from old DC will this impact my DHCP settings on PXE and all other?    

Or it could only impact in moment when i remove AD DS role on old DC? @Anonymous

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-03*

Hi,  

***On old DC:  

Backup AD CS - then remove AD CS role, but what to do with IIS ? Because it's related to CA.  

Remove AD DS role  

Restart server - add AD CS role and return it from backup.  

Is this will work?***  

It should work for AD CS if you want remove AD CS temporary to be able to demote domain controller.   

Don't worry about IIS , you can keep you don't need to remove it.  

And what about DHCP? - could i remove AD DS without removing DHCP?  

Regarding you question about DHCP , the answer is YES. You don't have to remove DHCP to demote the domain   

controller role.  

Also i have domain trust and this server IP is figuring out there.. how could i be sure that after removing AD DS role from this server trust between domains will be working?  

When you change the IP , you should check if the new IP has all required network flow opened for the trust. If the network flows is ok , there is no impact on domain trust.  

***Also i have installed new AD servers and promoted them to DC.  

How could i reconfigure DNS so workstations will be using new AD DC DNS not old ones that is now?***  

Yes you should update the IP of DNS resolver on all members machines (workstation and servers). To lelt them able to resolve the domain DNS name.  

Please don't forget to mark this reply as answer if it help you to fix your issue
