---
id: SEG-002
titulo: Proibida a execução de código arbitrário e comandos de shell não higienizados
categoria: seguranca
severidade: obrigatoria
status: ativa
linguagens: [python]
aplica_se_a:
  - "**/*.py"
excecoes: []
---

## Regra

Funções que avaliam dinamicamente código (como `eval` ou `exec`) ou que executam comandos no sistema operacional (como `os.system` ou `subprocess` com `shell=True`) utilizando concatenação ou entrada dinâmica não devem ser utilizadas.

## Motivação

O uso de `eval()` ou comandos de shell montados via interpolação/concatenação de strings introduz vulnerabilidades críticas de Execução Remota de Código (RCE) e Injeção de Comandos (Command Injection), permitindo a execução de instruções arbitrárias no ambiente do servidor.

## Como identificar

Procurar por invocações diretas de `eval()`, `exec()`, `os.system()` ou chamadas de `subprocess` com o argumento `shell=True` recebendo variáveis dinamicas.

## Exemplo incorreto

```python
def executar_expressao(expr):
    return eval(expr)

def rodar_comando(param):
    os.system("echo " + param)
```

## Exemplo correto

```python
import ast
import subprocess

def avaliar_literal(expr):
    return ast.literal_eval(expr)

def rodar_comando_seguro(param):
    subprocess.run(["echo", param], check=True)
```
