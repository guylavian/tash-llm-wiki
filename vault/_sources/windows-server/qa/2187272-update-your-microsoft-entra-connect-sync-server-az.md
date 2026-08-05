---
title: "Update your Microsoft Entra Connect Sync server - Azure AD Connect V2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2187272/update-your-microsoft-entra-connect-sync-server-az
question_id: 2187272
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 1
qa_tags: ["windows-business-windows-server-directory-services-directory-services-active-directory"]
---
# Update your Microsoft Entra Connect Sync server - Azure AD Connect V2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2187272/update-your-microsoft-entra-connect-sync-server-az (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I received an email inform me ( Action required: Update your Microsoft Entra Connect Sync server by 1 October 2023 to keep your identities syncing )

I use AD on a server running Windows Server 2012R2, when I try to install Azure AD Connect V2 Setup I get an error(AADConnect is only supported on Windows Server 2016 or higher).

Is there any way to  to install Azure AD Connect V2 on the current operating system Windows Server 2012R2 ?

Please Advise.

Azure AD Connect V2 Download link : https://www.microsoft.com/en-us/download/details.aspx?id=47594

## Answer (community) — community member

*upvotes: 0 · updated: 2023-10-05*

Hello Ahmad Al Talla,  

Thank you for posting in Microsoft Community forum.  

From the description above, I understand your question is related to install Azure AD Connect V2 on Windows Server 2012R2.   

Since there are no engineers dedicated to Azure/ Cloud in this forum. in order to be able to get a quick and effective handling of your issue, I recommend that you repost your question in the Q&A forum, where there will be a dedicated engineer to give you a professional and effective reply.

Here is the link for Q&A forum.  

Questions - Microsoft Q&A  

Click the "Ask a Question" button in the upper right corner to post your question and select "Azure Active Directory" tag and "Azure Cloud Services" tag and any other Azure tag related to your products (because there are more Tags related to Azure when you type Azure key word).  

Also, here is a similar thread for your reference.  

Azure AD Connect on Windows 2012 R2 - Microsoft Community  

If you have any question or concern, please feel free to let us know.  

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2023-09-28*

Unfortunately not.  You'll need to migrate AD Connect to a 2016 or newer server somewhere.
