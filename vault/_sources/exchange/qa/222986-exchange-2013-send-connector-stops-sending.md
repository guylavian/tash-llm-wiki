---
title: "Exchange 2013 send connector stops sending"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/222986/exchange-2013-send-connector-stops-sending
question_id: 222986
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2013 send connector stops sending

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/222986/exchange-2013-send-connector-stops-sending (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Have a weird issue, where the send connector stops sending external ,emails.  I have to change from sending directly to any mail server to a smarthost and reboot, then when it stops I need to change it back and reboot.  

I have done patches to the server as it was not updated in years and plan on going from CU1 to CU23.  But trying to resolve this issue before hand.  This seems to have started after I started patching and removing the antivirus in preparation of the upgrade this started last week and I want to do the upgrade this weekend.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-13*

Hi @Terry Schultz       

Have you received any NDRs? After the send connector stops working, send an email and you may receive a NDR like this:     

     

If you have received the NDR, please share it with me by covering your personal information.    

but exchange only allows one internet send connector.    

Are there error messages or logs showing this or you have failed creating another internet send connector? If you get an error message, please share it with me, also remember to cover your personal information.    

And are you using Internet Explorer 11 to access the Exchange Control Panel(ECP) and the Exchange version is earlier than CU13? It’s a known issue: Can't create a new send connector in Exchange Control Panel in Exchange Server 2013    

If so, what about using this cmdlet in EMS?     

New-SendConnector -Internet -Name “Test Internet” -AddressSpaces outlook.com    

Under normal circumstances, Exchange allows multiple internet send connectors.      

     

In this screenshot, the Gmail and Outlook are both internet send connectors using MX records but different scopes.     

The send connectors are independent, you don’t have to worry about breaking other send connectors.    

You can create a new internet send connector(MX record) following these steps:    

-  Disable the old internet send connector first and create a new one to test.    

     

-  EAC -> Mail flow -> send connectors -> New (Make sure the Name is different with other send connectors)    

     

-  Then choose the MX record.    

     

-  Specify the address space as *, so it could route messages to all domains.    

     

-  Choose the source server and finish. The example uses Exchange 2013 CU23.    

     

-  After creating this, send a message to the external recipient and check the result.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-01-11*

Hi Lou,  

I have it down to where I change the send connector from route mail through smart hosts to MX record associated with recipient domain. I hity save then go back and change it back to Route mail through smart hosts and then add the ip's for the smart hosts hit save and reboot.  This seems to get it working for about a day then it stops again.  

I went in to create another internet send connector, but exchange only allows one internet send connector.   Should I setup a custom connector and disable the internet send connector would that work.  My biggest fear is breaking the send connector completely where no one can send email out of the exchange server.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-01-08*

Hi @Terry Schultz   ,

the send connector stops sending external ,emails.

Do you mean these messages couldn’t sent to the external recipients? Are there any NDRs? If so, please share them by covering your personal information.

I have to change from sending directly to any mail server to a smarthost and reboot, then when it stops I need to change it back and reboot.

Does that mean the send connector will be OK after 2 reboots? And it stops working again after a while?

This seems to have started after I started patching and removing the antivirus in preparation of the upgrade

Have you performed other operations except changing Network settings to smarthost?

Based on my knowledge, I think there could be some problems with the send connector. Please try the following methods for a further troubleshooting.  

-  Create a new Internet Send Connector and test sending messages to external address. If it’s ok, please compare the settings with the problematic one.  

-  Restart the MS Exchange Transport Service and have a test.

Here is an article about creating send connectors and testing, I think it may be helpful: Outbound Mail Flow for Exchange Server 2016.  

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.

Regards,

Lou

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
