HiMCM 2013-2014
==========

This repository contains our paper, as well as all of our code and other research for the HiMCM 2013, Problem A.

Abstract
----------

The continental United States is divided into several states, counties, and districts all with their own populations, geography, and needs. We were provided with one such county and asked to find the most efficient allocation of ambulances in order to maximize the number of people who could be reached in under a certain response time. Using only the county’s demographics and the average travel times between the county’s zones, we devised a model to determine in which zones ambulances should be placed. This model is both scalable and efficient, and can be applied to every county, regardless of size or population distribution.

We started by determining the number of people who could be reached by an ambulance if it were placed in a certain zone. Despite the minimal information provided, we managed to extrapolate the reach of an ambulance as a function of the county’s population distribution. This provides a realistic model of the situation by accounting for the size of each zone and the fact that an ambulance may only reach a portion of the people in a zone. 

Using this data, we developed a greedy heuristic that weighed population against travel times to determine a hierarchical order for the placement of ambulances. Each zone was ranked based on how much additional coverage an ambulance placed in it would provide, and using this information, we allocated the ambulances into said zones. We then applied our algorithm and the population distribution data for a specific county to test the efficacy of the model. With only three ambulances, we managed to cover 99.4% of the county’s population of 270,000 within the given response time—an optimal solution. Using our model, we can decrease the ambulance response time for people across the United States.

