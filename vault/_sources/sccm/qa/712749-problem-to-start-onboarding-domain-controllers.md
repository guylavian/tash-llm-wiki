---
title: "Problem to start onboarding domain controllers"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/712749/problem-to-start-onboarding-domain-controllers
question_id: 712749
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-other-l1"]
---
# Problem to start onboarding domain controllers

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/712749/problem-to-start-onboarding-domain-controllers (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi team,    

Could please help me with the following issue?    

I've successfully installed the Microsoft Windows Defender on my Domain Controllers but I'm not able to onboarding it with the "Windows Defender ATP LocalOnboardingScript". It fails when try to start the SENSE service.    

    

The same procedure worked on another Servers from our network.     

Can I onboarding domain controllers or there is a limitation here?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-01-28*

Hello @Vinicius Santos       

I would start recommending from the official article: https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/troubleshoot-onboarding?view=o365-worldwide    

Check the service health (sc query sense command). Make sure it's not in an intermediate state ('Pending_Stopped', 'Pending_Running') and try to run the script again (with administrator rights).    

If the device is running Windows 10, version 1607 and running the command sc query sense returns START_PENDING, reboot the device. If rebooting the device doesn't address the issue, upgrade to KB4015217 and try onboarding again.    

If the message of the error is: System error 577 or error 1058 has occurred, you need to enable the Microsoft Defender Antivirus ELAM driver, see Ensure that Microsoft Defender Antivirus is not disabled by a policy for instructions.    

Hope this helps with your query,    

-----------    

--If the reply is helpful, please Upvote and Accept as answer--
