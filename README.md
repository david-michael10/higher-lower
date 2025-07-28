<img width="763" height="289" alt="image" src="https://github.com/user-attachments/assets/8ea721c5-e034-45f5-89a5-725648ad2206" />

    Parte de importação

------------------

<img width="1034" height="563" alt="image" src="https://github.com/user-attachments/assets/f8675a21-ade9-49c8-b901-1a36dad84c4f" />

format_data():

    Criei essa função para formatar os dados tomando como referência as keys do banco de dados

    No final retorno como output o texto formatado

check_followers():

    Verifico qual celebridade tem mais seguidores fazendo condições com if e também o input
    do usuário que criarei mais pra frente

------------------

<img width="991" height="680" alt="image" src="https://github.com/user-attachments/assets/2ff79bd8-3401-4d54-9dd0-9b5a56b1e850" />

    Escolho um dicionário (que contém os dados) aleatório do banco de dados
    utilizando random.choice e armazeno em uma variável.

    Crio um while() que continuará rodando até o usuário errar

    Verifico se a celebridade B é igual ao A. Se sim faço um novo random.choice
    para que dessa forma não tenha duas celebridades iguais

    Chamo a função de formatar os dados e utilizo a variável contendo os dados
    da celebridade como argumento. Faço isso para definir 2 celebridades

    Também armazeno o número de seguidores em uma variável correspondente

    Printo as celebridades na variável formatada e também a arte de "VS"

------------------

<img width="1308" height="448" alt="image" src="https://github.com/user-attachments/assets/2c37ea66-6f04-4c71-9f1e-48b9019d08ea" />

    Pergunto ao usuário qual celebridade ele acha que tem mais seguidores com input e limpo a tela

    chamo a função qque criei lá em cima para checar se o usuário acertou e uso a variável contendo
    o número de seguidores A e B, além do input como argumentos

    Se o usuário acertou, contabilizo em 1, além de printar uma mensagem

    Se não acertou, paro o while() e mostro a pontuação
