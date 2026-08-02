---
title: "B2B user  accessing  exchange mailbox via resource tenant"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1122088/b2b-user-accessing-exchange-mailbox-via-resource-t
question_id: 1122088
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["office-exchange-office-exchange-server-management", "office-exchange-online", "office-outlook-platform-windows-classic-outlook-windows-business"]
answer_author_roles: ["Q&A User", "Volunteer Moderator"]
answer_author_affiliations: ["Mvp"]
---
# B2B user  accessing  exchange mailbox via resource tenant

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1122088/b2b-user-accessing-exchange-mailbox-via-resource-t (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hello,    

My tenant is   contoso.com  and I have one  guest user in it   with     ******@fabrikam.com    

when John hits   "OWA-  outlook web access" and   if   the authentication request  is  directed to my  contoso.com  tenant ,   contoso will prepare the token and  john will see his mailbox.    

Would above be possible  and if  answer is yes then      

how would it be different  if  the  authentication request  was directed to  John's  home tenant i.e.,   fabrikam.com  and   fabrikam   would have  prepared the token to put  John  on  his mailbox.    

Thanks.

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2022-12-13*

Can you help me please.  

I am trying to create following simple "claim-mapping-policy" and attaching it on the service-principal of client-app.

{  

"definition": [  

"{\"ClaimsMappingPolicy\":{\"Version\":1,\"IncludeBasicClaimSet\":\"true\",\"ClaimsSchema\": [{\"Source\":\"user\",\"ID\":\"proxyaddresses\",\"JwtClaimType\":\"proxyaddresses\"}]}}"  

],  

"displayName": "Test1234"  

}

However, I still DO NOT FIND proxyaddresses coming in the id-token

## Answer (community) — Volunteer Moderator [Mvp]

*upvotes: 0 · updated: 2022-12-09*

Not sure I understand the question here, are you asking whether Guest users can have a mailbox in the resource tenant? If so, the answer is yes, however this is not a supported scenario. It requires you to "convert" the userType to Member first, then you can assign a license: https://www.michev.info/Blog/Post/2256/some-new-interesting-experiences-with-guest-users-in-office-365    

Again, this is not really supported, as Exchange Online has no support for B2B. So while you can technically provision the mailbox, the user will not be able to access it. Well he can, if you reset his password in the resource tenant and login directly (another unsupported scenario). But you can still grant permissions on the mailbox and have someone else access it.    

And yes, it matters where you authenticate from. The supported scenario for a B2B user, even one with userType set to member, is to authenticate against their own AAD (you will notice that the user still has "ExternalAzureAD" value under Identities in the Azure portal). While you can technically override this by creating/resetting a password in the resource tenant, this is not supported.     

This article goes over the various types of B2B users and their properties: https://learn.microsoft.com/en-us/azure/active-directory/external-identities/user-properties
