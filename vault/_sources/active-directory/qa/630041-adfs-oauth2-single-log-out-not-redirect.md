---
title: "ADFS oauth2 Single log-out not redirect"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/630041/adfs-oauth2-single-log-out-not-redirect
question_id: 630041
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS oauth2 Single log-out not redirect

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/630041/adfs-oauth2-single-log-out-not-redirect (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Sir/Madam,    

When sign out from web portal and successful cleared cookies during ADFS oauth Single log-out, but the redirect still keep at AD FS Single log-out page and not redirect that after gived parameter id_token_hint and post_logout_redirect_uri (before added LogoutUri), May i know any wrong step during the single log-out that discontinue process or the step is just over?    

Document from below link:    

(https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/development/ad-fs-logout-openid-connect)    

p.s Using Mircorsoft server 2019 ADFS 4.0.    

Regards,    

KuSai

## Answer (community) — community member

*upvotes: 0 · updated: 2021-12-13*

Hi Piaudonn,    

Situation    

As previous capture are all setup at on-premise exchange server 2019, our portal using AD FS OAuth Single sign-on was successfully done and clears the authentication state well after Single logout, that meant when enter again AD FS OAuth is ready for next login.    

Problem    

When we given parameter id_token_hint and post_logout_redirect_uri to AD FS Single logout, but not redirect action to our portal( parameter setup in LogoutUri in photo 2 ). Only hold as AD FS login page ( Because of tiny difference from graph OAuth that graph will redirect back to our portal ).    

So, is that important of our server hostname (remove data) is using?    

If yes, i will clone the environment for testing this case.    

Enclosed below capture with missing :    

Photo 1 : On-premise AD FS server 2019 Hotfix state :     

    

Photo 2 : On-premise AD FS server 2019 LogoutUri :    

    

Regards,    

Carl

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-12-10*

Screenshots of Fiddler traces aren't usefull most of the time...I meant an actual trace from which you remove or rather replace data with bogus stuff (you can edit the frame and replace FQDN by contoso.com, access tokens by a random string and credentials by *** or something similar). If you're not comfortable with that, that's fine, but it will make the troubleshooting a longer and not always efficient.     

Make sure you have added the URI in the right places, this is described here: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/development/ad-fs-logout-openid-connect#client-configuration are you all set from that perspective?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-12-09*

Could you share a sanitized Fiddler trace?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-11-22*

If you are using an external claim provider in this config, note that there was a bug in ADFS 2019 which was corrected with the following update:  

https://support.microsoft.com/en-us/topic/september-21-2021-kb5005625-os-build-17763-2210-preview-5ae2f63d-a9ce-49dd-a5e6-e05b90dc1cd8  

Addresses an issue that fails to apply the post_logout_redirect_uri= parameter when you use an External Claims Provider.  

Maybe you are in this case...
