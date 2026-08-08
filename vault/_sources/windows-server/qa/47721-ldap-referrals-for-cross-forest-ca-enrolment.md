---
title: "LDAP Referrals for cross forest CA enrolment"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/47721/ldap-referrals-for-cross-forest-ca-enrolment
question_id: 47721
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-server-user-experience-user-experience-other"]
---
# LDAP Referrals for cross forest CA enrolment

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/47721/ldap-referrals-for-cross-forest-ca-enrolment (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am setting up Cross Forest certificate enrolment for 2 forests that have 2 way trusts and an existing mature Enterprise CA in both.    

I am using this documentation:    

https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/ff955845(v=ws.10)    

In the step by step at 5) it tell me to :    

Enable LDAP referral support on enterprise CAs. Start a command prompt, type certutil - setreg Policy\EditFlags +EDITF_ENABLELDAPREFERRALS, and press ENTER.    

If I need to back out enabling the cross forest LDAP referrals because of some unforeseen effects, am I able to do this easily? I suspect it is not as simple as re-running the command with DisableLDAPREFERRALS    

Would I be looking at a total rebuild of of both enterprise CAs along with all of the current extensive certificate configuration which would clearly be a hugely painful situation?    

any help appreciated    

Thanks    

Thread source link: https://social.technet.microsoft.com/Forums/windows/en-US/a2707ee2-f84a-4001-8d6b-516c742a8e98/ldap-referrals-for-cross-forest-ca-enrolment?forum=winserver8gen

## Answers

_No answers on this thread._
