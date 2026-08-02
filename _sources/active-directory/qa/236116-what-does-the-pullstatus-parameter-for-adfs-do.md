---
title: "What does the `pullStatus` parameter for ADFS do?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/236116/what-does-the-pullstatus-parameter-for-adfs-do
question_id: 236116
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# What does the `pullStatus` parameter for ADFS do?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/236116/what-does-the-pullstatus-parameter-for-adfs-do (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi everyone!  

I have encountered an interesting issue, on a corporate ADFS which i don't have much access to (no logs, not sure about version etc.), where two parameters are being added when navigating to to authorize endpoint:  

https://path-to-adfs-server/adfs/oauth2/authorize?response_type=token&client_id={client_id}&redirect_uri=https%3A%2F%2Flocalhost%3A3000&scope=read&resource=myresource&state=f02bf58ac7994e5af1b1a3b62d6a2dd8  

The two query parameters that are being automatically added are:  

-  pullStatus=0  

-  client-request-id={uuid}  

My question is: are these standard, but undocumented, ADFS parameters? Or is this something custom? I can't find any scripts or HTTP redirect that is redirecting me with these parameters, so i'm thinking it's something running on Windows adding it (like some sort of SSO? Bare with me, im new to all of this :-)) Also when doing searches for these parameters i end up with very few or 0 hits. E.g. i found this blog post mentioning pullStatus=0 but doesn't seem to be seem to be related to my issue.  

The issue is that i can't silently refresh tokens through an iframe because X-Frame-Options is always set to deny even though i clearly have a session cookie for the ADFS server and already fetched credentials interactively. If i add `&pullStatus=0` to the end of the silent refresh request all is good and no X-Frame-Options header is sent. Also if i open a popup to "silently" refresh it all works (popup opens and closes immediately without user interaction), because X-Frame-Options doesn't affect popups.   

I'm curious to what pullStatus actually is/does. In our production environment it isn't needed so i'm trying to figure out why it is needed in our test environment.

## Answer (community) — Q&A User [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-01-26*

Hi @Linde, Oscar  , The pullstatus=0 flag is used to skip PRT fetching. A Primary Refresh Token (PRT) is a key artifact of Azure AD authentication on Windows 10, Windows Server 2016 and later versions, iOS, and Android devices. It is a JSON Web Token (JWT) specially issued to Microsoft first party token brokers to enable single sign-on (SSO) across the applications used on those devices. I cant really think of a good reason why it would interfere with silently refreshing tokens.
