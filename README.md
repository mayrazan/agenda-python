Objetivo: Implementar um programa em python para uma agenda telefônica digital, seguindo os seguintes critérios:

• Menu: Deve ter as seguintes opções para o usuário:

◦ 1 - Inserir contato

◦ 2 - Editar contato

◦ 3 - Excluir contato

◦ 4 - Exibir contatos

◦ 5 – Buscar contato

◦ 6 – Contatos acessados recentemente

• Dados: Deve armazenar em uma nova estrutura do tipo fila, contendo
todos os dados dos últimos 5 usuários acessado.

• É considerado acesso ao usuário somente a operação de busca, ou seja,
operação 5 do menu.

• Para esse novo item do menu deve ser criado uma função e uma nova
estrutura de dados do tipo fila. Sendo que, quando a fila estiver cheia
com 5 usuários, e precisar adicionar um novo no final da fila, deve ser
retirado o primeiro da fila.

◦ 7 – Ordenar contatos

• Para esse novo item do menu deve ser criado uma função que
implementa a ordenação por seleção. Deve dar a possibilidade ao
usuário de escolher ordenar por nome ou idade. Toda a lista telefônica
será ordenada.

◦ 8 – Busca binária

• Para esse novo item do menu deve ser criado uma função que
implementa a busca binária. Deve dar a possibilidade ao usuário de
escolher buscar por nome ou idade. Para isso a lista telefônica deverá
estar ordenada pelo item escolhido.

◦ 0 – Sair

• Dados: Deve armazenar em uma lista, contendo os dados:
◦ Nome completo
◦ e-mail
◦ idade
◦ telefone

• As opções de buscar, excluir e editar contato, pode ser selecionado/buscado através do nome ou telefone.

• Cada item do menu deve ser pelo menos uma função, excluindo-se a opção sair.