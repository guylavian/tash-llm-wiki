---
title: "3rd party cookies gpo edge"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/805389/3rd-party-cookies-gpo-edge
question_id: 805389
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 2
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# 3rd party cookies gpo edge

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/805389/3rd-party-cookies-gpo-edge (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,  

I would like to allow 3rd party cookies only for specific site on Edge browser via GPO.  

Can I achieve it using this GPO: User Configuration\Administrative Templates\Microsoft Edge\Content Settings\allow cookies on specific sites and then the name of the site?It will allow the 3rd party cookies also?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-08-25*

I know this thread is old but I just ran into this myself and since no actual solution is listed here I though I'd post in case anyone else has this issue.    

You can block 3rd party cookies with the setting     

Admin Templates/Microsoft Edge/Block third party cookies = Enabled    

You can provide exceptions for specific third party cookies on specific sites with the setting    

Admin Templates/Microsoft Edge/Content Settings/Allow cookies on specific sites    

The setting should be comma separated with the site you want to allow to set 3rd party cookies first then the actual site you are on second.  For instance, I need accounts.google.com to be able to set third party cookies at edpuzzle.com so the sign in with Google button works so my setting is    

```
[*.]accounts.google.com,[*.]edpuzzle.com
```

This works in a Chrome GPO as well, same settings but Google/Google Chrome instead of Microsoft Edge.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-07*

screenshot is from my private laptop.Just wanted to explain how it looks on my working environment where I use gpo.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-06-07*

hello @Limitless Technology       

I created that policy cookiesallowedforurls and configure cookies- selected Block only third party cookies.     

Third party cookies are blocked by GPO point 1 on screenshot     

Cookies allowed for urls - exception appeared point 2 on screenshot    

but user can still add some websites (point 3a on screenshot )and I wondering why and how to block this for users.    

Also under the website added by user manually appears "including third party cookies on this site".     

My questions are. How prevent user from  adding sites manually ?    

Why "including third party cookies on this site" doesnt appear under site added by GPO.

## Answer (community) — community member

*upvotes: 0 · updated: 2022-04-15*

Hello @Anonymous       

Adding the domain/website will allow any cookies from that domain, as explained in the next article:    

https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies#cookiesallowedforurls    

However, it is important to check the policy in Administrative Templates>Windows Components>Microsoft Edge>Configure Cookies with value 1.Block only 3rd-party cookies in order to block the rest of 3rd Party cookies, and the previous policy will override for the specific allowed domains/websites    

Hope this helps with your query,    

------------    

--If the reply is helpful, please Upvote and Accept as answer--
