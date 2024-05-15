import streamlit as st
import requests
from itertools import cycle

# URL for VinoDine API
url = 'https://vinodine2-dxr2er4ueq-ew.a.run.app/predict'

# st.image("https://cdn.pixabay.com/photo/2024/05/05/23/00/ai-generated-8742016_1280.jpg", caption='VinoDine', output_format="auto")

st.markdown("""<h4 style='text-align: center; '>Unlock your <b>perfect Wine and Food pairing</b> in just 5 questions!</h4>""", unsafe_allow_html=True)

grapes = ['"BiancodAlessano"', '"LAcadieBlanc"', '"LendelEl"', '"LoindelOeil"', '"NerodAvola"', '"PineauDAunis"', '"RoussetteDAyze"', '"TrebbianodAbruzzo"', 'Abbuoto', 'Abouriou', 'Abrostine', 'Acolon', 'Agiorgitiko', 'Aglianico', 'Aidani', 'Airen', 'Albalonga', 'Albana', 'Albanella', 'Albariño', 'Albarola', 'Albarossa', 'AlbarínBlanco', 'Albillo', 'AlbilloCrimean', 'AlbilloMayor', 'AlbillodeAlbacete', 'Aleatico', 'AlfrocheiroPreto', 'Alibernet', 'AlicanteBouschet', 'AlicanteGanzin', 'Aligoté', 'Altesse', 'Alvarelhão', 'Alvarinho', 'Amigne', 'Ancellotta', 'Ansonica', 'AntãoVaz', 'Aragonez', 'Aramon', 'Arbane', 'Areni', 'Argaman', 'Arinarnoa', 'Arinto', 'ArintodeBucelas', 'ArintodosAçores', 'Arneis', 'Arnsburger', 'Arriloba', 'AspiranBouschet', 'AsprinioBianco', 'AssarioBranco', 'Assyrtiko', 'Athiri', 'Aurore', 'Avanà', 'Avesso', 'Avgoustiatis', 'AzalBranco', 'AzalTinto', 'Babić', 'Bacchus', 'BacoNoir', 'Baga', 'Barbarossa', 'Barbera', 'Barcelo', 'Barsaglina', 'BastardoMagarachsky', 'Batoca', 'Bellone', 'Bianca', 'Biancame', 'BianchettaTrevigiana', 'Biancolella', 'Bical', 'BlackQueen', 'Blauburger', 'Blauburgunder', 'BlauerPortugieser', 'Blaufränkisch', 'BoalBranco', 'Bobal', 'Bogazkere', 'BombinoBianco', 'BombinoNero', 'Bonamico', 'Bonarda', 'Bordô', 'Borraçal', 'Bosco', 'Bourboulenc', 'Bovale', 'Brachetto', 'Braquet', 'Braucol', 'Brianna', 'Bronner', 'BrunArgenté', 'Bruñal', 'Bual', 'BudaiZöld', 'Bukettraube', 'BurgundMare', 'BusuioacadeBohotin', 'BăbeascăNeagră', 'CabernetBlanc', 'CabernetCortis', 'CabernetCubin', 'CabernetDorsa', 'CabernetFranc', 'CabernetJura', 'CabernetMitos', 'CabernetRuby', 'CabernetSauvignon', 'CabernetSeverny', 'Cagnulari', 'CaiñoBlanco', 'CaiñoTinto', 'CalabresediMontenuovo', 'Caladoc', 'Calkarasi', 'Callet', 'Camarate', 'CanaioloBlanco', 'CanaioloNero', 'Cannonau', 'Carignan/Cariñena', 'Carmenère', 'Carricante', 'Casavecchia', 'Cascade', 'Casetta', 'Castelão', 'CatarrattoBianco', 'Catawba', 'CayugaWhite', 'Cencibel', 'Centesiminio', 'CercealBranco', 'Cesanese', 'Chambourcin', 'Chancellor', 'Charbono', 'Chardonel', 'Chardonnay', 'ChardonnayMusqué', 'Chasan', 'Chasselas', 'Chatus', 'Chenanson', 'CheninBlanc', 'Chinuri', 'Cienna', 'Ciliegiolo', 'Cinsault', 'Clairette', 'Cococciola', 'CodadiVolpeBianca', 'Colobel', 'Colombard', 'Coloraillo', 'ColorinodelValdarno', 'Concord', 'CorintoNero', 'Cornalin', 'Cornifesto', 'CorotNoir', 'Cortese', 'Corvina', 'Corvinone', 'Couderc', 'Counoise', 'CriollaGrande', 'Croatina', 'Crouchen', 'Cynthiana', 'CôdegadeLarinho', 'Côt', 'Dafni', 'Dakapo', 'DeChaunac', 'Debina', 'Diagalves', 'Dimiat', 'Dimrit', 'Dindarella', 'Diolinoir', 'Dolcetto', 'Domina', 'DonaBlanca', 'DonzelinhoBranco', 'DonzelinhoTinto', 'Dornfelder', 'Drupeggio', 'Dunkelfelder', 'Duras', 'Durella', 'Durif', 'DzvelshaviObchuri', 'Edelweiss', 'Egiodola', 'Ehrenfelser', 'EmeraldRiesling', 'Emir', 'Enantio', 'Encruzado', 'Erbaluce', 'Espadeiro', 'Falanghina', 'FalanghinaBeneventana', 'Famoso', 'Favorita', 'Fenile', 'FerServadou', 'FernãoPires', 'FeteascaAlba', 'FeteascaNeagra', 'FeteascaRegala', 'Fiano', 'Flora', 'FogliaTonda', 'Fokiano', 'Folgasao', 'FolleBlanche', 'FonteCal', 'Fragolino', 'Francusa', 'Frappato', 'Fredonia', 'Freisa', 'Friulano/Sauvignonasse', 'Frontenac', 'FruhroterVeltliner', 'Frühburgunder', 'Fumin', 'FuméBlanc', 'Furmint', 'Gaglioppo', 'Gaidouria', 'Galotta', 'Gamaret', 'GamayNoir', 'GamayTeinturierdeBouze', 'GambadiPernice', 'Garanoir', 'Garganega', 'Garnacha', 'GarnachaBlanca', 'GarnachaPeluda', 'GarnachaRoja', 'GarnachaTinta', 'GarnachaTintorera', 'GarridoFino', 'GelberMuskateller', 'Gewürztraminer', 'Gigiac', 'Ginestra', 'Girgentina', 'GiròBlanc', 'Glera/Prosecco', 'Godello', 'GoldTraminer', 'Goldburger', 'Golubok', 'Gorgollasa', 'GoruliMtsvane', 'Gouveio', 'GouveioReal', 'Graciano', 'GrandNoir', 'GrasadeCotnari', 'Grauburgunder', 'Grecanico', 'Grechetto', 'GrechettoRosso', 'Greco', 'GrecoBianco', 'GrecoNero', 'Grenache', 'GrenacheBlanc', 'GrenacheGris', 'Grignolino', 'Grillo', 'Gringet', 'Grolleau', 'Groppello', 'GrosManseng', 'GrosVerdot', 'GrünerVeltliner', 'Guardavalle', 'Gutedel', 'Hanepoot', 'Helios', 'Hibernal', 'HondarrabiBeltza', 'HondarrabiZuri', 'HumagneBlanche', 'HumagneRouge', 'Huxelrebe', 'Hárslevelű', 'IncrocioManzoni', 'Inzolia', 'IrsaiOliver', 'Isabella', 'Jacquère', 'Jaen', 'Jampal', 'Johannisberg', 'Johanniter', 'JuanGarcia', 'Kabar', 'Kadarka', 'Kakhet', 'Kakotrygis', 'KalecikKarasi', 'Kangun', 'Karasakiz', 'Karmahyut', 'Katsano', 'Keratsuda', 'Kerner', 'Khikhvi', 'Királyleányka', 'Kisi', 'Klevner', 'KokurBely', 'Koshu', 'Kotsifali', 'KrasnostopAnapsky', 'KrasnostopZolotovsky', 'Kratosija', 'Krstac', 'Kydonitsa', 'Kékfrankos', 'Lacrima', 'Lafnetscha', 'Lagrein', 'Lambrusco', 'Lampia', 'LandotNoir', 'Lauzet', 'Leanyka', 'Lefkada', 'Lemberger', 'Lenoir', 'LeonMillot', 'Liatiko', 'Limnio', 'Limniona', 'ListanNegro', 'Lorena', 'Loureiro', 'Macabeo', 'MadeleineAngevine', 'MaglioccoCanino', 'Malagouzia', 'Malbec', 'MalboGentile', 'Malvar', 'Malvasia', 'MalvasiaBiancaLunga', 'MalvasiaFina', 'MalvasiaIstriana', 'MalvasiaNera', 'MalvasiadelLazio', 'MalvasiadiCandia', 'MalvasiadiLipari', 'MalvasiadiSchierano', 'MalvazijaIstarska', 'Mammolo', 'Mandilaria', 'Mandón', 'Manseng', 'Manteudo', 'MantoNegro', 'ManzoniBianco', 'Maratheftiko', 'MarechalFoch', 'MariaGomes', 'Marmajuelo', 'Marquette', 'Marsanne', 'Marselan', 'Marufo', 'Marzemino', 'Mataro', 'MaturanaBlanca', 'MaturanaTinta', 'MauzacBlanc', 'MauzacNoir', 'Mavro', 'MavroKalavritino', 'Mavrodafni', 'Mavrotragano', 'MavroudiArachovis', 'Mavrud', 'Mayolet', 'Mazuelo', 'Melnik', 'Melody', 'MelondeBourgogne', 'Mencia', 'Menoir', 'Merlot', 'Merseguera', 'Michet', 'Millot-Foch', 'MisketCherven', 'MisketVrachanski', 'ModrýPortugal', 'Molinara', 'Mollard', 'Monastrell', 'MondeuseNoire', 'Monica', 'Montepulciano', 'Montuni', 'Moradella', 'Morava', 'Morellino', 'Morenillo', 'Moreto', 'Morio-Muskat', 'Moristel', 'Moschofilero', 'Moschomavro', 'Mouhtaro', 'Mourisco', 'Mourvedre', 'MtsvaneKakhuri', 'Muscadelle', 'Muscadine', 'Muscardin', 'Muscat/MoscatelGalego', 'Muscat/MoscatelRoxo', 'Muscat/MoscateldeGranoMenudo', 'Muscat/MoscatelloSelvatico', 'Muscat/Moscato', 'Muscat/MoscatoBianco', 'Muscat/MoscatoGiallo', 'Muscat/MoscatoRosa', 'Muscat/MoscatodiScanzo', 'Muscat/Muscatel', 'Muscat/MuskatMoravsky', 'MuscatBaileyA', 'MuscatBlack', 'MuscatBlanc', 'MuscatEarly', 'MuscatGolden', 'MuscatNoir', 'MuscatOrange', 'MuscatOttonel', 'MuscatValvin', 'MuscatYellow', 'MuscatofAlexandria', 'MuscatofFrontignan', 'MuscatofHamburg', 'MuscatofSetúbal', 'MustoasadeMaderat', 'Müller-Thurgau', 'Narince', 'Nascetta', 'Nasco', 'Nebbiolo', 'Negoska', 'NegraraTrentino', 'NegraraVeronese', 'Negrette', 'Negroamaro', 'NegrudeDragasani', 'NerelloCappuccio', 'NerelloMascalese', 'NerettaCuneese', 'NeroBuonodiCori', 'NerodiTroia', 'Neuburger', 'Niagara', 'NiagaraBlanc', 'Nieddera', 'Nielluccio', 'Noble', 'Nocera', 'Noiret', 'Norton', 'Nosiola', 'Nouvelle', 'Nuragus', 'Ojaleshi', 'OlaszRizling', 'Ondenc', 'Orion', 'OrleansGelb', 'Ortega', 'Ortrugo', 'Oseleta', 'OtskhanuriSapere', 'Padeiro', 'Pagadebit', 'Palava', 'PallagrelloBianco', 'PallagrelloNero', 'Palomino', 'Pamid', 'Pampanuto', 'Parellada', 'Parraleta', 'Pascale', 'Passerina', 'Pavana', 'País/Mission', 'Pecorino', 'Pederna', 'Pedral', 'PedroXimenez', 'Pelaverga', 'Peloursin', 'Perera', 'Perle', 'Perricone', 'Perrum', 'PetitCourbu', 'PetitManseng', 'PetitMeslier', 'PetitRouge', 'PetitVerdot', 'PetiteArvine', 'PetiteMilo', 'PetitePearl', 'PetiteSirah', 'Peverella', 'Phoenix', 'Picardan', 'PiccolaNera', 'Picolit', 'PicpoulBlanc', 'Piedirosso', 'Pigato', 'Pignoletto', 'Pignolo', 'Pinenc', 'PinotAuxerrois', 'PinotBlanc', 'PinotGrigio', 'PinotGris', 'PinotMeunier', 'PinotNero', 'PinotNoir', 'Pinotage', 'PiquepoulBlanc', 'PiquepoulNoir', 'PlavacMali', 'PolleraNera', 'PosipBijeli', 'Poulsard', 'Premetta', 'Prensal', 'PretoMartinho', 'PrietoPicudo', 'Primitivo', 'Prié', 'Procanico', 'Prokupac', 'PrugnoloGentile', 'Pugnitello', 'Pulcinculo', 'Rabigato', 'RabodeOvelha', 'RabosoPiave', 'RabosoVeronese', 'Ramisco', 'Rebo', 'Refosco', 'RefoscodalPeduncoloRosso', 'Regent', 'Reichensteiner', 'RibollaGialla', 'Riesel', 'Rieslaner', 'Riesling', 'RieslingItálico', 'RieslingRenano', 'Ripolo', 'Rivaner', 'Rkatsiteli', 'Robola', 'Roditis', 'Roesler', 'Rolle/Rollo', 'Romeiko', 'Romé', 'Rondinella', 'Rondo', 'Roobernet', 'Roscetto', 'Rosetta', 'Rossese', 'Rossignola', 'Rossola', 'Rotberger', 'RoterVeltliner', 'Rotgipfler', 'Rougeon', 'Roupeiro', 'Roussanne', 'RoyaldeAlloza', 'Rubin', 'Rubired', 'Ruché', 'Ruen', 'Rufete', 'Ruggine', 'Ruländer', 'Räuschling', 'Sabrevois', 'Sacy', 'Sagrantino', 'Samsó', 'Sangiovese', 'Saperavi', 'Sarba', 'SauvignonBlanc', 'SauvignonGris', 'SavagninBlanc', 'Savatiano', 'Scheurebe', 'Schiava', 'SchiavaGentile', 'SchiavaGrigia', 'Schioppettino', 'Schwarzriesling', 'Schönburger', 'Sciacarello', 'Sciascinoso', 'SearaNova', 'Segalin', 'Seibel', 'Sercial', 'Sercialinho', 'SeyvalBlanc', 'ShirokaMelnishka', 'Sibirkovi', 'Sideritis', 'Siegerrebe', 'Silvaner/Sylvaner', 'Smederevka', 'Solaris', 'Sousão', 'SouvignierGris', 'Spätburgunder', 'St.Croix', 'St.Laurent', 'Steuben', 'Sultana', 'Sultaniye', 'Sumoll', 'SumollBlanc', 'Susumaniello', 'SwensonWhite', 'Symphony', 'Syrah/Shiraz', 'Syriki', 'Szürkebarát', 'Sémillon', 'Síria', 'TamaioasaRomaneasca', 'Tamarez', 'Tannat', 'Tarrango', 'Tazzelenghe', 'Tempranillo', 'TempranilloBlanco', 'Teroldego', 'Terrano', 'Terrantez', 'Terret', 'Thrapsathiri', 'Tibouren', 'Timorasso', 'TintaAmarela', 'TintaBarroca', 'TintaCaiada', 'TintaCarvalha', 'TintaFrancisca', 'TintaMadeira', 'TintaMiúda', 'TintaNegraMole', 'TintaRoriz', 'TintadeToro', 'TintadelPais', 'Tintilia', 'Tintilla', 'TintoCão', 'TintoFino', 'TintoreDiTramonti', 'TocaiFriulano', 'TocaiItalico', 'Torbato', 'Torrontés', 'TourigaFranca', 'TourigaNacional', 'Trajadura', 'Traminer', 'Traminette', 'Trebbiano', 'TrebbianoGiallo', 'TrebbianoRomagnolo', 'TrebbianoToscano', 'Treixadura', 'Trepat', 'Trincadeira', 'Triomphe', 'Trollinger', 'Trousseau', 'TsimlyanskyCherny', 'Tsolikouri', 'Turan', 'Turbiana', 'UghettadiCanneto', 'UgniBlanc', 'UlldeLlebre', 'UvaRara', 'Vaccareze', 'Valdiguie', 'ValentinoNero', 'Verdeca', 'Verdejo', 'Verdelho', 'Verdello', 'Verdicchio', 'Verdiso', 'VerduzzoFriulano', 'Vermentino', 'VermentinoNero', 'Vernaccia', 'VernacciadiOristano', 'VernacciadiSanGimignano', 'Vernatsch', 'Vespaiola', 'Vespolina', 'VidalBlanc', 'Vidiano', 'ViendeNus', 'Vignoles', 'Vijiriega', 'Vilana', 'VillardNoir', 'Vincent', 'Vinhão', 'Viognier', 'Violeta', 'Viorica', 'Viosinho', 'Vital', 'Vitovska', 'Viura', 'Vranac', 'Weissburgunder', 'Welschriesling', 'Xarel-lo', 'Xinomavro', 'Xynisteri', 'Zalema', 'Zelen', 'Zengö', 'Zibibbo', 'Zierfandler', 'Zinfandel', 'ZinfandelWhite', 'Zlahtina', 'Zweigelt', 'Zéta', 'ÁguaSanta', 'Öküzgözü']
st.write('Select the type of wine')
Type  = st.selectbox('Type of the wine', options=['Red', 'White', 'Rose', 'Sparkling', 'Dessert/Port', 'Dessert'],
                     placeholder='Choose the type of wine...', index=None, label_visibility='collapsed')

