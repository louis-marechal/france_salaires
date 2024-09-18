import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import seaborn as sns
import plotly.express as px
from io import StringIO
import requests
from io import BytesIO
from PIL import Image
from scipy.stats import normaltest
from scipy.stats import norm
import pickle
import matplotlib.pyplot as plt

#Nouveaux DATAFRAMES
#GEO
geo_prem=pd.read_csv('geo1.csv')
geo_prem = geo_prem.drop("Unnamed: 0", axis=1)


geo2=pd.read_csv('geo2.csv')
geo2.set_index(geo2.columns[0], inplace=True)
geo2.index.name = None

geo3=pd.read_csv('geo3.csv')
geo3.set_index(geo3.columns[0], inplace=True)
geo3.index.name = "Colonne"
geo3.rename(columns={geo3.columns[0]: "NaNs"}, inplace=True)

#POP
pop1=pd.read_csv('pop1.csv')
pop1 = pop1.drop("Unnamed: 0", axis=1)


pop2=pd.read_csv('pop2.csv')
pop2.set_index(pop2.columns[0], inplace=True)
pop2.index.name = None

pop3=pd.read_csv('pop3.csv')
pop3.set_index(pop3.columns[0], inplace=True)
pop3.index.name = "Colonne"
pop3.rename(columns={pop3.columns[0]: "NaNs"}, inplace=True)


#ENT

ent1=pd.read_csv('ent1.csv')
ent1 = ent1.drop("Unnamed: 0", axis=1)


ent2=pd.read_csv('ent2.csv')
ent2.set_index(ent2.columns[0], inplace=True)
ent2.index.name = None

ent3=pd.read_csv('ent3.csv')
ent3.set_index(ent3.columns[0], inplace=True)
ent3.index.name = "Colonne"
ent3.rename(columns={ent3.columns[0]: "NaNs"}, inplace=True)

#SAL

sal1=pd.read_csv('sal1.csv')
sal1 = sal1.drop("Unnamed: 0", axis=1)


sal2=pd.read_csv('sal2.csv')
sal2.set_index(sal2.columns[0], inplace=True)
sal2.index.name = None

sal3=pd.read_csv('sal3.csv')
sal3.set_index(sal3.columns[0], inplace=True)
sal3.index.name = "Colonne"
sal3.rename(columns={sal3.columns[0]: "NaNs"}, inplace=True)

#CON
con1=pd.read_csv('con1.csv')
con1 = con1.drop("Unnamed: 0", axis=1)


con2=pd.read_csv('con2.csv')
con2.set_index(con2.columns[0], inplace=True)
con2.index.name = None

con3=pd.read_csv('con3.csv')
con3.set_index(con3.columns[0], inplace=True)
con3.index.name = "Colonne"
con3.rename(columns={con3.columns[0]: "NaNs"}, inplace=True)

#Code de l'application

st.title('French Industry')
# Configuration de la barre latérale
st.sidebar.title("Sommaire")
pages=["👋 Intro", "🔍 Exploration des données", "📊 Data Visualisation", "🧩 Modélisation", "🔮 Prédiction", "📌Conclusion"]
page=st.sidebar.radio("Aller vers", pages)
st.sidebar.markdown(
    """
    - **Cursus** : Data Analyst
    - **Formation** : Bootcamp
    - **Date** : Septembre 2024
    - **Groupe** : 
        - Louis MARECHAL
        - Charles BEYE
        - Sarah BENLALA""")

# Page d'introduction
if page == pages[0] :
    image_cover = "https://zupimages.net/up/24/36/0vj7.jpeg"
    st.image(image_cover, use_column_width=True)

    # Présentation projet
    st.caption("""**Cursus** : Data Analyst
    | **Formation** : Bootcamp
    | **Mois** : Juillet.2024
    | **Groupe** : Louis MARECHAL, Charles BEYE, Sarah BENLALA
""")

    st.header("👋 Intro")
    st.markdown("""<style>h1 {color: #4629dd;  font-size: 70px;/* Changez la couleur du titre h1 ici */} h2 {color: #440154ff;    font-size: 50px /* Changez la couleur du titre h2 ici */} h3{color: #27dce0; font-size: 30px; /* Changez la couleur du titre h3 ici */}</style>""",unsafe_allow_html=True)
    st.markdown("""<style>body {background-color: #f4f4f4;</style>""",unsafe_allow_html=True)

    st.write("Ce projet explore les inégalités salariales en France en s'appuyant sur les précieuses données de l'Insee, pour révéler les facteurs clés qui influencent les écarts de revenus. L'objectif est de dresser un portrait détaillé et de juger si ces données permettent une interprétation claire des mécanismes derrière ces inégalités.")



