# Surfs Up

## Surf Recommender for California Surf Spots

## Table of Contents
1. [Background](#background)
2. [Web Application](#web-application)
3. [Data Gathering Process](#Data-Gathering-Process])
4. [Technologies Used](#technologies-used)
5. [Recommender System](#recommender-system)
6. [Future Steps](#future-steps)

## Background

When I lived in San Diego, I enjoyed going surfing on my days off. The issue that I kept finding myself in is that I went to the same five breaks, even though California has over 250 surf spots. At the time the surfing forecast applications I used did not provide any useful recommenders that could give me locations that I could visit. There also was not a way to distinguish these breaks based on difficulty of the surf. I decided to make this recommender to help people find other Surf locations that may become their new favorite location.

## Web Application 

![image](images/Home.png)

Users are given two options to select from on the Home page. They can select the Surf Recommender or the Surf Suggestor which will provide you two different sets of locations.

![image](images/Surf_Choice.png)

The User is given two options to select from on this page. Your first selection would be the county of your favorite Surf Spot.

The Second option would be the Surf Spot itself.

![image](images/Cosine_Rec.png)

The User is then given the current conditions of their selected Surf location, and the top five similar Surf locations to the selected location. This is accomplished by getting the cosine similarity of the conditions.

![image](images/Surf_Suggestion.png)

For instances where the User has never surfed in California or in San Diego in general I made a Surf Sugesstion Page.

This page take 3 option.

1. The County where you will be Surfing.
2. Your Experience Level
3. If you want a Crowded Surf Spot or not.

![image](images/Suggestion.png)



