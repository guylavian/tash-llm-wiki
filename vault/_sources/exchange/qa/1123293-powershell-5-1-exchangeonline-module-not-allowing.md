---
title: "PowerShell 5.1 ExchangeOnline Module not allowing SSO authentication. \"Browser is out of date\""
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1123293/powershell-5-1-exchangeonline-module-not-allowing
question_id: 1123293
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online"]
---
# PowerShell 5.1 ExchangeOnline Module not allowing SSO authentication. "Browser is out of date"

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1123293/powershell-5-1-exchangeonline-module-not-allowing (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I'm currently utilizing PowerShell 5.1 to run ExchangeOnline to do several admin things that the Exchange Admin Center doesn't seem to allow or utilize. Normally when I try to Connect-ExchangeOnline it opens up a browser and asks me to use my SSO creds to log in to the admin center to make sure I'm able to connect. Lately though it's not been letting me log in and this is causing serious workflow issues. My senior tech doesn't have a clue what it could be about. I've made sure that my default browser for everything is Edge (it's trying to open an old version of explorer (which should also be up to date) from what I can gather) in settings. I just can't seem how to get it to proc correctly.     

    

Clicking the link to the aka.ms/mysecurityinfo throws me into a login loop where I'm asked to SSO into my admin account then asked to set up an MFA app which I have authentication through my phone and don't want to use an application, so I select "skip setup" in a normal login situation this would then load whatever I'm logging into. With this situation it pushes it back to the screen after I enter my password which says, "We need more information regarding your account" (which then selecting "Okay" pushes me back into the mfa "set up app" screen) and I can't ever be "logged in" to Exchange to utilize in PowerShell.     

It should be noted that I can use and login to PowerShell 7 but the code I'm running doesn't function correctly in it and the rest of my team is using 5.1 so I need to stay cohesive in my environment.     

If anyone has any advice, I'd be grateful.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-14*

Found a solution.

Setting the reg key as specified here resolved the issue for me.

https://support.microsoft.com/en-us/topic/error-this-web-browser-does-not-support-javascript-or-scripts-are-being-blocked-when-adding-a-google-workspace-account-b7cbc25e-5b2d-459a-97b8-c8b6adc7b2d4

HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\Main\FeatureControl\FEATURE_BROWSER_EMULATION

Set OUTLOOK.EXE DWORD to Decimal 11001 and restart Outlook.
