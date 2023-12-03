from functions import *

create_tables()

#Criação dos condomínios
create_cond("12345678901234", 5, 10, "Condomínio A", "Residencial", "2023-01-01")
create_cond("98765432109876", 3, 8, "Condomínio B", "Comercial", "2023-02-01")

#Leitura dos condomínios
condominios = get_conds()
print("Condomínios:", condominios)

#Atualização do condomínio com ID 1
update_conds(1, "Condomínio X")
condominios = get_conds()
print("Condomínios atualizados:", condominios)


#Criação dos moradores
create_residents("João Silva", "12345678901", "2020-02-10")
create_residents("Maria Santos", "98765432109", "2022-02-15")
create_residents("Carlos Pereira", "34567890123", "2023-01-01")

#Leitura dos moradores
moradores = get_residents()
print("Moradores:", moradores)

# Atualização do morador com ID 1
update_residents(1, "João da Silva", "98765432109")
moradores = get_residents()
print("Moradores atualizados:", moradores)


#Criação das localizações
create_location(1, "SP", "São Paulo", "Centro", "Avenida Paulista", "3524")
create_location(1, 'SC', 'Balneario camboriu', 'Centro', 'Avenida atlantica', '10')

#Leitura das localizações
localizacoes = get_locations()
print("Localizacoes:", localizacoes)

#Atualização da localização com ID 1
update_location(1, "RJ", "Rio de Janeiro", "Copacabana", "Rua 10", "456")
localizacoes = get_locations()
print("Localizacoes atualizadas:", localizacoes)


#Criação das relações morador_condominio
create_resident_cond(1, 1, "101", 2)
create_resident_cond(2, 2, "203", 2)
create_resident_cond(3, 1, "401", 2)

#Leitura das relações Morador_condominio
moradores_condominio = get_residents_cond()
print("Moradores_condominio:", moradores_condominio)

#Atualização da relação de morador_condominio com ID 1
update_residents_cond(1, "102", 3)
moradores_condominio = get_residents_cond()
print("Moradores_condominio atualizados:", moradores_condominio)



#Remoção das relações Morador_condominio (sem WHERE)
remove_residents_cond()
moradores_condominio = get_residents_cond()
print("Moradores_condominio após exclusão:", moradores_condominio)

#Remoção dos moradores
remove_residents(1)
moradores = get_residents()
print("Moradores após exclusão:", moradores)

#Remoção das localizações
remove_location(1)
localizacoes = get_locations()
print("Localizacoes após exclusão:", localizacoes)

#Remoção dos condominios
remove_cond(2)
condominios = get_conds()
print("Condomínios após exclusão:", condominios)