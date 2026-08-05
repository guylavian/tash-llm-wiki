---
title: "Outlook 2019 - Exchange 2016 On Premises - Non-Domain Login"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1153910/outlook-2019-exchange-2016-on-premises-non-domain
question_id: 1153910
fetched: 2026-07-25
answer_count: 11
has_accepted_answer: false
upvotes: 0
qa_tags: ["m365-office-install-redeem-activate-business-platform-windows", "office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
---
# Outlook 2019 - Exchange 2016 On Premises - Non-Domain Login

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1153910/outlook-2019-exchange-2016-on-premises-non-domain (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Just purchased a new laptop that I was not planning on joining to our domain for a remote employee.  Purchased 2019 Office and tried to connect Outlook to our on-premises Exchange Server 2016.  Anyway, entered his information to get outlook setup, and all it does it continuously ask for the password over and over and I cannot get past it.  No error message, nothing in event viewer.  Thinking it was the new laptop, I fired up a virtual machine with Window 11.  Amazingly enough, same problem, continuous request for the password, regardless of the "remember" setting.  Thinking it was Windows 11, fired up a virtual windows 10 machine, and same problem, endless password request.  I had just rebuilt a win10 machine a month ago and had no problems logging in, so I joined the test win 10 to the domain, logged in and Outlook setup like a charm.  Joined the Windows 11 machine to the domain, same, Outlook logged in.      

Question is, what do I have to change on the exchange server to allow a non-domain computer to have outlook connect to it.    

Microsoft Remote Connectivity Analyzer only complains about the ssl certificate (only 7 employee's, no need for the premium certificate).  Exchange server is the latest from Nov 22 (15.1.2507.016), BPA only complains about TTL on the internal network.  Remote internet or internal makes no difference.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-06*

I didn't think this would be the answer as creating new virtual machines still had this problem, but deleted the 3 saved passwords that existed but it did not resolve the problem,    

I can't find the security tab since I can't get past the initial dialog, but the info on the page says for outlook 2013 and 2016, I am using 2019.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-06*

Hello there,    

This issue can occur if the Logon network security setting on the Security tab of the Microsoft Exchange dialog box is set to a value other than Anonymous Authentication.    

Outlook continually prompts for your password when you try to connect to Microsoft 365 https://learn.microsoft.com/en-us/outlook/troubleshoot/authentication/continually-prompts-password-office-365    

If the above steps are not helpful try the below and see if that helps.    

In the Control Panel - User account -Manage credentials-Windows credentials    

Select all the credentials that say something about Office and delete them.    

Log in again and check if it asks for the credentials again.    

Hope this resolves your Query !!    

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — community member

*upvotes: 0 · updated: 2023-01-06*

Not understanding what certificate is needed.  auto discover and email have a public certificate that is used for owa and the rest.  why would the domain group policy be sending a separate certificate and why would that be required to log in?    

get-outlook anywhere is set for both external and internal.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-06*

I'll assume that the saved passwords have already been verified.    

    

About your question.    

-  A machine outside the domain may not receive the certificate, since it is certainly distributed by GPO. If configured to only accept connections that way.    

https://learn.microsoft.com/en-us/outlook/troubleshoot/connectivity/outlook-cannot-connect-to-exchange-certificate-validation    

-  Another item to check on the server, is the "anywhere" configuration is active.    

Get-OutlookAnywhere | Select Server,ExternalHostname,Internalhostname | fl
