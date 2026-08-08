---
title: "Exchange 2013 Get-ServerHealth -HealthSet 'hubtransport' failed for server error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/329047/exchange-2013-get-serverhealth-healthset-hubtransp
question_id: 329047
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Exchange 2013 Get-ServerHealth -HealthSet 'hubtransport' failed for server error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/329047/exchange-2013-get-serverhealth-healthset-hubtransp (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello, We get this error very often on our exchange 2013 server. How can I fix it? "Get-ServerHealth -HealthSet 'hubtransport' failed for server"

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2021-03-25*

Hi @IT MAN  ,

Is there any other information along with the error you mentioned?  

Aside from the error, did the users encounter any mail flow issues when the error occur?  

Which CU are you running? You can run the following command to view the build number:

```
Get-ExchangeServer | Format-List Name,Edition,AdminDisplayVersion
```

Besides, when the error appears, please follow the steps below to see if we can get more details for troubleshooting:  

1.Run the following command in EMS to retrieve the HubTransport health set details about the server:

```
Get-ServerHealth  | ?{$_.HealthSetName -eq "HubTransport"}
```

2.Review the command output and note the monitors that show as "Unhealthy".  

3. Rerun the associated probe for the monitor that's in an unhealthy state. Refer to the table in the Explanation section to find the associated probe. To do this, run the following command:

```
Invoke-MonitoringProbe \ -Server  | Format-List
```

4.Review the result section in the output to see if there's any clues.

If an Answer is helpful, please click "Accept Answer" and upvote it.  

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
