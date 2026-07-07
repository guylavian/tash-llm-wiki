---
title: "Developing Quarkus functions"
type: reference
domain: openshift
slug: serverless-4-22-serverless-developing-quarkus-functions
tier: reference
source: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/serverless/serverless-developing-quarkus-functions
version: 4.22
family: serverless
documentKind: "Documentation"
---

# Developing Quarkus functions

[id="serverless-developing-quarkus-functions"]
= Developing Quarkus functions

After you have created a Quarkus function project, you can modify the template files provided to add business logic to your function. This includes configuring function invocation and the returned headers and status codes.

[id="prerequisites_serverless-developing-quarkus-functions"]
== Prerequisites

* Before you can develop functions, you must complete the setup steps in Setting up {FunctionsProductName}.

// templates, invoking
// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-quarkus-functions.adoc

[id="serverless-quarkus-template_{context}"]
= Quarkus function template structure

When you create a Quarkus function by using the Knative (`kn`) CLI, the project directory looks similar to a typical Maven project. Additionally, the project contains the `func.yaml` file, which is used for configuring the function.

Both `http` and `event` trigger functions have the same template structure:

.Template structure
[source,terminal]
----
.
├── func.yaml <1>
├── mvnw
├── mvnw.cmd
├── pom.xml <2>
├── README.md
└── src
    ├── main
    │   ├── java
    │   │   └── functions
    │   │       ├── Function.java <3>
    │   │       ├── Input.java
    │   │       └── Output.java
    │   └── resources
    │       └── application.properties
    └── test
        └── java
            └── functions <4>
                ├── FunctionTest.java
                └── NativeFunctionIT.java
----
<1> Used to determine the image name and registry.
<2> The Project Object Model (POM) file contains project configuration, such as information about dependencies. You can add additional dependencies by modifying this file.
+
.Example of additional dependencies
[source,xml]
----
...
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.21</version>
      <scope>test</scope>
    </dependency>
    <dependency>
      <groupId>org.assertj</groupId>
      <artifactId>assertj-core</artifactId>
      <version>3.8.0</version>
      <scope>test</scope>
    </dependency>
  </dependencies>
...
----
+
Dependencies are downloaded during the first compilation.
<3> The function project must contain a Java method annotated with `@Funq`. You can place this method in the `Function.java` class.
<4> Contains simple test cases that can be used to test your function locally.
// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-quarkus-functions.adoc

[id="serverless-invoking-quarkus-functions_{context}"]
= About invoking Quarkus functions

You can create a Quarkus project that responds to cloud events, or one that responds to simple HTTP requests. Cloud events in Knative are transported over HTTP as a POST request, so either function type can listen and respond to incoming HTTP requests.

When an incoming request is received, Quarkus functions are invoked with an instance of a permitted type.

.Function invocation options
[options="header",cols="d,d,m"]
|====
|Invocation method |Data type contained in the instance |Example of data
|HTTP POST request | JSON object in the body of the request |`{ "customerId": "0123456", "productId": "6543210" }`
|HTTP GET request | Data in the query string |`?customerId=0123456&productId=6543210`
|`CloudEvent` | JSON object in the `data` property |`{ "customerId": "0123456", "productId": "6543210" }`
|====

The following example shows a function that receives and processes the `customerId` and `productId` purchase data that is listed in the previous table:

.Example Quarkus function
[source,java]
----
public class Functions {
    @Funq
    public void processPurchase(Purchase purchase) {
        // process the purchase
    }
}
----

The corresponding `Purchase` JavaBean class that contains the purchase data looks as follows:

.Example class
[source,java]
----
public class Purchase {
    private long customerId;
    private long productId;
    // getters and setters
}
----

[id="serverless-invoking-quarkus-functions-examples_{context}"]
== Invocation examples

The following example code defines three functions named `withBeans`, `withCloudEvent`, and `withBinary`;

.Example
[source,java]
----
import io.quarkus.funqy.Funq;
import io.quarkus.funqy.knative.events.CloudEvent;

public class Input {
    private String message;

    // getters and setters
}

public class Output {
    private String message;

    // getters and setters
}

public class Functions {
    @Funq
    public Output withBeans(Input in) {
        // function body
    }

    @Funq
    public CloudEvent<Output> withCloudEvent(CloudEvent<Input> in) {
        // function body
    }

    @Funq
    public void withBinary(byte[] in) {
        // function body
    }
}
----

The `withBeans` function of the `Functions` class can be invoked by:

* An HTTP POST request with a JSON body:
+
[source,terminal]
----
$ curl "http://localhost:8080/withBeans" -X POST \
    -H "Content-Type: application/json" \
    -d '{"message": "Hello there."}'
----
* An HTTP GET request with query parameters:
+
[source,terminal]
----
$ curl "http://localhost:8080/withBeans?message=Hello%20there." -X GET
----
* A `CloudEvent` object in binary encoding:
+
[source,terminal]
----
$ curl "http://localhost:8080/" -X POST \
  -H "Content-Type: application/json" \
  -H "Ce-SpecVersion: 1.0" \
  -H "Ce-Type: withBeans" \
  -H "Ce-Source: cURL" \
  -H "Ce-Id: 42" \
  -d '{"message": "Hello there."}'
