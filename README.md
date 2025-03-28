# Persa_Bot Your guide in the journey of getting your dream tattoo by Persa Tattoo studio :)
![image](https://github.com/Kleo-Karap/My_chatbot/assets/117507917/1d894c6c-5005-49e6-b913-0ad212eaf853)
![image](https://github.com/user-attachments/assets/e66344d6-dea1-454b-8eac-132bfdb067da)

**Domain**
***
Persa_Bot is a Lead Generation assistant for tattoo studios. The bot is able to handle queries regarding the following intents: 
1. Book free consultation about a specific tattoo design (Can I book an appointment for a consultation?)
2. Tattoo cost estimator (Can you give me an estimate for the pricing?)
3. Find tattoo idea (I need inspiration for a tattoo)
***

**Problem Statement**
We know how important it is for the artist to build trust with each customer. 
So we don't want to automate the whole appointment booking process. Only the parts that are really redundant and can actually be executed via a bot exaclty like they would have been done by a human secretary.

### Scenario 1
***
- Customer wants to find a tattoo idea.
- Bot redirects to Persa's Instagram page or AI Tattoo generation apps
  
### Scenario 2
***
- User wants consultation about a specific tattoo design
- Bot asks about preferable communication channel (call/e-mail)
- e-mail
- For the e-mail channel a Form is activated in order to collect specific information from the user (Full Name, E-mail, Artist, Concept, Size, Placement)
- The bot saves user's given info in [Airtable](https://airtable.com/) sheet through an external API key, for the artist's reference.
- User says thank you
- Bot makes a summary of the saved slots and reassures that the artist will reach out to them (as requested) via e-mail
- user says bye
- bot replies bye

### Scenario 3 
User wants a price approximation for a tattoo. We can treat this either similar to Scenario 2 and let the artist contact the user via e-mail. Or we can answer this question statically with an FAQ response like: "Tattoo pricing is based on a few specific things: Location, size, complexity, and style. Our shop minimum is €50.00 and our hourly rates can be between €80.00 to €150.00 per hour based on that criteria."  

### Scenario 4



**Ideal functionalities**
1. Instagram Integration: We ideally what to integrate this chatbot with our Instagram as a messaging channel, since this is our main source for lead generation.
2. Tattoo-generation (useful feature for lead generation): OpenAI function calling: https://platform.openai.com/docs/guides/images
3. Book consulting appointment: For customers that need the artists's advice on the design and the body spot --> appointment with a fixed max duration (e.g. 30 minutes). Provide available timeslots starting from current week based on Persa's Google calendar. : Rasa resource: https://rasa.com/blog/connect-your-assistant-with-google-calendar/
4. Price estimation: FAQ page redirection in which the hourly estimate price chart along with other procedural info are provided.


**Current issues** 
Appointment booking works on the side of the user, but no access to the tattoo artist's schedule is given to ensure schedule compatibility
Temporary solution: Provide avaiable timeslots on the user to pic from. Update it's Goggle calendar. Once the slot is user, delete it from the list of avaiable slots.
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



