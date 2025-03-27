"""Odeio o Pylint, mas é necessário para esse projeto do GitHub. """

LINHAS_DO_PUZZLE = [
    "ISRIEOBISDLIEHKP",
    "CEVTMEHJRWMONOTR",
    "FHNYERVSGSSUOSYW",
    "MLNYPRUIGSMCYHFA",
    "ONPPWKLMJDJKFLFJ",
    "EIMSIOPDWSGMMLRL",
    "JVLYLSARKWMPDLEE",
    "NEVYSCHCVTJPYKLV",
    "LOFIIUEKAGITSWHT",
    "SUWIMRSFTRTJSVSU",
    "HYMBEGPPISEATLAG",
    "RTCOEHITVRCTTKDW",
    "CDIJFSGCIMURNIHY",
    "EPFCDGTLDRUTKIUH",
    "BHRAICAAALDJMNRC",
    "SNBCASOSDEUSOYEM",
    "FVIJHDISEOFOEEHV",
    "TDTHDMFESESGTLTM",
    "OGFFAVNSSPCHCDIB",
]

def buscar_palavra_na_matriz(grade, palavra):
    """
    Busca a palavra em todas as direções possíveis na grade.
    """
    linhas = len(grade)
    colunas = len(grade[0]) if linhas > 0 else 0
    tam_palavra = len(palavra)
    posicoes_encontradas = []

    matriz = [list(linha) for linha in grade]

    for linha_idx in range(linhas):
        for coluna_idx in range(colunas):

            # Horizontal (esquerda->direita)
            if coluna_idx + tam_palavra <= colunas:
                trecho_h_l_r = "".join(
                    matriz[linha_idx][coluna_idx:coluna_idx + tam_palavra]
                )
                if trecho_h_l_r == palavra:
                    posicoes_encontradas.append((linha_idx, coluna_idx, "horizontal L->R"))

            # Horizontal (direita->esquerda)
            if coluna_idx - tam_palavra >= -1:
                trecho = matriz[linha_idx][coluna_idx - tam_palavra + 1:coluna_idx + 1]
                if "".join(trecho[::-1]) == palavra:
                    posicoes_encontradas.append((linha_idx, coluna_idx, "horizontal R->L"))

            # Vertical (cima->baixo)
            if linha_idx + tam_palavra <= linhas:
                trecho_v_c_b = "".join(
                    matriz[linha_idx + i][coluna_idx] for i in range(tam_palavra)
                )
                if trecho_v_c_b == palavra:
                    posicoes_encontradas.append((linha_idx, coluna_idx, "vertical top->down"))

            # Vertical (baixo->cima)
            if linha_idx - tam_palavra >= -1:
                trecho_v_b_c = "".join(
                    matriz[linha_idx - i][coluna_idx] for i in range(tam_palavra)
                )
                if trecho_v_b_c == palavra:
                    posicoes_encontradas.append((linha_idx, coluna_idx, "vertical bottom->top"))

            # Diagonal (canto superior esquerdo -> canto inferior direito)
            if (linha_idx + tam_palavra <= linhas) and (coluna_idx + tam_palavra <= colunas):
                trecho_diag_tl_br = "".join(
                    matriz[linha_idx + i][coluna_idx + i] for i in range(tam_palavra)
                )
                if trecho_diag_tl_br == palavra:
                    posicoes_encontradas.append((linha_idx, coluna_idx, "diagonal TL->BR"))

            # Diagonal (canto inferior direito -> canto superior esquerdo)
            if (linha_idx - tam_palavra >= -1) and (coluna_idx - tam_palavra >= -1):
                trecho_diag_br_tl = "".join(
                    matriz[linha_idx - i][coluna_idx - i] for i in range(tam_palavra)
                )
                if trecho_diag_br_tl == palavra:
                    posicoes_encontradas.append((linha_idx, coluna_idx, "diagonal BR->TL"))

            # Diagonal (canto superior direito -> canto inferior esquerdo)
            if (linha_idx + tam_palavra <= linhas) and (coluna_idx - tam_palavra >= -1):
                trecho_diag_tr_bl = "".join(
                    matriz[linha_idx + i][coluna_idx - i] for i in range(tam_palavra)
                )
                if trecho_diag_tr_bl == palavra:
                    posicoes_encontradas.append((linha_idx, coluna_idx, "diagonal TR->BL"))

            # Diagonal (canto inferior esquerdo -> canto superior direito)
            if (linha_idx - tam_palavra >= -1) and (coluna_idx + tam_palavra <= colunas):
                trecho_diag_bl_tr = "".join(
                    matriz[linha_idx - i][coluna_idx + i] for i in range(tam_palavra)
                )
                if trecho_diag_bl_tr == palavra:
                    posicoes_encontradas.append((linha_idx, coluna_idx, "diagonal BL->TR"))

    return posicoes_encontradas

if __name__ == "__main__":
    PALAVRA = input("Digite a palavra a ser procurada em maiúsculas: ")
    RESULTADO = buscar_palavra_na_matriz(LINHAS_DO_PUZZLE, PALAVRA)
    print(RESULTADO)
