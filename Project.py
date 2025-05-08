# Este é o início do projecto 2 de FP.
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']

def num_to_abc(num):
    '''
    int → caracter
    Esta função irá ajudar 
    a converter números para as respetivas colunas. 
    (Por exemplo, a coluna nº5 é a coluna "E"
    '''

    if 0 < num < 20:
        return abc[num-1]
    return ('inválido')


def abc_to_num(caracter):
    '''
    caracter → int
    Esta função faz o contrário da anterior: 
    Converte uma letra para a posição dessa letra no alfabeto
    '''
    
    return abc.index(caracter)+1


def cria_intersecao(coluna, linha):
    '''
    str × int → intersecao
    Esta função cri uma interseção que é um tuplo (coluna, linha).
    '''

    # Confirma se a coluna é uma letra válida e se a linha é um inteiro entre 0 e 20.
    if not (coluna in abc and isinstance(linha, int) and 0 < linha < 20):
        raise ValueError("cria_intersecao: argumentos invalidos")
    
    # retorna um tuplo interseção
    return (coluna, linha)


def obtem_col(intersecao):
    '''
    intersecao → str
    Esta função obtém a coluna de uma interseção.
    '''

    return intersecao[0]


def obtem_lin(intersecao):
    '''
    intersecao → int
    Esta função obtém a linha de uma interseção.
    '''

    return intersecao[1]


def eh_intersecao(universal):
    '''
    universal → booleano
    Esta função retorna True se o argumento é uma interseção e 
    False caso contrário.
    '''

    # Confirma se a interseção é um tuplo com 2 elementos 
    # em que o 1º é uma coluna e o 2º é uma linha.
    return isinstance(universal, tuple) and len(universal) == 2 and \
    isinstance(universal[0], str) and universal[0] in abc \
    and isinstance(universal[1], int) and 0 < universal[1] < 20


def intersecoes_iguais(intersecao1, intersecao2):
    '''
    universal × universal → booleano
    Esta função retorna True caso as interseções 
    são iguais e False caso contrário.
    '''

    # Confirma se as interseções são válidas e se as suas linhas e colunas são iguais.
    return eh_intersecao(intersecao1) and eh_intersecao(intersecao2) \
        and obtem_col(intersecao1) == obtem_col(intersecao2) and \
            obtem_lin(intersecao1) == obtem_lin(intersecao2)


def intersecao_para_str(intersecao):
    '''
    intersecao → str
    Esta função retorna a versão em string de uma interseção.
    '''

    return obtem_col(intersecao) + str(obtem_lin(intersecao))


def str_para_intersecao(string):
    '''
    str → intersecao
    Esta função retorna a interseção da sua versão em string.
    '''

    return cria_intersecao(string[0], int(string[1:]))


def obtem_intersecoes_adjacentes(intersecao, tamanho):
    '''
    intersecao × intersecao → tuplo
    Esta função retorna as interseções adjacentes, 
    dado uma interseção e o tamanho do goban.
    '''

    # Encontramos as 4 interseções ao somar/subtrair 1 valor à linha 
    # ou ao somar/subtrair 1 "passo" no alfabeto das colunas
    adjacentes = ()
    coluna= obtem_col(intersecao)
    linha = obtem_lin(intersecao)

    # intersecao_baixo
    if linha > 1:
        adjacentes += (cria_intersecao(coluna, linha - 1),)

    # intersecao_esquerda
    if coluna > "A":
        adjacentes += (cria_intersecao(num_to_abc(abc_to_num(coluna) - 1), linha),)

    #intersecao_direita
    if coluna < obtem_col(tamanho):
        adjacentes += (cria_intersecao(num_to_abc(abc_to_num(coluna) + 1), linha),)

    # intersecao_cima 
    if linha < obtem_lin(tamanho):
        adjacentes += (cria_intersecao(obtem_col(intersecao), obtem_lin(intersecao) + 1),)

    return adjacentes


