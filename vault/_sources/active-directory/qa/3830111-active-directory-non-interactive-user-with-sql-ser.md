---
title: "Active directory non-interactive user with sql server on premise, problem conection"
type: source
tier: community-qa
source: https://learn.microsoft.com/en-us/answers/questions/3830111/active-directory-non-interactive-user-with-sql-ser
question_id: 3830111
fetched: 2026-07-25
answer_count: 1
has_accepted_answer: false
upvotes: 0
qa_tags: []
---
# Active directory non-interactive user with sql server on premise, problem conection

> **Community Q&A (upstream).** Microsoft Q&A thread, not a Microsoft support statement.
> Accepted answers are frequently version-stale or wrong. Cite as
> `web:https://learn.microsoft.com/en-us/answers/questions/3830111/active-directory-non-interactive-user-with-sql-ser (fetched 2026-07-25)` and verify against vendor documentation before relying on it.

## Question

I am trying to configure a domain user that does not have Interactive Login active en Active Directory. So far I have not succeeded.

Image of AD

  

The connection is against an on-premises Sql Server DB (not Azure DB)

The test is with java code, any suggestions?

```
private static void ConectSqlServerUrl_test() throws ClassNotFoundException {
    System.out.println("====== ConectSqlServerUrl_TEST================");
    Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
    String connectionUrl = "jdbc:sqlserver://server.com;"
            + "databaseName=DBtest;"
            + "integratedSecurity=false;"
            + "user=DOM\\user;"
            + "password=password"
            + "trustServerCertificate=true;"
            + "authenticationScheme=NTLM;"
            //+ "sslProtocol=TLSv1.2;"
            ;
    // + "loginTimeout=30;";
    
    ResultSet resultSet = null;

    try (Connection connection = DriverManager.getConnection(connectionUrl);
            Statement statement = connection.createStatement();) {

        // Create and execute a SELECT SQL statement.
        String selectSql = "SELECT ORIGINAL_LOGIN( ), GETDATE();";

        resultSet = statement.executeQuery(selectSql);

        // Print results from select statement
        System.out.println("Conexion exitosa");
        while (resultSet.next()) {
            System.out.println(resultSet.getString(1));
        }
    } catch (SQLException e) {
        Date d = new Date();
        
        System.out.println("Ejecucion: " + d.toString());
        System.out.println();
        e.printStackTrace();
    }
}
```

This Error: Login failed for user 'DOM\USER'. Reason: Attempting to use an NT account name with SQL Server Authentication. [CLIENT: XX.XX.XX.XX]

## Answer (community) — community member

*upvotes: 0 · updated: 2022-03-01*

Your question is outside the scope of this Community.

The following forum(s) have migrated to Microsoft Q&A: All English SQL Server forums!   

Visit Microsoft Q&A to post new questions.

https://docs.microsoft.com/en-us/answers/products/sql-server
