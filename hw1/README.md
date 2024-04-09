# Dataset Info

**Name** <p>Datasets used for the [SpanConveRT paper](https://arxiv.org/pdf/2005.08866.pdf)
1. RESTAURANTS-8K
2. DSTC8
 </p>

**Data** <p>

RESTAURANTS-8K: It comprises conversations from a commercial restaurant booking system, and covers 5 slots essential for the booking task: date, time, people, first name, last name.

DSTC8 datasets: Span-annotated datasets extracted from the Schema Guided Dialog Dataset (SGDD). The authors are interested in single-domain dialogue, so they chose
datasets from four different domains of the original dataset (SGDD) : (1) bus and coach booking, (2) buying tickets for events, (3) property viewing and (4) renting cars. </p>

**Download location** <p>https://github.com/PolyAI-LDN/task-specific-datasets/tree/master/span_extraction</p>

**Data collection** <p> 
RESTAURANTS-8K:The data set spans 5 slots (date, time, people, first name, last name) and consists of actual user utterances collected “in the wild” (Turn-based span extraction). This comes with a broad range of natural and colloquial expressions. </p>

<p> DSTC8: For each of the four domains, they chose their first subdomain (Buses_1, Events_1, Homes_1, RentalCars_1), and took all turns from conversations that stay within this sub-domain. For the requested slots feature, they check for when the system action of the turn prior contains a REQUEST action. The training and development split is kept the same for all
extracted turns.Concerning the dialogue collection procedure followed in the original dataset (SGDD), synthetic implementations of a total of 45 services or APIs over 45 domains were created. Their simulator framework interacts with these services to generate dialogue outlines, which are a structured representation of dialogue semantics. They then use a crowd-sourcing procedure to paraphrase these outlines to natural language utterances. </p>

**Design Purpose**
<p>The datasets were designed for developing and testing models for dialog slot-filling tasks in the context of task-oriented dialog systems.Speciffically they were designed for SpanConveRT dialogue slot filling model, which frames the task as a turn-based, intent-agnostic span extraction task, making the slot-filling task independent of other system components.</p>

**Annotation** <p>
<p>RESTAURANTS-8K:Each training example is a dialog turn annotated with the slots requested by the system and character-based span indexing for all occurring values. </p>
<p>DSTC8: Since the datasets are extracted from SGDD, the same annotation guidelines were followed: The annotations include the active intents and dialogue states for each user utterance and the system actions for every system utterance. They create synthetic implementations of a total of 45 services or APIs over these domains. Their simulator framework interacts with these services to generate dialogue outlines, which are a structured representation of dialogue semantics. We then used a crowd-sourcing procedure to paraphrase these outlines to natural language utterances.Their novel crowd-sourcing procedure preserves all annotations obtained from the simulator and does not require any
extra annotations after dialogue collection.</p>

**Format** <p>The datasets are stored in json files.

**Licence** <p>CC-BY-4.0, which is the Creative Commons Attribution 4.0 International. It is the less restrictive Creative Commons Attribution licence is this international version 4, which gives recipients maximum freedom to do what they want with the work of the licensor. Recipents redistributing the work must give credit to the original author of the work (= attribution) and state changes if any, including a URL or link to the original work, this CC-BY licence and a copyright notice. Author can request to remove any attribution given information. Recipients re-distributing the work to third parties may not apply legal terms or technological measures (like Tivoisation) that legally restrict the rights granted by the licence. OKF (Open Knowledge Fundation) recommends this licence. The European Commission has adopted CC-BY-4.0 for sharing documents. </p>
# Stats
<p>
  
</p>

| domain     | total_sent_count|mean_sent_length|std_sent_length|total_word_count|mean_word_length|std_word_length|vocab_size|vocab_size_no_stopwords| 
|------------|-----------------|----------------|---------------|----------------|----------------|---------------|----------|-----------------------|
| restaurants|  8673           | 1.058          | 0.254         | 68637          | 8.372          |  5.147        |  4484    |                       |
| buses      |  1434           | 1.266          | 0.494         | 11377          | 10.041         |  4.806        |  513     |                       |          
| events     |  1906           | 1.272          | 0.502         | 14562          | 9.721          |  5.037        |  786     |                       |           
| homes      |  2636           | 1.277          | 0.509         | 19733          | 9.561          |  4.764        |  752     |                       |      
| car_rental |  1095           | 1.253          | 0.472         | 8873           | 10.152         |  6.187        |  585     |                       |
| SUM        |  15744          | 1.144          | 0.387         | 123182         | 8.9476         |  5.175        |  5281    |                       |

<p>For the stats above each utterance was split into sentences and tokens for the calculations.</p>

# Discussion
<p>
Considering the first dataset, Restaurants-8k, as it is mentioned above, each training example is a (human) dialog turn annotated with the slots requested by the system and character-based span indexing for all occurring values. It seems that due to the collection process followed, the dataset maintain the naturalness of human conversations, since a lot of colloquial expressions are included. The main limitation is the lack of system respones, to be able to get a full overview of the dialogue length, in terms of system and user turns.
</p>
 
 <p> 
 The domains covered by the DSTC8 datasets were chosen due to their high number of conversations and their large variety of slots (e.g. area of city to view an apartment, type of event to attend, time/date of coach to book). Again these datasets cover only the user responses for the slot filling task.
Dataset limitations: To reflect the constraints present in real-world services and APIs, we impose a few other restrictions. First, our dataset does not expose the set of all possible slot values for some slots.
Second, real-world services can only be invoked with a limited number of slot combinations: e.g. restaurant reservation APIs do not let the user search for restaurants by date without specifying a location.  Each intent specifies a set of required slots and the system is not allowed to call this intent without specifying values for these required slots. Each intent also lists a set of optional slots with default values, which the user can override.

</p>
