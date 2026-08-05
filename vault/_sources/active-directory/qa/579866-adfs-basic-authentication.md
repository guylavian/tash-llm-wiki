---
title: "ADFS  basic authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/579866/adfs-basic-authentication
question_id: 579866
fetched: 2026-07-25
answer_count: 12
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Microsoft Moderator", "Q&A User"]
answer_author_affiliations: ["MicrosoftEmployee"]
---
# ADFS  basic authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/579866/adfs-basic-authentication (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,     

When my web application is sending the browser to ADFS for authentication,  ADFS  is challenging the user with "BASIC Authentication"    

As a result, browser is asking user to provide username and password.    

My problem is,  if I am using  Firefox  I get the standard HTML basic-auth popup  as attached in the screen-shot.    

However,  if I am using  Edge then  I am seeing the native "windows security"  popup as attached in the screen-shot.    

My understanding is that this is the  default interpretation of Edge browser to resolve basic-authentication.    

I do not want edge to behave this way.    

Is it possible to configure edge to  take the standard html popup route ??

## Answer (community) — community member

*upvotes: 1 · updated: 2021-10-07*

Hi,    

If you are not going to use IWA, you might want to go to your ADFS server and disable Windows Authentication and allow forms authentication so that you don't get that authentication pop up. That Authentication Window is a Basic Authentication Popup because Negotiate (Kerberos, then NTLM) has failed.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-07*

Thanks @Nahuel Vacca       

No, I can not disable Windows Authentication.    

But when Windows Authentication  fails (because of any reason which is not important),  I want user to see pure HTML Basic-authentication popup as fallback.    

How can we do that ?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-10-07*

I guess I did not explain properly.  

Yes, you are right. Meaning  ADFS is configured to first try Integrated Windows Authentication.  

It will definitely fail in my case.  

So when it fails, what is the fallback authentication ?  

My understanding is it is  "Basic Auth"  

and for that I want the pure HTML based basic-auth popup.  

I do not want  "windows security" popup.  

Do you  think it is possible ?

## Answer (community) — Microsoft Moderator [MicrosoftEmployee]

*upvotes: 0 · updated: 2021-10-07*

This is not basic authentication, it is likely a Integrated Windows Authentication, not a basic auth.    

The troubleshooting steps are available here: https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/troubleshooting/ad-fs-tshoot-iwa

## Answer (community) — community member

*upvotes: 0 · updated: 2021-10-06*

Hello @testuser7       

Try below steps and see if this is the experience you are looking for    

You could open Internet Options and check the User Authentication option:    

Type "Internet Options" in the search box next to the Start menu button.    

Open Internet Options and click on Security tab.    

If the site is in Internet zone, click on Internet and under Security level click on Custon level.    

Scroll down for User Authentication and check if you have checked Prompt for user name and password.    

Choose other options if you have checked Prompt for user name and password.    

Click OK, Apply then restart the browser to try again.
