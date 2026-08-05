---
title: "Unable to connect to Active Directory using Java client with digest-md5, ssl enabled and qop auth-int/auth-conf when channel binding and signing are required in LDAP"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/2184900/unable-to-connect-to-active-directory-using-java-c
question_id: 2184900
fetched: 2026-07-25
answer_count: 3
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Unable to connect to Active Directory using Java client with digest-md5, ssl enabled and qop auth-int/auth-conf when channel binding and signing are required in LDAP

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/2184900/unable-to-connect-to-active-directory-using-java-c (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

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
```

}

We are encountering an error when connecting to an LDAP server using the above Java code (Java 17) with certain Active Directory registry settings. Specifically, when we set the following registry entries as per the Microsoft Guide:

-  LdapEnforceChannelBinding=2

-  ldapserverintegrity=2

We receive the following error message:  LDAP: error code 49 - 80090346: LdapErr: DSID-0C0906AC, comment: AcceptSecurityContext error, data 80090346, v4563

However, when we set LdapEnforceChannelBinding=1 (while keeping ldapserverintegrity=2), the connection is successful.

Additionally, with both LdapEnforceChannelBinding=2 and ldapserverintegrity=2, we can connect to the non-SSL LDAP URL "ldap://machine.domain.com:389".

Could you please assist us in resolving this issue?

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-28*

Hello   

Good day!  

The error code 49 in LDAP typically indicates an authentication issue. The specific subcode 80090346 suggests a particular problem with the credentials being used for authentication. 

Here's a breakdown of what might be happening: 

-  Error Code 49: Indicates an invalid credentials error. 

-  AcceptSecurityContext error, data 80090346: Usually means there is an issue with the credentials provided. 

Possible causes include:

1.Invalid Username/Password: The most common cause is that the username or password is incorrect. 

2.Account Issues: The account might be locked, expired, or disabled. 

3.Time Synchronization: There could be a time synchronization issue between the client and the server. 

4.Domain Issues: The account might not belong to the domain you are attempting to authenticate against. 

Here are some steps you can take to troubleshoot: 

1.Verify Credentials: Double-check the username and password being used. 

2.Account Status: Ensure the account is active, not locked, and not expired. 

3.Time Synchronization: Make sure that the client machine and the AD server have synchronized clocks. 

4.Domain: Ensure that the account is part of the correct domain and that you are pointing to the right domain controller. 

You may also try to look at the logs on the AD server for more detailed information related to the authentication failure.

Best Regards,  

Daisy Zhou

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-27*

We are able to connect to AD using ldp.exe on Domain Controller using DIGEST method but not SASL (not supported). 

We have tried all the 6 troubleshooting steps provided. 

In the network logs we see LDAP: error code 49 - 80090346: LdapErr: DSID-0C0906AC, comment: AcceptSecurityContext error, data 80090346, v4563 response from the AD Server.

## Answer (community) — community member

*upvotes: 0 · updated: 2024-06-27*

Hello Pratik Savla,  

Thank you for posting in Microsoft Community forum.  

Please check if you can connect to AD using ldp.exe on Domain Controller.  

On Domain Controller, open ldp.exe.

Click Connection and select Connect.

https://answers-afd.microsoft.com/static/images/image-not-found.jpgI am sorry, I'm not familiar with Java. However, you can check some suggestions below.

Here's some steps you can take to troubleshoot:

1.Ensure Java version and patches: Make sure you are running the latest version of Java 17 and that all patches and security updates have been applied. There might be updates related to LDAP and SSL/TLS handling.

2.Enable Extended Protection for Authentication (EPA): If you have not done so already, you will need to enable Extended Protection for Authentication (EPA) in your application. This typically involves configuring your Java environment to support CBT.

3.Java Configuration Changes:

    - Ensure that your Java application is configured to use SSL/TLS properly.

    - You might need to set some specific system properties related to SSL/TLS. For example, you may need to disable certain older protocols and enable newer ones:

4.Review Microsoft Documentation: Microsoft's documentation about LDAP channel binding tokens and LDAP signing requirements can provide additional insights. Make sure that your configurations align with the recommended settings for both the server and the client:

How to enable LDAP signing - Windows Server | Microsoft Learn

5.Use Proper Truststore/Keystore: Ensure that your Java application has the proper truststore and keystore configuration to trust the certificates being used by the LDAP server. This is crucial for SSL/TLS connections.

6.Debugging and Logging:

    - Enable detailed logging for the LDAP connection in your Java application. This can help you see what is happening during the handshake and connection phases.

I hope the information above is helpful.

If you have any question or concern, please feel free to let us know.

Best Regards,

Daisy Zho
