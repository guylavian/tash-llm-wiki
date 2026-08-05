---
title: "Connecting SQL server in java via kerberos authentication"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3192420/connecting-sql-server-in-java-via-kerberos-authent
question_id: 3192420
fetched: 2026-07-25
answer_count: 2
has_accepted_answer: false
upvotes: 5
qa_tags: []
---
# Connecting SQL server in java via kerberos authentication

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3192420/connecting-sql-server-in-java-via-kerberos-authent (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

Can someone help me how to connect a SQL server via Kerberos authentication in Java? I am following the steps suggested in this link but I am getting the following error

https://docs.microsoft.com/en-us/sql/connect/jdbc/using-kerberos-integrated-authentication-to-connect-to-sql-server?view=sql-server-2017

Caused by: javax.security.auth.login.LoginException: Unable to obtain Principal Name for authentication at com.sun.security.auth.module.Krb5LoginModule.promptForName(Krb5LoginModule.java:841) at com.sun.security.auth.module.Krb5LoginModule.attemptAuthentication(Krb5LoginModule.java:704)
 at com.sun.security.auth.module.Krb5LoginModule.login(Krb5LoginModule.java:617) at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
 at java.lang.reflect.Method.invoke(Method.java:498) at javax.security.auth.login.LoginContext.invoke(LoginContext.java:755) at javax.security.auth.login.LoginContext.access$000(LoginContext.java:195) at javax.security.auth.login.LoginContext$4.run(LoginContext.java:682)
 at javax.security.auth.login.LoginContext$4.run(LoginContext.java:680) at java.security.AccessController.doPrivileged(Native Method) at javax.security.auth.login.LoginContext.invokePriv(LoginContext.java:680) at javax.security.auth.login.LoginContext.login(LoginContext.java:587)

This is the code I am trying

String connectionUrl = "jdbc:sqlserver://MYHOST;databaseName=master;integratedSecurity=true;authenticationScheme=JavaKerberos";

Connection con = null; 

Statement stmt = null; 

ResultSet rs = null; 

System.setProperty("java.security.krb5.conf", "C:\KRB\krb5.conf"); 

System.setProperty("sun.security.krb5.debug", "true"); 

System.setProperty("java.security.auth.login.config", "C:\KRB\SQLJDBCDriver.config");

try 

{ 

   Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver"); 

   con = DriverManager.getConnection(connectionUrl); 

   DatabaseMetaData dbmd = con.getMetaData(); 

   System.out.println("dbmd:driver version = " + dbmd.getDriverVersion()); 

   System.out.println("dbmd:driver name = " + dbmd.getDriverName()); 

   System.out.println("db name = " + dbmd.getDatabaseProductName()); 

   System.out.println("db ver = " + dbmd.getDatabaseProductVersion()); 

} 

catch (Exception e) 

{ 

   e.printStackTrace(); 

}

## Answers

_No answers on this thread._
