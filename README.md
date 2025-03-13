# Persa_Bot Your guide in the journey of getting your dream tattoo by Persa Tattoo studio :)
![image](https://github.com/Kleo-Karap/My_chatbot/assets/117507917/1d894c6c-5005-49e6-b913-0ad212eaf853)
![image](https://github.com/user-attachments/assets/e66344d6-dea1-454b-8eac-132bfdb067da)

**Domain**
***
Persa_Bot is a tattoo information tracker assistant for the tattoo artist industry.
***

**Problem Statement**
We know how important it is for the artist to build trust with each customer. 
So we don't want to automate the whole appointment booking process. Only the parts that are really redundant and can actually be done via an bot exaclty like they would have been done by a human secretary.

### Scenario 1
***
- Customer wants to find a tattoo idea.
- Bot redirects to Persa's Instagram page

### Scenario 2
***
Customer wants information about a specific tattoo design
- A Form is activated in order to collect specific information from the user (Full Name, E-mail, Artist, Concept, Size, Placement)
- The bot saves user's given info in [Airtable](https://airtable.com/) through an external API key.
- User says thank you
- Bot replies Bye

### Scenario 3 
Customer books consulting appointment (fixed duration 1 hour)


**Ideal functionalities**
1. Instagram Integration: We ideally what to integrate this chatbot with our Instagram as a messaging channel, since this is our main source for lead generation.
2. Tattoo-generation: OpenAI function calling: https://platform.openai.com/docs/guides/images
3. Book consulting appointment: For customers that need the artists's advice on the design and the body spot --> appointment with a fixed max duration (e.g. 30 minutes). Provide available timeslots starting from current week based on Persa's Google calendar. : Rasa resource: https://rasa.com/blog/connect-your-assistant-with-google-calendar/
4. Price estimation: FAQ page redirection in which the hourly estimate price chart along with other procedural info are provided.


**Current issues** 
Appointment booking works on the side of the user, but no access to the tattoo artist's schedule is given to ensure schedule compatibility

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



