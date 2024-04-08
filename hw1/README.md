# Dataset Info

**Name** <p>Datasets used for the [SpanConveRT paper](https://arxiv.org/pdf/2005.08866.pdf)
1. RESTAURANTS-8K
2. DSTC8
 </p>

**Data** <p>

RESTAURANTS-8K: It comprises conversations from a commercial restaurant booking system, and covers 5 slots essential for the booking task: date, time, people, first name, last name.

DSTC8 datasets: Span-annotated datasets extracted from the Schema Guided Dialog Dataset (SGDD). The authors are interested in single-domain dialogue, so they chose
datasets from four different domains of the original dataset (SGDD) : (1) bus and coach booking, (2) buying tickets for events, (3) property viewing and (4) renting cars. These domains were selected due to their high number of conversations and their large variety of slots (e.g. area of city to view an apartment, type of event to attend, time/date of coach to book) </p>

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

| language | Vocab | unique intent count | dialogue count | turn count | word count | word mean | word std | sentence count | sentence mean | sentence std |
|----------|-------|---------------------|----------------|------------|------------|-----------|----------|----------------|---------------|--------------|
| English  | 4110  | 12                  | 30521          | 30521      | 221009     | 7.25      | 2.50     | 30580          | 1.001         | 0.044        |
| Spanish  | 1974  | 12                  | 28936          | 28936      | 209512     | 7.24      | 2.75     | 28968          | 1.001         | 0.033        |
| Thai     | 2101  | 10                  | 28028          | 28028      | 45422      | 1.62      | 0.96     | 28184          | 1.005         | 0.080        | 
| Sum      | 7600  | 12                  | 87485          | 87485      | 475943     | 5.55      | 3.46     | 87732          | 1.002         | 0.005        | 

<p>For the stats above each utterance was split into sentences and tokens for the calculations.</p>

# Discussion
<p>The data doesn’t look natural, since it’s comprised by one-way user utterances towards a system, with the Spanish and Thai utterances being a result of translation, making the naturality suffer even more. That being the case, the data has the exact format that can be used to easily train the intent recognition model of a conversational agent for a low-resource language, especially when extending a base model from the English language to work for the target languages.</p><p>The limitations of this dataset are the low number of samples for the target languages, since it’s very expensive and slow to create a quality human translation. To mitigate this issue the researchers upsampled both the Spanish and Thai part of the datasets, by duplicating samples randomly. This brought the languages to an adequate level for training, but sacrificed data quality.</p>
