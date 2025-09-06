import sys
import os
from parse import *

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

        
        # Parse das linhas de instruções
        instrucoes = parser_linhas_instrucoes(linhas)
        print(f"\nInstruções encontradas: {instrucoes}")
        
        # Exemplo de como usar os resultados
        if instrucoes:
            print(f"\nPrimeira instrução: {instrucoes[0]}")
            print(f"Total de instruções: {len(instrucoes)}")

        memoria = [0] * registradores
        for i in range(len(memoria)):
            memoria[i] = valores_iniciais[i]
        
        print(f"\nMemória inicial: {memoria}")
        
        for instrucao in instrucoes:
            print(f"\nInstrução: {instrucao}")

if __name__ == "__main__":
    main()