# Page d'exploration des données
if page == pages[1] : 
    st.header("🔍 Exploration des Données")
    st.markdown("""<style>h1 {color: #4629dd;  font-size: 70px;/* Changez la couleur du titre h1 ici */} h2 {color: #440154ff;    font-size: 50px /* Changez la couleur du titre h2 ici */} h3{color: #27dce0; font-size: 30px; /* Changez la couleur du titre h3 ici */}</style>""",unsafe_allow_html=True)
    st.markdown("""<style>body {background-color: #f4f4f4;</style>""",unsafe_allow_html=True)


    #Afficher le Dataset df_geo
    st.subheader("Dataset sur les données géographiques des codes urbains")
    st.write("**Voici les premières lignes de ce jeu de données:**")
    st.dataframe(geo_prem)
    st.write("**Informations principales sur ce jeu de données:**")
    st.write("- Nombre de lignes:", "36840")
    st.write("- Nombre de colonnes:", "14")
    st.write("- Résumé statistique de tout le jeu de données :")
    st.dataframe(geo2)
    st.write("")
    col1, col2 = st.columns([1.75,3])
    with col1 : 
     st.write("- Valeurs manquantes :", geo3)

    with col2:
     st.write("- Informations :")
     image_geo4 = "geo4.png"
     st.image(image_geo4, use_column_width=True)

     st.write("")
     
    if st.button("Passer au DataFrame répartition démographique et cohabitation") :
        #Afficher le Dataset df_population
        st.subheader("Dataset sur les données population")
        st.write("**Voici les premières lignes de ce jeu de données:**")
        st.dataframe(pop1)
        st.write("**Informations principales sur ce jeu de données:**")
        st.write("- Nombre de lignes:", "8536584")
        st.write("- Nombre de colonnes:", "7")
        st.write("- Résumé statistique de tout le jeu de données :")
        st.dataframe(pop2)
        st.write("")
        col1, col2 = st.columns([1.75,3])
        with col1 : 
            st.write("- Valeurs manquantes :", pop3)

        with col2:
            st.write("- Informations :")
            image_pop4 = Image.open("pop4.png")
    
    # Calculer la largeur pour dézoomer de 90%
            width, height = image_pop4.size
            new_width = int(width * 0.9)  # Dézoom de 90%
    
    # Afficher l'image redimensionnée
            st.image(image_pop4, width=new_width)

            st.write("")
            
    if st.button("Passer au DataFrame distribution des entreprises par taille") :
        #Afficher le Dataset df_etablissement
        st.subheader("Dataset sur les données établissement")
        st.write("**Voici les premières lignes de ce jeu de données:**")
        st.dataframe(ent1)
        st.write("**Informations principales sur ce jeu de données:**")
        st.write("- Nombre de lignes:", "36681")
        st.write("- Nombre de colonnes:", "14")
        st.write("- Résumé statistique de tout le jeu de données :")
        st.dataframe(ent2)
        st.write("")
        col1, col2 = st.columns([1.75,3])
        with col1 : 
            st.write("- Valeurs manquantes :", ent3)

        with col2:
            st.write("- Informations :")
            image_ent4 = Image.open("ent4.png")
    
    # Calculer la largeur pour dézoomer de 80%
            width, height = image_ent4.size
            new_width = int(width * 0.8)  # Dézoom de 80%
    
    # Afficher l'image redimensionnée
            st.image(image_ent4, width=new_width)

            st.write("")
            
    if st.button("Passer au DataFrame des salaires nets moyens et répartition par catégorie"):
        #Afficher le Dataset df_salary
        st.subheader("Dataset sur les données salaire")
        st.write("**Voici les premières lignes de ce jeu de données:**")
        st.dataframe(sal1)
        st.write("**Informations principales sur ce jeu de données:**")
        st.write("- Nombre de lignes:", "5136")
        st.write("- Nombre de colonnes:", "26")
        st.write("- Résumé statistique de tout le jeu de données :")
        st.dataframe(sal2)
        st.write("")
        col1, col2 = st.columns([1.75,3])
        with col1 : 
            st.write("- Valeurs manquantes :", sal3)

        with col2:
             
             st.write("- Informations :")
              # Charger l'image
             image_sal4 = Image.open("sal4.png")
    
    # Calculer la largeur pour dézoomer de 80%
             width, height = image_sal4.size
             new_width = int(width * 0.8)  # Dézoom de 80%
    
    # Afficher l'image redimensionnée
             st.image(image_sal4, width=new_width)

             st.write("")
             
             
            #Afficher le Dataset df
    if st.button("Passer au DataFrame concaténé") :
        st.write("Afin de continuer notre étude pour comprendre les inégalités en France, nous avons réalisé des modifications sur ces 4 datasets pour ainsi obtenir un fichier exploitable et pertinent.")
        col4, col5 = st.columns([1,1])
        with col4:
            st.write("_Pour la partie Visualisation des données_")
            st.write("- Gestions des valeurs manquantes (suppression ou remplacement des données).")
        with col5:
            st.write("_Pour les parties Modélisation et Prédictions_")
            st.write("- Sélection et suppression de colonnes non nécessaires")
            st.write("- Ajout de colonnes manquantes dans les dataframes selon pertinence")
            st.write("- Numérisation des colonnes")
            st.write("- Gestion des NaNs")
        
        st.write("")
        st.write("")

        #Afficher le Dataset df
        st.subheader("Concaténation des datasets")
        st.write("**Voici les premières lignes de ce jeu de données:**")

        st.dataframe(con1)
        
        st.write("")
        st.write("")

        st.markdown("**Informations principales sur ce jeu de données:**")
        st.write("- Nombre de lignes:", "5135")
        st.write("- Nombre de colonnes:", "42")
        st.write("- Résumé statistique de tout le jeu de données :")
        st.dataframe(con2)
        st.write("")
        col1, col2 = st.columns([1.75,3])
        with col1 : 
            st.write("- Valeurs manquantes :", con3)

        with col2:
            st.write("- Informations :")
            image_con4 = "con4.png"
            st.image(image_con4, use_column_width=True)

            st.write("")
            
