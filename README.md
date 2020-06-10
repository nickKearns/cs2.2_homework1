# Homework 1: Graph ADT & Traversals

Follow the instructions [here](https://make-school-courses.github.io/CS-2.2-Graphs-Recursion/#/Assignments/01-Graph-ADT) to complete this assignment.

## Discussion Questions

1. How is Breadth-first Search different in graphs than in trees? Describe the differences in your own words.

Trees are acyclic meaning that there cannot be a way to get back to any given node without going backwards through nodes already seen. Graphs can have cycles so it is possible to end up going back to a node or vertex that has already been searched. So if you tried the way you do breadth first search on a graph the way you would do it for a tree you could end up in a never ending loop of searching through the same nodes over and over.

2. What is one application of Breadth-first Search (besides social networks)? Describe how BFS is used for that application. If you need some ideas, check out [this article](https://www.geeksforgeeks.org/applications-of-breadth-first-traversal/?ref=rp).

One application of Breadth first search is gps navigation. BFS is a great way to find the shortest path between two points through a graph and using streets as edges you could map out an area into a graph with buildings and things like that as vertices and the roads as edges. So using BFS to find the shortest path is probably a great way to start I would imagine. But I'm sure there are more variables at play when something like google maps tries to find the fastest route but finding the shortest route is something that could definitely be taken care of using Breadth-first Search.