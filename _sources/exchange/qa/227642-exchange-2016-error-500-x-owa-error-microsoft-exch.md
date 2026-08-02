---
title: "Exchange 2016 error 500 X-OWA-Error Microsoft.Exchange.Diagnostics.ExAssertException"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/227642/exchange-2016-error-500-x-owa-error-microsoft-exch
question_id: 227642
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 error 500 X-OWA-Error Microsoft.Exchange.Diagnostics.ExAssertException

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/227642/exchange-2016-error-500-x-owa-error-microsoft-exch (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi All,    

I'm getting this error when trying to login to OWA locally and remotely:    

    

Backround information:    

Exchange 2016    

server 2012 r2    

Single exchange server.    

Also getting this error in event viewer:    

An error occurred while using SSL configuration for endpoint [::]:443.  The error status code is contained within the returned data.    

Log Name:      System    

Source:        Microsoft-Windows-HttpEvent    

Date:          12/01/2021 11:16:17    

Event ID:      15021    

Task Category: None    

Level:         Error    

Keywords:      Classic    

User:          N/A    

Computer:      SBNLVM-EXCH1.SBNGC.local    

Description:    

An error occurred while using SSL configuration for endpoint [::]:443.  The error status code is contained within the returned data.    

Event Xml:    

<Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">    

  <System>    

    <Provider Name="Microsoft-Windows-HttpEvent" Guid="{7b6bc78c-898b-4170-bbf8-1a469ea43fc5}" EventSourceName="HTTP" />  

    <EventID Qualifiers="49152">15021</EventID>  

    <Version>0</Version>  

    <Level>2</Level>  

    <Task>0</Task>  

    <Opcode>0</Opcode>  

    <Keywords>0x80000000000000</Keywords>  

    <TimeCreated SystemTime="2021-01-12T11:16:17.241910600Z" />  

    <EventRecordID>29156582</EventRecordID>  

    <Correlation />  

    <Execution ProcessID="4" ThreadID="12364" />  

    <Channel>System</Channel>  

    <Computer>XXXXXXXX</Computer>  

    <Security />  

  </System>    

  <EventData>    

    <Data Name="DeviceObject">\Device\Http\ReqQueue</Data>  

    <Data Name="Endpoint">[::]:443</Data>  

    <Binary>000004000200300000000000AD3A00C00000000000000000000000000000000000000000000000005F0000C0</Binary>  

  </EventData>    

</Event>    

I use a wildcard SSL and this shows correctly before a user logins in. When they login they hit the error 500 page above. I noticed the this SSL expired: Microsoft Exchange Server Auth Certificate so I have renewed this using the ECP button.     

I have checked the bindings on IIS on both default and backend and they are set to my wildcard SSL.    

Any ideas would be a great help :)    

Adam

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-13*

@Zhengqi Lou-MSFT  

Legend! Followed the steps and working :)

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2021-01-12*

Hi @AdamSadler-1783   ,    

Please find the below suggestions,    

Is the certificate "Microsoft Exchange Server Auth Certificate" showing as valid when you run Get-ExchangeCertificate?    

Have you run IISreset after renewing the certificate?    

Try running updatecas.ps1 and updateConfigfile.ps1 and verify    

Also, please select the "Microsoft Exchange" certificate in the BackEnd website and remove the wildcard certificate. run IISReset and check again.    

https://pdhewaju.com.np/2017/12/23/exassertexception-issue-on-exchange-owa/    

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.    

If the above suggestion helps, please click on "Accept Answer" and upvote it