def ordena_intersecoes(tuplo):
    '''
    tuplo → tuplo
    Esta função recebe um tuplo de interseções e 
    devolve-o ordenado pela ordem de leitura.
    '''

    # Ordena o tuplo primeiro pelo segundo elemento e depois pelo primeiro. 
    # Transforma a lista resultante em tuplo.
    tuplo_ordenado = tuple(sorted(tuplo, key=lambda x: (obtem_lin(x), obtem_col(x))))
    return tuplo_ordenado


def cria_pedra_branca():
    '''
    → pedra
    Retorna uma pedra branca
    '''

    return 1


def cria_pedra_preta():
    '''
    → pedra
    Retorna uma pedra preta
    '''

    return -1


def cria_pedra_neutra():
    '''
    → pedra
    Retorna uma pedra neutra
    '''

    return 0


def eh_pedra(pedra):
    '''
    universal → booleano
    Retorna True se o argumento for uma pedra e False caso contrário.
    '''

    return pedra in (cria_pedra_preta(), cria_pedra_neutra(),cria_pedra_branca())


def eh_pedra_branca(pedra):
    '''
    pedra → booleano
    Retorna True se o argumento for uma pedra branca e False caso contrário.
    '''

    return pedra == cria_pedra_branca()


def eh_pedra_preta(pedra):
    '''
    pedra → booleano
    Retorna True se o argumento for uma pedra preta e False caso contrário.
    '''

    return pedra == cria_pedra_preta()

def pedras_iguais(pedra1, pedra2):
    '''
    universal × universal → booleano
    Retorna True se as pedras recebidas são iguais.
    '''

    # Confirma se as pedras são válidas e se são iguais
    return all((eh_pedra(pedra1), eh_pedra(pedra2), \
        eh_pedra_branca(pedra1) == eh_pedra_branca(pedra2), \
        eh_pedra_preta(pedra1) == eh_pedra_preta(pedra2)))


def pedra_para_str(pedra):
    '''
    pedra → str
    Esta função recebe uma pedra e retorna a sua versão em string.
    '''
    
    # Este dicionário corresponde a cor de cada pedra à sua string.
    pedras = {cria_pedra_preta(): "X", cria_pedra_neutra(): ".", cria_pedra_branca(): "O"}

    return pedras[pedra]


def eh_pedra_jogador(pedra):
    '''
    pedra → booleano
    Retorna True se a pedra recebida não for neutra.
    '''

    return eh_pedra_branca(pedra) or eh_pedra_preta(pedra)


def cria_goban_vazio(n):
    '''
    int → goban
    Esta função cria um goban vazio de dimensões n x n.
    '''

    #Confirma se n é um inteiro de dimensões válidas.
    if not(isinstance(n, int) and n in (9, 13, 19)):
        raise ValueError("cria_goban_vazio: argumento invalido") 

    # O goban criado é um dicionário de tamanho n*n em que cada chave é uma
    # interseção que corresponde à pedra aí existente.
    goban = {}
    for coluna in range(1, n+1):
        for linha in range(1, n+1):
            intersecao = intersecao_para_str(cria_intersecao(num_to_abc(coluna), linha))
            goban[intersecao] = cria_pedra_neutra()

    return goban