#PAGE DE DATAVIZ
if page == pages[2] :
    st.header("📊 Data Visualisation")
    st.markdown("""<style>h1 {color: #4629dd;  font-size: 70px;/* Changez la couleur du titre h1 ici */} h2 {color: #440154ff;    font-size: 50px /* Changez la couleur du titre h2 ici */} h3{color: #27dce0; font-size: 30px; /* Changez la couleur du titre h3 ici */}</style>""",unsafe_allow_html=True)
    st.markdown("""<style>body {background-color: #f4f4f4;</style>""",unsafe_allow_html=True)

    #Histogramme Distribution du Salaire Moyen
    if st.button("Histogramme du Salaire Net Moyen"):
        image_dataviz1 = "dataviz1.png"
        st.image(image_dataviz1, use_column_width=True)
   
        
    # Boxplot du Salaire Net Moyen
    if st.button("Boxplot du Salaire Net Moyen"):
        image_dataviz2 = "dataviz2.png"
        st.image(image_dataviz2, use_column_width=True)


    # Barplot comparaison salaire Paris vs moyenne reste de la France
    if st.button("Comparaison du salaire entre Paris et le reste de la France"):
        image_dataviz3 = "dataviz3.png"
        st.image(image_dataviz3, use_column_width=True)


 
    # Courbe de l'évolution du salaire avec l'âge en fonction du sexe
    if st.button("Courbe de l'évolution du salaire avec l'âge en fonction du sexe"):

        image_dataviz4 = "dataviz4.png"
        st.image(image_dataviz4, use_column_width=True)


    # CARTE SALAIRE
    if st.button("Salaire Horaire Net Moyen par Région"):

        info_cartes= pd.read_csv('info_cartes.csv')
        
        # Charger le GeoJSON des régions françaises
        geojson_url = 'https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions-avant-redecoupage-2015.geojson'
        response = requests.get(geojson_url)
        geojson_data = response.json()

        # Créer la carte choroplèthe
        fig = px.choropleth(
            info_cartes,
            geojson=geojson_data,
            featureidkey='properties.nom',
            locations='nom_région',
            color='salaire_moyen_région',
            color_continuous_scale='Redor',
            labels={'NB': 'Population'},
            title='Salaire horaire net moyen en France'
        )

        # Mettre à jour les propriétés de la carte pour centrer sur la France et ajuster le zoom
        fig.update_geos(
            fitbounds="locations",
            visible=True
        )

        # Afficher la carte dans Streamlit
        st.plotly_chart(fig)

    # CARTE POPULATION
    if st.button("Population par région"):

        info_cartes= pd.read_csv('info_cartes.csv')
        
        # Charger le GeoJSON des régions françaises
        geojson_url = 'https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions-avant-redecoupage-2015.geojson'
        response = requests.get(geojson_url)
        geojson_data = response.json()

        # Créer la carte choroplèthe
        fig = px.choropleth(
            info_cartes,
            geojson=geojson_data,
            featureidkey='properties.nom',
            locations='nom_région',
            color='NB',
            color_continuous_scale='Redor',
            labels={'NB': 'Population'},
            title='Population par région en France'
        )

        # Mettre à jour les propriétés de la carte pour centrer sur la France et ajuster le zoom
        fig.update_geos(
            fitbounds="locations",
            visible=True
        )

        # Afficher la carte dans Streamlit
        st.plotly_chart(fig)

