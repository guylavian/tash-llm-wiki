---
title: "Issue Connecting to Active Directory User via \"Log On To\" Restriction"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2111887/issue-connecting-to-active-directory-user-via-log
question_id: 2111887
fetched: 2026-07-25
answer_count: 0
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory"]
---
# Issue Connecting to Active Directory User via "Log On To" Restriction

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2111887/issue-connecting-to-active-directory-user-via-log (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have an Active Directory (AD) server where I've created a user, and I can successfully connect to it using LDAP search with the following command:

```
ldapsearch -x -H  -D "cn=user_test,cn=users,dc=,dc=" -w  -b "cn=,cn="
```

However, when I set the "Log On To" restriction in AD and specify a particular computer name, I encounter the following error:

```
ldap_bind: Invalid credentials (49)
additional info: 80090308: LdapErr: DSID-0C090434, comment: AcceptSecurityContext error, data 52e, v4f7c
```

I have already  joined my Linux machine to the AD domain using these steps:

```
sudo apt install -y realmd libnss-sss libpam-sss sssd sssd-tools adcli samba-common-bin oddjob oddjob-mkhomedir packagekit
sudo hostnamectl set-hostname .
echo 'nameserver ' > /etc/resolv.conf
realm discover 
realm --verbose join -U '' 
```

`realm --verbose join -U '<username>' <domain_name>`  

I can verify that the computer is joined to the domain both by using `realm list` and by checking in the AD UI.

Could anyone help me understand why the "Log On To" restriction might be causing this authentication issue, and how I can resolve it? Thank you!

## Answers

_No answers on this thread._