def cria_goban(n, tuplo_b, tuplo_p):
    '''
    int × tuplo × tuplo → goban
    Esta função cria um goban de dimensões n x n, com pedras brancas nas interseções 
    dentro de tuplo_b e com pedras pretas nas interseções dentro de tuplo_p.
    '''

    # Confirma se n é uma dimensão válida e se os outros argumentos são tuplos.
    if not(isinstance(n, int) and n in (9, 13, 19)):
        raise ValueError("cria_goban: argumentos invalidos") 
    if not(isinstance(tuplo_b, tuple) and isinstance(tuplo_p, tuple)):
        raise ValueError("cria_goban: argumentos invalidos") 
    
    def auxilia_validacao(n, tuplo1, tuplo2):
        '''
        int × tuplo → booleano
        A função recebe um tuplo de interseções e uma dimensão n para o goban e 
        confirma se todas as interseções dentro do tuplo são válidas.
        '''
        for intersecao in tuplo1:
            if not(eh_intersecao(intersecao) and obtem_col(intersecao) <= \
                   num_to_abc(n) and obtem_lin(intersecao) <= n) or intersecao in tuplo2:
                return False
            if tuplo1.count(intersecao) > 1:
                return False
        return True

    # Confirma se as interseções dentro dos tuplos são válidas.
    if not(auxilia_validacao(n, tuplo_b, tuplo_p) and auxilia_validacao(n, tuplo_p, tuplo_b)):
        raise ValueError("cria_goban: argumentos invalidos") 

    goban = cria_goban_vazio(n)

    def altera_goban(goban, tuplo, pedra):
        '''
        goban × tuplo × pedra → goban
        A função recebe um goban e um tuplo de interções 
        e coloca uma pedra em cada uma das interseções.
        '''

        for intersecao in tuplo:
            intersecao = intersecao_para_str(intersecao)
            goban[intersecao] = pedra
        return goban
    
    # Coloca as peças no goban vazio.
    goban = altera_goban(goban, tuplo_b, cria_pedra_branca())
    goban = altera_goban(goban, tuplo_p, cria_pedra_preta())

    return goban


def cria_copia_goban(goban):
    '''
    goban → goban
    Retorna uma cópia independente do goban original.
    '''

    copia_goban = dict(goban)
    return copia_goban


def obtem_ultima_intersecao(goban):
    '''
    goban → intersecao
    Retorna a interseção do canto superior direito de um goban.
    '''

    return str_para_intersecao(tuple(goban.keys())[-1])


def obtem_pedra(goban, intersecao):
    '''
    goban × intersecao → pedra
    Retorna a pedra correspondente a uma interseção dado um goban.
    '''

    return goban[intersecao_para_str(intersecao)]


def obtem_cadeia(goban, intersecao):
    '''
    goban × intersecao → tuplo
    Esta função obtém a cadeia a partir de uma dada interseção, ou seja,
    todas as interseções com uma pedra do mesmo tipo e conectadas entre si.
    '''
    
    tipo_de_cadeia = obtem_pedra(goban, intersecao)
    cadeia = [intersecao]
    tamanho = obtem_ultima_intersecao(goban)

    # A função passa por todos os elementos que vão sendo adicionados à cadeia. 
    # Desta forma, o processo repete-se até pararem de ser 
    # adicionados elementos à cadeia.
    for intersecao_cadeia in cadeia:
        # Passa por todas as interseções adjacentes.
        for intersecao_adjacente in \
        obtem_intersecoes_adjacentes(intersecao_cadeia, tamanho):
            # Confirma se as interseções fazem parte da cadeia e 
            # se ainda não estão na cadeia.
            if intersecao_adjacente not in cadeia and \
            pedras_iguais(obtem_pedra(goban, intersecao_adjacente), tipo_de_cadeia):
                cadeia.append(intersecao_adjacente) 

    # Ordena a cadeia e transforma em tuplo.
    cadeia_ordenada = ordena_intersecoes(cadeia)
    return cadeia_ordenada


def coloca_pedra(goban, intersecao, pedra):
    '''
    goban × intersecao × pedra → goban
    Esta função coloca uma dada pedra numa interseção do goban.
    '''

    goban[intersecao_para_str(intersecao)] = pedra
    return goban



def remove_pedra(goban, intersecao):
    '''
    goban × intersecao → goban
    Esta função remove uma pedra numa interseção do goban
    '''

    goban = coloca_pedra(goban, intersecao, cria_pedra_neutra())
    return goban


def remove_cadeia(goban, tuplo):
    '''
    goban × tuplo → goban
    Esta função remove todas as pedras dentro do tuplo de interseções que recebe
    '''

    for intersecao in tuplo:
        remove_pedra(goban, intersecao)

    return goban
    

def eh_goban(goban):
    '''
    universal → booleano
    Confirma se o argumento é um TAD goban.
    '''

    # Confirma se o goban é um dicionário de tamanho n*n.
    if not(isinstance(goban, dict) and len(goban) in (81, 169, 361)):
        return False
    # Percorre todos os pares chave, valor do tipo (interseção, pedra).
    for intersecao in tuple(goban.items()):
        if not(eh_intersecao(str_para_intersecao(intersecao[0])) and eh_pedra(intersecao[1])):
            return False
    return True