st.write('Select the body of wine')
Body  = st.selectbox('Body of the wine', options=['Very full-bodied','Full-bodied', 'Medium-bodied', 'Light-bodied','Very light-bodied'],
                     placeholder='Choose the body of the wine...', index=None, label_visibility='collapsed')

st.write('Select the acidicity of the wine')
Acidity = st.selectbox("acidity of  wine", options=['High', 'Medium', 'Low'],
                       placeholder='Choose the acidity of the wine...', index=None, label_visibility='collapsed')

st.write('Select at least of type of grapes')
Grapes = st.multiselect("Type of grapes", options=grapes,
                        placeholder='Select the type of the grapes...', label_visibility='collapsed')

if Grapes == ['']:
    st.write("Please choose at least one sort of grapes")

st.write("Provide the alcohol percentage (in %)")
ABV = st.text_input("alcohol percentage", value=0.0, label_visibility='collapsed')
if "," in ABV:
    ABV=ABV.replace(",",".")

if st.button('Results'):
    if Type == '' or Body == '' or Acidity == '' or len(Grapes) == 0 or ABV == '':
        st.error('Please answer all questions to proceed')
    else:
        params = {'Type': Type,
            'ABV': float(ABV),
            'Body': Body,
            'Acidity': Acidity,
            'grapes': Grapes}

        # st.write(params)
        response = requests.get(url, params=params).json()['foods']
        # st.write(response)

        '''
        ### Suggested foods:
        '''
        i = 1
        for food in response:
            if food == "Appetizer":
                st.write(f'{i}. {food}')
                st.page_link("https://www.loveandlemons.com/appetizers/", icon='🧑‍🍳', label="Discover tantalizing appetizer recipes in one click!")
            elif food == "Beef":
                st.write(f'{i}. {food}')
                st.page_link("https://www.mob.co.uk/recipes/collections/mobs-best-beef-recipes", icon='🧑‍🍳', label="Check out amazing beef recipes with one click here!")
            elif food == "Cured Meat":
                st.write(f'{i}. {food}')
                st.page_link("https://www.epicurious.com/ingredient/cured-meat", icon='🧑‍🍳', label="Explore delicious cured meat recipes with a single click!")
            elif food == "Game Meat":
                st.write(f'{i}. {food}')
                st.page_link("https://www.bbc.co.uk/food/game", icon='🧑‍🍳', label="Embark here on a culinary adventure with game meat recipes!")
            elif food == "Lamb":
                st.write(f'{i}. {food}')
                st.page_link("https://www.delish.com/cooking/recipe-ideas/g26886001/best-lamb-recipes/", icon='🧑‍🍳', label="Indulge in mouthwatering lamb recipes just a click away!")
            elif food == "Pasta":
                st.write(f'{i}. {food}')
                st.page_link("https://www.foodandwine.com/pasta-noodles/pasta", icon='🧑‍🍳', label="Cliccate qui per una meravigliosa ricetta di pasta!")
            elif food == "Pork":
                st.write(f'{i}. {food}')
                st.page_link("https://www.delicious.com.au/recipes/collections/gallery/53-life-changing-pork-recipes-for-easy-weeknight-meals/f0f1uli4", icon='🧑‍🍳', label="Dive into the world of pork recipes with just one click!")
            elif food == "Poultry":
                st.write(f'{i}. {food}')
                st.page_link("https://www.foodandwine.com/poultry-dishes-7497047", icon='🧑‍🍳', label="Elevate your meals with poultry recipes at the click of a button!")
            elif food == "Rich Fish":
                st.write(f'{i}. {food}')
                st.page_link("https://www.bbc.co.uk/food/oily_fish", icon='🧑‍🍳', label="Discover exquisite recipes featuring rich fish with a single click!")
            elif food == "Shellfish":
                st.write(f'{i}. {food}')
                st.page_link("https://www.delicious.com.au/recipes/collections/gallery/40-shellfish-recipes-that-will-have-you-on-a-seafood-high/jjfk8a8v?page=2", icon='🧑‍🍳', label="Delight your taste buds with succulent shellfish recipes in one click!")
            elif food == "Soft Cheese":
                st.write(f'{i}. {food}, with the following suggestions of pairing :')
                st.page_link("https://www.france44cheeseshop.com/blog/2024/1/8/soft-cheese-pairing-guide", icon='🧑‍🍳', label="Click here to dive into delicious soft cheese pairings!")
            elif food == "Spicy Food":
                st.write(f'{i}. {food}')
                st.page_link("https://www.mob.co.uk/recipes/collections/spicy-recipes", icon='🧑‍🍳', label="Spice up your meals with tantalizing spicy food recipes at the click of a button!")
            elif food == "Veal":
                st.write(f'{i}. {food}')
                st.page_link("https://www.foodandwine.com/meat-poultry/veal/veal", icon='🧑‍🍳', label="Enjoy tender and flavorful veal recipes with a single click!")
            elif food == "Vegetarian":
                st.write(f'{i}. {food}')
                st.page_link("https://www.jamieoliver.com/recipes/category/special-diets/vegetarian/", icon='🧑‍🍳', label="Explore a world of vegetarian delights with just one click!")
            i += 1

