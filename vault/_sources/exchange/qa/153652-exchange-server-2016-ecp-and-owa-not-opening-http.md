---
title: "Exchange Server 2016 ecp and owa not opening-http 500 internal server error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/153652/exchange-server-2016-ecp-and-owa-not-opening-http
question_id: 153652
fetched: 2026-07-25
answer_count: 5
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
---
# Exchange Server 2016 ecp and owa not opening-http 500 internal server error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/153652/exchange-server-2016-ecp-and-owa-not-opening-http (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Alert me|Edit|Change type  

Question  

You cannot vote on your own post  

0  

We have updated the new cumulative update 18 on exchange server 2016.After 4days in one of the exchange server ecp and owa stopped working and showing "http 500 internal server error"." Website Cannot display the Webpage More Likely Causes:  

Website is Under Maintenance  

The Website has Programming error   

we have done troubleshooting step. But issue is not solved. Kindly provide a solution.

## Answer (community) — community member

*upvotes: 1 · updated: 2022-12-18*

My issue was trying to login to ECP through OWA was not possible unless the Admin has a mailbox. In our domain Admins are not aloud to have mailboxes.     

We tried recreating Virtual Directories for Front End and Back End for ECP and OWA. Ran the Updatecas and updateconfigfile scripts. After doing so we did not have any success. We also tried to use the Setup /mode:Upgrade command but it failed due to a service not being able to start. (Yes.. we ran iisreset a million times)    

We eventually came to the conclusion below -    

It was discovered after running "Get-Mailbox -Arbitration" we saw that there were no System Mailboxes.    

Using the link below we recreated the System Mailboxes and were able to login again. The Admin issue was occurring on both Email Exchange ECP websites. I believe because they both work together, that these System Mailboxes are shared between the two.     

https://learn.microsoft.com/en-us/exchange/architecture/mailbox-servers/recreate-arbitration-mailboxes?view=exchserver-2019

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2024-02-01*

It is an older topic already, but I faced the same issue in our multi-site environment when the user-account that starts the https://localhost/ecp EAC page does NOT have a mailbox in the onpremises organization and when that particular exchange node is an 'internal/not-internetfacing' server that has the externalUrl values of the various VirtualDirectories set to $null.
The moment I open the https://localhost/ecp/?ExchClientVer=15 on an internal server with an account that has a mailbox on that box/site it works fine. Similarly if I open that https://localhost/ecp/?ExchClientVer=15 on a central/internet-facing server (externalUrl NOT $null) with an admin-account that has no mailbox (or a hybrid cloud mailbox for that matter) the ECP also runs without issues.
hope it helps someone.
Kind regards.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-07-19*

I faced the similar issue and in my case it was that my Exchange VM simply had not enough CPU's allocated to it. no issues with configurations at all. once added more cores the Exchange started working without any issues. so look for the computer power as well.  

hope it helps.  

Kind Regards,

## Answer (community) — Volunteer Moderator

*upvotes: 0 · updated: 2020-11-12*

Most of the time it seems that whenever you login to your Exchange Admin centre (EAC) a common Exchange server http 500 error occurs. The main source of this problem is caused due to improper configuration of the device. The Error indicates that the device tried to establish a connection with the server, but the request was rejected with an error message by the Exchange server itself. Let's see the solution of Exchange Server 500 error.  

Please check step by step guide  

https://exchange-server-guide.blogspot.com/2018/10/exchange-server-http-500-error.html  

i hope answer the question if issue resolve dont forget to mark as answer

## Answer (community) — community member

*upvotes: 0 · updated: 2020-11-09*

Hi  @Muhammed Shehim   ,    

As we discussed in this thread: Migrated from MSDN Exchange Dev Exchange Server 2016 ecp and owa not opening-http 500 internal server error    

Could you please check the application log when failed login the ECP and OWA page, share the error logs here which will be helpful to troubleshooting this issue.    

If you get event id like 1309, check the SharedWebConfig.config are located in below paths    

C:\Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy    

C:\Program Files\Microsoft\Exchange Server\V15\ClientAccess    

resolution here to generate the missing file.    

If an Answer is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
