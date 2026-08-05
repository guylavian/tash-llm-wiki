---
title: "Active Directory 复制错误 1722：RPC 服务器不可用"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1692190/active-directory-1722-rpc
question_id: 1692190
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Active Directory 复制错误 1722：RPC 服务器不可用

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1692190/active-directory-1722-rpc (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

碰到一个ad问题，今天远程上域控，打开AD用户与计算机，无论是选择OU还是用户看属相，都提示“不能显示域服务器对象，该服务器不可操作”，

主机：单域控+dns +文件共享smb

ping -a 域名  能正常获取域服务器Ip，

上网认证也能认证（我用了ldap认证）

计算机加域也能正常加上，域用户也能登录，就是组策略脚本没有推送运行，

看了下日志；

运行dcdiag自检，返回信息提示题目的错误，信息这里1、filename.log，，2、test.log

，全局目录GC我也测试过，注册表和端口都正常的，现在就是不清楚如何回复服务正常运行，各位大佬帮忙看看这咋搞，单域控，不敢乱重启

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-11*

计算机加域也能正常加上，域用户也能登录，就是组策略脚本没有推送运行，

这个今天又试了一下，加域没提示错误，但是域用户，提示没可链接的服务器了
