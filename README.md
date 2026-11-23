# Classificador de Sentimento de Comentários

Aplicação em Python desenvolvida como parte do P0 — P0-PRIMEIRO-FLUXO-LLM, que recebe um comentário digitado no terminal e usa o
LLM **Gemini** para classificá-lo como **Positivo**, **Neutro** ou **Negativo**.

## Como a solução funciona

1. O usuário digita um comentário no terminal (`src/main.py`).
2. `src/client.py` lê a configuração das variáveis de ambiente (`.env`).
3. O código monta uma requisição HTTP: as instruções da tarefa vão na mensagem
   de sistema e o comentário vai na mensagem do usuário.
4. A requisição é enviada por `POST` à API REST do Gemini (formato "chat completions"),
   com a chave no cabeçalho `Authorization`.
5. O código lê o JSON da resposta, extrai o texto da categoria e o exibe ao usuário.

## Provedor e modelo

- **Provedor:** Google Gemini, acessado pelo Google AI Studio.
- **Modelo:** `gemini-3.1-flash-lite`
- **Parâmetros configurados:** `temperature=0.0` (respostas mais consistentes, adequado
  a classificação), `max_tokens=1000` e `timeout=30` segundos.

## Estrutura do projeto

```
.
├── src/
│   ├── client.py        # configuração e chamada ao LLM
│   └── main.py          # entrada pelo terminal e exibição do resultado
├── requirements.txt
├── .env.example
└── README.md
```

## Instalação

Pré-requisitos: Python 3.9 ou superior e Git.

```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPO.git
cd NOME_DO_REPO
python -m venv .venv
```

Ative o ambiente virtual:

- Windows (PowerShell): `.venv\Scripts\Activate.ps1`
- Windows (CMD): `.venv\Scripts\activate.bat`
- Linux/macOS: `source .venv/bin/activate`

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração do acesso ao LLM

1. Gere uma chave de API gratuita em https://aistudio.google.com (opção **Get API key**).
2. Copie o arquivo de exemplo para `.env`:
   - Windows: `copy .env.example .env`
   - Linux/macOS: `cp .env.example .env`
3. Abra o `.env` e substitua `coloque_sua_chave_aqui` pela sua chave.

| Variável | Descrição | Valor usado |
|---|---|---|
| `LLM_BASE_URL` | Endereço base da API | `https://generativelanguage.googleapis.com/v1beta/openai/` |
| `LLM_API_PATH` | Caminho do endpoint | `/chat/completions` |
| `LLM_API_KEY` | Chave de API (**secreta**) | sua chave |
| `LLM_MODEL_NAME` | Nome do modelo | `gemini-3.1-flash-lite` |
| `LLM_TEMPERATURE` | Aleatoriedade das respostas | `0.0` |
| `LLM_MAX_TOKENS` | Tamanho máximo da resposta | `1000` |
| `LLM_TIMEOUT` | Tempo máximo de espera (segundos) | `30` |

O `.env` está no `.gitignore` e **nunca** deve ser enviado ao GitHub.

## Execução

Na raiz do projeto, com o ambiente virtual ativo:

```bash
python -m src.main
```

## Exemplos de entrada e saída

```
--- Classificador de Sentimentos ---
Digite o comentário para analisar: Adorei o atendimento, super recomendo!

Sentimento identificado: Positivo
```

```
--- Classificador de Sentimentos ---
Digite o comentário para analisar: O produto chegou na terça-feira.

Sentimento identificado: Neutro
```

```
--- Classificador de Sentimentos ---
Digite o comentário para analisar: Péssimo, demorou demais e veio quebrado.

Sentimento identificado: Negativo
```

## Uso de ferramentas de IA no desenvolvimento

Usei o Claude (Anthropic) como apoio para planejar as etapas do projeto,
entender alguns conceitos, corrigir erros e estruturar o README. A escolha do
problema, desenvolvimento do código, a execução dos testes e a validação dos resultados foram feitas por mim.

## Autor

Desenvolvido por **Lorrany Queiroz Dantas Vital**
