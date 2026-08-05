---
title: "Active Directory 2019 backup on AWS EC2"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1295917/active-directory-2019-backup-on-aws-ec2
question_id: 1295917
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-client-it-pros-user-experience-user-experience-other", "windows-business-windows-server-devices-deployment-set-up-install-upgrade"]
answer_author_affiliations: ["Mvp"]
---
# Active Directory 2019 backup on AWS EC2

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1295917/active-directory-2019-backup-on-aws-ec2 (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Hi team

We are considering deploying domain controllers on AWS as ec2.

The doubt comes from the backup strategy.

AWS has a service called AWS BACKUP, the doubt is that we are not sure if recovering a snapshop is viable on the platform and not have problems.

The version we will use is windows server 2019 that although it is already prepared to virtualize AD, I have doubts about which strategy to use.

Any recommendations?

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-02*

Hello there,

In Windows Wbadmin.exe is a command-line utility that enables you to back up and restore your operating system, volumes, files, folders, and applications from a command prompt.

You can use either Windows Server backup or Wbadmin.exe to perform a System State backup of a domain controller to back up Active Directory. Microsoft recommends using either a dedicated internal disk or an external removable disk such as a USB hard disk to perform the backups.

You might be guided well if you can post this in AWS-specific forums.

Hope this resolves your Query !!

--If the reply is helpful, please Upvote and Accept it as an answer–

## Answer (community) — community member [Mvp]

*upvotes: 0 · updated: 2023-06-02*

The much simpler safer method is to always maintain at least two domain controllers for high availability and for disaster mitigation.    

--please don't forget to `upvote` and `Accept as answer` if the reply is helpful--
