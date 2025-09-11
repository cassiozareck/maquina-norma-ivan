
import os

def ler_arquivo_linha_por_linha(nome_arquivo):
    """
    Lê um arquivo linha por linha, imprime cada linha e retorna uma lista com todas as linhas.
    
    Args:
        nome_arquivo (str): Caminho para o arquivo a ser lido
        
    Returns:
        list: Lista contendo todas as linhas do arquivo (sem quebras de linha)
    """
    linhas = []
    
    try:
        # Verifica se o arquivo existe
        if not os.path.exists(nome_arquivo):
            print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
            return linhas
        
        # Abre e lê o arquivo linha por linha
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            numero_linha = 1
            for linha in arquivo:
                # Remove quebras de linha e espaços em branco no final
                linha_limpa = linha.rstrip()
                linhas.append(linha_limpa)
                
                
        print(f"\nTotal de linhas lidas: {len(linhas)}")
        return linhas
                
    except FileNotFoundError:
        print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
        return linhas
    except PermissionError:
        print(f"Erro: Permissão negada para ler o arquivo '{nome_arquivo}'.")
        return linhas
    except UnicodeDecodeError:
        print(f"Erro: Não foi possível decodificar o arquivo '{nome_arquivo}'. Pode não ser um arquivo de texto.")
        return linhas
    except Exception as e:
        print(f"Erro ao ler o arquivo '{nome_arquivo}': {e}")
        return linhas

def remover_comentarios(linha):
    """
    Remove comentários de uma linha (tudo após ;).
    
    Args:
        linha (str): Linha que pode conter comentários
        
    Returns:
        str: Linha sem comentários e com espaços em branco removidos
    """
    if ';' in linha:
        return linha.split(';')[0].strip()
    return linha.strip()

def parser_linhas_inicializacao(linhas):
    """
    Parser das linhas de inicialização.
    
    Args:
        linhas (list): Lista de linhas do arquivo
        
    Returns:
        tuple: (quantidade_registradores, valores_iniciais)
    """
    # Remove comentários da primeira linha (quantidade de registradores)
    linha_registradores = remover_comentarios(linhas[0])
    registradores = int(linha_registradores)
    
    # Remove comentários da segunda linha (valores iniciais)
    linha_valores = remover_comentarios(linhas[1])
    valores_iniciais = [int(valor) for valor in linha_valores.split()]
    
    return registradores, valores_iniciais

def parser_linhas_instrucoes(linhas):
    """
    Parser das linhas de instruções.
    
    Args:
        linhas (list): Lista de linhas do arquivo
        
    Returns:
        list: Lista de instruções, cada uma contendo [rótulo, operação, registrador, rótulo_verdadeiro, rótulo_falso]
    """
    resultado = []
    
    for linha in linhas[2:]:
        linha = linha.strip()
        if linha and not linha.startswith(';') and ':' in linha:  # Ignora linhas vazias, comentários e linhas sem rótulo
            # Remove comentários da linha
            linha_sem_comentario = remover_comentarios(linha)
            
            # Como só teremos dois tipos de instruções, podemos apenas remover as palavras da sintaxe, dai sobrarão os valores que estamos interessados
            linha_limpa = linha_sem_comentario.replace(":", "").replace("vá_para", "").replace("então", "").replace("senão", "").replace("faça", "").replace("se", "")

            # Separar a linha em partes
            partes = linha_limpa.split()

            rotulo = partes[0]

            # A parte de operação e registrador vem juntas apenas separadas por underline
            operacao_registrador = partes[1]
            operacao = operacao_registrador.split("_")[0]
            registrador = operacao_registrador.split("_")[1]
            
            rotulo_verdadeiro = partes[2]
            rotulo_falso = partes[3] if len(partes) >= 4 else partes[2]

            instrucao = [int(rotulo), operacao, int(registrador), int(rotulo_verdadeiro), int(rotulo_falso)]
            resultado.append(instrucao)
    
    return resultado

def ler_macros(nome_arquivo_macros="macros"):
    """
    Lê o arquivo de macros e retorna um dicionário com nome da macro e suas instruções.
    
    Args:
        nome_arquivo_macros (str): Caminho para o arquivo de macros (padrão: "macros")
        
    Returns:
        dict: Dicionário onde a chave é o nome da macro e o valor é uma lista de instruções
    """
    macros = {}
    
    try:
        # Verifica se o arquivo existe
        if not os.path.exists(nome_arquivo_macros):
            print(f"Erro: Arquivo de macros '{nome_arquivo_macros}' não encontrado.")
            return macros
        
        with open(nome_arquivo_macros, 'r', encoding='utf-8') as arquivo:
            macro_atual = None
            instrucoes_macro = []
            
            for linha in arquivo:
                linha = linha.strip()
                
                # Se a linha está vazia, pula
                if not linha:
                    continue
                
                # Se a linha termina com ':', é o nome de uma macro
                if linha.endswith(':'):
                    # Se já temos uma macro sendo processada, salva ela no dicionário
                    if macro_atual is not None:
                        macros[macro_atual] = instrucoes_macro.copy()
                    
                    # Inicia nova macro
                    macro_atual = linha[:-1]  # Remove o ':'
                    instrucoes_macro = []
                
                # Se não é nome de macro e temos uma macro ativa, adiciona a instrução
                elif macro_atual is not None:
                    # Remove comentários da linha
                    linha_sem_comentario = remover_comentarios(linha)
                    if linha_sem_comentario:  # Só adiciona se não estiver vazia após remover comentários
                        instrucoes_macro.append(linha_sem_comentario)
            
            # Adiciona a última macro se existir
            if macro_atual is not None:
                macros[macro_atual] = instrucoes_macro.copy()
        
        print(f"Macros carregadas: {list(macros.keys())}")
        return macros
        
    except FileNotFoundError:
        print(f"Erro: Arquivo de macros '{nome_arquivo_macros}' não encontrado.")
        return macros
    except PermissionError:
        print(f"Erro: Permissão negada para ler o arquivo de macros '{nome_arquivo_macros}'.")
        return macros
    except UnicodeDecodeError:
        print(f"Erro: Não foi possível decodificar o arquivo de macros '{nome_arquivo_macros}'. Pode não ser um arquivo de texto.")
        return macros
    except Exception as e:
        print(f"Erro ao ler o arquivo de macros '{nome_arquivo_macros}': {e}")
        return macros