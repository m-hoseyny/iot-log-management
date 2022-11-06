# IoT Log Management (Data Gathering)

This is a project to handle huge amount of data with horizantaly scale capability. With this project, users can manage their devices, create organizations and talents to visualize and gather enge devices data.

In an IoT environment, we face a huge amount of devices needing to be monitored, gather logs to be searched, set alerts to handle critical problems and … This leads us to implement a stream system to gather, process, and store data. Furthermore, data can transfer to information or knowledge, even they can return to the system as feedback.
All of the mentioned problems and needs propel us to design and implement a data flow to overcome the problems.



## The architecture
Data pipelines or streams are not new or novel ideas. Different architectures and technologies have been presented such as server monitoring. As a result, we do not need to reinvent the wheel. 
This project combines different architectures and benchmarks different projects to customize for these issues. 
Three different layers should be considered:

1. Authentication and Authorization
2. Processing and Storing
3. Alerting

To address the first layer, the device must be authenticated to the system to be known for the system. Authorization is skipped due to this stage of development. However, the component is considered.
The processing layer is the most important that process and manipulates the data to be stored in the suited database (or even lake)
The third part is not developed, but it will be located on the top of the process layer. 
* The processing and storing layers are separated components.

![Log management Arcitecture](img/Proposed%20Architecture.jpg)

The architecture above shows the overview of the system. Gateway and Processing parts are separated.


## Architecture in Detail
### Gateway
Gateway can be the single point of failure. All of system traffic pass through this layer. This layer is responsible of authentication and authorization. 


## Backend Requirements

* [Docker](https://www.docker.com/).
* [Docker Compose](https://docs.docker.com/compose/install/).
* [Poetry](https://python-poetry.org/) for Python package and environment management.

## Frontend Requirements

* Node.js (with `npm`).

