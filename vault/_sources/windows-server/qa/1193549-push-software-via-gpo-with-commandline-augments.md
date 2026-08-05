---
title: "Push software via GPO with commandline augments"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1193549/push-software-via-gpo-with-commandline-augments
question_id: 1193549
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# Push software via GPO with commandline augments

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1193549/push-software-via-gpo-with-commandline-augments (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have a client that needs to push a file via GPO but needs it to used a proxy. How do you add a proxy into the msi file? Ive sued MSIEXEC with command lines but need it pushed out to groups of computers with the proxy.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-03-28*

```
Hello there,

See the following command examples for installation options:

msiexec.exe /i ".msi file path" /quiet WRAPPED_ARGUMENTS="/silent /apiserver={apiserver} /key={key} /secret={secret} "
    
To connect using a proxy, without credentials:

 msiexec.exe /i ".msi file path" /quiet WRAPPED_ARGUMENTS="/silent /apiserver=apiserver /key=key /secret=secret /proxyip=proxyIP /proxyport=proxyport /gatewayprofileuuid=profile_UUID_of_the_gateway**"
    
To connect using a proxy, using credentials:

  msiexec.exe /i ".msi file path" /quiet WRAPPED_ARGUMENTS="/silent /apiserver=apiserver /key=key /secret=secret /proxyip=proxyIP /proxyport=proxyport /gatewayprofileuuid=profile_UUID_of_the_gateway /proto=http or https /proxyusername=proxy_server_username /proxypassword=proxy_server_b64encoding_password"
    

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer--
```
