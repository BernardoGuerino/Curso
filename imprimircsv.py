def ler_arquivo_csv () :
    with open(arquivo_csv, 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)

        except FileNotFoundError:
            print(f'O arquivo {arquivo_csv} não foi encontrado.')
    
def imprimir_csv(arquivo_csv):
    ler_arquivo_csv()
    for linha in leitor_csv:
        imp1=(linha['Valor']*imp1)/100
        imp2=(linha['Valor']*imp2)/100
        imp3=(linha['Valor']*imp3)/100
        frete=(linha['Frete']/qnt)
        valor_final=valor+imp1+imp2+imp3+frete
        venda=valor_final+(valor_final*(ganho/100))    
        print(linha)
           
   