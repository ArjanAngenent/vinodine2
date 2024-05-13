import streamlit as st
import requests

# URL for VinoDine API
url = 'https://vinodine-dxr2er4ueq-ew.a.run.app/predict'

st.image("https://cdn.pixabay.com/photo/2024/05/05/23/00/ai-generated-8742016_1280.jpg", caption='VinoDine', output_format="auto")

st.markdown("<h2 style='text-align: center; '>Discover the perfect match of foods with your wine by answering these 4 questions / Découvrez l'accord parfait entre les mets et votre vin en répondant à ces 4 questions</h2>", unsafe_allow_html=True)

grapes = ['Abbuoto', 'Abouriou', 'Abrostine', 'Acolon', 'Agiorgitiko', 'Aglianico', 'Aidani', 'Airen', 'Albalonga', 'Albana', 'Albanella', 'Albariño', 'Albarola', 'Albarossa', 'Albarín Blanco', 'Albillo', 'Albillo Crimean', 'Albillo Mayor', 'Albillo de Albacete', 'Aleatico', 'Alfrocheiro Preto', 'Alibernet', 'Alicante Bouschet', 'Alicante Ganzin', 'Aligoté', 'Altesse', 'Alvarelhão', 'Alvarinho', 'Amigne', 'Ancellotta', 'Ansonica', 'Antão Vaz', 'Aragonez', 'Aramon', 'Arbane', 'Areni', 'Argaman', 'Arinarnoa', 'Arinto', 'Arinto de Bucelas', 'Arinto dos Açores', 'Arneis', 'Arnsburger', 'Arriloba', 'Aspiran Bouschet', 'Asprinio Bianco', 'Assario Branco', 'Assyrtiko', 'Athiri', 'Aurore', 'Avanà', 'Avesso', 'Avgoustiatis', 'Azal Branco', 'Azal Tinto', 'Babić', 'Bacchus', 'Baco Noir', 'Baga', 'Barbarossa', 'Barbera', 'Barcelo', 'Barsaglina', 'Bastardo Magarachsky', 'Batoca', 'Bellone', 'Bianca', 'Biancame', 'Bianchetta Trevigiana', "Bianco d'Alessano", 'Biancolella', 'Bical', 'Black Queen', 'Blauburger', 'Blauburgunder', 'Blauer Portugieser', 'Blaufränkisch', 'Boal Branco', 'Bobal', 'Bogazkere', 'Bombino Bianco', 'Bombino Nero', 'Bonamico', 'Bonarda', 'Bordô', 'Borraçal', 'Bosco', 'Bourboulenc', 'Bovale', 'Brachetto', 'Braquet', 'Braucol', 'Brianna', 'Bronner', 'Brun Argenté', 'Bruñal', 'Bual', 'Budai Zöld', 'Bukettraube', 'Burgund Mare', 'Busuioaca de Bohotin', 'Băbească Neagră', 'Cabernet Blanc', 'Cabernet Cortis', 'Cabernet Cubin', 'Cabernet Dorsa', 'Cabernet Franc', 'Cabernet Jura', 'Cabernet Mitos', 'Cabernet Ruby', 'Cabernet Sauvignon', 'Cabernet Severny', 'Cagnulari', 'Caiño Blanco', 'Caiño Tinto', 'Calabrese di Montenuovo', 'Caladoc', 'Calkarasi', 'Callet', 'Camarate', 'Canaiolo Blanco', 'Canaiolo Nero', 'Cannonau', 'Carignan/Cariñena', 'Carmenère', 'Carricante', 'Casavecchia', 'Cascade', 'Casetta', 'Castelão', 'Catarratto Bianco', 'Catawba', 'Cayuga White', 'Cencibel', 'Centesiminio', 'Cerceal Branco', 'Cesanese', 'Chambourcin', 'Chancellor', 'Charbono', 'Chardonel', 'Chardonnay', 'Chardonnay Musqué', 'Chasan', 'Chasselas', 'Chatus', 'Chenanson', 'Chenin Blanc', 'Chinuri', 'Cienna', 'Ciliegiolo', 'Cinsault', 'Clairette', 'Cococciola', 'Coda di Volpe Bianca', 'Colobel', 'Colombard', 'Coloraillo', 'Colorino del Valdarno', 'Concord', 'Corinto Nero', 'Cornalin', 'Cornifesto', 'Corot Noir', 'Cortese', 'Corvina', 'Corvinone', 'Couderc', 'Counoise', 'Criolla Grande', 'Croatina', 'Crouchen', 'Cynthiana', 'Côdega de Larinho', 'Côt', 'Dafni', 'Dakapo', 'De Chaunac', 'Debina', 'Diagalves', 'Dimiat', 'Dimrit', 'Dindarella', 'Diolinoir', 'Dolcetto', 'Domina', 'Dona Blanca', 'Donzelinho Branco', 'Donzelinho Tinto', 'Dornfelder', 'Drupeggio', 'Dunkelfelder', 'Duras', 'Durella', 'Durif', 'Dzvelshavi Obchuri', 'Edelweiss', 'Egiodola', 'Ehrenfelser', 'Emerald Riesling', 'Emir', 'Enantio', 'Encruzado', 'Erbaluce', 'Espadeiro', 'Falanghina', 'Falanghina Beneventana', 'Famoso', 'Favorita', 'Fenile', 'Fer Servadou', 'Fernão Pires', 'Feteasca Alba', 'Feteasca Neagra', 'Feteasca Regala', 'Fiano', 'Flora', 'Foglia Tonda', 'Fokiano', 'Folgasao', 'Folle Blanche', 'Fonte Cal', 'Fragolino', 'Francusa', 'Frappato', 'Fredonia', 'Freisa', 'Friulano/Sauvignonasse', 'Frontenac', 'Fruhroter Veltliner', 'Frühburgunder', 'Fumin', 'Fumé Blanc', 'Furmint', 'Gaglioppo', 'Gaidouria', 'Galotta', 'Gamaret', 'Gamay Noir', 'Gamay Teinturier de Bouze', 'Gamba di Pernice', 'Garanoir', 'Garganega', 'Garnacha', 'Garnacha Blanca', 'Garnacha Peluda', 'Garnacha Roja', 'Garnacha Tinta', 'Garnacha Tintorera', 'Garrido Fino', 'Gelber Muskateller', 'Gewürztraminer', 'Gigiac', 'Ginestra', 'Girgentina', 'Girò Blanc', 'Glera/Prosecco', 'Godello', 'Gold Traminer', 'Goldburger', 'Golubok', 'Gorgollasa', 'Goruli Mtsvane', 'Gouveio', 'Gouveio Real', 'Graciano', 'Grand Noir', 'Grasa de Cotnari', 'Grauburgunder', 'Grecanico', 'Grechetto', 'Grechetto Rosso', 'Greco', 'Greco Bianco', 'Greco Nero', 'Grenache', 'Grenache Blanc', 'Grenache Gris', 'Grignolino', 'Grillo', 'Gringet', 'Grolleau', 'Groppello', 'Gros Manseng', 'Gros Verdot', 'Grüner Veltliner', 'Guardavalle', 'Gutedel', 'Hanepoot', 'Helios', 'Hibernal', 'Hondarrabi Beltza', 'Hondarrabi Zuri', 'Humagne Blanche', 'Humagne Rouge', 'Huxelrebe', 'Hárslevelű', 'Incrocio Manzoni', 'Inzolia', 'Irsai Oliver', 'Isabella', 'Jacquère', 'Jaen', 'Jampal', 'Johannisberg', 'Johanniter', 'Juan Garcia', 'Kabar', 'Kadarka', 'Kakhet', 'Kakotrygis', 'Kalecik Karasi', 'Kangun', 'Karasakiz', 'Karmahyut', 'Katsano', 'Keratsuda', 'Kerner', 'Khikhvi', 'Királyleányka', 'Kisi', 'Klevner', 'Kokur Bely', 'Koshu', 'Kotsifali', 'Krasnostop Anapsky', 'Krasnostop Zolotovsky', 'Kratosija', 'Krstac', 'Kydonitsa', 'Kékfrankos', "L'Acadie Blanc", 'Lacrima', 'Lafnetscha', 'Lagrein', 'Lambrusco', 'Lampia', 'Landot Noir', 'Lauzet', 'Leanyka', 'Lefkada', 'Lemberger', "Len de l'El", 'Lenoir', 'Leon Millot', 'Liatiko', 'Limnio', 'Limniona', 'Listan Negro', "Loin de l'Oeil", 'Lorena', 'Loureiro', 'Macabeo', 'Madeleine Angevine', 'Magliocco Canino', 'Malagouzia', 'Malbec', 'Malbo Gentile', 'Malvar', 'Malvasia', 'Malvasia Bianca Lunga', 'Malvasia Fina', 'Malvasia Istriana', 'Malvasia Nera', 'Malvasia del Lazio', 'Malvasia di Candia', 'Malvasia di Lipari', 'Malvasia di Schierano', 'Malvazija Istarska', 'Mammolo', 'Mandilaria', 'Mandón', 'Manseng', 'Manteudo', 'Manto Negro', 'Manzoni Bianco', 'Maratheftiko', 'Marechal Foch', 'Maria Gomes', 'Marmajuelo', 'Marquette', 'Marsanne', 'Marselan', 'Marufo', 'Marzemino', 'Mataro', 'Maturana Blanca', 'Maturana Tinta', 'Mauzac Blanc', 'Mauzac Noir', 'Mavro', 'Mavro Kalavritino', 'Mavrodafni', 'Mavrotragano', 'Mavroudi Arachovis', 'Mavrud', 'Mayolet', 'Mazuelo', 'Melnik', 'Melody', 'Melon de Bourgogne', 'Mencia', 'Menoir', 'Merlot', 'Merseguera', 'Michet', 'Millot-Foch', 'Misket Cherven', 'Misket Vrachanski', 'Modrý Portugal', 'Molinara', 'Mollard', 'Monastrell', 'Mondeuse Noire', 'Monica', 'Montepulciano', 'Montuni', 'Moradella', 'Morava', 'Morellino', 'Morenillo', 'Moreto', 'Morio-Muskat', 'Moristel', 'Moschofilero', 'Moschomavro', 'Mouhtaro', 'Mourisco', 'Mourvedre', 'Mtsvane Kakhuri', 'Muscadelle', 'Muscadine', 'Muscardin', 'Muscat Bailey A', 'Muscat Black', 'Muscat Blanc', 'Muscat Early', 'Muscat Golden', 'Muscat Noir', 'Muscat Orange', 'Muscat Ottonel', 'Muscat Valvin', 'Muscat Yellow', 'Muscat of Alexandria', 'Muscat of Frontignan', 'Muscat of Hamburg', 'Muscat of Setúbal', 'Muscat/Moscatel Galego', 'Muscat/Moscatel Roxo', 'Muscat/Moscatel de Grano Menudo', 'Muscat/Moscatello Selvatico', 'Muscat/Moscato', 'Muscat/Moscato Bianco', 'Muscat/Moscato Giallo', 'Muscat/Moscato Rosa', 'Muscat/Moscato di Scanzo', 'Muscat/Muscatel', 'Muscat/Muskat Moravsky', 'Mustoasa de Maderat', 'Müller-Thurgau', 'Narince', 'Nascetta', 'Nasco', 'Nebbiolo', 'Negoska', 'Negrara Trentino', 'Negrara Veronese', 'Negrette', 'Negroamaro', 'Negru de Dragasani', 'Nerello Cappuccio', 'Nerello Mascalese', 'Neretta Cuneese', 'Nero Buono di Cori', "Nero d'Avola", 'Nero di Troia', 'Neuburger', 'Niagara', 'Niagara Blanc', 'Nieddera', 'Nielluccio', 'Noble', 'Nocera', 'Noiret', 'Norton', 'Nosiola', 'Nouvelle', 'Nuragus', 'Ojaleshi', 'Olasz Rizling', 'Ondenc', 'Orion', 'Orleans Gelb', 'Ortega', 'Ortrugo', 'Oseleta', 'Otskhanuri Sapere', 'Padeiro', 'Pagadebit', 'Palava', 'Pallagrello Bianco', 'Pallagrello Nero', 'Palomino', 'Pamid', 'Pampanuto', 'Parellada', 'Parraleta', 'Pascale', 'Passerina', 'Pavana', 'País/Mission', 'Pecorino', 'Pederna', 'Pedral', 'Pedro Ximenez', 'Pelaverga', 'Peloursin', 'Perera', 'Perle', 'Perricone', 'Perrum', 'Petit Courbu', 'Petit Manseng', 'Petit Meslier', 'Petit Rouge', 'Petit Verdot', 'Petite Arvine', 'Petite Milo', 'Petite Pearl', 'Petite Sirah', 'Peverella', 'Phoenix', 'Picardan', 'Piccola Nera', 'Picolit', 'Picpoul Blanc', 'Piedirosso', 'Pigato', 'Pignoletto', 'Pignolo', "Pineau D'Aunis", 'Pinenc', 'Pinot Auxerrois', 'Pinot Blanc', 'Pinot Grigio', 'Pinot Gris', 'Pinot Meunier', 'Pinot Nero', 'Pinot Noir', 'Pinotage', 'Piquepoul Blanc', 'Piquepoul Noir', 'Plavac Mali', 'Pollera Nera', 'Posip Bijeli', 'Poulsard', 'Premetta', 'Prensal', 'Preto Martinho', 'Prieto Picudo', 'Primitivo', 'Prié', 'Procanico', 'Prokupac', 'Prugnolo Gentile', 'Pugnitello', 'Pulcinculo', 'Rabigato', 'Rabo de Ovelha', 'Raboso Piave', 'Raboso Veronese', 'Ramisco', 'Rebo', 'Refosco', 'Refosco dal Peduncolo Rosso', 'Regent', 'Reichensteiner', 'Ribolla Gialla', 'Riesel', 'Rieslaner', 'Riesling', 'Riesling Itálico', 'Riesling Renano', 'Ripolo', 'Rivaner', 'Rkatsiteli', 'Robola', 'Roditis', 'Roesler', 'Rolle/Rollo', 'Romeiko', 'Romé', 'Rondinella', 'Rondo', 'Roobernet', 'Roscetto', 'Rosetta', 'Rossese', 'Rossignola', 'Rossola', 'Rotberger', 'Roter Veltliner', 'Rotgipfler', 'Rougeon', 'Roupeiro', 'Roussanne', "Roussette D'Ayze", 'Royal de Alloza', 'Rubin', 'Rubired', 'Ruché', 'Ruen', 'Rufete', 'Ruggine', 'Ruländer', 'Räuschling', 'Sabrevois', 'Sacy', 'Sagrantino', 'Samsó', 'Sangiovese', 'Saperavi', 'Sarba', 'Sauvignon Blanc', 'Sauvignon Gris', 'Savagnin Blanc', 'Savatiano', 'Scheurebe', 'Schiava', 'Schiava Gentile', 'Schiava Grigia', 'Schioppettino', 'Schwarzriesling', 'Schönburger', 'Sciacarello', 'Sciascinoso', 'Seara Nova', 'Segalin', 'Seibel', 'Sercial', 'Sercialinho', 'Seyval Blanc', 'Shiroka Melnishka', 'Sibirkovi', 'Sideritis', 'Siegerrebe', 'Silvaner/Sylvaner', 'Smederevka', 'Solaris', 'Sousão', 'Souvignier Gris', 'Spätburgunder', 'St. Croix', 'St. Laurent', 'Steuben', 'Sultana', 'Sultaniye', 'Sumoll', 'Sumoll Blanc', 'Susumaniello', 'Swenson White', 'Symphony', 'Syrah/Shiraz', 'Syriki', 'Szürkebarát', 'Sémillon', 'Síria', 'Tamaioasa Romaneasca', 'Tamarez', 'Tannat', 'Tarrango', 'Tazzelenghe', 'Tempranillo', 'Tempranillo Blanco', 'Teroldego', 'Terrano', 'Terrantez', 'Terret', 'Thrapsathiri', 'Tibouren', 'Timorasso', 'Tinta Amarela', 'Tinta Barroca', 'Tinta Caiada', 'Tinta Carvalha', 'Tinta Francisca', 'Tinta Madeira', 'Tinta Miúda', 'Tinta Negra Mole', 'Tinta Roriz', 'Tinta de Toro', 'Tinta del Pais', 'Tintilia', 'Tintilla', 'Tinto Cão', 'Tinto Fino', 'Tintore Di Tramonti', 'Tocai Friulano', 'Tocai Italico', 'Torbato', 'Torrontés', 'Touriga Franca', 'Touriga Nacional', 'Trajadura', 'Traminer', 'Traminette', 'Trebbiano', 'Trebbiano Giallo', 'Trebbiano Romagnolo', 'Trebbiano Toscano', "Trebbiano d'Abruzzo", 'Treixadura', 'Trepat', 'Trincadeira', 'Triomphe', 'Trollinger', 'Trousseau', 'Tsimlyansky Cherny', 'Tsolikouri', 'Turan', 'Turbiana', 'Ughetta di Canneto', 'Ugni Blanc', 'Ull de Llebre', 'Uva Rara', 'Vaccareze', 'Valdiguie', 'Valentino Nero', 'Verdeca', 'Verdejo', 'Verdelho', 'Verdello', 'Verdicchio', 'Verdiso', 'Verduzzo Friulano', 'Vermentino', 'Vermentino Nero', 'Vernaccia', 'Vernaccia di Oristano', 'Vernaccia di San Gimignano', 'Vernatsch', 'Vespaiola', 'Vespolina', 'Vidal Blanc', 'Vidiano', 'Vien de Nus', 'Vignoles', 'Vijiriega', 'Vilana', 'Villard Noir', 'Vincent', 'Vinhão', 'Viognier', 'Violeta', 'Viorica', 'Viosinho', 'Vital', 'Vitovska', 'Viura', 'Vranac', 'Weissburgunder', 'Welschriesling', 'Xarel-lo', 'Xinomavro', 'Xynisteri', 'Zalema', 'Zelen', 'Zengö', 'Zibibbo', 'Zierfandler', 'Zinfandel', 'Zinfandel White', 'Zlahtina', 'Zweigelt', 'Zéta', 'Água Santa', 'Öküzgözü']


