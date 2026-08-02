---
title: "WSUS GPO - Disable WU Internet Locations also disable Windows Store App Installs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/456233/wsus-gpo-disable-wu-internet-locations-also-disabl
question_id: 456233
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["Mvp"]
---
# WSUS GPO - Disable WU Internet Locations also disable Windows Store App Installs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/456233/wsus-gpo-disable-wu-internet-locations-also-disabl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Everyone,    

Many thanks in advance!    

In the company I work for, we have a GPO for WSUS where I have configured the preference setting "Do not connect to any Windows Update Internet locations" in order to avoid users from accidentally clicking the button to check for updates from internet. However, we can see this preference is also interfering with Windows Store App installs/Updates.    

I am wondering if anyone has come across this before, and would be able to provide some guidance on how to proceed in order to block Windows Updates connection to Internet Locations while still allowing the Windows Store to continue to operate normally for app installs and updates.     

Is there anyway that we can block updates from internet for enforcing WSUS while still keeping the Windows Store fully functional (Online App Install & Updates)?    

    

Kind Regs,    

Bruno

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-30*

@Adam J. Marshall   , @Rita Hu -MSFT   ,     

​We still want to allow for the ​option to "Check for Updates" to be visible. However, we want to block/hide the other button that says "Check online for updates from Microsoft Update".     

An option to block Windows Update from accessing Internet locations is acceptable, but only where it does not remove the Windows Store Online functions, such as Install/Update Apps, etc.    

For reference, you can see the button we need to get rid off highlighted in the screenshot, below:    

    

P.S.: We do have a patch orchestration system in house and our WSUS GPO has the following settings configured at the moment to allow for any approved patches to be automatically downloaded to the computers, then the patch orchestration system would get to install those at specified maintenance windows. Please, see our current WSUS GPO settings, below:

## Answer (community) — Q&A User [Mvp]

*upvotes: 0 · updated: 2021-06-29*

Set the policy " Do not connect to any Windows Update Internet locations " back to Not Configured    

If you're trying to prevent users from possibly clicking the "Check for Updates" link, hide the Settings panel for Windows Update instead.    

https://learn.microsoft.com/en-us/troubleshoot/windows-client/group-policy/use-settings-app-group-policy    

windowsupdate-action or windowsupdate (depending on what you want to hide)    

https://www.howtogeek.com/308489/how-to-hide-pages-from-windows-10s-settings-app/