# foods = [‘Appetizer’, ‘Beef’, ‘Cured Meat’, ‘Game Meat’, ‘Lamb’, ‘Pasta’, ‘Pork’, ‘Poultry’, ‘Rich Fish’, ‘Shellfish’, ‘Soft Cheese’, ‘Spicy Food’, ‘Veal’, ‘Vegetarian’]

def run():
    st.markdown("<h4 style='text-align: center; '>The creators of VinoDine</h4>", unsafe_allow_html=True)
    image_size = 120

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
        'Arjan' : ['https://avatars.githubusercontent.com/u/161768796?v=4','http://www.linkedin.com/in/arjanangenent'],
        'Florian' : ['https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1710834888/uzueseo7zyyykjantnnn.jpg', 'https://www.linkedin.com/in/florian-haindl-05b848187/'],
        'James' : ['https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1710833790/s6zy2sc8qsmrlf0g04ac.jpg', 'https://www.linkedin.com/in/james-kubik-a982712bb/'],
        'Tobias' : ['https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1710264098/h5jfyf2dqi2lor5zdbc5.jpg', 'https://linkedin.com/in/tobias-eckers']
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
        padding: 5px;
        margin: 20px;
        margin-left: 35px;
        box-shadow: 0 0 4px #eee;
    }}


    .creator-card span {{
        text-align: center;
    }}

    .creator-card a {{
        text-align: center;
        color: #FFFFFF;
    }}


    """


    CREATOR_CARD = """\
        <div class="creator-card">
            <img src="{url}">
             <span>{name}</span>
             <a href={linkedin}><img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" style="width: 30px; height: 30px;"></a>
        </div>
    """

    creators = ''.join([CREATOR_CARD.format(name=f'{name.split()[0]}', url=url[0], linkedin=url[1]) for name, url in CREATORS.items()])

    CREATOR_HTML = f"""
    <style>
    {CREATOR_CSS}
    </style>
    <div id="creators">
        {creators}
    </div>
    """


    st.write(CREATOR_HTML, unsafe_allow_html=True)


run()

background_style = """
.stApp {
  background-image: url(https://cdn.pixabay.com/photo/2019/03/23/23/38/wine-4076627_1280.jpg);
  background-size: cover;
  opacity:1
}
"""

st.markdown(f'<style>{background_style}</style>', unsafe_allow_html=True)
