---
title: "Exchange 2016 have error while retrieving tracking information between root and child domain"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/110957/exchange-2016-have-error-while-retrieving-tracking
question_id: 110957
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Q&A User"]
---
# Exchange 2016 have error while retrieving tracking information between root and child domain

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/110957/exchange-2016-have-error-while-retrieving-tracking (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi Support,  

Both of our root domain and child domain installed exchange 2016.  

In root domain exchange EAC delivery reports, after click the search, it will have Warning "Server ex16.abc.com encountered an error while retrieving tracking information from https://ex16.xyz.abc.com:444/ews/exchange.asmx". And it cannot show any result  

In child domain exchange EAC delivery reports, after click the search, it will have Warning "Server ex16.xyz.abc.com encountered an error while retrieving tracking information from https://ex16.abc.com:444/ews/exchange.asmx". And it cannot show any result  

Confirmed the 444 port opened between 2 servers. Both of them can access other side "https://server:444/ews/exchange.asmx" in web browser after grant the permission on the folder "c:\program files\microsoft\exchange server\v15\frontend\httpproxy"  

Thanks  

Chong

## Answer (community) — community member

*upvotes: 0 · updated: 2020-10-22*

Hi @Anonymous   ,  

Sorry for keeping you waiting.During this time, I installed Exchange 2016 on the root and child domains in different AD sites. According to my test results, the root and child domains in different sites can search for delivery reports and message tracking logs. However, there may be delays in DC replication at different sites, so for newly created users and emails, you need to wait for DC replication to complete before you can search normally.  

And if we want to search message tracking log in EMS, we need to run the following command:

```
Get-Transportservice | Get-Messagetrackinglog -Sender <>
```

-   Please make sure that the account you use has full access to the message tracking log folder in the other party's domain.

-   After you re-create the virtualdirectory, please remember to run the IISreset in CMD strat as administrator to restar the iis.

-   Please view the authencation methoth in EWS in IIS, screenshot below is the default settings in my lab environment.  

    
    4.  Is there a firewall between the parent and child domains? If it exists, please check the firewall settings to see if there is a security policy or other settings blocking communication.If possible, please try to temporarily turn off the firewall and third-party anti-virus software.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2020-10-12*

Hi @Lucas Liu-MSFT   ,    

If cannot trace email to other AD site is by design, it will show error message that encountered an error while retrieving tracking information? Even send to external also will not show any error.

## Answer (community) — community member

*upvotes: 0 · updated: 2020-09-30*

Hi @Anonymous   ,  

Did you any changes before this error occurred?  

In the EAC in the root domain, is there an error in searching the mailbox in the root domain?  

-  Please make sure the services required by Exchange are running.  

-  What is your Exchange CU version? According to my research, similar problems occurred in earlier versions of Exchange. If your Exchange version is lower, please upgrade Exchange to a newer version.  

-  Please run the following command to check whether the Url settings of EWS virtual directory is correct:    Get-Webservicesvirtualdirectory -showmailboxvirtualdirectories | fl Identity,url  

For more information: Setting Exchange 2016 Virtual Directory  

Please Note: Since the web site is not hosted by Microsoft, the link may change without notice. Microsoft does not guarantee the accuracy of this information.  

  

4.Based on my knowledge, delivery reports for administrators uses the Exchange admin center (EAC) to perform a targeted search of the message tracking logs. So please make sure the message tracking logs are exists normally.  

5.Please try to run the following commands to remove and recreate the EWS virtual directory:

```
Remove-WebServicesVirtualDirectory -Identity <>  
New-WebServicesVirtualDirectory -WebSiteName <> -InternalUrl <> -ExternalUrl <>
```

6.Please check if there are any related error logs in the event viewer. If so, please share with us. What needs attention is to cover your personal information.

If the response is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
