---
title: "GPO Wifi for login - after login wifi is stuck \"Connecting\" - Certificate?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/233755/gpo-wifi-for-login-after-login-wifi-is-stuck-conne
question_id: 233755
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# GPO Wifi for login - after login wifi is stuck "Connecting" - Certificate?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/233755/gpo-wifi-for-login-after-login-wifi-is-stuck-conne (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have deployed enterprise wifi that logs in via radius/NPS when users login. I have used a purchased SSL just "radius.domain.com" and using this. Certificate is valid from what I can see.  

When users connect at login they get a "confirm" prompt for the certificate to trust it. Once logged in at desktop they have no network access and the wifi status is "Connecting".  

Is this due to the certificate? If so is there a way to fix this? Am I using incorrect type certificate? Am I meant to deploy it out to be trusted somehow? Can't fnd info on what should affect every single person ever?  

I have played with all options in the GPO around the cert verification, either don't verify or verify with my domain radius.domain.com and every cert authority ticked, still prompts to accept cert on clients..

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-18*

Hi ,    

Does anything appear for NPS in the Windows Security Event log on the NPS server.  It will usually say why the request has been denied or NPS granted access to a user.    

Here is an article talking about tips for troubleshooting 802.1X connections, you may have a look:    

https://www.networkworld.com/article/2160056/tips-for-troubleshooting-802-1x-connections.html    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

Best Regards,    

Candy    

--------------------------------------------------------------    

If the Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
