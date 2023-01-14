import io
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

class generadorSQL(tk.Tk):

    #se crea la ventana y se le pasa por parametro
    def __init__(self):
        super().__init__()

        #Tamaño de la ventana
        self.geometry("800x300")
        #Se le pone titulo a la ventana
        self.title("Generador de Inserts")

        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.contenedor()
    
    def contenedor(self):

        def abrirArchivo():

            filepath = askopenfilename(

                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]

            )

            if not filepath:

                return

            txt_edit.delete("1.0", tk.END)

            with open(filepath, mode="r", encoding="utf-8") as input_file:

                text = input_file.read()

                txt_edit.insert(tk.END, text)
        
        def generarSql():

            from tkinter.simpledialog import askinteger
            idCuestionario = askinteger('Numero id del cuestionario', 'Introducir ID cuestionario')
            

            filepath = asksaveasfilename(

                defaultextension=".sql",

                filetypes=[("Text Files", "*.sql"), ("All Files", "*.*")],

            )

            if not filepath:

                return

            with open(filepath, mode="w", encoding="utf-8") as archivoResultante:

                texto = txt_edit.get("1.0", tk.END)

                contador = 0

                bloque=[]

                cuestionario = io.StringIO(texto)
            
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
                                    
                        sql = "INSERT INTO wp_mlw_questions VALUES (NULL, '" + str(idCuestionario) + "', '', 'a:4:{\
i:0;a:3:{i:0;s:" + str(len(bloque[1].encode("utf8"))) + ":\"" + bloque[1] + "\";i:1;d:0;i:2;i:" + esCorrecta[1] + ";}\
i:1;a:3:{i:0;s:" + str(len(bloque[2].encode("utf8"))) + ":\"" + bloque[2] + "\";i:1;d:0;i:2;i:" + esCorrecta[2] + ";}\
i:2;a:3:{i:0;s:" + str(len(bloque[3].encode("utf8"))) + ":\"" + bloque[3] + "\";i:1;d:0;i:2;i:" + esCorrecta[3] + ";}\
i:3;a:3:{i:0;s:" + str(len(bloque[4].encode("utf8"))) + ":\"" + bloque[4] + "\";i:1;d:0;i:2;i:" + esCorrecta[4] + ";}\
}', '', '0', '', '0', '', '0', '', '0', '', '0', '', '0', '0', '', '1', '', '1', '0', '0', 'a:14:\
{s:8:\"required\";i:1;s:12:\"answerEditor\";s:4:\"text\";s:14:\"question_title\";s:" + str(len(bloque[0].encode("utf8")))+":\"\
"+bloque[0]+"\";s:14:\"featureImageID\";s:0:\"\";s:15:\"featureImageSrc\";s:0:\"\";s:11:\"matchAnswer\";s:6:\"\
random\";s:14:\"case_sensitive\";s:0:\"\";s:16:\"image_size-width\";s:0:\"\";s:17:\"image_size-height\";s:0:\"\"\
;s:8:\"autofill\";s:0:\"\";s:10:\"limit_text\";s:1:\"0\";s:23:\"limit_multiple_response\";s:1:\"0\";s:17:\
\"file_upload_limit\";s:1:\"0\";s:16:\"file_upload_type\";s:0:\"\";}', '', '0', '0');\n"

                        archivoResultante.write(sql)
                        bloque.clear()
                        esCorrecta.clear()

                        contador = 0
                
            messagebox.showinfo(message="Generado!", title="Guardado")
        
        def vaciaTexto():
            txt_edit.delete("1.0", tk.END)
            
        txt_edit = tk.Text(self)

        menu = tk.Frame(self, relief=tk.RAISED)

        btnAbrir = tk.Button(menu, text="Abrir", command=abrirArchivo)

        btnGenerar = tk.Button(menu, text="Generar", command=generarSql)

        limpiar = tk.Button(menu, text="Vaciar", command=vaciaTexto)

        menu.grid(row=0, column=0, sticky="ns")

        btnAbrir.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

        btnGenerar.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        limpiar.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        txt_edit.grid(row=0, column=1, sticky="nsew")

if __name__ == "__main__":
    app = generadorSQL()
    app.mainloop()