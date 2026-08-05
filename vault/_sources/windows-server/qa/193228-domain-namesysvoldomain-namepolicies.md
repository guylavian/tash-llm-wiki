---
title: "在一台域控的\\\\domain_name\\Sysvol\\domain_name\\Policies中新建的文件夹，在其他域控不能同步，不能访问"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/193228/domain-namesysvoldomain-namepolicies
question_id: 193228
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# 在一台域控的\\domain_name\Sysvol\domain_name\Policies中新建的文件夹，在其他域控不能同步，不能访问

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/193228/domain-namesysvoldomain-namepolicies (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

在一台域控的\domain_name\Sysvol\domain_name\Policies中新建的文件夹，在其他域控不能同步，不能访问

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-18*

Hi,  

请问是否只有这个server有问题？如果是，建议在想要访问这个文件夹路径的其他serve中执行下面步骤测试下是否是firewall block了，如果connect failed需要unblock server的ip和对应端口。  

-  打开command line；  

-  执行‘ telnet  serverip 445  

     其中serverip是当前有问题server的IP地址

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2020-12-11*

你好，    

为更好的了解您的问题，请确认以下信息：    

域中有几台DC?    

除了这一台的文件不能复制到其他DC之外，其他DC之前的同步是否正常。    

如果只有一台DC的sysvol文件有问题，可以考虑使用非授权还原。注意是在有问题的DC上进行操作。    

https://learn.microsoft.com/en-us/troubleshoot/windows-server/group-policy/force-authoritative-non-authoritative-synchronization    

注意：请备份好的DC上的sysvol文件。

## Answer (community) — community member

*upvotes: 0 · updated: 2020-12-10*

其他域控访问不了，且复制不了
