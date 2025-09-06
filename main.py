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
        
        pc = 0
        while pc < len(instrucoes):
            instrucao = instrucoes[pc]
            print(f"\nInstrução: {instrucao}")
            if instrucao[1] == "zero": # então devemos testar se o registrador escolhido é zero
                registrador = instrucao[2]
                if memoria[registrador] == 0: # entao devemos ir para o rotulo verdadeiro
                    rotulo_verdadeiro = instrucao[3]
                    pc = rotulo_verdadeiro
                else:
                    rotulo_falso = instrucao[4]
                    pc = rotulo_falso
            elif instrucao[1] == "add": # então devemos adicionar 1 ao registrador escolhido
                registrador = instrucao[2]
                memoria[registrador] += 1
                proximo_rotulo = instrucao[3]
                pc = proximo_rotulo
            elif instrucao[1] == "sub": # então devemos subtrair 1 do registrador escolhido
                registrador = instrucao[2]
                memoria[registrador] -= 1
                proximo_rotulo = instrucao[3]
                pc = proximo_rotulo
            pc += 1

        print(f"\nMemória final: {memoria}")

if __name__ == "__main__":
    main()