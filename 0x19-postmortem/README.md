![Nginx Server Down](71LxIfqkLTL.jpg)
Issue Summary
The duration of the outage was recorded from 13:18 to 14:18 EAT on the 13th August, 2023.
The service that was down was the nginx server, which led to complete inaccessibility of the website resources to all users.
The root cause could have been a system error that led to the nginx server shutting down completely.

Timeline
+ The issue was detected at 13:18 EAT.
+ The issue was detected by an engineer who noticed the service was down while sending http requests to test the system.
+ The actions taken included checking the nginx configuration files for presence and correctness in addition to checking the running services on the server to ascertain the server was online. These were the leading assumptions.
+ The nature of the issue was not that deep to lead the developers down misleading paths.
+ The DevOps team was alerted to the issue upon its discovery.
+ The issue was resolved via bash scripts to automate resolution of the issue.

Root Cause and Resolution
+ The nginx server was offline.
+ The DevOps team wrote a script to bring the server back online.

Corrective and Preventative measures
+ A possible point of improvement is system monitoring to ascertain all servers are running at all times.
+ Addition of server memory monitoring should be a priority.