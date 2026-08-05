---
title: "WIndows DC NTLM ERROR Apache SSPI"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2713596/windows-dc-ntlm-error-apache-sspi
question_id: 2713596
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# WIndows DC NTLM ERROR Apache SSPI

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2713596/windows-dc-ntlm-error-apache-sspi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We use Apache 2.x as a web server with SSPI as a Single SignOn authentification for our users. When we create a new web application, we usually configure it as follow in the hhtp.conf file:

<VirtualHost *:80> 

ServerName somapp 

DocumentRoot "C:/www/someapp 

<Directory C:/www/someapp> 

Order Allow,Deny 

Allow from all 

</Directory> 

<IfModule mod_auth_sspi.c> 

<Location />

AuthName "A Protected Place" 

AuthType SSPI SSPIAuth On 

SSPIAuthoritative On 

SSPIOfferBasic On 

SSPIOmitDomain Off 

require valid-user 

</Location> 

</IfModule> 

</VirtualHost>

When the user arrive at the site, the users is automatically logged in to the app. All was ok until last week.  

Now, the authentification window pops-up

And the following error 

[Wed Mar 30 08:52:53 2016] [error] [client 127.0.0.1] (OS 1326)Échec d’ouverture de session : nom d’utilisateur inconnu ou mot de passe incorrect. : user xxxx01: authentication failure for "/"

[Wed Mar 30 08:52:53 2016] [error] [client 127.0.0.1] (OS 1326)Échec d’ouverture de session : nom d’utilisateur inconnu ou mot de passe incorrect. : user xxxx01: authentication failure for "/error/HTTP_UNAUTHORIZED.html.var"

This problem apears to have started when we applied the most recent windows update patch on our DC. We have since uninstalled the updates but the problem remains. The problem appears on all our Apache servers (on my local machine and on two servers)

Here's some details about our environment:  

-  Three apache 2.x servers on Windows 7 Pro, Windows 2008 R2 and Windows 2012 R2  

-  Two DC's, both Windows 2008 R2  

We've tried a variety of changes to the mod_auth_sspi parameters (the domain, ip adress, etc.) but we have not been successful. Any help would be appreciated.

## Answer (community) — community member

*upvotes: 0 · updated: 2016-04-10*

Hello,

Thank you for contacting Microsoft support. 

The present forum is dedicated to the French speaking community. 

To post in English, please do refer to the English speaking forum:

http://answers.microsoft.com/en-us.

Otherwise we invite you to post your issue in French.

Kind regards,

Thanh
