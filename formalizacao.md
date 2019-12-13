# Formalização

## 1 O orientador reviu a formalização? NB: não deve ser submetida sem ser revista pelo orientador.

Sim

## 2 Título

Explicação automática de conceitos

## 3 Número (da proposta) do projeto (cf. Moodle)

20192031

## 4 Organização proponente

GILT - ISEP

## 5 Outra, se não estiver na lista

## 6 Sigla do orientador

NFE

## 7 Sigla/Nome do co-orientador

## 8 Nome do supervisor (empresa)

## 9 mail do supervisor (empresa)

## 10 Problema

A explicação de conceitos é um processo necessário para a aprendizagem, quer seja em ambiente educativo, quer seja
no nosso dia-a-dia em contexto profissional ou pessoal. Esta necessidade é particularmente determinante em línguas
com léxicos pouco elaborados, como é o caso das línguas gestuais e, em particular da Língua Gestual Portuguesa
(LGP). O léxico da Língua Gestual Portuguesa é constituído por vários gestos, correspondendo cada um a uma
palavra/termo ou expressão da língua Portuguesa. No entanto, existem muitas palavras para as quais não existe um
gesto correspondente. Essas palavras/conceitos têm que ser explicadas usando o léxico disponível. Este problema é
recorrente em domínios científicos. Termos como “nanotecnologia” não têm um gesto correspondente sendo necessário
explicar o conceito por outras palavras. Pretende-se nesta tese desenvolver um sistema automático de interpretação que
possa resolver este problema recorrendo a técnicas da área do Information Retrieval (IR), Information Extraction (IE) e
Text Mining (TM).

## 11 Objetivos

Deve ser criada uma aplicação que utilize técnicas de Text Mining, Information Scraping e Information Retrival para poder gerar uma explicação para uma dada palavra ou expressão. A expressão gerada será posteriomente traduzida para linguagem gestual através de um avatar, o qual faz parte de outro projeto do GILT-ISEP.
Esta aplicação pretende assim promover a inclusão e igualdade de oportunidades da comunidade surda, facilitando a produção de conteúdos em LGP.

## Outcomes

Como é que o desenvolvimento do projeto endereça os outcomes da UC?

Sugestão: preencher as secções seguintes com partes do texto do “problema” e dos “objetivos”.

Nota: Pode ser necessário alterar o texto original do “problema” e “objetivos” para que todos os outcomes sejam
contemplados.

## Outcome 1: Interpretar o problema a resolver (Nível 5)

### 12 O problema a resolver será analisado, interpretado e sistematizado?

Sim

### 13 Qual a abordagem/método a seguir para interpretar e sistematizar o problema a resolver?

Numa fase preliminar irá haver discussão com a comunidade surda, em particular no Agrupamento de Escolas Dona Maria II, escola de referência para surdos, para perceber quais as necessidades reais dos utilizadores finais. Em paralelo com este estudo iremos analisar alguns dicionários de língua gestual disponíveis online com o intuíto de identificar funcionalidades e formas de interação comuns neste tipo de aplicações.

## Outcome 2: Sintetizar conhecimento existente relacionado com o problema ou as abordagens para a resolução do problema (Nível 4)

### 14 Será sintetizado conhecimento relacionado com o problema e métodos e tecnologias para a sua resolução?

Sim

### 15 Qual a abordagem/método a seguir para sintetizar o conhecimento existente relacionado com o problema ou as abordagens para a resolução do problema? Se não for feito, porquê?

Será feito um levantamento do estado da arte relacionada com métodos e abordagens para a extração de conceitos presentes em texto e de aplicações onde é gerada uma explicação para uma determinada palavra ou expressão. Serão estudadas as características gramaticais da língua gestual e o seu vocabulário para perceber o grau de simplicidade das explicações produzidas.

## Outcome 3: Avaliar diferentes abordagens para a resolução do problema (Nível 5)

### 16 Serão avaliados métodos ou tecnologias para resolução do problema?

Sim

### 17 Como serão avaliadas as diferentes abordagens (métodos e tecnologias) para a resolução do problema? Se não for avaliada, porquê?