####PAGE MODELISATION

if page == pages[3] : 
    st.header("🧩 Modélisation")
    st.markdown("""<style>h1 {color: #4629dd;  font-size: 70px;/* Changez la couleur du titre h1 ici */} h2 {color: #440154ff;    font-size: 50px /* Changez la couleur du titre h2 ici */} h3{color: #27dce0; font-size: 30px; /* Changez la couleur du titre h3 ici */}</style>""",unsafe_allow_html=True)
    st.markdown("""<style>body {background-color: #f4f4f4;</style>""",unsafe_allow_html=True)

    
    st.subheader("Objectif")
    st.write("Prédire le salaire net moyen horaire en fonction de différentes variables explicatives")
    
    st.write("")
    st.write("")

    if st.button("Modèles de Machine Learning") :
        st.subheader("Choix des modèles")
        st.markdown("""
                    Dans le cadre de notre problématique, qui s'apparente à une régression linéaire, nous avons testé les modèles suivants :
                    - LinearRegression
                    - Lasso
                    - DecisionTreeRegressor
                    - GradientBoosting
                    - RandomForestRegressor
                    - Ridge
        """)

        st.write("")
        st.write("")

        st.subheader("Preprocessing")
        st.markdown("""
                    Avant la mise en oeuvre de nos modèles, nous avons réalisé des étapes de preprocessing sur nos jeux de données initiaux, dont vous retrouverez les détails dans notre rapport. En voici les grandes lignes : 
                    - Regroupement (merge)
                    - Gestion des NaNs
                    - Numérisation des valeurs
                    - Création de colonnes pertinentes, principalement par regroupement (e.g. "hommes" / "femmes" ; "24_49 ans"...)
                    - Suppression de colonnes (e.g. les moins de 15 ans)
                """)
    
