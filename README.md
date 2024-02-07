# AirBnB Clone Project

###### Prepared by *Starlee Jiles* & *Courtney Graham*

This project is an implementation of a simplified version of the back-end of the AirBnB platform, including a command-line interface for managing various objects in the application. It features classes such as BaseModel, User, State, City, Amenity, Place, and Review, with functionalities for creating, updating, deleting, and displaying instances of these classes. This program operates as a complete console package for use by the developer.

## Command Interpreter

To start the command interpretor, run the following command in your terminal:
  - *./console.py*

How to use:
  - The command interpreter allows you to perform various actions, including _creating_, _showing_, _updating_, _deleting_, and _listing_ _instances_ of the supported classes.

Available Commands:

<details>
  <summary><b>create:</b></summary>
  <ul>
    <li>Creates a new instance of a class and saves it to the JSON file.</li>
    <ul> <li>Example on command line:</li> 
      <ul> <li>(hbnb) create BaseModel</li> </ul></ul>
</details>

<details>
  <summary><b>show:</b></summary>
  <ul>
    <li>Displays the string representation of an instance based on the class name and id.</li>
    <ul> <li>Example on command line:</li> 
      <ul> <li>(hbnb) show BaseModel 1234-5678</li> </ul></ul>
</details>

<details>
  <summary><b>destroy:</b></summary>
    <ul>
      <li>Deletes an instance based on the class name and id.</li>
      <ul> <li>Example on command line:</li> 
      <ul> <li>(hbnb) destroy BaseModel 1234-5678</li> </ul></ul>
</details>

<details>
  <summary><b>all:</b></summary>
    <ul>
      <li>Displays the string representations of all instances of a class.</li>
      <ul> <li>Example on command line:</li> 
      <ul> <li>(hbnb) all BaseModel</li> </ul></ul>
</details>

<details>
  <summary><b>update:</b></summary>
    <ul>
    <li>Updates an instance based on the class name and id by adding or updating attributes.</li>
     <ul> <li>Example on command line:</li> 
      <ul> <li>(hbnb) update BaseModel 1234-5678 name "New Name"</li> </ul></ul>
  </details>

  <details>
    <summary><b>quit:</b></summary>
    <ul>
      <li>Exits the command interpreter.</li>
      <ul> <li>Example on command line:</li> 
      <ul> <li>(hbnb) quit</li> </ul></ul>
  </details>

  
