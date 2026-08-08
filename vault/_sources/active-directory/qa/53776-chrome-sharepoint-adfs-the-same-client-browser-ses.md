---
title: "Chrome Sharepoint ADFS the same client browser session has made 6 requests"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/53776/chrome-sharepoint-adfs-the-same-client-browser-ses
question_id: 53776
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-office-sp-server-business", "microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Chrome Sharepoint ADFS the same client browser session has made 6 requests

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/53776/chrome-sharepoint-adfs-the-same-client-browser-ses (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Weird issue. Any insight is highly appreciated. A handful of users complaining about errors when trying to login from chrome to the sharepoint portal via adfs 3.0 sso. Reports started coming after migration to 2016 sharepoint portal. One user had this  

An error occurred  

An error occurred. Contact your administrator for more information.  

Error details  

• Activity ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx  

• Relying party: my-sharepoint-portal  

• Error time: Mon, 19 Jul 2020 18:44:41 GMT  

• Cookie: enabled  

• User agent string: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36  

In adfs saw "MSIS7042 The same client browser session has made 6 requests message" corresponding to the activity ID.   

The user upgraded Chrome to newest version (cleared cache). Same issue. It is only handful of users. I use chrome version 84 and it works.   

I have gone through many forums and the answers don't seem correct. We migrated to sharepoint 2016 over a month ago. Some users had errors fro chrome after that but clearing browser cache helped. For the others issue still persists. We didn't change anything on ADFS except mimic the relying party trust of the previous one.   

FYI ExtendedProtectionTokenCheck  is set to none.   

Some links that I have seen:  

https://social.technet.microsoft.com/Forums/lync/en-US/98b5590e-b700-4dc9-8cc6-98e14b5c9576/sso-for-o365-works-for-ie-11-but-not-chrome-version-63?forum=ADFS   

https://www.vspbreda.nl/nl/ms-office/office-365/solved-adfs-enable-single-sign-on-sso-for-edge-and-chrome-browser/  

The above adds chrome to wiasupporteduseragents list but doesn't work per the user. So not sure this is the right one since I use chrome and it works for me (and for a lot of others).  

https://social.technet.microsoft.com/Forums/en-US/3308946a-a850-459a-9ee5-83e852645887/endless-loop-between-and-wsfed-app-and-adfs-30?forum=ADFS  

is not relevant since it deals with another application.   

Another one that I came across was   

http://iamprogrammerdotnet.blogspot.com/2012/07/same-client-browser-session-has-made-6.html  

But that seems to be changing the token lifetime in sharepoint. Wonder if that would have any repercussions since login works for all except a few chrome users.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-07-28*

Thank you very much for the response. The current claims rule in adfs has the following  

-  pass through all claim values for windows account name  

-  Pass through all claim values for incoming claim type name  

-  Ldap attributes as claims from Active Directory : e-mail-address to E-mail Address, sam-account-Name to User Logon Name, "Token-Groups - Unqualified Names" to Role  

One of the users that I am aware of is a member of 79 groups in AD. I believe there are quite a few cases across the organization (not sure if all are members of large number of groups). How would we be able to fix the issue if it is related to group membership as this happens on Chrome? We could try the solution for this one user and see if that is the case?   

Also curious, this particular user didn't have issues previously and from what I have been told this started sometime after migrating to new sharepoint portal.   

FYI, the test portal works for that user with that same login. The production portal exhibits that chrome issue. (just found out this information)

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-07-28*

In a WS-Fed scenario such like yours, SharePoint is supposed to redirect the user to ADFS for authentication and then the user POST a token back to SharePoint (assuming that the authentication was successful).   

If SharePoint accepts it, it creates a bootstrap cookie and that cookie is used for further access.  

If SharePoint doesn't accept it, or the token isn't valid yet (case of time sync issue between the SharePoint servers and the ADFS servers) or if it cannot make use of it, and can't create this bootstrap cookie, then the user is redirected to ADFS again to obtain a valid token. There is also a known issue if SharePoint rejects tokens which are about to expire. If you reduce the default token lifetime (which is 1 hour) to something a bit too short like few minutes, in that case even a brand new token will be rejected because SharePoint wants something valid for longer. But that's a corner case and all users would be affected.  

Now if clearing the cookies sometimes fixes the issues, it might be an issue with the cookie manager of the browser. Or the cookie is too large and can't be processed. I don't know what SharePoint puts in the cookie. But if there is the group membership information in it, that could explain the size and why not all users are affected. But that also depends on what claims you send to the SharePoint to start with.  

If you capture (sanitize and share) a Fiddler trace, we can maybe narrow down this cookie mystery.
