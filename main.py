import sys
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
    registradores = linha_registradores
    
    # Remove comentários da segunda linha (valores iniciais)
    linha_valores = remover_comentarios(linhas[1])
    valores_iniciais = linha_valores.split()
    
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
    
    for linha in linhas:
        linha = linha.strip()
        if linha and not linha.startswith(';') and ':' in linha:  # Ignora linhas vazias, comentários e linhas sem rótulo
            # Remove comentários da linha
            linha_sem_comentario = remover_comentarios(linha)
            
            # Como só teremos dois tipos de instruções, podemos apenas remover as palavras da sintaxe, dai sobrarão os valores que estamos interessados
            linha_limpa = linha_sem_comentario.replace(":", "").replace("vá_para", "").replace("então", "").replace("senão", "").replace("faça", "").replace("se", "")

            # Separar a linha em partes
            partes = linha_limpa.split()
            
            if len(partes) >= 4:
                # A parte de operação e registrador vem juntas apenas separadas por underline
                operacao_registrador = partes[1]
                operacao = operacao_registrador.split("_")[0]
                registrador = operacao_registrador.split("_")[1]
                
                instrucao = [partes[0], operacao, registrador, partes[2], partes[3]]
                resultado.append(instrucao)
    
    return resultado

def main():
    """
    Função principal para lidar com argumentos da linha de comando e ler o arquivo.
    """
    # Verifica se o argumento do nome do arquivo foi fornecido
    if len(sys.argv) != 2:
        print("Uso: python main.py <nome_arquivo>")
        print("Exemplo: python main.py ex-instrucoes1.norma")
        sys.exit(1)
    
    nome_arquivo = sys.argv[1]
    linhas = ler_arquivo_linha_por_linha(nome_arquivo)
    
    if linhas:
        print("\n=== PARSING DAS LINHAS ===")
        
        # Parse das linhas de inicialização
        registradores, valores_iniciais = parser_linhas_inicializacao(linhas)
        print(f"\nQuantidade de registradores: {registradores}")
        print(f"Valores iniciais: {valores_iniciais}")
        
        # Parse das linhas de instruções
        instrucoes = parser_linhas_instrucoes(linhas)
        print(f"\nInstruções encontradas: {instrucoes}")
        
        # Exemplo de como usar os resultados
        if instrucoes:
            print(f"\nPrimeira instrução: {instrucoes[0]}")
            print(f"Total de instruções: {len(instrucoes)}")

if __name__ == "__main__":
    main()