def eh_intersecao_valida(goban, intersecao):
    '''
    goban × intersecao → booleano
    Confirma se uma interseção é válida para um certo goban.
    '''

    tamanho = obtem_ultima_intersecao(goban)

    # Confirma se é interseção e se tem o tamanho válido de acordo com o goban.
    return eh_intersecao(intersecao) and obtem_col(intersecao) <= obtem_col(tamanho)\
            and 0 < obtem_lin(intersecao) <= obtem_lin(tamanho)


def gobans_iguais(goban1, goban2):
    '''
    universal × universal → booleano
    Confirma se 2 gobans são iguais.
    '''

    # Confirma se são gobans do mesmo tamanho.
    if not all((eh_goban(goban1), eh_goban(goban2), len(goban1) == len(goban2))):
        return False
    tamanho = obtem_lin(obtem_ultima_intersecao(goban1))
     # Passa por todas as interseções.
    for coluna in abc[:tamanho]:
        for linha in range(1, tamanho+1):
            intersecao = cria_intersecao(coluna, linha)
            # Confirma se as pedras são iguais em cada interseção.
            if not pedras_iguais(obtem_pedra(goban1, intersecao), obtem_pedra(goban2, intersecao)):
                return False
    return True



def goban_para_str(goban):
    '''
    goban → str
    Transforma o goban numa string que o representa, 
    de forma a que o utilizador possa ver o goban.
    '''

    tamanho = obtem_lin(obtem_ultima_intersecao(goban))
    
    linha_letras = "   " # 3 espaços
    linha_meio = ""

    # Adiciona as letras que aparecem na primeira e última linhas.
    letras = [letra for letra in abc[:tamanho]]
    for letra in letras:
        linha_letras += f'{letra} '
    linha_letras = linha_letras[:-1] # Retira o último espaço que estava a mais.

    for i in range (tamanho, 0, -1): 
        # Adiciona o número da linha
        if len(str(i)) == 2:
            linha = f'{i} '
        else:
            linha = f' {i} '
        
        # Adiciona o conteúdo de cada linha (. ou X).
        for j in range(tamanho):
            intersecao = cria_intersecao(num_to_abc(j+1), i)
            linha += f'{pedra_para_str(obtem_pedra(goban, intersecao))} '

        # Adiciona o número da linha.
        if len(str(i)) == 2:
            linha += f'{i}'
        else:
            linha += f' {i}'
        linha_meio += f'{linha}\n'

    # Junta tudo numa só variável.
    string_goban = f'{linha_letras}\n{linha_meio}{linha_letras}'

    return string_goban


def obtem_territorios(goban):
    '''
    goban → tuplo
    Retorna um tuplo com todas as cadeias de interseções livres de um goban.
    '''

    territorios = ()
    tamanho = obtem_lin(obtem_ultima_intersecao(goban))
    visto = ()

    # Passa por todas as interseções.
    for linha in range(1, tamanho+1):
        for coluna in abc[:tamanho]:
            intersecao = cria_intersecao(coluna, linha)
            # Adiciona o território caso ele não faça parte do territorios.
            if pedras_iguais(obtem_pedra(goban, intersecao), cria_pedra_neutra())\
                  and intersecao not in visto:
                # Adiciona o território ordenado caso ele não faça parte do territorios.
                cadeia = obtem_cadeia(goban, intersecao)
                territorios += ((cadeia),)
                visto += cadeia
    # Retorna os territórios.
    return territorios


def obtem_adjacentes_diferentes(goban, tuplo):
    '''
    goban × tuplo → tuplo
    Retorna um tuplo com a fronteira de uma cadeia ou as liberdades de uma cadeia.
    '''

    output = ()

    # Percorre as interseções do tuplo
    for intersecao in tuplo:
        # Percorre interseções adjacentes
        for intersecao_adj in obtem_intersecoes_adjacentes\
            (intersecao, obtem_ultima_intersecao(goban)):
            # Confirma se a interseção adjacente é diferente
            if eh_pedra_jogador(obtem_pedra(goban, intersecao)) != \
                eh_pedra_jogador(obtem_pedra(goban, intersecao_adj)) \
                    and intersecao_adj not in output:
                # Adiciona ao tuplo final
                output += (intersecao_adj,)

    # Retorna o tuplo ordenado
    return ordena_intersecoes(output)


