---
title: "What is the verson value for Exchange2019 in RequestServerVersion"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/422876/what-is-the-verson-value-for-exchange2019-in-reque
question_id: 422876
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 1
qa_tags: ["office-exchange-office-exchange-server-development", "office-exchange-office-exchange-server-management"]
---
# What is the verson value for Exchange2019 in RequestServerVersion

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/422876/what-is-the-verson-value-for-exchange2019-in-reque (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are using EWS API to connect to an on-premise Exchange2019.  When the EWS client try to connect to the server with RequestServerVersion Version="Exchange2019", the server returns 500 ErrorInvalidRequest. If we change to use Version="Exchange2016", the same server returns 200  

EWS Request:  

<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:m="http://schemas.microsoft.com/exchange/services/2006/messages" xmlns:t="http://schemas.microsoft.com/exchange/services/2006/types">soap:Header<t:RequestServerVersion Version="Exchange2019"></t:RequestServerVersion></soap:Header>soap:Body<m:GetFolder><m:FolderShape><t:BaseShape>AllProperties</t:BaseShape></m:FolderShape><m:FolderIds><t:DistinguishedFolderId Id="inbox"></t:DistinguishedFolderId></m:FolderIds></m:GetFolder></soap:Body>  

</soap:Envelope>  

Response from Exchange2019 server:  

<s:Body><s:Fault>a:ErrorInvalidRequestThe request is invalid.<e:ResponseCode xmlns:e="http://schemas.microsoft.com/exchange/services/2006/errors">ErrorInvalidRequest</e:ResponseCode><e:Message xmlns:e="http://schemas.microsoft.com/exchange/services/2006/errors">The request is invalid.</e:Message></s:Fault></s:Body></s:Envelope>  

If using Version="Exchange2016" in request, the Response is:  

NoError  

<m:Folders><t:Folder><t:FolderId Id="AQMkADY2AGY4ZGY0Zi05YTNlLTRiY......"/><t:ParentFolderId Id="AQMkADY2AGY4ZGY0Zi........." ChangeKey="AQ......"/><t:FolderClass>IPF.Note</t:FolderClass><t:DisplayName>Inbox</t:DisplayName><t:TotalCount>0</t:TotalCount><t:ChildFolderCount>0</t:ChildFolderCount><t:EffectiveRights><t:CreateAssociated>true</t:CreateAssociated><t:CreateContents>true</t:CreateContents><t:CreateHierarchy>true</t:CreateHierarchy><t:Delete>true</t:Delete><t:Modify>true</t:Modify><t:Read>true</t:Read><t:ViewPrivateItems>true</t:ViewPrivateItems></t:EffectiveRights><t:UnreadCount>0</t:UnreadCount></t:Folder></m:Folders>  

</m:GetFolderResponseMessage></m:ResponseMessages></m:GetFolderResponse></s:Body></s:Envelope>  

Is this an expected behavior ?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-05-15*

I'm facing the same issue, Exchange2019 version returns an error, while Exchange2016 works.    Are there any formal documentation stating API usage for Exchange2019 should be handled with version Exchange2016?