#ICI EVENTUELLEMENT AJOUTER une photo du JEU DE DONNEE FINAL (voir rapport) et descirption des colonnes 5135 col x 42 entrées

        st.subheader("Etapes de mise en oeuvre")
        st.markdown("""
                    Pour chaque modèle retenu, nous avons mis en oeuvre les étapes suivantes :
                    1. Isoler la varibale cible
                    2. Séparation des données en un jeu d'entraînement et de test (80%, 20%)
                    3. Gestions des NaNs restant
                    4. Mise à l'échelle éventuelle
                    5. Instanciation et entraînement du modèle
                    6. Analyse des performances par le biais de métriques et visualisation des prédictions ainsi que des "features importance"
                    7. Optimisation du modèle
                """)
    
   
    if st.button("Comparaison des modèles") :
        data = {
        'Modèles': ['Linear Regression 1', 'Linear Regression 2', 'Lasso 1', 'Lasso 2', 'DecisionTree Regressor 1', 'DecisionTree Regressor 2', 'DecisionTree Regressor 3', 'Gradient Boosting', 'RandomForestRegressor 1', 'RandomForestRegressor 2', 'Ridge'],
        'R² train': [0.9997, 0.9513, 0.0658, 0.9492, 0.7171, 0.7092, 0.7379, 0.9991, 0.9731, 0.8388, 0.6597],
        'R² test': [0.9995, 0.9389, 0.0260, 0.9372, 0.7296, 0.7224, 0.7655, 0.9970, 0.8074, 0.7854, 0.6278],
        'MSE train': [0.0023, 0.3385, 6.4897, 0.4315, 1.8152, 1.8661, 1.6819, " ", 0.1745, 1.0444, 1.0444],
        'MSE test': [0.0026, 0.3027, 4.8278, 0.4156, 1.9147, 1.9662, 1.6610, " ", 1.3362, 1.4885, 2.5818],
        'RMSE train': [0.0477, 0.5818, 2.5475, 0.3526, 1.3473, 1.3660, 1.2969, 0.0775, 0.4178, 1.0220, 1.0220],
        'RMSE test': [0.0512, 0.5502, 2.1972, 0.3114, 1.3837, 1.4022, 1.2888, 0.1468, 1.1559, 1.2200, 1.6068],
        'MAE train': [0.0378, 0.4255, 1.7064, 0.5938, 1.0428, 1.0531, 1.0293, " ", 0.1958, 0.4624, 0.4624],
        'MAE test': [0.0394, 0.4119, 1.5718, 0.5580, 1.0345, 1.0480, 1.0131, " ", 0.5348, 0.5455, 0.8243]
                }

        # Création du DataFrame
        tab = pd.DataFrame(data)
        tab.index = tab.index #+ 1
        # Trouver l'index de la ligne correspondant à "Lin Reg 2"
        lr2_index = tab[tab['Modèles'] == 'Linear Regression 2'].index

        # Appliquer un style personnalisé à la ligne spécifique
        styled_tab = tab.style.apply(lambda x: ['background: #27dce0' if x.name in lr2_index else '' for i in x], axis=1)
        
        st.write("")
        st.write("")

        # Afficher le tableau avec le style appliqué
        st.subheader("Tableau des métriques de performance")
        st.table(styled_tab)
        
        st.write("")
        st.write("#### Modèle retenu : Linear Regression 2")

    if st.button("Evaluation du modèle") :
        st.subheader("QQ Plot")
        image_qqplot = Image.open("qqplot.png")
    
    # Calculer la largeur pour dézoomer de 80%
        width, height = image_qqplot.size
        new_width = int(width * 0.8)  # Dézoom de 80%
    
    # Afficher l'image redimensionnée
        st.image(image_qqplot, width=new_width)


        st.subheader("Importance des variables")
        image_featimp = "featimp.png"
        st.image(image_featimp, use_column_width=True)

        
        st.markdown("""
                    ##### Points principaux :         
                    - Prédictions suivent la ligne
                    - Performances liées à un nombre élevé de features
                    """)
        
        st.write("")
        st.write("")

#####PAGE PREDICTION 

