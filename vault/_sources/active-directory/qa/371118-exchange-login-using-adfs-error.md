---
title: "Exchange login using adfs error"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/371118/exchange-login-using-adfs-error
question_id: 371118
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# Exchange login using adfs error

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/371118/exchange-login-using-adfs-error (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Some clients will sometimes report the following errors，But it doesn't appear 100%    

The passive protocol context was not found or it is invalid. If the context is stored in a cookie, the cookie provided by the client is invalid. Please make sure that the client browser is configured to accept cookies from this website, and then retry this request.

## Answer (community) — community member

*upvotes: 0 · updated: 2021-04-26*

联合身份验证被动请求期间遇到错误。   

其他数据   

协议名称:   

Saml   

信赖方:   

异常详细信息:   

Microsoft.IdentityServer.Web.CookieManagers.InvalidContextException: MSIS7001: 未找到被动协议上下文或其无效。如果上下文存储在 Cookie 中，则客户端提供的 Cookie 无效。请确保将客户端浏览器配置为接受此网站中的 Cookie，然后重试此请求。  

   在 Microsoft.IdentityServer.Web.Protocols.Saml.SamlProtocolHandler.GetOriginalRequestFromResponse(ProtocolContext context, Boolean deleteCookie)  

   在 Microsoft.IdentityServer.Web.PassiveProtocolListener.ProcessProtocolRequest(ProtocolContext protocolContext, PassiveProtocolHandler protocolHandler)  

   在 Microsoft.IdentityServer.Web.PassiveProtocolListener.OnGetContext(WrappedHttpListenerContext context)
