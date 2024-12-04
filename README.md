# Desenvolvimento de Algoritmos de Processamento de Imagens para Identificação de Pragas em Lavouras de Trigo

#### Otto Camargo Kuchkarian¹; Wânderson de Oliveira Assis²  
1. Aluno de Iniciação Científica do Instituto Mauá de Tecnologia (IMT)  
2. Professor do Instituto Mauá de Tecnologia (IMT)

## Índice
1. [Descrição](#descrição)  
2. [Objetivo](#objetivo)  
3. [Pré-requisitos](#pré-requisitos)  
4. [Como Usar](#como-usar)  
   - [Ambiente Virtual (.venv)](#venv)  
   - [Pasta Archives](#archives)  
   - [Pasta Database](#database)  
   - [Pasta Functions](#functions)  
   - [Pasta Models](#models)  
   - [Pasta SRC](#src)  
   - [Pasta Study](#study)  
   - [Pasta Tests](#tests)  
   - [Instalação de Dependências](#instalação-de-dependências)  
   - [Execução](#execução)

---

## 1. Descrição
A cultura do trigo é fundamental para a segurança alimentar, geração de renda e desenvolvimento socioeconômico no Brasil. No entanto, enfrenta grandes desafios devido à incidência de pragas que afetam a produtividade e a lucratividade dos agricultores. Com o avanço das tecnologias computacionais e ferramentas de processamento de imagens, soluções baseadas em IoT estão se tornando cada vez mais relevantes para a agricultura de precisão.

Este projeto visa o desenvolvimento de um sistema de monitoramento em tempo real de lavouras de trigo, utilizando processamento de imagens com Python, OpenCV e a plataforma Roboflow. O sistema identificará pragas comuns e espigas de trigo, integrando técnicas de Machine Learning para melhorar a precisão. O sistema será testado em diferentes condições de campo para avaliar sua robustez, contribuindo para a detecção precoce de pragas e a adoção de medidas corretivas. Com isso, espera-se aumentar a produtividade e a sustentabilidade da produção de trigo no Brasil. Além disso, o projeto poderá ser adaptado para outras culturas agrícolas, impulsionando ainda mais a agricultura de precisão.

---

## 2. Objetivo
O objetivo deste projeto é desenvolver um sistema de processamento de imagens que utilize dados coletados por câmeras e sensores na agricultura de precisão, focando na cultura do trigo. Usando Python e suas bibliotecas, além da plataforma Roboflow, o sistema será capaz de identificar padrões e pragas nas plantações. O monitoramento contínuo e automatizado permitirá a detecção precoce de pragas e contribuirá para a adoção rápida de medidas corretivas, promovendo a eficiência na gestão agrícola.

---

## 3. Pré-requisitos
Antes de iniciar, certifique-se de ter instalado os seguintes componentes em sua máquina:

- **Python 3.12.4**: [Instale o Python](https://www.python.org/downloads/)
- **Bibliotecas listadas no `requirements.txt`** (Ver [Instalação de Dependências](#instalação-de-dependências))
- **Ambiente virtual Python** (recomendado)

Além disso, é necessário um ambiente de desenvolvimento adequado, como o Visual Studio Code, PyCharm, ou qualquer outro editor de código Python.

---

## 4. Como Usar

### .venv
O ambiente virtual `.venv` armazena todas as bibliotecas necessárias para o projeto. As principais bibliotecas e suas versões são:

- [Python 3.12.4](https://www.python.org/downloads/)
- [matplotlib 3.9.0](https://pypi.org/project/matplotlib/)
- [opencv-python 4.10.0.84](https://pypi.org/project/opencv-python/)
- [roboflow 1.1.36](https://pypi.org/project/roboflow/)

### archives
A pasta `archives` contém pesquisas e materiais de referência utilizados no início do projeto, abordando temas como a tecnologia IoT e o ciclo de vida do trigo, além de outras informações essenciais.

### database
A pasta `database` organiza os dados das cinco espécies de pragas selecionadas para o modelo de identificação. Cada sub-pasta armazena informações relevantes para o treinamento do modelo. As espécies são:

1. **Metopolophium**: Pulgão-verde-pálido (*Metopolophium dirhodum*)  
2. **Rhopalosiphum**: Piolho-da-cereja-brava (*Rhopalosiphum padi*)  
3. **Schizaphis**: Pulgão-verde-dos-cereais (*Schizaphis graminum*)  
4. **Sipha maydis**: Pulgão-preto-dos-cereais (*Sipha maydis*)  
5. **Sitobion avenae**: Pulgão-da-espiga (*Sitobion avenae*)

### Functions
A pasta `functions` contém as funções essenciais usadas no projeto. Para utilizar uma função em seu código Python, basta importar da seguinte forma:

```python
from functions import nome_da_função
```

### Models
A pasta `models` contém os testes relacionados ao modelo de detecção do Roboflow. Ela inclui resultados de testes de precisão para diferentes classes de objetos, bem como o desempenho do sistema ao lidar com imagens e vídeos.

### src
A pasta `src` armazena o código-fonte principal da aplicação.

### study
A pasta `study` inclui materiais de estudo que auxiliaram no desenvolvimento do projeto, como tutoriais sobre o uso da biblioteca OpenCV e a integração com a plataforma Roboflow.

### tests
A pasta `tests` contém scripts e arquivos de teste que verificam a funcionalidade correta de diversas partes do sistema, garantindo que o projeto funcione conforme o esperado.

### Instalação de Dependências
Para garantir que todas as dependências do projeto sejam instaladas corretamente, siga os passos abaixo:

1. Clone do repositório:
```
git clone https://github.com/Ottock/projeto-identificacao-pragas.git
```

2. Entre no diretório do projeto:
```
cd projeto-identificacao-pragas
```

3. Crie e ative um ambiente virtual:
```
python -m venv .venv
source .venv/bin/activate  # Linux/MacOS
.venv\Scripts\activate      # Windows
```

4. Instale as dependências listadas no `requirements.txt`:
```
pip install -r requirements.txt
```

### Execução
Após configurar o ambiente e instalar as dependências, execute o projeto seguindo os passos abaixo:

1. Navegue até o diretório `src`:
`cd src`

2. Execute o sistema:
`python src/main.py`

Agora o sistema estará em funcionamento, monitorando as imagens para detecção de pragas em tempo real.
