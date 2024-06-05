# Simple Web Stack

![Image of a simple web stack](0-simple_web_stack.jpg)


## Description

This is a basic web infrastructure that hosts a website accessible at www.foobar.com. It lacks firewalls and SSL certificates to protect the server's network. All components, including the database and application server, must share the server's resources such as CPU, RAM, and SSD.

## Specifics About This Infrastructure

+ What a server is.<br/>A server is a computer system, either hardware or software, that provides services to other computers, referred to as clients.

+ The role of the domain name.<br/>A domain name offers a human-friendly way to identify an IP address. For instance, www.wikipedia.org is more memorable and easier to use than 91.198.174.192. The mapping between the domain name and the IP address is handled by the Domain Name System (DNS).

+ The type of DNS record `www` is in `www.foobar.com`.<br/>www.foobar.com uses an A record. This can be verified by running dig www.foobar.com.
Note: The exact results might vary, but for this setup, an A record is used.
An Address Mapping record (A Record) — commonly known as a DNS host record, links a hostname to its corresponding IPv4 address.

+ The role of the web server.<br/>The web server is responsible for handling HTTP or HTTPS requests and delivering the requested content or an error message to the client.

+ The role of the application server.<br/>The application server hosts and runs applications, providing essential services to users, IT departments, and organizations, enabling the deployment and operation of complex consumer or business applications.

+ The role of the database.<br/>The database server manages a structured collection of data, making it easily accessible, manageable, and updatable.

+ What the server uses to communicate with the client (computer of the user requesting the website).<br/>The communication between the client and the server occurs over the internet using the TCP/IP protocol suite.

## Issues With This Infrastructure

+ Single Points of Failure (SPOF)<br/>This infrastructure contains multiple single points of failure. For instance, if the MySQL database server fails, the entire website becomes inaccessible.

+ Downtime during maintenance<br/>Maintenance activities, such as updates or checks, require taking components offline or restarting the server. With only one server, any maintenance will result in website downtime.

+ Scalability limitations under high traffic<br/>This setup is not easily scalable. Since all components are hosted on a single server, the system can quickly become overwhelmed and slow down or crash under heavy traffic loads.
