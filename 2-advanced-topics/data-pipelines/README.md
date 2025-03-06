# DEC-foundations-of-python

This repository contains all the material for the DEC Python training.
This training is developed by DIME Analytics and DECID.

## Course content

This training is structured into three parts.
Part 0 is a single-session introduction for people with no coding background.
Part 1 is a course that covers the foundations of Python
used in almost any type of Python data science project.
Part 2 is a collection of stand-alone sessions that
assumes knowledge in the foundations of Python
and each session dives deeper into the advanced topic.

* intro_data_pipelines : Overview of data pipelines with code snippets and explanatory notes on the medallion architecture, auxiliary data, transformations and orchestration. This is the entry point giving users a global scope of whats done in the other parts of the course.

* bronze : The first stage of the processing the dataset in the medallion scheme which includes loading the data from sources 

* silver : The second stage of the processing where multiple transformations and standardizations are done

* gold : The third and final stage of processing where we construct the final cleaned and ready dataset

* subnational_population: An example of auxiliary data retrieval used within the project

* kenya_func_agg : An exmaple of aggregation of the main public finance data and the auxiliary data