def jogada(goban, intersecao, pedra):
    '''
    goban × intersecao × pedra → goban
    Esta função executa uma jogada de go.
    '''

    tamanho = obtem_ultima_intersecao(goban)
    coloca_pedra(goban, intersecao, pedra)

    # Cria um tuplo com as cadeias adjacentes de peças de 
    # cor contrária ao jogador que colocou a pedra.
    cadeias = ()
    visto = ()
    for intersecao_adj in obtem_intersecoes_adjacentes(intersecao, tamanho):
        pedra_adj = obtem_pedra(goban, intersecao_adj) 
        if not pedras_iguais(pedra_adj, pedra) and intersecao_adj not in visto:
            cadeia = obtem_cadeia(goban, intersecao_adj)
            cadeias += (cadeia,)
            visto += cadeia       

    # Para todas as cadeias adjacentes criadas acima, 
    # confirma se estas têm liberdades
    for cadeia in cadeias:
        if not obtem_adjacentes_diferentes(goban, cadeia):
            remove_cadeia(goban, cadeia)
    
    return goban


def obtem_pedras_jogadores(goban):
    '''
    goban → tuplo
    Esta função conta a quantidade de pedras brancas e pretas de um goban.
    '''

    brancas = 0
    pretas = 0

    tamanho = obtem_lin(obtem_ultima_intersecao(goban))

    # Passa por todas as interseções
    for coluna in abc[:tamanho]:
        for linha in range(1, tamanho+1):
            intersecao = cria_intersecao(coluna, linha)
            if eh_pedra_branca(obtem_pedra(goban, intersecao)):
                brancas += 1
            if eh_pedra_preta(obtem_pedra(goban, intersecao)):
                pretas += 1

    return brancas, pretas


def calcula_pontos(goban):
    '''
    goban → tuplo
    Esta função calcula os pontos de ambos os jogadores, para um dado goban.
    '''

    brancos = 0
    pretos = 0

    # Obtém os territórios do goban
    territorios = obtem_territorios(goban)
    # Obtém as fronteiras de cada território
    for territorio in territorios:
        fronteira = obtem_adjacentes_diferentes(goban, territorio)
        if fronteira == ():
            return brancos, pretos
        pedra = obtem_pedra(goban, fronteira[0])
        # Confirma se a fronteira é constituída por peças só de uma cor.
        pontos_extra = True
        for intersecao in fronteira:
            if not pedras_iguais(obtem_pedra(goban, intersecao), pedra):
                pontos_extra = False
        # Caso o território seja de um jogador, ganha os pontos correspondentes.
        if pontos_extra:
            if eh_pedra_branca(pedra):
                brancos += len(territorio)
            else:
                pretos += len(territorio)
    
    # Atualiza os pontos correspondentes ao número de pedras.
    pontos = obtem_pedras_jogadores(goban)
    brancos += pontos[0]
    pretos += pontos[1]

    return brancos, pretos


def eh_jogada_legal(goban, intersecao, pedra, goban_ko):
    '''
    goban × intersecao × pedra × goban → booleano
    Confirma se uma jogada é legal.
    '''

    # Confirma se não existe já uma peça de um jogador
    if eh_pedra_jogador(obtem_pedra(goban, intersecao)):
        return False
    
    # É feita uma simulação de uma jogada possivelmente ilegal
    simula = cria_copia_goban(goban)
    jogada(simula, intersecao, pedra)

    return not gobans_iguais(simula, goban_ko) \
          and obtem_adjacentes_diferentes(simula, obtem_cadeia(simula, intersecao))


