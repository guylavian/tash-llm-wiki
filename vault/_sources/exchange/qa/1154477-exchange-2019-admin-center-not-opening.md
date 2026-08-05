---
title: "Exchange 2019 Admin Center Not Opening"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1154477/exchange-2019-admin-center-not-opening
question_id: 1154477
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-office-exchange-server-other-l1"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Exchange 2019 Admin Center Not Opening

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1154477/exchange-2019-admin-center-not-opening (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

One of our clients Exchange 2019 server is not opening exchange admin center after logging in; it just spins.  It is running on Windows Server 2019 Standard and is an on-premise server. Server is up to date on all Windows and exchange (CU12 15.2.1118.20) updates. I am seeing errors Event ID 5139 WAS source in system log and Event ID 2280 IIS-W2SVC source in application log (details of these are listed below). I have removed and recreated the OWA & ECP virtual directories, Checked the bindings on default website and backend which both are correct, and ran SFC repair.  I did find another article that suggested removing DynamicCompressionModule from applicationhost.config file which did stop the above errors from occurring but also stopped all email from being received or sent. I have compared this with another client's Exchange server and cannot find anything out of place. I appreciate any and all help.    

Log Name:      System    

Source:        Microsoft-Windows-WAS    

Date:          1/6/2023 6:03:09 AM    

Event ID:      5139    

Task Category: None    

Level:         Warning    

Keywords:      Classic    

User:          N/A    

Computer:      BN-MAIL-2019.cityofbn.com    

Description:    

A listener channel for protocol 'http' in worker process '28652' serving application pool 'DefaultAppPool' reported a listener channel failure.  The data field contains the error number.    

Event Xml:    

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">    

  <System>    

    <Provider Name="Microsoft-Windows-WAS" Guid="{524B5D04-133C-4A62-8362-64E8EDB9CE40}" EventSourceName="WAS" />  

    <EventID Qualifiers="32768">5139</EventID>  

    <Version>0</Version>  

    <Level>3</Level>  

    <Task>0</Task>  

    <Opcode>0</Opcode>  

    <Keywords>0x80000000000000</Keywords>  

    <TimeCreated SystemTime="2023-01-06T12:03:09.517096100Z" />  

    <EventRecordID>624506</EventRecordID>  

    <Correlation />  

    <Execution ProcessID="0" ThreadID="0" />  

    <Channel>System</Channel>  

    <Computer>BN-MAIL-2019.cityofbn.com</Computer>  

    <Security />  

  </System>    

  <EventData>    

    <Data Name="AppPoolID">DefaultAppPool</Data>  

    <Data Name="ProcessID">28652</Data>  

    <Data Name="param3">0</Data>  

    <Data Name="ProtocolID">http</Data>  

    <Binary>05000780</Binary>  

  </EventData>    

</Event>    

Log Name:      Application    

Source:        Microsoft-Windows-IIS-W3SVC-WP    

Date:          1/6/2023 6:31:17 AM    

Event ID:      2280    

Task Category: None    

Level:         Error    

Keywords:      Classic    

User:          N/A    

Computer:      BN-MAIL-2019.cityofbn.com    

Description:    

The Module DLL E:\MSExchange2019\ClientAccess\Owa\auth\exppw.dll failed to load.  The data is the error.    

Event Xml:    

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">    

  <System>    

    <Provider Name="Microsoft-Windows-IIS-W3SVC-WP" Guid="{670080D9-742A-4187-8D16-41143D1290BD}" EventSourceName="W3SVC-WP" />  

    <EventID Qualifiers="49152">2280</EventID>  

    <Version>0</Version>  

    <Level>2</Level>  

    <Task>0</Task>  

    <Opcode>0</Opcode>  

    <Keywords>0x80000000000000</Keywords>  

    <TimeCreated SystemTime="2023-01-06T12:31:17.412174600Z" />  

    <EventRecordID>5620139</EventRecordID>  

    <Correlation />  

    <Execution ProcessID="0" ThreadID="0" />  

    <Channel>Application</Channel>  

    <Computer>BN-MAIL-2019.cityofbn.com</Computer>  

    <Security />  

  </System>    

  <EventData>    

    <Data Name="ModuleDll">E:\MSExchange2019\ClientAccess\Owa\auth\exppw.dll</Data>  

    <Binary>05000000</Binary>  

  </EventData>    

</Event>

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-01-09*

Try to Stop and restart the application pool. Application pools occasionally need to be restarted in order to return to normal operation. Because application pools depend on the Windows Process Activation Service (WAS), you may have to restart WAS. If you restart WAS, you may also have to restart the World Wide Web Publishing Service (W3SVC), which depends on WAS.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-01-09*

Hi @Bernard Grieshaber   ，    

 I did find another article that suggested removing DynamicCompressionModule from applicationhost.config file which did stop the above errors from occurring but also stopped all email from being received or sent.     

Was the module backed up before it was removed? If possible ,please recover the module you deleted first.    

Then please refer to the following steps to try to resolve the error ID 2880：    

-  Remove the exppw.dll entry from applicationhost.cofig (c:\windows\system32\inetsrv\config)    

Note: Remember take a backup before you remove the line.    

-  Then registered the exppw.dll by following the below steps:    

-  IIS Manager -> Select the Server Name in the left Pane -> Open Modules in the middle pane.    

-  Click on ‘Configure Native Modules’ in the right pane -> Click the button ‘Register’ -> Type the name as ‘exppw’    

-  Browse and select the path of above file as:E:\MSExchange2019\ClientAccess\Owa\auth\exppw.dll    

-  Made sure that the 'exppw.dll' is only present at OWA level and not at any of the top heirarchy.    

-  Then ensured for this module in OWA (VDir), ‘Module Type’ is set to ‘Native’ and ‘Entry Type’ is ‘Local’    

-  Run IISreset /noforce    

Here is a similar thread for you reference : The Module DLL C:\Program Files\Microsoft\Exchange Server\V14\ClientAccess\Owa\auth\exppw.dll failed to load    

Hope this helps!    

(Note: Microsoft provides third-party contact information to help you find additional information about this topic. This contact information may change without notice. Microsoft does not guarantee the accuracy of third-party contact information.)    

If the answer is helpful, please click "Accept Answer" and kindly upvote it. If you have extra questions about this answer, please click "Comment".    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
