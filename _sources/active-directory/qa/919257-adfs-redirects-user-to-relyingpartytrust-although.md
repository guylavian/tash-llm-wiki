---
title: "ADFS redirects User to RelyingPartyTrust although wrong username"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/919257/adfs-redirects-user-to-relyingpartytrust-although
question_id: 919257
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services", "windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS redirects User to RelyingPartyTrust although wrong username

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/919257/adfs-redirects-user-to-relyingpartytrust-although (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello guys,    

On our adfs-server we have a few relying-party-trusts - but one have a special behaviour (let it call "App123")    

Expected normal behaviour:    

-  Open the the website of that App123    

-  user will be redirected to our ADFS-server    

-  enter your correct username/password    

-  redirect to App123    

The point is, when entering a wrong username, the ADFS-Server also redirects the user to the App123.    

For other relying-party-trusts the ADFS-Server shows message wrong username, but for this RPT the ADFS-Server still redirects to the App123 and there we get an error.    

When entering a correct username + wrong password, the ADFS-Server shows an error. But entering a Username i.e. "Notavailable@keyman  .com" which does not exist in our "domain.com", then the ADFS-Server redirects that user.    

Does someone know how we can crosscheck why the ADFS-Server still redirects the user with wrong username?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2022-07-12*

AD FS just authenticates the user, issues a token and then redirects the user back to the SP.    

As long as the logon is successful, and the account allowed, you get redirected.    

If you type a wrong username and password and still gets redirected, we have a big issue indeed. But we'll need to see some logs. Ideally a Fiddler trace?

## Answer (community) — community member

*upvotes: 0 · updated: 2022-07-11*

Hi there,     

It could be any number of things that is causing this issue.     

-Web application is holding onto identity (or cookie isn't getting cleared)    

-ADFS is sending the same user token for both users (unlikely)    

-ADFS is caching user identity    

-Proxy between ADFS and web application is caching token    

You can use fiddler to watch the token move across the wire, and that should tell you what is happening exactly.     

You can try some additional troubleshooting steps grin this article     

https://learn.microsoft.com/en-us/troubleshoot/windows-server/identity/troubleshoot-ad-fs-sso-issue    

I hope this information helps. If you have any questions please let me know and I will be glad to help you out.    

--------------------------------------------------------------------------------------------------------------------------------    

--If the reply is helpful, please Upvote and Accept it as an answer--
