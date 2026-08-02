---
title: "Custom Receive Connector on Exchange 2019 not working properly"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/165982/custom-receive-connector-on-exchange-2019-not-work
question_id: 165982
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management"]
answer_author_roles: ["Microsoft Moderator"]
---
# Custom Receive Connector on Exchange 2019 not working properly

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/165982/custom-receive-connector-on-exchange-2019-not-work (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

In Exchange 2019, I recently created a new receive connector in EMS to allow anonymous users to relay.  It’s configured only to allow a specific server to send messages.  Messages destined for internal users are delivered.  However, messages for external email addresses are not delivered.  This is the error in the logs:  Unable to relay recipient in non-accepted domain.  

This hasn’t been working for a while, possibly since we installed Exchange 2019 this past summer. I removed the previous receive connector and created a new one in power shell with no success.  These are the commands I used:  

```
New-ReceiveConnector -Name "Relay Out" -TransportRole FrontendTransport -Custom -Bindings 172.x.x.x:25 -RemoteIpRanges 172.x.x.x

 Set-ReceiveConnector "Relay Out" -PermissionGroups AnonymousUsers

 Get-ADPermission "Relay Out" -User "MS Exchange\Externally Secured Servers" | where {($_.Deny -eq $false) -and ($_.IsInherited -eq $false)} | Format-Table User,ExtendedRights
```

How do I allow the server to send to anyone?

## Answer (community) — Microsoft Moderator

*upvotes: 0 · updated: 2020-11-18*

@Steege       

Hi,    

```
New-ReceiveConnector -Name "Relay Out" -TransportRole FrontendTransport -Custom -Bindings 172.x.x.x:25 -RemoteIpRanges 172.x.x.x
```

Does the ip address in "Bindings" belong to the specific server which you would like to allow to send messages?    

It is supposed to be the ip address of the network adapters on the Exchange server.    

If so,please change it to 0.0.0.0:25 or the ip address of a specific network adapter.    

And see if the problem persists.    

If the response is helpful, please click "Accept Answer" and upvote it.    

Note: Please follow the steps in our documentation to enable e-mail notifications if you want to receive the related email notification for this thread.
