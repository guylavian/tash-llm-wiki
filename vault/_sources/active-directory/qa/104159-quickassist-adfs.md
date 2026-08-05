---
title: "QuickAssist + Adfs"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/104159/quickassist-adfs
question_id: 104159
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
answer_author_roles: ["Q&A User"]
---
# QuickAssist + Adfs

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/104159/quickassist-adfs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

We have a office 365 Tenant. Run ADFS. We have all our domains federate in Azure AD.    

We would really like to use quickassist to help our employees but are expericing a weird issue we can't seem to figure out.    

When trying to offer support to an employee, i can hit the button offer assistance. We log in using our company email adres..    

We then get a popup (webbrowser) to log into our company STS page. Once i fill in my credentials a page opens I can only see the option to fill in a code.    

I do not get quickassist up with a code to provide someone to help them.    

If i make a cloud only user in azure AD and use a domain which is not federate, the following happens (this is how it should work)    

-I open quick assist and click on the button "offer assistance"    

-I log in using my email adres ******@on.microsoft.com (not federate + cloud only user)    

-I do not get redirected to a brwoser.. quick assist start whith the prompt of a code and a timer showing how long the code can be used.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-03-05*

Same problem, only when using company email address with ADFS.  

Using "Micrososft Account" (Private) or Azure AD only it works perfectly.  

Someone know how to solve this?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-09-25*

Hi,  

The symptoms are the same that what I just had.  

All I had to do was to disconnect and re-add the o365 account in «Access work or school» in Windows 10 settings. ADFS was activated after the account was already configured on my PC.   

Be sure to sign out of MS applications that use the o365 account before disconnecting. For example teams gave me "Your organization has deleted this device" error by not signing out.  

I hope it will help you.
