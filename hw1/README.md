# Dataset Info

**Name** <p>Datasets used for evaluation on the [SpanConveRT model](https://arxiv.org/pdf/2005.08866.pdf)
1. RESTAURANTS-8K
2. DSTC8
 </p>

**Data** <p>

RESTAURANTS-8K: It comprises conversations from a commercial restaurant booking system, and covers 5 slots essential for the booking task: date, time, people, first name, last name.

DSTC8 datasets: Span-annotated datasets extracted from the Schema Guided Dialog Dataset (SGDD). The datasets contain single-domain dialogues, on the following 4 domains:
(1) bus and coach booking, (2) buying tickets for events, (3) property viewing and (4) renting cars. </p>

**Download location** <p>https://github.com/PolyAI-LDN/task-specific-datasets/tree/master/span_extraction</p>

**Data collection** <p> 
RESTAURANTS-8K: The data set spans 5 slots (date, time, people, first name, last name) and consists of actual user utterances collected “in the wild” throuhh turn-based span extraction. No further information is provided about the data collection procedure   </p>

<p> DSTC8: For each of the four domains, they chose their first subdomain (Buses_1, Events_1, Homes_1, RentalCars_1), and took all turns from conversations that stay within this sub-domain. For the requested slots feature, they check for when the system action of the turn prior contains a REQUEST action. The training and development split is kept the same for all
extracted turns.

Concerning the dialogue collection procedure followed in the original dataset (SGDD), synthetic implementations of a total of 45 services or APIs over 45 domains were created. Their simulator framework interacts with these services to generate dialogue outlines, which are a structured representation of dialogue semantics. They then use a crowd-sourcing procedure to paraphrase these outlines to natural language utterances. </p>

**Design Purpose**
<p>The datasets were designed for testing models on the dialog slot-filling tasks .Speciffically they were designed for SpanConveRT dialogue slot filling model, which uses subword representations from conversational pretraining.The authors frame the slot-filling task as a span-extraction task and claim that this pretraining is crucial for the span-extraction performance in few-shot settings like ours, were the dataset sizes are small.

**Annotation** <p>
<p>RESTAURANTS-8K:Each training example is a dialog turn annotated with the slots requested by the system and character-based span indexing for all occurring values. </p>
<p>DSTC8: Since the datasets are extracted from SGDD, the same annotation guidelines were followed: The annotations include the active intents and dialogue states for each user utterance and the system actions for every system utterance. They create synthetic implementations of a total of 45 services or APIs over these domains. Their simulator framework interacts with these services to generate dialogue outlines, which are a structured representation of dialogue semantics. They also use a crowd-sourcing procedure to paraphrase these outlines to natural language utterances.Their procedure preserves all annotations obtained from the simulator and does not require any extra annotations after dialogue collection.</p>

**Format** <p>The datasets are stored in json files.

**Licence** <p>CC-BY-4.0, which is the Creative Commons Attribution 4.0 International. It is the less restrictive Creative Commons Attribution licence is this international version 4, which gives recipients maximum freedom to do what they want with the work of the licensor. Recipents redistributing the work must give credit to the original author of the work (= attribution) and state changes if any, including a URL or link to the original work, this CC-BY licence and a copyright notice. Author can request to remove any attribution given information. Recipients re-distributing the work to third parties may not apply legal terms or technological measures (like Tivoisation) that legally restrict the rights granted by the licence. OKF (Open Knowledge Fundation) recommends this licence. The European Commission has adopted CC-BY-4.0 for sharing documents. </p>

# Stats

| domain     |total_turn_count|total_sent_count|mean_sent_count  |std_sent_count |total_word_count|mean_word_count |std_word_count |vocab_size|vocab_size_no_stopwords| 
|------------|----------------|--------------- |---------------- |---------------|----------------|----------------|---------------|----------|-----------------------|
| restaurants| 8198           |8783            | 1.071           | 0.283         | 62330          | 7.603          |  4.738        |  4426    |       4314            |
| buses      | 1133           |1430            | 1.262           | 0.491         | 9694           | 8.556          |  4.459        |  501     |   429                 |          
| events     | 1498           |1911            | 1.276           | 0.510         | 12209          | 8.150          |  4.645        |  773     |  692                  |           
| homes      | 2064           |2621            | 1.270           | 0.505         | 16701          | 8.092          |  4.362        |  738     |    653                |      
| car_rental | 874            |1103            | 1.262           | 0.485         | 7643           | 8.745          |  5.785        |  566     |     495               |
| SUM        | 13767          |15848           | 1.151           | 0.398         | 108577         | 7.887	         |  4.740	       |  5202    |   5082                |

| domain     |unique_slots                                      |count           |
|------------|--------------------------------------------------|--------------- |
| restaurants|{people,date,time,first_name,last_name}           |5               | 
| buses      |{to_location,leaving_date,from_location}          |3               |         
| events     |{city_of_event,subcategory,date,event_name}       |4               |          
| homes      |{area,visit_date}                                 |2               |  
| car_rental |{dropoff_date,pickup_time,pickup_city,pickup_date}|4               | 
| SUM        |                                                  |17              |
<p>For the stats above each utterance was split into sentences and tokens for the calculations.Punctuation characters were omitted during word tokenization</p>

# Comments on statistics
Due to the design purpose of the datasets for evaluation of the span-extraction (slot-filling) model, there is no dialogue structure on the datasets. Each row in the 'text' part of the 'userInput' column is a human turn extracted from various conversations in a random mannner ('in the wild'). With this in mind, it is expected to observe low variation in the count of sentences per row, since we refer to single human replies/ turns, out of which specific slots should be filled, whereas it is also expected to observe high variation (std) in the count of words per turn 
  
# Discussion
<p>

Considering the first dataset, Restaurants-8k, it seems that due to the collection process followed, the dataset maintains the naturalness through colloquial expressions and informal vocabulary.
</p>
 
 <p> 
The domains covered by the DSTC8 datasets were chosen due to their high number of conversations and their large variety of slots (e.g. area of city to view an apartment, type of event to attend, time/date of coach to book). Again these datasets cover only the user responses for the slot filling task.
Dataset limitations:As mentioned in the paper of the original dataset, it does not expose the set of all possible slot values for some slots, due to impracticality and the unlimited possible slot values.
Second, the authors address the restrictions of real-word services, who can only be invoked with a limited number of slot combinations: e.g. restaurant reservation APIs do not let the user search for restaurants by date without specifying a location. In this sense, we can agree that the dataset approaches real-life scenarios.

The datasets contain all necessary data for conducting the span extraction tasks, including : UserInput (text) and the labels (slot-value,start and endIndex)
They claim that thanks to conversational pretraining the SpanConveRT model will be able to perform well on smaller datasets like ours.
</p>
