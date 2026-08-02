---
title: "unable to update adfs database permission for ESL"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1297061/unable-to-update-adfs-database-permission-for-esl
question_id: 1297061
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["microsoft-security-security-active-directory-federation-services"]
---
# unable to update adfs database permission for ESL

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1297061/unable-to-update-adfs-database-permission-for-esl (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I have the regular lockout function setup on our ADFS server and it is working fine. I am now trying to enable the Extranet Smartlockout function but I am running into a problem. When updating the ADFS artifact database using the update-adfsartifactdatabasepermission cmdlet, I was given the following error.

```
Update-AdfsArtifactDatabasePermission : PS0359: Node server.domain does not have all updates installed.  This
node must be updated before permissions can be granted.  See https://go.microsoft.com/fwlink/?linkid=864556 for more
information.
At line:1 char:1
+ Update-AdfsArtifactDatabasePermission -Credential $cred
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotImplemented: (server.domain:String) [Update-AdfsArtifactDatabasePermission],
    Exception
    + FullyQualifiedErrorId : PS0359,Microsoft.IdentityServer.Management.Commands.AddArtifactDatabasePermission
```

The server has the latest update installed. The credential I used also have the admin permission on the server. I am not sure what could be wrong with this.

Any insight? Thanks.

## Answer (community) — community member

*upvotes: 0 · updated: 2023-06-09*

This is caused by an DNS configuration issue. We managed to fix the issue by updating the DNS.

Thanks
