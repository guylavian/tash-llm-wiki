---
title: "Windows sever 2016 AD CS"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/371057/windows-sever-2016-ad-cs
question_id: 371057
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
answer_author_affiliations: ["MicrosoftVendor"]
---
# Windows sever 2016 AD CS

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/371057/windows-sever-2016-ad-cs (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Windows sever 2016 AD CS 重新安装之后没有出现证书“凭证”配置界面，之前安装配置也没有“certificate template”？重新配置证书在哪里啊 ？    

    

想要这样的效果，怎么设置 Windows server 2016

## Answer (community) — community member [MicrosoftVendor]

*upvotes: 0 · updated: 2021-04-26*

你好，    

如果要配置凭证，可以点击更改，也可以保持默认配置。    

    

在选择CA类型是不是选择的企业CA?    

    

    

正常情况下是不需要去特别配置证书模板的，如果是企业CA的话，默认就是会出现证书模板的。    

因为不清楚你具体的配置步骤，所以不知道具体哪个环节出现了问题。    

具体的步骤，可以查看以下链接：    

https://social.technet.microsoft.com/wiki/contents/articles/11750.adcs-step-by-step-guide-single-tier-pki-hierarchy-deployment.aspx    

Fan
