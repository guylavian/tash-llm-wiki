---
title: "GPO WSUS In Windows 11 not is applied"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1374259/gpo-wsus-in-windows-11-not-is-applied
question_id: 1374259
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-intune-configuration-manager-updates", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor", "Mvp"]
---
# GPO WSUS In Windows 11 not is applied

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1374259/gpo-wsus-in-windows-11-not-is-applied (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hey Guys

I create a GPO for WSUS, but in a machine with windows 11 not has beem applied.

Look my configuration of GPO in the server:

The GPO has been applied in the computer;

but see how is the polices on computer:

Sorry that my Windows is in Portuguese :(

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-01-17*

I resolved it by formatting the server, updating it to the maximum and configuring WSUS from scratch.

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2023-10-04*

Follow my guide. Part 4 and part 5.

https://www.ajtek.ca/wsus/how-to-setup-manage-and-maintain-wsus-part-4-creating-your-gpos-for-an-inheritance-setup/

You likely have an ORDER problem with existing GPOs

Another good page to help would be 

https://www.ajtek.ca/wsus/client-machines-not-reporting-to-wsus-properly/

which gpresult /h gpo.htm is likely your real troubleshooting command as it produces a nice html output that gives you the RSOP of the device.

But likely part 4/5 will be your fix.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2023-09-22*

Hi,

Thank you for posting in Microsoft Q&A forum.

1,The local group policy will be overridden by GPO. We can run the gpresult command with administrator right to check if the policy is applied on the client. As shown below:  

2,We can also check the WSUS related registry keys to check if it is configured correctly. 

HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate

Thanks for your time. Have a nice day!

Best regards,

Simon

If the response is helpful, please click "Accept Answer" and upvote it.

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
