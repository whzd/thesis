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

#### How to make words with vectors: Phrase generation in distributional semantics

(<https://www.aclweb.org/anthology/P14-1059/>)

In this paper the authors used an approach that revert the composition process and propose a framework of data-induced, syntax-dependent functions that decompose a single vetor into vetor sequence.
This approach was tested in a monolingual scenario and in a cross-lingual setting.

#### Automatically deriving structured knowledge bases from on-line dictionaries (NOT RELATED)

(<https://www.researchgate.net/publication/2610226_Automatically_Deriving_Structured_Knowledge_Bases_From_on-Line_Dictionaries>)

In this paper the authors present an approach to build a lexical knowledge base from on-line dictionaries.

#### Wanderlust: Extracting Semantic Relations from Natural Language Text Using Dependency Grammar Patterns

(<http://citeseerx.ist.psu.edu/viewdoc/summary;?doi=10.1.1.204.5708>)

In this paper the authors developed an algorithm called Wanderlust which automatically extracts semantic relations from natural language text.
The paper focus on the following use case: "Applying Wanderlust to the English Wikipedia corpus and use the obtained semantic relations to populate a semantic wiki."
In this use case, a precision value of over 80% was measured.

#### Neural Net Model for Featured Word Extraction

(<https://arxiv.org/abs/cs/0206001>)

In this paper the authors present a theoretical model bases on using Neural Network.
This model gives emphasis on extracting 'featured words' from an article.
Since this is a theoretical work there are no tests an therefor no result values.

#### Automatic Extraction of Definitions in Portuguese: A Rule-Based Approach

(<https://link.springer.com/chapter/10.1007%2F978-3-540-77002-2_55>)

In this paper the authors used a rule-based system for automatic extraction of definition from Portuguese texts.
The system was tested using texts from three different domains: information society, computer science for non experts and e-learning.
The results of the approach presented in this paper were in average 14% for precision, 86% for recall and 0.33 for F2 score.

**Notes:**

* A rule-based system is used to store and manipulate knowledge to interpret information in a useful way.

* The F2 score is used in applications where it's more importante to classify correctly as many positive samples as possible, rather than maximixing the number of correct classifications. (<https://www.quora.com/What-is-the-F2-score-in-machine-learning>)

### Information Retrival

**O que é ?**
**Para que serve ?**
**Como surgiu ?**
**Aplicações ?**

The discipline of information retrieval has developed automatic methods, typically of a statistical flavor, for indexing large document collections and classifying documents.

The search for information is a human activity that was always present.
The World Wide Web brought the commodity of searching information from within one's home, where before it was required to go to a place that stored said information, mainly libraries.

Information Retrival (IR), as the name suggests, is the act of retriving information from a source, but this definition can be very broad.
Christopher D. Manning et al. (cite) wrote on his book that Information Retrival is finding materials of an unstructured nature that satisfies an information need from within large collections.

The IR systems can be arranged in three groups based on its scale.
This groups are: Web search, personal information retrieval and institutional, and domain-specific search.

The Web search

### Information Extraction

Information Extraction (<https://www.nowpublishers.com/article/Details/DBS-003>)

**O que é ?**
**Para que serve ?**
**Como surgiu ?**
**Aplicações ?**

As society became more data oriented having access to both structured and unstructured data became easy.
The difference between those those types of data is that structured data is semantically defined for a target domain and is interpreted with respect to category and context.
Therefor the need for applications capable of extracting structured data had increased.

Information Extraction (IE) is the name given to the process of automatically extracting structured information from an unstructured sources, mainly texts.
The result of an IE process is different for every case since it can be tailored according to the application needs.
Nowadays this applications can be used to fullfill personal, scientific and enterprise needs.

With the evolution of technology, IE also evolved and different models for the extraction of information were created.
These models are the following: Rule-based, Statictical, Hybrids (both rule-based and statistical) and Conditional Random Fields (cite).

One example of a rule-based approach is given by Rosa Del Gaudio and António Branco (cite), in this paper the authors created a IE system that was capable extracting the definition of a word from texts written in Portuguese.

### Portuguese Sign Language

"Serão estudadas as características gramaticais da língua gestual e o seu vocabulário para perceber o grau de simplicidade das explicações produzidas."

A Letra e o Gesto Estruturas Linguísticas em Língua Gestual Portuguesa e Língua Portuguesa - Tânia Margarida Martins

Lingua Gestual Portuguesa (LGP):

* Características gramaticais

* Vocabulário

Sign language was created to allow people to communicate through signs instead of sounds.
This is particularly usefull for those that have some earing impairment that made them incapable of learing to communicate through sounds.
In the context of a sign language, a sign, which is composed by the movement of the upper limbs, the configuration and orientation of the hands and facial expression, is used to represent an idea.
According to the Portuguese Deaf Association there are around 150000 people with some type of earing impairment and around 30000 of those that use the Portuguese Sign Language (PSL). (cite1)
This language was approved by the Constitution of the Portuguese Republic, in 1997, and became one of the three oficial languages in Portugal.
There are three ways to structure a sentence In PSL: subject-object-verb, subject-verb-object or object-subject-verb.
The other parts used in Portuguese Language, like the propositions and the arthicles, are omitted when converted to PSL. (cite2) & (cite3)

Some grammatical characteristics of the Portuguese Sign Language are:

* In most cases the prefix "women" is used to identify the female version of a being while the male version is identified by the lack of a prefix "male".

* To describe a quantity of a given subject a number can be added or the use of the suffix "many".

* To represent temporal placement its used the suffix "past" or "future" to the verb.

* The negation of a sentence is defined by the word "not" at the end.

* It is used an interrogative pronoun at the end of the sentence to represent it as a question.

VOCABULARY?

## Others

### Text Evaluation Metrics

**Evaluation Metrics for Text and Creation of Writing Tool for Sports Journalism** - Luís Correia

*Flesch Reading Ease Score*

The score ranges from 0 to 100, and the readability levels were mapped to the scores.
Higher values indicate better legibility, intelligibility and readability.
The initial aim of this metric was to assess the legibility in educational texts.

The formula takes in consideration the following variables:
total words, total sentences and total syllables.

*Flesch-Kincaid Grade Level*

This metric was the recalculation of the previous metric.
Rather than having mapped values, the results are equivalent to the grade level of education required to understand the text.

The formula takes in consideration the same variables as the previous one.

*Gunning Fog Index*

The score ranges from 0 to 20.
The value of the score corresponds to the education grade that the reader should have to understand the text on the first reading.


The formula takes in consideration the following variables:
total words, total sentences and complex words.

Complex words are words with three or more syllables with some exceptions.

*Automated Readability Index*

The score value corresponds to the education grade level.

The formula takes in consideration the following variables:
total characters, total words and total sentences.

*Coleman-Liau Index*

The score value aims to approximates the minimum U.S. education grade level to comprehend a certain text.

The formula takes in consideration the following variables:
number of letters per 100 words and number of sentences per 100 words.

*Dale-Chall and New Dale-Chall*

The score aims to find the grade level required to comprehend a certain text.

The formula takes in consideration the following variables:
total words, total sentences and difficult words.

The difficult words are all the words that do not appear in a list of common words for the English language.
Having difficult words defined by a list allows to adjust said difficult to different contexts by adding words to the list.

*Simple Measure of Gobbledygook (SMOG)*

The score aims to determine the grade level required to comprehend a certain text.

The formula takes in consideration only one variable: polysyllable count.

The polysyllable words(3 or more syllables) are counted from the 30 lines (first 10, middle 10 and last 10).

*Fry Graph*

The score is based in a graph that estimates the required grade level.

The graph was built assuming that texts that contained shorter sentences and words with less syllables become more readable.

*Raygor Estimate Graph*

Like the previous one, the score is based in a graph that estimates the required grade level.

The formula used to calculate the score takes in consideration the number of words with more than 6 letters in 100 lines of text.

*FORCAST*

The score aims indicates either the grade level required or the age required.
It is used for multiple-choice quizzes and forms rather than text.

The formula takes in consideration only one variable: the number of monosyllabic words.

*SPACHE*

The score aims to determine the grade level required to comprehend a given text.
It is used for texts that are used to third-grade or lower.

The formula used to calculate the score takes in consideration the following variables:
total words, sentence length and under of unfamiliar words.

*Conclusion*

The main variables taken in consideration in the metrics used to calculate readability are the following:
Characters, complex words, syllables, words and sentences.

In a sign language this variables that might be taken in consideration are:

Number of signs per sentence.

Complex signs - Signs that required more complex hand movements or, that require both hands or that required facial expression.

### Random Information

Examples of online sign language dictionaries:
<https://www.spreadthesign.com>
<https://www.signbsl.com/>

* Unlike the previous papers where there was a fixed databased required for the training phase of the neural networks.
This means that new words that were not presented in those databases will have a chance to be wrongly defined.
The approach used in this work uses a web crawler to search for information that will later extracted and mined.
And by doing so, the definition of new words will be found somewhere and not guessed, therefor it will most likely be correct.

* In the generated definition of the concept, all the word need to be in the databases, so that the avatar can properly translated it to sign language.

* A explicação do conceito tem de ser o mais simples possível.

* O indicador da simplicidade semântica do conceito pode ser o numero de palavra ja definidas na base de dados.

### Open-source Web crawlers

<https://scrapy.org/> - Mainly written on Python

<https://github.com/internetarchive/heritrix3/wiki> - Mainly written on Java

### Server

nginx reverse proxy

explanation api - systemd service
sudo systemctl start explanation

web app - pm2 process
pm2 start website/node_modules/react-scripts/scripts/start.js --name "eac"
pm2 start eac

### TODO/Feedback

Fix report:

(Survey for the ability to understand a concept based on a generated explanation)
(explain canvas model)
(value)
(Information retrival)

\section{Technologies}
\label{sec:technologies}

\dots

\subsection{NLTK}

Natural Language Toolkit (NLTK) is a plataform to build python programs

\subsection{openNLP}

\dots

\subsection{Google Cloud Natural Language API}

\dots

(chapter3 - end of Stage 1
The tools here shown as alternatives are described in more detail in Section~\ref{sec:technologies}.)

-------------

Base de dados (class de queries como em node.js)
Tabela sings-lingua
Palavra

Mock Glosa API
method(string)
return string

Text mining approach
Coseno mais baixo entre duas frases = contextos diferentes
Coseno mais alto entre duas frases = contextos similares
(distancia de jankar)

Processo de obtenção da explicação
1. Procurar a palavra
If(source dont provide diferente context):
	2. Calcular o coseno entre as explicações.
	2.1 If(coseno < x) = newContext
Else:
	2.Dividir as explicações consoante o contexto
3. Enviar frase a frase para a Mock glosa
4. Verificar as frases com o maior numero de palavras presentes na base de dados
5. Apresentar a explicação com o maior numero de palavras, uma por contexto.

FrontEnd fix
1. Feedback button per explanation with the option to look for a new one.
2. Display an image per explanation.
3. Increase font size.
4. Fix "Fontes" to only display the source page.
5. Add "Infomação adicional" to display usefull links
6. Implemente second language using language file

-----------------------------------------------------

1. Formula de legibilidade para lingua gestual portuguesa
numero de configuraçao de mao, numero de momentos( fases dos gestos), utilizaçao de mao dominante ou ambas, numero de expressoes facias

2. artigo
descrição, indicador a desenvolver, problema, solução, possiveis resultados (não por esta ordem)

apresentar o primeiro esboço

3. text mining
nrr, nova descrisão usando outra origem

obter todo o texto, dividir o texto por frases. procurar referencias a definição já existente nas frases

4. site
site de referencia para cada linguaguem (px. portugues = priberam)
configuraçao de qual site de referencia usar

usar text mining para nova descrição ou para a primeira caso não exista site de referência

adicionar o indice  de legibilidade de cada definição, apos estar desenvolvida

5. relatorio

descrever de uma forma geral que formulas existem e como podem ser usada uma abordagem semelhante para a criação de uma formula para a linguagem gestual

### Question(s)

