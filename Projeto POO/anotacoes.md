# Menu da Farmácia ***( Nome da pessoa )*** `main.py`  

## Cadastro de clientes ***( Victor Hugo )*** `Cliente.py`  
- Busca por CPF  
- Adicionar, alterar e consultar cliente  
- Arquivo .json contendo um exemplo de cadastros
- **Classe Cliente** `CPF, Nome, Data_de_Nascimento`


## Cadastro de medicamentos ***( Arthur )*** 
- **Classe Medicamentos Quimioterápicos** `medic_quimio.py`  
  - `Nome, Principal_composto, Laboratorio, Descricao, Necessita_receita, Valor_de_venda`  
  - Arquivo .json contendo um exemplo de cadastros  
- **Classe Medicamentos Fitoterápicos** `medic_fit.py`  
  - `Nome, Principal_composto, Laboratorio, Descricao, Valor_de_venda`  
  - Arquivo .json contendo um exemplo de cadastros  
- **Classe Laboratório** laboratorio.py`  
  - `Nome, Endereco, Telefone, Cidade, Estado`   
  - Arquivo .json contendo um exemplo de cadastros  

## Efetuar Vendas ***( Erick )*** `vendas.py`
- Apenas para clientes cadastrados -> `if Cliente.CPF or Cliente.Nome:`  
- 20% de desconto para clientes idosos (acima de 65 anos)  `if Cliente.idade > 65:`  
- 10% de desconto nas compras acima de 150 reais `... medic_quimio.Valor_de_venda ... medic_fit.Valor_de_venda `
- Se Quimioterápicos for do tipo controlado, exige receita, emite alerta perguntando se o atendente verificou `if medic_quimio.Necessita_receita`
- Arquivo .json contendo um exemplo de cadastros
- **Classe Vendas** `Data_e_hora_da_venda, Produtos_vendidos, Cliente, Valor_total`  

## Emitir relatórios ***( Nome da pessoa )*** `nome_da_classe_do_emitir_relatoios.py` 
- Listar clientes  
- Listar medicamentos por ordem alfabética  
- Listar medicamento quimio ou fito  
- Estatísticas dos atendimentos realizados no dia

- Estoque (quantidade de medicamentos) 




 
