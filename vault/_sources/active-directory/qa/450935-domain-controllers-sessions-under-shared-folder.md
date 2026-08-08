---
title: "Domain Controller's Sessions under Shared folder"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/450935/domain-controllers-sessions-under-shared-folder
question_id: 450935
fetched: 2026-07-25
answer_count: 7
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["Mvp"]
---
# Domain Controller's Sessions under Shared folder

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/450935/domain-controllers-sessions-under-shared-folder (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

On a Domain Controller what does sessions under shared folder indicate?    

Under User I can computername$(covered with red) & user id's(covered with blue)    

    

Does it mean these computername$ & user id are authenticating via this DC or does it mean something else ?    

Do note that "open files" is "0" for any of the users.    

I'm doubtful about that coz when I login to a member server, run "set l" or "nltest /dsgetdc:domain name" & then login the DC which it is showing. It doesn't list the memberservername or my user id under sessions     

So what exactly is this ? Thanks

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-30*

Hi,  

Welcome to share your current situation if there are any updates.  

Please feel free to let us know if you need further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-28*

Hi,  

Welcome to share your current situation if there are any updates.  

Please feel free to let us know if you need further assistance.  

Best Regards,  

Vicky

## Answer (community) — community member

*upvotes: 0 · updated: 2021-06-25*

Hi，  

》》Does this session mean the mentioned user id are authenticating via this DC?  

You can understand what it means  

》》Should I still be seeing these sessions on previously mapped DC?  

You can see these sessions on the mapped DC  

Hope this information can help you  

Best wishes  

Vicky

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-24*

The open shared folder is in a SMB session, the default timeout for SMB session is 15 minutes. If the SMB session is inactive for 15 minutes the server will send a TCP reset to close the SMB connection. Until the Autodisconnect timer is reached, the server will send an NBT keep-alive packet every two minutes. In this case either the default may have been changed or something strange going on client-side.    

https://learn.microsoft.com/en-us/troubleshoot/windows-client/networking/mapped-drive-connection-to-network-share-lost#method-1-using-registry-editor    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2021-06-24*

Most likely is a connection at some point to this server's sysvol /netlogon shares. Looks like they can come and go quite quickly depending on what the client computer is doing.  

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
