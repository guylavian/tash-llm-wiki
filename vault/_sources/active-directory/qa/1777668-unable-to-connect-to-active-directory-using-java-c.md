---
title: "Unable to connect to Active Directory using Java client with digest-md5, ssl enabled and qop auth-int/auth-conf when channel binding and signing are required in LDAP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/1777668/unable-to-connect-to-active-directory-using-java-c
question_id: 1777668
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: ["windows-business-windows-client-it-pros-directory-services-directory-services-active-directory", "windows-business-windows-server-user-experience-user-experience-other"]
answer_author_roles: ["Q&A User"]
---
# Unable to connect to Active Directory using Java client with digest-md5, ssl enabled and qop auth-int/auth-conf when channel binding and signing are required in LDAP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/1777668/unable-to-connect-to-active-directory-using-java-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

We are trying to connect to LDAP using below sample java code (Java 17).

```
import javax.naming.*;
import javax.naming.ldap.InitialLdapContext;
import javax.naming.ldap.LdapContext;
import java.util.Hashtable;
public class LDAPBindSSLExample {
    public static void main(String[] args) throws Exception {
        String ldapURL = "ldaps://machine.domain.com:636";
        String username = "username"; // without @domain
        String domainName = "domain.com";
        String password = "password";
        String timeout = "5000";
        Hashtable env = new Hashtable<>();
        env.put(Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.ldap.LdapCtxFactory");
        env.put("java.naming.security.sasl.realm", domainName);
        env.put(Context.SECURITY_AUTHENTICATION, "DIGEST-MD5");
        env.put(Context.SECURITY_PROTOCOL, "ssl");
        env.put("javax.security.sasl.qop", "auth");
        env.put(Context.PROVIDER_URL, ldapURL);
        env.put(Context.SECURITY_PRINCIPAL, username);
        env.put(Context.SECURITY_CREDENTIALS, password);
        env.put(Context.REFERRAL, "ignore");
        env.put("java.naming.ldap.version", "3");
        env.put("com.sun.jndi.ldap.tls.cbtype", "tls-server-end-point");
        env.put("com.sun.jndi.ldap.connect.pool", "true");
        env.put("com.sun.jndi.ldap.connect.timeout", timeout);
        LdapContext ctx = null;
        try {
            ctx = new InitialLdapContext(env, null);
            System.out.println("Bind successful");
        } catch (Exception e) {
            e.printStackTrace();
	} 
        finally {
            if (ctx!=null) {
                ctx.close();
            }
        }
    }
}
```

We are encountering an error when connecting to an LDAP server using the above Java code (Java 17) with certain Active Directory registry settings. Specifically, when we set the following registry entries as per the Microsoft Guide:

-  LdapEnforceChannelBinding=2

-  ldapserverintegrity=2

We receive the following error message: LDAP: error code 49 - 80090346: LdapErr: DSID-0C0906AC, comment: AcceptSecurityContext error, data 80090346, v4563

However, when we set LdapEnforceChannelBinding=1 (while keeping ldapserverintegrity=2), the connection is successful.

Additionally, with both LdapEnforceChannelBinding=2 and ldapserverintegrity=2, we can connect to the non-SSL LDAP URL "ldap://machine.domain.com:389".

Could you please assist us in resolving this issue?

## Answer (community) — Q&A User

*upvotes: 0 · updated: 2025-09-05*

We are facing the same issue with one of our customers. Did anyone ever help resolve this?
