with open("cuestionario.txt", mode="r") as cuestionario:

    contador = 0

    bloque=[]
    archivoResultante = open("sentencias.sql", "w")
    
    for linea in cuestionario:
           
        bloque.append(linea.strip()) #Se instroduce la linea se le quita con strip los espacios y saltos de linea
        contador+=1

        if contador > 4:
            esCorrecta = {}
            #Se salta la posicion 0 poniendo range 1 hasta la longitud del array para ir a las respuestas >>> {1: 0, 2: 0, 3: 1, 4: 0}
            for indice in range(1,len(bloque)):

                esCorrecta[indice] = "1"                    #Por defecto todas empiezan como respuestas correctas
    
                bloque[indice] = bloque[indice][3:]         #Se quita las letras a), b), c) y d)
                test = bloque[indice][-1]
                if bloque[indice][-1] == '*':               #si tiene asterisco al final
                    bloque[indice] = bloque[indice][:-2]    #Se quita asterisco
                else:                                       #Si no tiene asterisco al final
                    esCorrecta[indice] = "0"                #Se marca como incorrecta
                            
            sql = "INSERT INTO wp_mlw_questions VALUES (NULL, '1', '', 'a:4:{\
i:0;a:3:{i:0;s:" + str(len(bloque[1].encode("utf8"))) + ":\"" + bloque[1] + "\";i:1;d:0;i:2;i:" + esCorrecta[1] + ";}\
i:1;a:3:{i:0;s:" + str(len(bloque[2].encode("utf8"))) + ":\"" + bloque[2] + "\";i:1;d:0;i:2;i:" + esCorrecta[2] + ";}\
i:2;a:3:{i:0;s:" + str(len(bloque[3].encode("utf8"))) + ":\"" + bloque[3] + "\";i:1;d:0;i:2;i:" + esCorrecta[3] + ";}\
i:3;a:3:{i:0;s:" + str(len(bloque[4].encode("utf8"))) + ":\"" + bloque[4] + "\";i:1;d:0;i:2;i:" + esCorrecta[4] + ";}\
}', '', '0', '', '0', '', '0', '', '0', '', '0', '', '0', '0', 'MUY BIEEEEEN', '1', '', '1', '0', '0', 'a:14:\
{s:8:\"required\";i:1;s:12:\"answerEditor\";s:4:\"text\";s:14:\"question_title\";s:" + str(len(bloque[0].encode("utf8")))+":\"\
"+bloque[0]+"\";s:14:\"featureImageID\";s:0:\"\";s:15:\"featureImageSrc\";s:0:\"\";s:11:\"matchAnswer\";s:6:\"\
random\";s:14:\"case_sensitive\";s:0:\"\";s:16:\"image_size-width\";s:0:\"\";s:17:\"image_size-height\";s:0:\"\"\
;s:8:\"autofill\";s:0:\"\";s:10:\"limit_text\";s:1:\"0\";s:23:\"limit_multiple_response\";s:1:\"0\";s:17:\
\"file_upload_limit\";s:1:\"0\";s:16:\"file_upload_type\";s:0:\"\";}', '', '0', '0');\n"

            archivoResultante.write(sql)
            bloque.clear()
            esCorrecta.clear()

            contador = 0

archivoResultante.close()