if page == pages[4] :

  
    
    st.header("🔮 Prédiction")
    st.markdown("""<style>h1 {color: #4629dd;  font-size: 70px;/* Changez la couleur du titre h1 ici */} h2 {color: #440154ff;    font-size: 50px /* Changez la couleur du titre h2 ici */} h3{color: #27dce0; font-size: 30px; /* Changez la couleur du titre h3 ici */}</style>""",unsafe_allow_html=True)
    st.markdown("""<style>body {background-color: #f4f4f4;</style>""",unsafe_allow_html=True)

    def charger_modele():

        # Charger le modèle à partir du fichier Pickle
        with open('modele.pkl', 'rb') as fichier_modele:
            modele = pickle.load(fichier_modele)
        return modele

# Interface utilisateur Streamlit
    st.subheader("Prédiction avec LinearRegression - Modèle limité aux 5 features principales")

    st.markdown(f"<p style='font-size:24px; font-weight:bold;'> Attribuez des valeurs à un espace géographique donné</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:14px; color:grey; font-style:italic;'>Attention : pour éviter les prédictions aberrantes, veillez à entrer des valeurs cohérentes (ordres de grandeur respectés, proportions réalistes du nombre d'entreprises par rapport à la population, etc.)</p>", unsafe_allow_html=True)           





# Créer des curseurs pour chaque caractéristique en utilisant les noms et valeurs
    caracteristique1 = st.slider("total_entreprises", 6.0, 427385.0, 3453.0)
    caracteristique2 = st.slider("autres_entreprises", 6.0, 316603.0, 2087.0)
    caracteristique3 = st.slider("hommes ", 604.0, 858091.0, 16811.0)
    caracteristique4 = st.slider("femmes", 641.0, 1000061.0, 18170.0)
    caracteristique5 = st.slider("24_49ans", 306.0, 858882.0, 14701.0)


# Prétraitement des caractéristiques avec LinearRegression
    caracteristiques = np.array([caracteristique1, caracteristique2, caracteristique3, caracteristique4,caracteristique5])

#Reshape pour éliminer un bug A ENLEVER SI CA FONCTIONNE PAS
# Reshape des caractéristiques en 2D array (1 ligne, N colonnes)
    caracteristiques = caracteristiques.reshape(1, -1)


# Prévoir avec le modèle
    modele = charger_modele()
    prediction = modele.predict(caracteristiques)
# Afficher la prédiction
    st.markdown(f"<p style='font-size:24px; font-weight:bold;'>La prédiction du salaire net moyen horaire est de : {prediction[0]}</p>", unsafe_allow_html=True)



    data_pred = {
        'Variables': ['Total entreprises', 'Autres entreprises', 'Hommes', 'Femmes', '24 49 ans', 'Salaire net moyen horaire'],
        'Paris (CODGEO : 75056)': [427385, 316603, 858091, 1000061, 858882, 22.2],
        'Valenciennes (CODGEO : 59606)': [3453, 2087, 16811, 18170, 14701, 13.8]
    }

    st.write("")

    if st.checkbox("Cas concret de prédiction"):

        #st.write("##### Cas concret de prédiction :")
        tab = pd.DataFrame.from_dict(data_pred, orient='index')
        # Définir les colonnes en utilisant la première ligne du DataFrame
        tab.columns = tab.iloc[0]
        # Exclure la première ligne du DataFrame
        tab = tab[1:]    
        st.table(tab)


##CONCLUSION
if page == pages[5] :

  
    
    st.header("📌Conclusion")
    st.markdown("""<style>h1 {color: #4629dd;  font-size: 70px;/* Changez la couleur du titre h1 ici */} h2 {color: #440154ff;    font-size: 50px /* Changez la couleur du titre h2 ici */} h3{color: #27dce0; font-size: 30px; /* Changez la couleur du titre h3 ici */}</style>""",unsafe_allow_html=True)
    st.markdown("""<style>body {background-color: #f4f4f4;</style>""",unsafe_allow_html=True)

    import streamlit as st

    # Ajouter l'image à la page
    image_ccl = Image.open("wordcloud3.jpg")
    
    
    # Calculer la largeur pour dézoomer
    width, height = image_ccl.size
    new_width = int(width * 0.5)  # Dézoom
    
    # Afficher l'image redimensionnée
    st.image(image_ccl, width=new_width)
