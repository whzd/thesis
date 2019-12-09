# Notes

## State of art

### Suggested links

#### Automatic Extraction of Concepts from Texts and Applications

(<https://run.unl.pt/handle/10362/14268>)

In this PhD report presents an alternative approach to the extraction of relevant terms from text.
Since relevance of a term is not conceptual, the author proposes to extract all concepts, which have a less fuzzy nature, and let the downstream application decide the relevance of those concepts.
A concept in the text mining area consists of a word or sequence of words which possess semantic value.

Using a statistical and language independent approach for extraction of single-word and multi-word concepts, which the author called *ConceptExtractor*, was achieved values around 90% in **Precision** and **Recall**.
The limitations of this approach, that the author pointed out, are the fact that some multi-words concetps score high in their specificity, even though they might not be complete.

**Note:**

**Precision** is the proportion of positive identifications that were actually correct.

**Recall** is the proportion of actual positives that were identified correctly.

#### Towards Automatic Text Summarization: Extractive Methods

(<https://www.kdnuggets.com/2019/03/towards-automatic-text-summarization.html>)

In this post the author writes about the traditional approaches used in text summarization.
There are two types of summarization: extractive and abstractive.
Even though abstractive summarization is closer to human-like interpretation, extractive is proven to yield better results.

The core of extractive summarization is composed by three tasks:

1. Construction of an intermediate representation of input text

    There are two types of representation-based approaches:

    * Topic representation

    * Indicator representation

2. Scoring the sentences based on the representation

    After the intermediate representation is generated, each sentence has a score attributed to them.

    In topic representation the score represents how well a senteces explains the most importante topics of the text.

    In indicator representation the score is computed by aggregating the evidence from different weight indicators.

3. Selection of a summary comprising a number of sentences

    The system selects the top K most importante sentences.
    This can done using greedy algorithms or make the selection a optimization problem with the constraints to maximize overall importance and coherency and minimize redundancy.

Topic Representation Approaches

    Tranforms text into an intermediate representation and interpret the topics discussed in the text.

1. Topic words

    This technique identifies the words that describe the topic of a given document.

    There are two ways to compute the importance of a sentence:

    * As a function of the number of topic signatures it contains.
    This benefits longer senteces due to an higher amount of words.

    * As the proportion of the topic signatures in the sentence.
    This measures the density of the topic.

2. Frequency-driven approaches

    This approach calculates word importance based on its frequency.

    The two most common techniques used are:

    * Word probability - Words with higher probability are assumed to represent the topic of the document and are included in the summary.

    * TF-IDF (Term Frequency Inverse Document Frequency) - Assesses the importance of words and identifies very common words, that should be omitted, by giving low weights to words appearing in most documents.

3. Latent Semantic Analysis

    This is an unsupervised method for extracting a representation of text semantics based on observed words.

4. Discourse Based Method

    This technique focus on performing a discourse analysis, which consists in finding the semantic relation between textual units, to form a summary.
    The limitation of this method is that the relation need to be explicitly determined by human input.

5. Bayesian Topic Models

    This approach creates models that can represent the information that is lost in other approaches.
    Said model is constantly improved by going through many interations where a prior probability is updated with new observational evidence to produce a new probability.

Indicator representation approaches

    Describes every sentence as a list of features of importance such as sentence length, position in the document, having certain phrases, etc.

1. Graph Methods

    This methods represent the text of a document as a connected graph.
    In the graph, the vertices are sentences and the edges, that connect them, indicate how similar the two sentences are.
    The more connection a vertice has, the more importante a sentence is, and it will be included in the summary.

    A limitation of this method is that by only measuring the formal side the evaluation will be lacking the syntactic and semantic information.

2. Machine Learning

#### Automatic Extraction of Spatial Information From Text

In this thesis report the author is optimizing common information extraction algorithms, for the detection of spatial locations presented in texts written in Portuguese.
The results produced in this theses had a Precision raging from 70 to 78 and a recall raging from 30 to 49.

### Links Found

#### Learning to Explain Non-Standard English Words and Phrases

(<https://arxiv.org/abs/1709.09254>)

In this paper the authors used a Machine Learning approach to generate a explanation of a given word or expression.
The focus was non-standard expressions, such as slang, and the databased used to get the definitions of said expressions was a plataform called Urban Dictionary (<https://www.urbandictionary.com/>).

#### Definition Modeling: Learning to define word embeddings in natural language

(<https://arxiv.org/abs/1612.00394>)

In this paper the authors trained Recurrent Neural Network models to generate a definitions of a given word.
The data set used was bases on a dictionary definitions.

**NOTE:**

* Unlike the previous papers where there was a fixed databased required for the training phase of the neural networks.
This means that new words that were not presented in those databases will have a chance to be wrongly defined.
The approach used in this work uses a web crawler to search for information that will later extracted and mined.
And by doing so, the definition of new words will be found somewhere and not guessed, therefor it will most likely be correct.

* In the generated definition of the concept, all the word need to be in the databases, so that the avatar can properly translated it to sign language.

* A explicação do conceit tem de ser o mais simples possível.

O indicador da simplicidade semântica do conceito pode ser o numero de palavra ja definidas na base de dados.

### Information Retrival

"Information retrieval (IR) is finding material (usually documents) of an
unstructured nature (usually text) that satisfies an information need from
within large collections (usually stored on computers)."

### Information Extraction

## Others

Examples of online sign language dictionaries:
<https://www.spreadthesign.com>
<https://www.signbsl.com/>

### Open-source Web crawlers

<https://scrapy.org/> - Mainly written on Python

<https://github.com/internetarchive/heritrix3/wiki> - Mainly written on Java

### TODO

uc 1 encontra a definição da palavra

uc 2 avaliar a simplicidade do ponto de vista semântica de um conceito

uc 3 simplificar a explicação

ea:
information retrival
information extraction

adicionar alimentar avatar ao diagram

numero de palavras max, como metodo de avaliação

descrever o processo desde o estado base atual até ao avanºado

adopatr uma abordagem capaz de suportar varias lingua ex ficheiro de def, ou sites referencias

segunda 9/12 -18h 