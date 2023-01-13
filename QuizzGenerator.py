import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():

    filepath = askopenfilename(

        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]

    )

    if not filepath:

        return

    txt_edit.delete("1.0", tk.END)

    with open(filepath, mode="r", encoding="utf-8") as input_file:

        text = input_file.read()

        txt_edit.insert(tk.END, text)

def save_file():

    filepath = asksaveasfilename(

        defaultextension=".sql",

        filetypes=[("Text Files", "*.sql"), ("All Files", "*.*")],

    )

    if not filepath:

        return

    with open(filepath, mode="w", encoding="utf-8") as output_file:

        text = txt_edit.get("1.0", tk.END)

        output_file.write(text)

ventana = tk.Tk()
ventana.title("Generador de Inserts")

#frame3 = tk.Frame(master=ventana, width=300, height=300, bg="blue")
#frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

ventana.rowconfigure(0, minsize=300)

ventana.columnconfigure(1, minsize=300)


txt_edit = tk.Text(ventana)

frm_buttons = tk.Frame(ventana, relief=tk.RAISED, bd=2)

btn_open = tk.Button(frm_buttons, text="Abrir", command=open_file)

btn_save = tk.Button(frm_buttons, text="Generar", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_save.grid(row=1, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")

txt_edit.grid(row=0, column=1, sticky="nsew")


ventana.mainloop()

"""
with open("limpieza1.txt", mode="r") as cuestionario:

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
                    bloque[indice] = bloque[indice][:-1]    #Se quita asterisco
                else:                                       #Si no tiene asterisco al final
                    esCorrecta[indice] = "0"                #Se marca como incorrecta
                            
            sql = "INSERT INTO wp_mlw_questions VALUES (NULL, '3', '', 'a:4:{\
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

archivoResultante.close()"""