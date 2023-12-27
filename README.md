# Interaction Manager for Human-Robot Interactions: RASA
This repo contains the rasa files utilized for training the model of the conversational system within the project  ["Interaction Manager for Human-Robot Interactions"](https://github.com/changchuntzu0618/pepper_ros_idiap#interaction-manager-for-human-robot-interactions). Additionally, the [model](./models/20231218-135055-pepper-idiap_v2.tar.gz) employed in the demo is included. 

#### [Domain](./domain.yml)
The primary file for configuring the conversational system is responsible for defining the intents, entities, slots, responses, and actions utilized in the model.

#### [Story](./data/stories.yml)
This document outlines the potential storyline for the conversation.

#### [NLU](./data/nlu.yml)
This file contains and defines NLU training data used for this project.

#### [Action](./actions/actions.py)
This file includes the necessary custom action functions for the system.

#### [Trained model](./models/20231218-135055-pepper-idiap_v2.tar.gz)
A trained model used in the project.