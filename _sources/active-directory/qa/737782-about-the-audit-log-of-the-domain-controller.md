---
title: "About the audit log of the domain controller"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/737782/about-the-audit-log-of-the-domain-controller
question_id: 737782
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-set-up-install-upgrade", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# About the audit log of the domain controller

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/737782/about-the-audit-log-of-the-domain-controller (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Windows Server 2019: I am operating a Domain Controller.  

I have enabled the audit settings below, but after a certain period of time, the settings return to the default settings.  

Policy / Windows Settings / Security Settings / Local Policy / Audit Policy  

Account management audit  

Define the settings for these policies  

Success: Valid  

Failure: Valid  

Auditing directory service access  

Define the settings for these policies  

Success: Valid  

Do you know any possible causes or remedies?  

Thank you.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-02-17*

Hello @ryosk25  ,    

You should check if you have a GPO that override your setting by using gpresult /H gpreport.html.    

If it's the case you should create a new GPO linked on the domain controllers OU with a precedence of 1 if possible by using group policy management console (GPMC.MSC) and configure the audit settings as you wish    

Regards,

## Answer (community) — community member

*upvotes: 0 · updated: 2022-02-17*

Hello @ryosk25       

You may need to check the Default Domain Controllers Policy: A default GPO that is automatically created and linked to the domain whenever a server is promoted to a domain controller. This GPO represents the default policy that is applied to all domain controllers in the Domain Controllers container. Since the domain policies prevail over local policies, they will rewrite your settings.     

To edit this GPO you need to enter the group policy management console from the DC (running GPEDIT from elevated command prompt) and find the GPO from the folders in the left side menu. Once these policies are applied there, will not revert.     

More information about precedence and group policy hierarchy: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-gpod/566e983e-3b72-4b2d-9063-a00ebc9514fd    

Hope this helps with your query,    

--    

--If the reply is helpful, please Upvote and Accept as answer--
