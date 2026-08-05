---
title: "How to create an Exchange Web Services Listener via PowerShell"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1302288/how-to-create-an-exchange-web-services-listener-vi
question_id: 1302288
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management", "windows-business-windows-server-user-experience-powershell"]
answer_author_roles: ["Q&A User"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# How to create an Exchange Web Services Listener via PowerShell

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1302288/how-to-create-an-exchange-web-services-listener-vi (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a mailbox for a service account which uses scheduled tasks to scrape the mailbox using Exchange Web Services. This all works well, but I want to be able to use this mailbox for SOAR. I need to create a listener using EWS via PowerShell (sorry, I'm not a developer but can do .NET via PS) so that when emails come in, I can automate actions. I haven't attempted this yet but also haven't found any documentation on how to make this happen. I want this listener to work 24x7. Once I figure out how to create the listener, I will be able to have it take actions on any new emails - that part shouldn't be a problem - but I'm just not certain how to create the listener itself. Any help is much appreciated.

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2023-06-16*

@RJames2010  

Glad to see that your issue had already been resolved and thanks for sharing the solution so that others experiencing the same thing can easily reference this! Since the Microsoft Q&A community has a policy that "The question author cannot accept their own answer. They can only accept answers by others", I'll repost your solution in case you'd like to "Accept" the answer.

 

 

 

[How to create an Exchange Web Services Listener via PowerShell]

 

Issue Symptom:

I need to create a listener using EWS via PowerShell (sorry, I'm not a developer but can do .NET via PS) so that when emails come in, I can automate actions.

 

Solution:

I went a different route and created a subscription in EWS which is now working.

Best regards,

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2023-06-15*

So, I went a different route and created a subscription in EWS which is now working. Thanks for your help!

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-09*

Hello there,

This is made possible by the .NET HttpListener.

-  Create and Start the HTTP Listener

$httpListener = New-Object System.Net.HttpListener

$httpListener.Prefixes.Add('http://localhost:5001/')

$httpListener.Start()

Here, I’m listening for requests aimed at  http://localhost:5001/, but you could listen to any other interface or port on your machine.

Listen on all interfaces by using a +, like so: http://+:5001/

HttpListener requires that you include a trailing / in the prefix.

In a separate PowerShell session:

Invoke-WebRequest 'http://localhost:5001/big-test'

You could kick off a request from anywhere though. It doesn’t have to be from PowerShell or even from your machine.

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer–
