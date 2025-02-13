# Persa_Bot Your guide in the journey of getting your dream tattoo by Persa Tattoo studio :)
![image](https://github.com/Kleo-Karap/My_chatbot/assets/117507917/1d894c6c-5005-49e6-b913-0ad212eaf853)
![image](https://github.com/user-attachments/assets/e66344d6-dea1-454b-8eac-132bfdb067da)

**Domain**
***
Persa_Bot is a tattoo information tracker assistant for the tattoo artist industry.
***

**Problem Statement**

*Tattoo info tracking*
<p> Customer is asked to submit information about their tattoo idea. 

   1. Full Name
   2. E-mail
   3. Artist name
   5. Concept
   6. Size
   7. Placement 

### Scenario 1
***
Customer wants to find a tattoo idea.
The bot  is able to 
1) Redirect to Persa's Instagram page

### Scenario 2
***
Customer wants to book an appointment
The bot 
1) Saves customer's data in [Airtable](https://airtable.com/) (Full Name, E-mail, Artist, Concept, Size, Placement) through an external API key.

   
**Future Objectives**
We know how important it is for the artist to build trust with each customer. 
So we don't want to automate the whole appointment booking process. Only the parts that are really redundant and can actually be done via an bot exaclty like they would have been done by a human secretary.

**Ideal functionalities**
1. Instagram Integration: We ideally what to integrate this chatbot in our Instagram account chat, since this is our main source for lead generation.
2. Tattoo-generation: Connect the chatbot with a platform like : https://blackink.ai/. This site requires the user to create an account, but we would like the user of the chat to have direct access to the pltforms interface to be able to generate their tattoo straightaway.
3. Book tattoo appointment: Based on the tattoo design, give the customer an appointment duration estimate, and then provide available timeslots starting from current week based on Persa's Google calendar.
4. Book consulting appointment: For customers that need the artists's advice on the design and the body spot --> appointment with a fixed max duration (e.g. 30 minutes).
5. Price estimation: FAQ page redirection in which the hourly estimate price chart along with other procedural info are provided.
6. Geolocation: Customer asks studio's location: Bot responds with a pin to Google maps from the user's current location to the studio


**Current issues** 

# Getting started
```
pip install rasa
```
Split terminal in two, first run:

```
rasa run actions
```

then run:
```
rasa shell
```



