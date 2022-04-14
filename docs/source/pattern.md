# Design Pattern: Adapter #

## Problem ##

The adapter design pattern was invented for occasions when two interfaces have to communicate with each other but are not
able to due to whatever reasons (e.g. different language or format). A non-programming example for that could be something 
like Apple´s Lightning to 3.5 mm headphone adapter. 


## Solution ##

Whenever two different interfaces need to communicate an adapter comes in handy. It acts like a translator or a converter. 
Just like the Lightning to 3.5 mm adapter converts iPhone´s outlet into a socket which can be used with regular headphones. 


## Example ##


![Example](https://user-images.githubusercontent.com/91896194/154337780-f800a727-afa1-4469-b4a2-189089a07371.png)


1.	The Client is an already existing class.
2.	The Client interface symbolizes the rules and norms that everyone who wants to interact must follow.
3.	The Service represents a class that the Client wants to interact with but is not able to because of different interfaces.
4.	The Adapter is a class which knows how to interact with the Client as well as the Service. In order to do so it carries 
    out the Clients interface while translating the Service´s commands into a format which can be understood by the Client.





### Sources: ###

- https://refactoring.guru/design-patterns/adapter
- https://sourcemaking.com/design_patterns/adapter
- https://www.tutorialspoint.com/design_pattern/adapter_pattern.htm
- https://www.geeksforgeeks.org/adapter-pattern/