Existem várias técnicas utilizadas para a extração de conceitos. Pretende-se que sejam avaliadas as técnicas utilizadas previamente, em trabalhos desenvolvidos (ver referências bibliográficas), assim como outras existentes para que sejam racionalmente e justificadamente aplicadas no desenvolvimento da solução. A avaliação que dará resultado à escolha de umas técnicas em detrimento de outras será feita com base na eficiência, na documentação e suporte disponível.

## Outcome 4: Desenhar uma solução para o problema adotando boas práticas de engenharia informática (Nível 4)

### 18 Será desenhada (design) uma solução informática?

Sim

### 19 Qual o método preconizado para desenhar uma solução e alternativas? É assumida uma arquitetura (qual)?

Em primeiro lugar será desenhada uma abordagem de alto nível que permita identificar e caracterizar os componentes do sistema a implementar. Cada um destes componentes será desenvolvido recorrendo às tecnologias atuais que permitam implementar o algoritmo mais simples que possa resolver o problema. O componente será avaliado e, caso não corresponda às expetativas será desenhada uma atualização ao componente para resolver problemas pendentes. Este processo iterativo será seguido até que o componente cumpra as especificações. Serão também apresentadas e discutidas alternativas de design.

## Outcome 5: Construir a solução para o problema aplicando boas práticas de engenharia informática (Nível 4)

### 20 Vai ser realizada implementação/construção?

Sim

### 21 Como é preconizada a construção/implementação da solução (e.g. método, tecnologia)?

Será utilizada uma abordagem SCRUM, com sprints de duração por volta de 15 dias, onde os componentes
desenhados, de acordo com a metodologia descrita no ponto 4, irão sendo integrado na solução à medida que vão
sendo desenvolvidos. Serão feitos testes de integração, testes funcionais e testes de sistema à medida que a
implementação atinja um estado em que estes tipos de testes sejam viáveis.

## Outcome 6: Avaliar a solução desenhada/implementada aplicando boas práticas de engenharia informática (Nível 5)

### 22 A solução proposta vai ser avaliada?

Sim

### 23 Como é preconizada a avaliação da solução? Se não for avaliada, porquê?

Serão utilizadas métricas de avaliação para algoritmos de text mining. A solução será avaliada quanto à sua precisão e à simplicidade da definição gerada tendo em conta as limitações do léxico da LGP.

## 24 Referências bibliográficas

Noraset, T., Liang, C., Birnbaum, L., & Downey, D. (2017, February). Definition modeling: Learning to define word embeddings in natural language. In Thirty-First AAAI Conference on Artificial Intelligence.

Ventura, J. M. (2014). Automatic Extraction of Concepts from Texts. Lisboa: Faculdade de Ciências e Tecnologia - Universidade Nova de Lisboa;

Del Gaudio R., Branco A. (2007) Automatic Extraction of Definitions in Portuguese: A Rule-Based Approach. In: Neves J., Santos M.F., Machado J.M. (eds) Progress in Artificial Intelligence. EPIA 2007. Lecture Notes in Computer Science, vol 4874. Springer, Berlin, Heidelberg;

Das, A., Marko, M., Probst, A., Porter, M. A., & Gershenson, C. (2008). Neural net model for featured word extraction. In Unifying Themes in Complex Systems IV (pp. 353-361). Springer, Berlin, Heidelberg;

Ni, K., & Wang, W. Y. (2017). Learning to explain non-standard English words and phrases. arXiv preprint arXiv:1709.09254.

Dinu, G., & Baroni, M. (2014, June). How to make words with vectors: Phrase generation in distributional semantics. In Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) (pp. 624-633).

## 25 Descrição do estágio (se existir)

(e.g. Duração, Horário, Local)

## 26 Módulos curriculares (obrigatório)

1. Análise de problemas, pesquisa e escrita técnico-científica (obrigatório: escolher como 1)

2. Experimentação e avaliação

3. Análise de valor de negócio

4. Demonstração de teoremas

5. Investigação operacional

6. Modelação e simulação

7. Especificação formal de algoritmos e verificação

8. Equações diferenciais
