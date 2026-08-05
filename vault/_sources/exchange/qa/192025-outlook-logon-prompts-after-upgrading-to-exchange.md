---
title: "Outlook logon prompts after upgrading to Exchange 2016 CU18"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/192025/outlook-logon-prompts-after-upgrading-to-exchange
question_id: 192025
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Outlook logon prompts after upgrading to Exchange 2016 CU18

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/192025/outlook-logon-prompts-after-upgrading-to-exchange (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi all,

We run a DAG containing 9 members, 3 members being in our secondary datacenter and hold DB copies. All client access is through our primary datacenter to the other 6 nodes.

All servers are running Exchange 2016 CU15. We tried upgrading two (ServerA in primary DC, ServerB in secondary DC) to CU18 recently and since then, when we test directly against ServerA Outlook clients (v2016 across the board) they're getting prompted for logon credentials. When the user's enter their credentials, they're not accepted. What we have noticed is that if we delete their autodiscover.xml file, Outlook can connect to Exchange. However, when the .xml file re-appears in their profile they're back to getting the logon prompts. We believe autodiscover is working fine in our environment.  

We noticed on ServerA, its Program Files\Microsoft\Exchange Server\V15\FrontEnd\HttpProxy\autodiscover\web.config file had this added to it after the CU18 upgrade:

<httpProtocol>  

<customHeaders>  

<add name="X-FEServer" value="servername" />  

</customHeaders>  

</httpProtocol>  

<security>  

<authentication>  

<windowsAuthentication>  

<providers>  

<clear />  

<add value="Negotiate" />  

<add value="NTLM" />  

</providers>  

</windowsAuthentication>  

</authentication>  

</security>  

ServerB had the same ' <add name="X-FEServer" value="servername" />' bit, but it didn't have the authentication settings. We removed these authentication settings from the web.config on ServerA, did an IISreset, but we still have the issues with the user logon prompts.

The release notes from CU18 mentions a known Autodiscover error (KB4532190). We tried this and we still got the Outlook logon popups.

We're currently running NTLM authentication across the environment. I'm aware this could be contributing to the issues, but we're trying to resolve a few other issues and get everything patched to CU18 before we look to switch to Kerberos.

Hope this all makes sense and has anyone else come across this issue?

Thanks in advance,

Stu

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-12-10*

Hi KyleC-9016 ,    

Thanks for your response.    

Because of the problem with ServerA running CU18, I don't want to upgrade all other DAG members yet as all our users (15,000) might start getting the logon prompts, which would be very bad.  Especially if their logon credentials aren't accepted.    

If I point users to ServerA, they get a logon prompt when opening Outlook.  Same thing happens if I close and reopen Outlook several times.  I delete the Autodiscover.xml file in their profile (C:\Users\username\AppData\Local\Microsoft\Outlook) they can open Outlook fine and no logon prompts.  Once the .xml is recreated and they close Outlook, the logon prompts return.  I've compared an Autodiscover.xml file from a client that is connecting to a CU15 and CU18 server, and the contents appear the same - please see attached,.46951-autodiscover-edited.txt    

If I run 'Test Email AutoConfiguration' against a CU15 and CU18 server, I'm also seeing the same result:    

    

Regarding the snipped of code from the web.config file, I don't know where that came from.  I thought the CU18 added that, though as I mentioned above when we upgraded ServerB to CU18, which is in our secondary/DR datacentre that clients don't hit for CAS services (we're using a "bound" namespace model), those lines of code don't exist in the web.config.      

We did try removing the lines of code from ServerA's web.config, as you suggested, and this made no difference - we still got the Outlook logon prompts.    

As I also mentioned, we're using NTLM authentication across our Exchange environment and not sure if this is causing us issues.  We'd like to Kerberos, but we wanted to get everything upgraded to CU18 first.    

Thanks,    

Stu

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-10*

@Stu C      

First, put the DAG members in the same CU. DAG member could running with different CU, but may not works very well.    

What we have noticed is that if we delete their autodiscover.xml file,    

Do you mean delete the client computer .xml file?    

I would suggest you try to reconfigure Outlook profile again. Check whether this user could reconfigure Outlook successfully, if this user cannot reconfigure Outlook, which step this issue occur? Could you also provide a screenshot about the result of “Test Email AutoConfiguration” to us?    

    

Do you add those information below into the web.config on your Exchange server? Please delete them or copy a original xml file from another Exchange which in the same CU.    

    

There doesn't exist those information in my Exchange server, could you tell use why do you added those information into the config file?    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
