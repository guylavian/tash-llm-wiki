---
title: "unable to send email from exchange 19"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/387864/unable-to-send-email-from-exchange-19
question_id: 387864
fetched: 2026-07-25
answer_count: 6
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# unable to send email from exchange 19

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/387864/unable-to-send-email-from-exchange-19 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Dear Experts I need your help,   

I have installed ex19 for migration from ex16. but unfortunate i stuck an issue during migration, installation setup of ex19 done successfully.  i have set virtual directories on ex19. email received from externals is ok but when changed smtp send connector from ex16 to ex19. user unable to send emails on other(external) domains, email stuck in que viewer with error code.  

LED= 451.4.4.397 error communication with target host 421.4.2.1 socket timeout socket error 10060  

further sometime emails delivered with delayed but mostly stuck  

-  open port scanner > port 25 is open  

-  mxtoolbox test smtp> successful and point to ex19  

-  The Microsoft Connectivity Analyzer failed to test inbound SMTP mail flow.  

Test Steps  

Attempting to retrieve DNS MX records for domain 'domain.com'.One or more MX records were successfully retrieved from DNS.  

Additional Details  

Testing Mail Exchanger smtp1.domain.com.This Mail Exchanger was tested successfully.  

Test Steps  

Testing Mail Exchanger smtp2.domain.com.One or more SMTP tests failed for this Mail Exchanger.  

Test Steps  

Attempting to resolve the host name smtp2.domain.com in DNS.The host name resolved successfully.  

Additional Details  

Testing TCP port 25 on host smtp2.domain.com to ensure it's listening and open.The specified port is either blocked, not listening, or not producing the expected response.

## Answer (community) — Q&A User

*upvotes: 1 · updated: 2021-05-10*

For Exchange, there are a couple of configuration overrides that you need to set for email to work:  

$config['email_crlf']    = "\r\n";  

$config['email_newline'] = "\r\n";  

Add those, restart your server, and you should be good to go.  

Note: Make sure to use those double quotes around the \r\n strings.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-10*

on my network gateway firewall(fortigate) i just switch the local ip from ex16 to ex19 for nat binding for example    

ex16    

nothing changed in default smtp send connectors. internal domain emails send received ok on owa, outlook, and mobile.    

public IP >>NAT>>192.168.3.30(ex16)    

when change smtp from ecp from ex16 to ex19. same thing i changed in firewall for nat.    

same public IP>>NAT>>192.168.3.34(ex19) further nothing change in firewall policies.    

as you guide I found one more thing regarding smtp ports, snapshot attached.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-10*

Hi,    

"email received from externals is ok but when changed smtp send connector from ex16 to ex19"    

What did you change?     

Check if you create send connector correctly: Create a Send connector to send mail to the internet    

"user unable to send emails on other(external) domains"    

You failed testing inbound SMTP mail flow in EXRCA also, does it mean you can't sending emails both internally and externally?     

Have you changed anything on the default receive connectors since installed?    

Can you telnet you Exchange 2019 server on port 25 within you network successfully？ And from external network?    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-05-09*

thanks for your support.  

i am little confused here, as this new installation coexistence of ex16. on my old ex16 things are working smooth no issue. still when i moved my smtp towards ex16 all things start working good. but when i moved my smtp to my new server ex19 email out going start block . i don't know my troubleshooting on right side or not.    

-  i put sever firewall off and check the issue but nothing positive.  

-  Nat enabled on my firewall. email receiving on ex19 is ok, sometime outgoing worked but mostly emails stuck in que. keep trying.  

-  in my case smart host not enabled.

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2021-05-09*

-  Firewall on port 25 outbound is open? You confirmed that?  

-  Did you NAT the 2019 server to an external IP?  

-  Do you send outbound through any smarthost or other SMTP Gateway? If so, have you configured it to allow the new server to send through it?
