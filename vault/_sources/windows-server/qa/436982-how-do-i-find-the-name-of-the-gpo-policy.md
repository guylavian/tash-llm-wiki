---
title: "How do I find the name of the GPO policy?"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/436982/how-do-i-find-the-name-of-the-gpo-policy
question_id: 436982
fetched: 2026-07-25
answer_count: 4
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How do I find the name of the GPO policy?

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/436982/how-do-i-find-the-name-of-the-gpo-policy (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi. I have warning in logs:  

GroupPolicy ( Microsoft-Windows-GroupPolicy ) 1085  

-  <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">  

-  <System>  

  <Provider Name="Microsoft-Windows-GroupPolicy" Guid="{aea1b4fa-97d1-45f2-a64c-4d69fffd92c9}" />   

  <EventID>1085</EventID>   

  <Version>0</Version>   

  <Level>3</Level>   

  <Task>0</Task>   

  <Opcode>1</Opcode>   

  <Keywords>0x8000000000000000</Keywords>   

  <TimeCreated SystemTime="2021-06-15T12:03:37.754016600Z" />   

  <EventRecordID>34148</EventRecordID>   

  <Correlation ActivityID="{cd5a87f3-8843-4ddc-9be7-c48712ce8cfc}" />   

  <Execution ProcessID="1744" ThreadID="6548" />   

  <Channel>System</Channel>   

  <Computer>Dattum-rdp-13.resoleasing.com</Computer>   

  <Security UserID="S-1-5-18" />   

  </System>  

-  <EventData>  

  <Data Name="SupportInfo1">1</Data>   

  <Data Name="SupportInfo2">5079</Data>   

  <Data Name="ProcessingMode">0</Data>   

  <Data Name="ProcessingTimeInMilliseconds">7656</Data>   

  <Data Name="ErrorCode">183</Data>   

  <Data Name="ErrorDescription">The file cannot be created because it already exists.</Data>   

  <Data Name="DCName">\DC-01.daomain.local</Data>   

  <Data Name="ExtensionName">Group Policy Files</Data>   

  <Data Name="ExtensionId">{7150F9BF-48AD-4da4-A49C-29EF4A8369BA}</Data>   

  </EventData>  

  </Event>  

How can I find out what this policy is?  

How can I fix this? Do I have to apply the policy once?

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-24*

Hello @Андрей Михалевский  ,    

Thank you for your update and accepting my reply as answer.    

"ExtensionName">Group Policy Files means it is the configuration Under Preferences.    

And I can see there is Preferences Group Policy Files setting under both User Configuration\Preferences and Computer Configuration\Preferences.    

Why I think it is the Preferences Group Policy Files setting under User Configuration\Preferences, because from the gpresult file, I can see the Action is Create under User Configuration\Preferences.    

Create will create a new file, but if the file with the same name existing, it will report the error message below:    

<Data Name="ErrorDescription">The file cannot be created because it already exists.    

But from the gpresult file, I can see the Action is Replcae or Update under Computer Configuration\Preferences.    

Replace or Update will “replace” the existing file, even if the file name is the same.    

    

Hope the information above is also helpful.    

Should you have any question or concern, please feel free to let us know.    

Best Regards,    

Daisy Zhou    

============================================    

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — Q&A User [MicrosoftVendor]

*upvotes: 0 · updated: 2021-06-16*

Hello @Андрей Михалевский  ,

Thank you for posting here.

Based on the information above, you saw the information on machine named "Dattum-rdp-13.resoleasing.com", is it right?

And {cd5a87f3-8843-4ddc-9be7-c48712ce8cfc} is <Correlation ActivityID> not GPO GUID.

{7150F9BF-48AD-4da4-A49C-29EF4A8369BA} is <Data Name="ExtensionId">not GPO GUID.

We can try to look for 7150F9BF-48AD-4da4-A49C-29EF4A8369BA through gpresult report or running gpupdate /force.

1.On machine Dattum-rdp-13.resoleasing.com:  

log on using Domain Administrator account,  

open CMD (run as Administrator),  

run gpupdate /force to check if both user policy and computer policy updates successfully.

2.On machine Dattum-rdp-13.resoleasing.com:  

log on using Domain Administrator account,  

open CMD(run as Administrator),  

Type gpresult /h C:\gpo.html and click Enter.  

Open gpo.html and search the ExtensionId 7150F9BF-48AD-4da4-A49C-29EF4A8369BA to see if you can find it.

And then if you find out 7150F9BF-48AD-4da4-A49C-29EF4A8369BA, maybe we will find the corresponding GPO name and the corresponding GPO GUID.

Here is a similar case for your reference.

Cannot Find Failing GPO  

https://community.spiceworks.com/topic/2005815-cannot-find-failing-gpo

If it does not work above, please refer to the following two threads to see if it helps.

Group Policy always gives an error with Event ID 1101 and GUID on it as AEA1B4FA-97D1-45F2-A64C-4D69FFFD92C9. How do i get rid of this error please.  

https://social.technet.microsoft.com/Forums/office/en-US/925f8a6c-71d7-4e5e-9764-ff264eee165f/group-policy-always-gives-an-error-with-event-id-1101-and-guid-on-it-as?forum=winserverGP

GPO Error 1125 and 7016  

https://learn.microsoft.com/en-us/answers/questions/84851/gpo-error-1125-and-7016.html

Hope the information above is also helpful.

Should you have any question or concern, please feel free to let us know.

Please note: Information posted in the given link is hosted by a third party. Microsoft does not guarantee the accuracy and effectiveness of information.

Best Regards,  

Daisy Zhou

============================================

If the Answer is helpful, please click "Accept Answer" and upvote it.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-15*

Hi @Андрей Михалевский  ,    

You have the GUID of the Group Policy in your event log, you can use the Get-GPO PowerShell cmdlet to find which GPO it is.    

For example:    

```
Get-GPO -Guid aea1b4fa-97d1-45f2-a64c-4d69fffd92c9 -Domain "your.domain.com"
```

----------    

If the reply was helpful please don't forget to `upvote` and/or `accept as answer`, thank you!    

Best regards,    

Leon
