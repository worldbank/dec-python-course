# Introduction to data pipelines

Data pipelines are essential for efficiently collecting, processing, and analyzing data. They enable automation, reproducibility, scalability, and more importantly, reliability in data workflows, ensuring data is clean, structured, and ready for analysis. In this hands-on session, we will explore the fundamentals of data pipelines, including their structure, key components, and practical applications.

Using a public finance dataset, we will walk through an end-to-end example, introducing the Medallion architecture—a framework for organizing data in Bronze, Silver, and Gold layers. We will also demonstrate how to execute different stages of the pipeline using workflow orchestration to automate tasks within the databricks environment.

Basic proficiency in Python would be assumed, and we will walk through the PySpark code during the session, explaining concepts as necessary. By the end of this session, participants will have a foundation in designing and running data pipelines for their own datasets.

## Folder contents

* intro_data_pipelines : Overview of data pipelines with code snippets and explanatory notes on the medallion architecture, auxiliary data, transformations and orchestration. This is the entry point giving users a global scope of whats done in the other parts of the course.

* bronze: The first stage of the processing the dataset in the medallion scheme which includes loading the data from sources 

* silver: The second stage of the processing where multiple transformations and standardizations are done

* gold: The third and final stage of processing where we construct the final cleaned and ready dataset

* subnational_population: An example of auxiliary data retrieval used within the project

* kenya_func_agg: An example of aggregation of the main public finance data and the auxiliary data
