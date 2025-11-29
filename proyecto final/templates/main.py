from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
        
        
        
    return render_template('index.html')
@app.route("/Almuerzos")
def almuerzos():
    almuerzos = [{
            "categoria": "Almuerzo",
            "titulo": "Arroz con pollo",
            "imagen": "arroz con pollo.png",
            "ingredientes": "Arroz, pollo desmechado, verduras, cebolla, ajo",
            "pasos": "Sofríe el pollo con verduras y ajo, luego agrega arroz y cocina hasta que todo esté listo."
        },
        {
            "categoria": "Almuerzo",
            "titulo": "Lentejas con arroz",
            "imagen": "lentejas.jpg",
            "ingredientes": "Lentejas, arroz, zanahoria, cebolla, plátano maduro",
            "pasos": "Cocina las lentejas con verduras, sirve con arroz y plátano frito."
        },
        {
            "categoria": "Almuerzo",
            "titulo": "Spaghetti con salsa de tomate",
            "imagen": "spaghetti.png",
            "ingredientes": "Spaghetti, tomate, ajo, cebolla, albahaca",
            "pasos": "Hierve la pasta, prepara una salsa con los ingredientes y mézclalo todo al final."
        },
        {
            "categoria": "Almuerzo",
            "titulo": "Filete de pollo a la plancha",
            "imagen": "filete de pollo.png",
            "ingredientes": "Pechuga de pollo, sal, limón, especias",
            "pasos": "Sazona el pollo con limón y especias, cocínalo a la plancha hasta dorar."
        },
        {
            "categoria": "Almuerzo",
            "titulo": "Ensalada mixta",
            "imagen": "ensalada mixta.jpg",
            "ingredientes": "Lechuga, tomate, zanahoria, pepino, vinagreta",
            "pasos": "Lava y corta los vegetales, mezcla y sirve con vinagreta."
        }]
    return render_template("recetas_almuerzo.html", almuerzos = almuerzos)
@app.route("/Cenas")
def cenas():
    cenas = [{
            "categoria": "Cena",
            "titulo": "Sopa de verduras",
            "imagen": "sopa de verduras.png",
            "ingredientes": "Zanahoria, papa, cebolla, apio, caldo",
            "pasos": "Corta las verduras y cocínalas en el caldo por 30 minutos."
        },
        {
            "categoria": "Cena",
            "titulo": "Tortilla de papa",
            "imagen": "tortilla de papa.png",
            "ingredientes": "Huevos, papa, cebolla, aceite, sal",
            "pasos": "Fríe la papa en tajadas, mezcla con huevo y cebolla, y cocina en sartén por ambos lados."
        },
        {
            "categoria": "Cena",
            "titulo": "Sándwich mixto",
            "imagen": "sandwich.png",
            "ingredientes": "Pan tajado, jamón, queso, mantequilla",
            "pasos": "Unta mantequilla en el pan, agrega jamón y queso, y calienta en sartén o sandwichera."
        },
        {
            "categoria": "Cena",
            "titulo": "Arepa con huevo",
            "imagen": "arepa de huevo.png",
            "ingredientes": "Arepa, huevo, sal",
            "pasos": "Haz una abertura en la arepa, introduce el huevo y cocina en sartén por ambos lados."
        },
        {
            "categoria": "Cena",
            "titulo": "Wrap de pollo",
            "imagen": "wrap de pollo.png",
            "ingredientes": "Tortilla de trigo, pollo desmechado, lechuga, salsa",
            "pasos": "Pon el pollo y vegetales sobre la tortilla, agrega salsa y enrolla."
        }
    ]
    return render_template("cenas.html", cenas = cenas)


@app.route("/recetas")
def recetas():
    return render_template("recetas.html")
@app.route("/Desayunos")
def desayunos():
    desayunos = [ {
            "categoria": "Desayuno",
            "titulo": "Arepa con queso",
            "imagen": "arepa.png",
            "ingredientes": "Arepas, queso doble crema, mantequilla",
            "pasos": "Asar las arepas, Añadir queso por encima y luego cocinar hasta que se derrita."
        },
        {
            "categoria": "Desayuno",
            "titulo": "Huevos pericos",
            "imagen": "huevos pericos.jpg",
            "ingredientes": "Huevos, tomate, cebolla, sal, aceite",
            "pasos": "Pica el tomate y la cebolla, sofríelos, añade los huevos batidos y revuelve hasta que se cocinen."
        },
        {
            "categoria": "Desayuno",
            "titulo": "Tostadas con aguacate",
            "imagen": "tostadas con aguacate.png",
            "ingredientes": "Pan, aguacate, limón, sal",
            "pasos": "Tuesta el pan, machaca el aguacate con limón y sal, y úntalo sobre el pan."
        },
        {
            "categoria": "Desayuno",
            "titulo": "Batido de frutas",
            "imagen": "batido de frutas.png",
            "ingredientes": "Banano, fresa, leche, miel",
            "pasos": "Licúa todas las frutas con leche y miel hasta obtener una mezcla homogénea."
        },
        {
            "categoria": "Desayuno",
            "titulo": "Omelette con jamón y queso",
            "imagen": "omelette.png",
            "ingredientes": "Huevos, jamón, queso, sal, pimienta",
            "pasos": "Bate los huevos, agrégales sal y pimienta, cocina en sartén con jamón y queso dentro."
        },

    ]
    return render_template("desayunos.html",desayunos = desayunos)

if __name__ == '__main__':
    app.run(debug=True)