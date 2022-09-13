

tamanho_tubo = 6

menu = int(input("SISTEMA UNIÃO INOX: \n" +

                 "1 - TUBOS PX\n" +
                 "2 - PIVO\n" +
                 "3 - ARMADOR\n" +
                 "4 - RELATORIO\n" +
                 "0 - SAIR"))

while (menu >= 1):
    if (menu == 1):
        metros_tubos = int(input("Infome quantos metros foi comprado?"))
        quant_tubos = metros_tubos / tamanho_tubo
        print(("Quantidade de Tubos 40x10 que Chegou: ", quant_tubos, "tubos"))

        quantPux150 = float(input("Adicione a quantidade de px: 150cm"))
        resultadoPux150 = (((quantPux150 * 1.5) * 2) / 6)
        print(resultadoPux150)

        quantPux120 = float(input("Adicione a quantidade de px: 120cm"))
        resultadoPux120 = ((quantPux120 * 1.2) * 2) / 6
        print(resultadoPux120)

        quantPux100 = float(input("Adicione a quantidade de px: 100cm"))
        resultadoPux100 = ((quantPux100 * 1.0) * 2) / 6
        print(resultadoPux100)

        quantPux80 = float(input("Adicione a quantidade de px: 80cm"))
        resultadoPux80 = ((quantPux80 * 0.8) * 2) / 6
        print(resultadoPux80)

        quantPux70 = float(input("Adicione a quantidade de px: 70cm"))
        resultadoPux70 = ((quantPux70 * 0.7) * 2) / 6
        print(resultadoPux70)

        quantPux60 = float(input("Adicione a quantidade de px: 60cm"))
        resultadoPux60 = ((quantPux60 * 0.6) * 2) / 6
        print(resultadoPux60)

        quantPux50 = float(input("Adicione a quantidade de px: 50cm"))
        resultadoPux50 = ((quantPux50 * 0.5) * 2) / 6
        print(resultadoPux50)

        quantPux40 = float(input("Adicione a quantidade de px: 40cm"))
        resultadoPux40 = ((quantPux40 * 0.4) * 2) / 6
        print(resultadoPux40)

        quantPux30 = float(input("Adicione a quantidade de px: 30cm"))
        resultadoPux30 = ((quantPux30 * 0.3) * 2) / 6
        print(resultadoPux30)

        resultadoPuxTotal = resultadoPux30 + resultadoPux40 + resultadoPux50 + resultadoPux60 + resultadoPux70 + resultadoPux80 + resultadoPux100 + resultadoPux150
        (print("Quantidade de tubos usado é: ", resultadoPuxTotal))

        resultadoPuxTotal = quant_tubos - resultadoPuxTotal

        (print("Resta em quantidade de tubos: ", resultadoPuxTotal, " unidades"))

        menu = int(input("SISTEMA UNIÃO INOX: \n" +

                         "1 - TUBOS PX\n" +
                         "2 - PIVO\n" +
                         "3 - ARMADOR\n" +
                         "4 - RELATORIO\n" +
                         "0 - SAIR"))
    elif (menu == 2):

        barraTresOitav150 = 0.05
        barraTresOitav250 = 0.05
        barraTresOitavBergue = 0.05

        canoMeiaUmCinco150 = 0.05
        canoMeiaUmCinco250 = 0.05
        canoMeiaUmCincoBergue = 0.05

        paraf150 = 8
        paraf250 = 8
        paraf350 = 8
        parafBergue = 4
        parafMiniPivo = 4

        barraMeia350 = 0.05
        canoCincoOitav350 = 0.05

        barraTresOivtavMini = 0.045

        pivo150 = float(input("Informe quantos pivo 150kg "))

        barraTresOitav150 = pivo150 * barraTresOitav150 / 6

        print("Quantidade de barra redonda 3/8: ", barraTresOitav150)

        canoMeiaUmCinco150 = pivo150 * canoMeiaUmCinco150 / 6

        print("Quantidade de Cano 1/2 ( 1.5): ", canoMeiaUmCinco150)

        paraf150 = pivo150 * paraf150

        print("Quantidade de Parafusos 4.8x50 inox e Buchas 0.8: ", paraf150)

        #PIVÔ 250KG

        pivo250 = float(input("Informe quantos pivo 250kg "))
        barraTresOitav250 = pivo250 * barraTresOitav250 / 6
        print("Quantidade de barra 3/8: " , barraTresOitav250)
        canoMeiaUmCinco250 = pivo250 * canoMeiaUmCinco250 /6
        print("Quantidade de Cano 1/2 ( 1.5): " , canoMeiaUmCinco250)
        paraf250 = pivo250 * paraf250
        print("Quantidade de Parafusos 4.8x50 inox e Buchas 0.8: " , paraf250)

        # PIVÔ 350KG

        pivo350 = float(input("Informe quantos pivo 350kg "))
        barraMeia350 = pivo350 * barraMeia350 / 6
        print("Quantidade de barra redonda 1/2: ",barraMeia350)
        canoCincoOitav350 = pivo350 * canoCincoOitav350 /6
        print("Quantidade de Cano 5/8 (1.5) : ", canoCincoOitav350)
        paraf350 = pivo350 * paraf350
        print("Quantidade de Parafusos 4.8x50 inox e Buchas 0.8: ",paraf350)

        miniPivo = float(input("Informe quantos mini Pivo  "))
        barraTresOivtavMini = miniPivo * barraTresOivtavMini / 6
        print("Quantidade de barra Redonda 3/8: ", barraTresOivtavMini)
        parafMiniPivo = miniPivo * parafMiniPivo
        print("Quantidade de Parafusos 3.2x30 inox e Buchas 0.5: ", parafMiniPivo)


        #RESULTADO TODAL

        resultadoTotalPivoTresOitav = barraTresOitav150 + barraTresOitav250 + barraTresOitavBergue + barraTresOivtavMini;
        print("Quantidade Total Barra Redonda 3/8: ", resultadoTotalPivoTresOitav)
        resultadoTotalCanoMeia = canoMeiaUmCinco250 + canoMeiaUmCinco150 + canoMeiaUmCincoBergue
        print("Quantidade Total Cano 1/2 (1.5): ", resultadoTotalCanoMeia)
        print("Quantidade de Barra Redonoda 1/2: ", barraMeia350)
        print("Quantidade de Cano 5/8 (1.5): ", canoCincoOitav350)

        print("Quantidade Total de Parafusos 4.8x50 e Bucha 0.8: ", paraf150 + paraf250 + paraf350 + parafBergue)
        print("Quantidade Total de Parafusos 3.2x30 e Bucha 0.5: ", parafMiniPivo)

        menu = int(input("SISTEMA UNIÃO INOX: \n" +

                         "1 - TUBOS PX\n" +
                         "2 - PIVO\n" +
                         "3 - ARMADOR\n" +
                         "4 - RELATORIO\n" +
                         "0 - SAIR"))

    elif (menu == 3):

        quantArmadorB = float(input(" Informe quantos Amadores Batom "))
        Gancho = 0.16
        canoRegulagem = 0.07
        batomInox = 0.05
        barraRegulagem = 0.02
        SeguraRegulagem = 0.03
        chumbador = 0.05

        canoRegulagem = (quantArmadorB * 2 * canoRegulagem / 6)

        print("Quantidades de Tubos 7/8 Regulagem: ",canoRegulagem)

        Gancho = (quantArmadorB * Gancho * 2) / 6

        print("Quantidade de Tubos 5/16 Ganchos (S) : ",Gancho)

        batomInox = (quantArmadorB * 2 * batomInox / 6)

        print("Quantidade de Tubos 3/4 Batom: ",(batomInox))

        SeguraRegulagem = (quantArmadorB * 2 * SeguraRegulagem / 6)

        print("Quantidade de Tubos 1': ",SeguraRegulagem)

        barraRegulagem = (quantArmadorB * 2 * barraRegulagem / 6)

        print("Quantidade de Tubos 1/4: ",barraRegulagem)

        chumbador = (quantArmadorB * 4 * chumbador / 6)
        print("Quantidade de Tubos 3/16: ",chumbador)

        menu = int(input("SISTEMA UNIÃO INOX: \n" +

                         "1 - TUBOS PX\n" +
                         "2 - PIVO\n" +
                         "3 - ARMADOR\n" +
                         "4 - RELATORIO\n" +
                         "0 - SAIR"))

    elif (menu == 4):

        int(input("SISTEMA UNIÃO INOX: \n" +

                  "1 - Relatorio de Tubos\n" +
                  "2 - Relatorio de PIVO\n" +
                  "3 - ARMADOR\n" +
                  "4 - RELATORIO\n" +
                  "0 - SAIR"))



