## Lesson Recap
In this lesson you learned how to use Kafka Connect to quickly integrate Kafka into a number of your existing data stores and workflows. We went hands-on with the JDBC and FileStream connectors and saw how to configure and deploy them. Next, we saw how REST Proxy can be used to bring Kafka to applications that can’t integrate native clients, but do have REST capabilities.

##Glossary of Key Terms in this Lesson: (same as provided in beginning of lesson)

- Kafka Connect - A web server and framework for integrating Kafka with external data sources such as SQL databases, log files, and HTTP endpoints.

- JAR - Java ARchive. Used to distribute Java code reusably in a library format under a single file.

- Connector - A JAR built on the Kafka Connect framework which integrates to an external system to either source or sink data from Kafka

- Source - A Kafka client putting data into Kafka from an external location, such as a data store

- Sink - A Kafka client remove data from Kafka into an external location, such as a data store

- JDBC - Java Database Connectivity. A Java programming abstraction over SQL database interactions.

- Task - Responsible for actually interacting with and moving data within a Kafka connector. One or more tasks make up a connector.

- Kafka REST Proxy - A web server providing APIs for producing and consuming from Kafka, as well as fetching cluster metadata.