Type  = st.selectbox('Select the Type of the wine / Sélectionnez le genre du vin', ['Red', 'White', 'Rose', 'Sparkling', 'Dessert/Port', 'Dessert'])
Body  = st.selectbox('Select the Body of the wine / Sélectionnez le corps du vin', ['Very full-bodied','Full-bodied', 'Medium-bodied', 'Light-bodied','Very light-bodied'])
Acidity = st.selectbox("Select the Acidity of the wine / Sélectionnez l'acidité du vin", ['High', 'Medium', 'Low'])
Grapes = st.selectbox("Choose the name of the grape / Indiquer le nom du cépage", grapes)
ABV = st.text_input("Provide the Alcohol Percentage (in %) / Indiquer le pourcentage d'alcool (en %)", value=12.0)
if "," in ABV:
    ABV=ABV.replace(",",".")


# need to make sure that comma is replaced by dot
# ABV = st.slider("Provide the Alcohol Percentage", value=12.0, min_value=0.0, max_value=30.0, step=0.1)

if st.button('Results / Résultats'):
    params = {'Type': Type,
            'ABV': float(ABV),
            'Body': Body,
            'Acidity': Acidity,
            'Grapes': Grapes}

    # st.write(params)
    response = requests.get(url, params=params).json()['foods']

    '''
    ### Suggested foods / Aliments recommandés:
    '''
    i = 1
    for food in response:
        st.write(f'{i}. {food}')
        i += 1


