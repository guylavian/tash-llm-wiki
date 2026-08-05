---
title: "Webex Teams SSO ADFS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/160785/webex-teams-sso-adfs
question_id: 160785
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# Webex Teams SSO ADFS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/160785/webex-teams-sso-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Community,    

I dont know if somebody was facing the same issue but I will give a try and ask you..    

I have implemented SSO, Webex Teams in dCloud and this is the scenario:    

User Cholland is loging to the system with dcloud.cisco.loc or dcloud.cisco.com and in the Cloud is synced with Cisco Directory Connector with the email address. In my case it was ******@cb150.dc-03.com.    

 I have configured the ADFS and provided him alternative ID to login/authenticated with the mail address.    

    

If I try to login I will all time get the message to login again and authenticated.    

    

If the user has user logon name the same like email everything works just fine.    

    

    

If I turn off the windows authentication i will get a page from ADFS and Im able to use the email to login to system.    

 If I turn on the windows authentication and the mail address is the same like logon name everything works just fine.    

 If I turn on the windows authentication and the mail address is different from logon name the authentication doenst work. What I have to do to bring this working?    

Do you have somebody any idea what I have to setup on ADFS to have a working SSO if the user has .loc or .cisco.com user logon name?     

Thank you so much!

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2020-11-14*

Windows Integrated Authentication uses the UPN or the DOMAIN\samaccoutname format. Not the alternate login ID you set.   

From your link:   

Wenn die integrierte Windows-Authentifizierung (WIA) ausgeführt wird (z. b. Wenn Benutzer versuchen, über das Intranet auf eine Unternehmens Anwendung auf einem in eine Domäne eingebundenen Computer zuzugreifen, und AD FS Administrator die Authentifizierungs Richtlinie für die Verwendung von WIA für das Intranet konfiguriert hat), wird der UPN für die Authentifizierung verwendet.  

From the English version:  

When Windows Integrated Authentication (WIA) is performed (for example, when users try to access a corporate application on a domain-joined machine from intranet and AD FS administrator has configured the authentication policy to use WIA for intranet), UPN isused for authentication.
