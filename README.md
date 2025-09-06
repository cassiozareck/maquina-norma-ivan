# Máquina Norma

## Especificação

A **Máquina Norma** é uma máquina de computação simples que opera com registradores de inteiros e suporta um conjunto básico de operações.

### Características Principais

- **Tipo**: Máquina de registradores
- **Registradores**: N registradores de inteiros (configurável)
- **Operações**: 3 tipos de operações fundamentais

### Operações Suportadas

#### 1. Operação de Teste
- **`se zero_X`**: Testa se o registrador X é igual a zero
- **Resultado**: Verdadeiro ou falso

#### 2. Operações Aritméticas
- **`add_X`**: Adiciona 1 ao registrador X
- **`sub_X`**: Subtrai 1 do registrador X

### Sintaxe da Linguagem

#### Inicialização
```
<quantidade_registradores> ; quantidade de registradores
<valor1>, <valor2>, ..., <valorN> ; valores iniciais dos registradores
```

#### Instruções
```
<rótulo>: se zero_<registrador> então vá_para <rótulo_verdadeiro> senão vá_para <rótulo_falso>
<rótulo>: faça add_<registrador> vá_para <próximo_rótulo>
<rótulo>: faça sub_<registrador> vá_para <próximo_rótulo>
```

### Exemplo de Programa

```
4               ; quantidade registradores
0, 0, 0, 0      ; seus valores iniciais

1: se zero_b então vá_para 9 senão vá_para 2 
2: faça add_a vá_para 3 
3: faça add_a vá_para 4 
4: faça sub_b vá_para 1
```

### Funcionalidades do Parser

- ✅ **Parser da linguagem**: Analisa e processa arquivos .norma
- ✅ **Remoção de comentários**: Remove automaticamente comentários (texto após `;`)
- ✅ **Inicialização de registradores**: Configura quantidade e valores iniciais
- ✅ **Processamento de instruções**: Identifica e estrutura as operações

### Como Usar

```bash
python main.py <arquivo.norma>
```

Exemplo:
```bash
python main.py ex-instrucoes1.norma
```

### Status do Projeto

- [x] Criar parser da linguagem
- [x] Criar inicializador de registradores e quantidade de registradores
- [ ] Criar as operações (testa se zero, adiciona em reg x ou y)
- [ ] Criar 3 macros escolhidas
- [ ] Apresentar saída da computação