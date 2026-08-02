---
title: "Outlook cannot connect to exchange but OWA can"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/328877/outlook-cannot-connect-to-exchange-but-owa-can
question_id: 328877
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User"]
---
# Outlook cannot connect to exchange but OWA can

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/328877/outlook-cannot-connect-to-exchange-but-owa-can (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi,  

Ive built a new exchange 2019 environment on windows 2019 server (twice) and each time i get the following error when trying to connect my outlook on the win10 client to exchange   

"Cannot start Microsoft Outlook. Cannot open the Outlook window. The set of folders cannot be opened. The information store could not be opened."  

I can open up OWA and send mail (Send connector working) and i have configured the records for autodiscover and mx records.  

When i go through the mail option in control panel to setup profiles it successfully pulls the profile from the exchange server and creates the OST file.  

Ive tried opening outlook in /safe mode and /resetnavpane.  

Also disabling firewalls, antivirus, uninstalled skype and tried reinstalling office.  

I have a certificate chain that the system is happy with and dont get any messages.  

 I've followed the exchange deployment assistant and don't feel i missed any steps. The environment is not connected to the internet and only needs to send mail in a small intranet.   

I cant seem to find any logs on the client which may suggest why the outlook client gives that error.  

I downloaded the troubleshooter EMT tool and it confirms that things should be working.  

I'm out of ideas here and would love any advice or ideas to what i may have missed  

Thanks for your time and support  

Regards,  

Nathan

## Answer (community) — community member

*upvotes: 1 · updated: 2021-03-25*

Hi @zznate   ,  

Does theissue occur on only one computer, or does all computers fail to log in to mailbox through Outlook client?  

After you have tried all the above methods, does the same error appear?

1.Please check Exchange-related services and make sure all services are running normally.  

2.Please check the Outlook client connection by using ExRCA.  

Please refer to: Microsoft Remote Connectivity Analyzer

In addition, I found an official article on this issue, you can refer to the solution provided in it: I can’t start Microsoft Outlook or receive the error “Cannot start Microsoft Office Outlook. Cannot open the Outlook Window”

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-11-30*

I figured out what is happening.    

After verifying the Exchange connection and setting up the profile successfully, the Outlook client pings the default gateway before connecting to the Information Store. If the ping is not successful, Outlook stops and reports that it either can't open the information store or that it can't open your profile's set of folders. This happens even though when you set up the profile, it successfully connected to Exchange.    

So in my test environment, where the client machine was getting a default gateway through DHCP, but where that default gateway didn't actually exist, I had to set a static IP address on the client machine, and used the AD server in my restore environment as the gateway. Even though it won't really route any traffic, it was enough for Outlook to get an ICMP response from the server to fake it into thinking the gateway was up, and I was able to load Outlook with no issues after that.
