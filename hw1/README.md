# Dataset Info

**Name** <p>Data used for the [SpanConveRT paper](https://arxiv.org/pdf/2005.08866.pdf)
 </p>

**Data** <p>

RESTAURANTS-8K: It comprises conversations from a commercial restaurant booking system, and covers 5 slots essential for the booking task: date, time, people, first name, last name.

4 DSTC8-based: We extract span annotated data sets from SGDD in four different domains based on their large variety of slots: (1) bus and coach booking (labelled Buses_1), (2) buying tickets for events (Events_1), (3) property viewing (Homes_1) and renting cars (RentalCars_1).</p>

**Download location** <p>https://github.com/PolyAI-LDN/task-specific-datasets/tree/master/span_extraction</p>

**Data collection** <p>In the first step of data accumulation 43000 English utterances were collected across the three listed domains, by asking native English speakers to produce utterances for each intent, the way they would ask an English conversational agent. </p> <p>Following the collection of the English utterances, two annotators would label the intent and spans that correspond to the slots for each utterance. If a disagreement arose, a third annotator would resolve the difference.</p><p>The next step was to collect the Spanish and Thai data, where native speakers of each language would translate a sample of the collected English utterances. For Spanish the same annotation procedure as English was followed, where the third annotator was a bilingual English/Spanish speaker, but for Thai as there was no bilingual speaker available, meaning that they had to throw out all utterances where the two annotators couldn’t come to the same conclusion.</p><p>In the end the Spanish and Thai portion of the dataset was upscaled to reach the same number of English samples.
<p>The main use for this dataset is to facilitate the creation of conversational models in low-resource countries through cross lingual transfer learning.</p>

**Annotation** <p>

**Format** <p>The datasets are stored in json files.

**Licence** <p>CC-BY-4.0, which is the Creative Commons Attribution 4.0 International. It is the less restrictive Creative Commons Attribution licence is this international version 4, which gives recipients maximum freedom to do what they want with the work of the licensor. Recipents redistributing the work must give credit to the original author of the work (= attribution) and state changes if any, including a URL or link to the original work, this CC-BY licence and a copyright notice. Author can request to remove any attribution given information. Recipients re-distributing the work to third parties may not apply legal terms or technological measures (like Tivoisation) that legally restrict the rights granted by the licence. OKF (Open Knowledge Fundation) recommends this licence. The European Commission has adopted CC-BY-4.0 for sharing documents.
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
