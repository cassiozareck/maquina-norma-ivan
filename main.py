import sys
import os
from parse import *

def findRotulo(rotulo, instrucoes):
    for instrucao in instrucoes:
        if instrucao[0] == rotulo:
            return instrucao
    return None

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
        
        instrucao_atual = instrucoes[0]
        while instrucao_atual is not None:
            print(f"\nInstrução: {instrucao_atual}")

                
            if instrucao_atual[1] == "zero": # então devemos testar se o registrador escolhido é zero
                registrador = instrucao_atual[2]
                if memoria[registrador] == 0: # entao devemos ir para o rotulo verdadeiro
                    rotulo_verdadeiro = instrucao_atual[3]
                    proximo_rotulo = rotulo_verdadeiro
                else:
                    rotulo_falso = instrucao_atual[4]
                    proximo_rotulo = rotulo_falso
            elif instrucao_atual[1] == "add": # então devemos adicionar 1 ao registrador escolhido
                registrador = instrucao_atual[2]
                memoria[registrador] += 1
                proximo_rotulo = instrucao_atual[3]
            elif instrucao_atual[1] == "sub": # então devemos subtrair 1 do registrador escolhido
                registrador = instrucao_atual[2]
                memoria[registrador] -= 1
            
                proximo_rotulo = instrucao_atual[3]

            instrucao_atual = findRotulo(proximo_rotulo, instrucoes)

        print(f"\nMemória final: {memoria}")

if __name__ == "__main__":
    main()