def user_input(pedra):
    '''
    - > str
    Esta função recolhe input do utilizador. É uma função auxiliar do turno_jogador.
    '''

    mensagem = f'Escreva uma intersecao ou \'P\' para passar [{pedra_para_str(pedra)}]:'
    return input(mensagem)


def turno_jogador(goban, pedra, goban_ko):
    '''
    goban × pedra × goban → booleano
    Esta função recolhe input do utilizador, confirma se é válido 
    e em caso afirmativo, executa uma jogada com esse input ou passa a vez. 
    Retorna False se o jogador passou e retorna True se for feita uma jogada.
    '''

    turno_invalido = True
    while turno_invalido:
        turno = user_input(pedra)
        if turno == "P":
            return False
        # Confirma se é possível passar a interseção turno para string.
        if len(turno) in (2, 3) and turno[0] in abc and turno[1:].isnumeric() \
        and 0 < int(turno[1:]) < 20:
            intersecao = str_para_intersecao(turno)
            # Se a interseção dada for válida e a jogada legal, 
            # o loop acaba e a jogada realiza-se.
            if eh_intersecao_valida(goban, intersecao)\
                and eh_jogada_legal(goban, intersecao, pedra, goban_ko):
                turno_invalido = False

    jogada(goban, intersecao, pedra)

    return True


def go(n, tuplo_b, tuplo_p):
    '''
    int × tuple × tuple → booleano
    Esta é a função principal do programa e permite jogar o jogo em si. 
    O goban é de dimensão n e pode ser criado com pedras brancas e 
    pretas nas interseções em tuplo_b e tuplo_p, respetivamente.
    '''

    def valida_strings(tuplo):
        '''
        tuplo - > booleano
        Confirma a validade dos argumentos das strings dentro dos tuplos e,
          no caso de serem válidas, transforma-as para interseções
        '''
        tuplo_intersecoes = ()
        if not isinstance(tuplo, tuple):
            raise ValueError('go: argumentos invalidos')
        for string in tuplo:
            if not isinstance(string, str) or len(string) not in (2, 3) or\
                string[0] not in abc or not string[1:].isnumeric() or not 0 < int(string[1:]) < 20:
                raise ValueError('go: argumentos invalidos')               
            tuplo_intersecoes += (str_para_intersecao(string),)
        return tuplo_intersecoes
    
    tuplo_b = valida_strings(tuplo_b)
    tuplo_p = valida_strings(tuplo_p)

    # Confirma se é possível criar o goban. Caso não seja,
    # a função cria_goban vai levantar um ValueError.
    try:
        goban = cria_goban(n, tuplo_b, tuplo_p)
    except ValueError:
        raise ValueError('go: argumentos invalidos')
    
    new_goban_ko = cria_copia_goban(goban)
    p, b = cria_pedra_preta(), cria_pedra_branca()
    turno = 1
    game_on = True
    pass_b = False

    # Loop principal do jogo.
    while game_on:
        # Calcula e imprime os pontos.
        pontos = calcula_pontos(goban)
        print(f'Branco (O) tem {pontos[0]} pontos\n'
            f'Preto (X) tem {pontos[1]} pontos')
        # Imprime o goban.
        print(goban_para_str(goban))
        # As 2 últimas posições são guardadas. Isto garante que possamos
        # comparar a repetição usando a posição N-2.
        old_goban_ko = cria_copia_goban(new_goban_ko)
        new_goban_ko = cria_copia_goban(goban)

        # As pretas jogam caso o turno seja 1. As brancas jogam caso o turno seja 0.
        if turno:
            pass_p = turno_jogador(goban, p, old_goban_ko)
            turno += -1
        else:
            pass_b = turno_jogador(goban, b, old_goban_ko)
            turno += 1

        # Se ambos os jogadores passarem. O jogo acaba.
        if not(pass_p or pass_b):
            game_on = False
            pontos = calcula_pontos(goban)
            print(f'Branco (O) tem {pontos[0]} pontos\n'
                f'Preto (X) tem {pontos[1]} pontos')
            print(goban_para_str(goban))

    # Retorna True caso as brancas ganhem e False caso as pretas ganhem.
    if pontos[0] >= pontos[1]:
        return True
    return False