# st.markdown("<h2 style='text-align: center; '>The creators of VinoDine / Les créateurs de VinoDine</h2>", unsafe_allow_html=True)

# # need jpeg files instead of URL to our Le Wagon entree
# CREATORS = {
#             'Arjan' : 'https://avatars.githubusercontent.com/u/161768796?v=4',
#             'Florian' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1710834888/uzueseo7zyyykjantnnn.jpg',
#             'James' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1710833790/s6zy2sc8qsmrlf0g04ac.jpg',
#             'Tobias' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1710264098/h5jfyf2dqi2lor5zdbc5.jpg'
#         }
# col1, col2=st.columns(2)
# with col1:
#     for title, image in CREATORS.items():
#         if title=='Arjan' or title == 'Florian':
#             st.image(image, caption=title,use_column_width=True)


# with col2:
#     for title, image in CREATORS.items():
#         if title=='James' or title == 'Tobias':
#             st.image(image, caption=title,use_column_width=True)

def title():
    return 'Injecting HTML 🧙‍♂️'


def run():

    if st.checkbox('Show creators'):
        image_size = st.slider('Zoom', 50, 250, 119)

        # https://kitt.lewagon.com/camps/414/contracts
        # document.querySelectorAll('tr').forEach(elt => {
        #     const img = elt.getElementsByTagName('img');
        #     if (img.length > 0) {
        #         const name = elt.getElementsByTagName('td')[1].innerText;
        #         const src = img[0].src;
        #         console.log(`'${name}' : '${src}',`);
        #     }
        # });

        CREATORS = {
            'Arjan' : 'https://avatars.githubusercontent.com/u/161768796?v=4',
            'Florian' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1710834888/uzueseo7zyyykjantnnn.jpg',
            'James' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1710833790/s6zy2sc8qsmrlf0g04ac.jpg',
            'Tobias' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1710264098/h5jfyf2dqi2lor5zdbc5.jpg'
        }

        CREATOR_CSS = f"""
        #creators {{
            display: flex;
            flex-wrap: wrap;
        }}

        .creator-card {{
            display: flex;
            flex-direction: column;
        }}

        .creator-card img {{
            width: {image_size}px;
            height: {image_size}px;
            border-radius: 100%;
            padding: 4px;
            margin: 10px;
            box-shadow: 0 0 4px #eee;
        }}

        .creator-card span {{
            text-align: center;
        }}
        """

        # streamlit html injection seems to sensitive to new lines...
        # remove that \ and the html gets displayed instead of being interpreted
        CREATOR_CARD = """\
            <div class="creator-card">
                <img src="{url}">
                <span>{name}</span>
            </div>
        """

        creators = ''.join([CREATOR_CARD.format(name=f'{name.split()[0]}', url=url) for name, url in CREATORS.items()])

        CREATOR_HTML = f"""
        <style>
        {CREATOR_CSS}
        </style>
        <div id="creators">
            {creators}
        </div>
        """

        st.write(CREATOR_HTML, unsafe_allow_html=True)
