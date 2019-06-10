
import os
import time
import numpy as np

############ CHANGE HERE ############
continent = 'oceania' # america africa europe asia oceania
training_city_and_capital = True # True or False depending if wants to train city & capital or only city
number_of_practices = 2 # np.inf for all random elements

time_for_response = 1 # in seconds
####################################

country_capital_continent = [
    ['Afeganistão', 'Cabul', 'Ásia'],
    ['África do Sul', 'Pretória', 'África'],
    ['Albânia', 'Tirana', 'Europa'],
    ['Alemanha', 'Berlim', 'Europa'],
    ['Andorra', 'Andorra-a-Velha', 'Europa'],
    ['Angola', 'Luanda', 'África'],
    ['Antiga e Barbuda', 'São João', 'América'],
    ['Arábia Saudita', 'Riade', 'Ásia'],
    ['Argélia', 'Argel', 'África'],
    ['Argentina', 'Buenos Aires', 'América'],
    ['Arménia', 'Erevã', 'Ásia'],
    ['Austrália', 'Camberra', 'Oceania'],
    ['Áustria', 'Viena', 'Europa'],
    ['Azerbaijão', 'Bacu', 'Ásia'],
    ['Bahamas', 'Nassau', 'América'],
    ['Bangladexe', 'Daca', 'Ásia'],
    ['Barbados', 'Bridgetown', 'América'],
    ['Barém', 'Manama', 'Ásia'],
    ['Bélgica', 'Bruxelas', 'Europa'],
    ['Belize', 'Belmopã', 'América'],
    ['Benim', 'Porto Novo', 'África'],
    ['Bielorrússia', 'Minsque', 'Europa'],
    ['Bolívia', 'Sucre', 'América'],
    ['Bósnia e Herzegovina', 'Saraievo', 'Europa'],
    ['Botsuana', 'Gaborone', 'África'],
    ['Brasil', 'Brasília', 'América'],
    ['Brunei', 'Bandar Seri Begauã', 'Ásia'],
    ['Bulgária', 'Sófia', 'Europa'],
    ['Burquina Faso', 'Uagadugu', 'África'],
    ['Burúndi', 'Bujumbura', 'África'],
    ['Butão', 'Timbu', 'Ásia'],
    ['Cabo Verde', 'Praia', 'África'],
    ['Camarões', 'Iaundé', 'África'],
    ['Camboja', 'Pnom Pene', 'Ásia'],
    ['Canadá', 'Otava', 'América'],
    ['Catar', 'Doa', 'Ásia'],
    ['Cazaquistão', 'Astana', 'Ásia'],
    ['Chade', 'Jamena', 'África'],
    ['Chile', 'Santiago', 'América'],
    ['China', 'Pequim', 'Ásia'],
    ['Chipre', 'Nicósia', 'Europa'],
    ['Colômbia', 'Bogotá', 'América'],
    ['Comores', 'Moroni', 'África'],
    ['Congo-Brazzaville', 'Brazavile', 'África'],
    ['Coreia do Norte', 'Pionguiangue', 'Ásia'],
    ['Coreia do Sul', 'Seul', 'Ásia'],
    ['Cosovo', 'Pristina', 'Europa'],
    ['Costa do Marfim', 'Iamussucro', 'África'],
    ['Costa Rica', 'São José', 'América'],
    ['Croácia', 'Zagrebe', 'Europa'],
    ['Cuaite', 'Cidade do Cuaite', 'Ásia'],
    ['Cuba', 'Havana', 'América'],
    ['Dinamarca', 'Copenhaga', 'Europa'],
    ['Dominica', 'Roseau', 'América'],
    ['Egito', 'Cairo', 'África'],
    ['Emirados Árabes Unidos', 'Abu Dabi', 'Ásia'],
    ['Equador', 'Quito', 'América'],
    ['Eritreia', 'Asmara', 'África'],
    ['Eslováquia', 'Bratislava', 'Europa'],
    ['Eslovénia', 'Liubliana', 'Europa'],
    ['Espanha', 'Madrid', 'Europa'],
    ['Estado da Palestina', 'Jerusalém Oriental', 'Ásia'],
    ['Estados Unidos', 'Washington, D.C.', 'América'],
    ['Estónia', 'Talim', 'Europa'],
    ['Etiópia', 'Adis Abeba', 'África'],
    ['Fiji', 'Suva', 'Oceania'],
    ['Filipinas', 'Manila', 'Ásia'],
    ['Finlândia', 'Helsínquia', 'Europa'],
    ['França', 'Paris', 'Europa'],
    ['Gabão', 'Libreville', 'África'],
    ['Gâmbia', 'Banjul', 'África'],
    ['Gana', 'Acra', 'África'],
    ['Geórgia', 'Tebilíssi', 'Ásia'],
    ['Granada', 'São Jorge', 'América'],
    ['Grécia', 'Atenas', 'Europa'],
    ['Guatemala', 'Cidade da Guatemala', 'América'],
    ['Guiana', 'Georgetown', 'América'],
    ['Guiné', 'Conacri', 'África'],
    ['Guiné Equatorial', 'Malabo', 'África'],
    ['Guiné-Bissau', 'Bissau', 'África'],
    ['Haiti', 'Porto Príncipe', 'América'],
    ['Honduras', 'Tegucigalpa', 'América'],
    ['Hungria', 'Budapeste', 'Europa'],
    ['Iémen', 'Saná', 'Ásia'],
    ['Ilhas Marechal', 'Majuro', 'Oceania'],
    ['Índia', 'Nova Déli', 'Ásia'],
    ['Indonésia', 'Jacarta', 'Ásia'],
    ['Irão', 'Teerão', 'Ásia'],
    ['Iraque', 'Bagdade', 'Ásia'],
    ['Irlanda', 'Dublim', 'Europa'],
    ['Islândia', 'Reiquiavique', 'Europa'],
    ['Israel', 'Jerusalém', 'Ásia'],
    ['Itália', 'Roma', 'Europa'],
    ['Jamaica', 'Kingston', 'América'],
    ['Japão', 'Tóquio', 'Ásia'],
    ['Jibuti', 'Jibuti', 'África'],
    ['Jordânia', 'Amã', 'Ásia'],
    ['Laus', 'Vienciana', 'Ásia'],
    ['Lesoto', 'Maseru', 'África'],
    ['Letónia', 'Riga', 'Europa'],
    ['Líbano', 'Beirute', 'Ásia'],
    ['Libéria', 'Monróvia', 'África'],
    ['Líbia', 'Trípoli', 'África'],
    ['Listenstaine', 'Vaduz', 'Europa'],
    ['Lituânia', 'Vílnius', 'Europa'],
    ['Luxemburgo', 'Luxemburgo', 'Europa'],
    ['Macedónia', 'Escópia', 'Europa'],
    ['Madagáscar', 'Antananarivo', 'África'],
    ['Malásia', 'Cuala Lumpur', 'Ásia'],
    ['Maláui', 'Lilôngue', 'África'],
    ['Maldivas', 'Malé', 'Ásia'],
    ['Mali', 'Bamaco', 'África'],
    ['Malta', 'Valeta', 'Europa'],
    ['Marrocos', 'Rebate', 'África'],
    ['Maurícia', 'Porto Luís', 'África'],
    ['Mauritânia', 'Nuaquechote', 'África'],
    ['México', 'Cidade do México', 'América'],
    ['Mianmar', 'Nepiedó', 'Ásia'],
    ['Micronésia', 'Paliquir', 'Oceania'],
    ['Moçambique', 'Maputo', 'África'],
    ['Moldávia', 'Quixinau', 'Europa'],
    ['Mónaco', 'Mónaco', 'Europa'],
    ['Mongólia', 'Ulã Bator', 'Ásia'],
    ['Montenegro', 'Podgoritsa', 'Europa'],
    ['Namíbia', 'Vinduque', 'África'],
    ['Nauru', 'Iarém', 'Oceania'],
    ['Nepal', 'Catmandu', 'Ásia'],
    ['Nicarágua', 'Manágua', 'América'],
    ['Níger', 'Niamei', 'África'],
    ['Nigéria', 'Abuja', 'África'],
    ['Noruega', 'Oslo', 'Europa'],
    ['Nova Zelândia', 'Wellington', 'Oceania'],
    ['Omã', 'Mascate', 'Ásia'],
    ['Países Baixos', 'Amesterdão', 'Europa'],
    ['Palau', 'Ngerulmud', 'Oceania'],
    ['Panamá', 'Cidade do Panamá', 'América'],
    ['Papua Nova Guiné', 'Porto Moresby', 'Oceania'],
    ['Paquistão', 'Islamabade', 'Ásia'],
    ['Paraguai', 'Assunção', 'América'],
    ['Peru', 'Lima', 'América'],
    ['Polónia', 'Varsóvia', 'Europa'],
    ['Portugal', 'Lisboa', 'Europa'],
    ['Quénia', 'Nairóbi', 'África'],
    ['Quirguistão', 'Bisqueque', 'Ásia'],
    ['Quiribáti', 'Taraua do Sul', 'Oceania'],
    ['Reino Unido', 'Londres', 'Europa'],
    ['República Centro-Africana', 'Bangui', 'África'],
    ['República Checa', 'Praga', 'Europa'],
    ['República Democrática do Congo', 'Quinxassa', 'África'],
    ['República Dominicana', 'São Domingos', 'América'],
    ['Roménia', 'Bucareste', 'Europa'],
    ['Ruanda', 'Quigali', 'África'],
    ['Rússia', 'Moscovo', 'Europa'],
    ['Salomão', 'Honiara', 'Oceania'],
    ['Salvador', 'São Salvador', 'América'],
    ['Samoa', 'Apia', 'Oceania'],
    ['Santa Lúcia', 'Castries', 'América'],
    ['São Cristóvão e Neves', 'Basseterre', 'América'],
    ['São Marinho', 'São Marinho', 'Europa'],
    ['São Tomé e Príncipe', 'São Tomé', 'África'],
    ['São Vicente e Granadinas', 'Kingstown', 'América'],
    ['Seicheles', 'Vitória', 'África'],
    ['Senegal', 'Dacar', 'África'],
    ['Serra Leoa', 'Freetown', 'África'],
    ['Sérvia', 'Belgrado', 'Europa'],
    ['Singapura', 'Singapura', 'Ásia'],
    ['Síria', 'Damasco', 'Ásia'],
    ['Somália', 'Mogadíscio', 'África'],
    ['Sri Lanca', 'Sri Jaiavardenapura-Cota', 'Ásia'],
    ['Suazilândia', 'Lobamba', 'África'],
    ['Sudão', 'Cartum', 'África'],
    ['Sudão do Sul', 'Juba', 'África'],
    ['Suécia', 'Estocolmo', 'Europa'],
    ['Suíça', 'Berna', 'Europa'],
    ['Suriname', 'Paramaribo', 'América'],
    ['Tailândia', 'Banguecoque', 'Ásia'],
    ['Taiuã', 'Taipé', 'Ásia'],
    ['Tajiquistão', 'Duchambé', 'Ásia'],
    ['Tanzânia', 'Dodoma', 'África'],
    ['Timor-Leste', 'Díli', 'Oceania'],
    ['Togo', 'Lomé', 'África'],
    ['Tonga', 'Nucualofa', 'Oceania'],
    ['Trindade e Tobago', 'Porto de Espanha', 'América'],
    ['Tunísia', 'Tunes', 'África'],
    ['Turcomenistão', 'Asgabate', 'Ásia'],
    ['Turquia', 'Ancara', 'Ásia'],
    ['Tuvalu', 'Funafuti', 'Oceania'],
    ['Ucrânia', 'Quieve', 'Europa'],
    ['Uganda', 'Campala', 'África'],
    ['Uruguai', 'Montevideu', 'América'],
    ['Usbequistão', 'Tasquente', 'Ásia'],
    ['Vanuatu', 'Porto Vila', 'Oceania'],
    ['Vaticano', 'Vaticano', 'Europa'],
    ['Venezuela', 'Caracas', 'América'],
    ['Vietname', 'Hanói', 'Ásia'],
    ['Zâmbia', 'Lusaca', 'África'],
    ['Zimbábue', 'Harare', 'África']
]

filtered_list = []

for element in country_capital_continent:
    if continent == 'america' and 'América' in element:
        filtered_list.append(element)
    elif continent == 'africa' and 'África' in element:
        filtered_list.append(element)
    elif continent == 'europe' and 'Europa' in element:
        filtered_list.append(element)
    elif continent == 'asia' and 'Ásia' in element:
        filtered_list.append(element)
    elif continent == 'oceania' and 'Oceania' in element:
        filtered_list.append(element)
    elif continent == 'all':
        filtered_list.append(element)

tried_list = []

if number_of_practices == np.inf:
    number_of_practices = len(filtered_list)

for times in range(0, number_of_practices):
    random_number = np.random.randint(0, len(filtered_list))
 
    tried_list.append(filtered_list[random_number])

    current_continent = filtered_list[random_number][2]
    current_country = filtered_list[random_number][0]
    current_capital = filtered_list[random_number][1]

    filtered_list.pop(random_number)

    print('say ' + current_continent)
    os.system('say ' + current_continent)

    print('say ' + current_country)
    os.system('say ' + current_country)

    time.sleep(time_for_response)

    if training_city_and_capital == True:
        print('say ' + current_capital)
        os.system('say ' + current_capital)
        time.sleep(time_for_response)