----
* A `CloudEvent` object in structured encoding:
+
[source,terminal]
----
$ curl http://localhost:8080/ \
    -H "Content-Type: application/cloudevents+json" \
    -d '{ "data": {"message":"Hello there."},
          "datacontenttype": "application/json",
          "id": "42",
          "source": "curl",
          "type": "withBeans",
          "specversion": "1.0"}'
----

The `withCloudEvent` function of the `Functions` class can be invoked by using a `CloudEvent` object, similarly to the `withBeans` function. However, unlike `withBeans`, `withCloudEvent` cannot be invoked with a plain HTTP request.

The `withBinary` function of the `Functions` class can be invoked by:

* A `CloudEvent` object in binary encoding:
+
[source]
----
$ curl "http://localhost:8080/" -X POST \
  -H "Content-Type: application/octet-stream" \
  -H "Ce-SpecVersion: 1.0"\
  -H "Ce-Type: withBinary" \
  -H "Ce-Source: cURL" \
  -H "Ce-Id: 42" \
  --data-binary '@img.jpg'
----
* A `CloudEvent` object in structured encoding:
+
[source]
----
$ curl http://localhost:8080/ \
  -H "Content-Type: application/cloudevents+json" \
  -d "{ \"data_base64\": \"$(base64 --wrap=0 img.jpg)\",
        \"datacontenttype\": \"application/octet-stream\",
        \"id\": \"42\",
        \"source\": \"curl\",
        \"type\": \"withBinary\",
        \"specversion\": \"1.0\"}"
----
// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-quarkus-functions.adoc

[id="serverless-quarkus-cloudevent-attributes_{context}"]
= CloudEvent attributes

If you need to read or write the attributes of a CloudEvent, such as `type` or `subject`, you can use the `CloudEvent<T>` generic interface and the `CloudEventBuilder` builder. The `<T>` type parameter must be one of the permitted types.

In the following example, `CloudEventBuilder` is used to return success or failure of processing the purchase:

[source,java]
----
public class Functions {

    private boolean _processPurchase(Purchase purchase) {
        // do stuff
    }

    public CloudEvent<Void> processPurchase(CloudEvent<Purchase> purchaseEvent) {
        System.out.println("subject is: " + purchaseEvent.subject());

        if (!_processPurchase(purchaseEvent.data())) {
            return CloudEventBuilder.create()
                    .type("purchase.error")
                    .build();
        }
        return CloudEventBuilder.create()
                .type("purchase.success")
                .build();
    }
}
----
// return values
// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-quarkus-functions.adoc

[id="serverless-quarkus-function-return-values_{context}"]
= Quarkus function return values

Functions can return an instance of any type from the list of permitted types. Alternatively, they can return the `Uni<T>` type, where the `<T>` type parameter can be of any type from the permitted types.

The `Uni<T>` type is useful if a function calls asynchronous APIs, because the returned object is serialized in the same format as the received object. For example:

* If a function receives an HTTP request, then the returned object is sent in the body of an HTTP response.

* If a function receives a `CloudEvent` object in binary encoding, then the returned object is sent in the data property of a binary-encoded `CloudEvent` object.

The following example shows a function that fetches a list of purchases:

.Example command
[source,java]
----
public class Functions {
    @Funq
    public List<Purchase> getPurchasesByName(String name) {
      // logic to retrieve purchases
    }
}
----

* Invoking this function through an HTTP request produces an HTTP response that contains a list of purchases in the body of the response.

* Invoking this function through an incoming `CloudEvent` object produces a `CloudEvent` response with a list of purchases in the `data` property.
// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-quarkus-functions.adoc

[id="serverless-functions-quarkus-return-value-types_{context}"]
= Permitted types

The input and output of a function can be any of the `void`, `String`, or `byte[]` types. Additionally, they can be primitive types and their wrappers, for example, `int` and `Integer`. They can also be the following complex objects: Javabeans, maps, lists, arrays, and the special `CloudEvents<T>` type.

Maps, lists, arrays, the `<T>` type parameter of the `CloudEvents<T>` type, and attributes of Javabeans can only be of types listed here.

.Example
[source,java]
----
public class Functions {
    public List<Integer> getIds();
    public Purchase[] getPurchasesByName(String name);
    public String getNameById(int id);
    public Map<String,Integer> getNameIdMapping();
    public void processImage(byte[] img);
}
----
// testing
// Module included in the following assemblies
//
// * serverless/functions/serverless-developing-quarkus-functions.adoc

[id="serverless-testing-quarkus-functions_{context}"]
= Testing Quarkus functions

Quarkus functions can be tested locally on your computer. In the default project that is created when you create a function using `kn func create`, there is the  `src/test/` directory, which contains basic Maven tests. These tests can be extended as needed.

.Prerequisites

* You have created a Quarkus function.
* You have installed the Knative (`kn`) CLI.

.Procedure

. Navigate to the project folder for your function.

. Run the Maven tests:
+
[source,terminal]
----
$ ./mvnw test
----

[id="next-steps_serverless-developing-quarkus-functions"]
== Next steps

* Build and deploy a function.
