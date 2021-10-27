#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
import dash_bootstrap_components as dbc 
import plotly.express as px
import pandas as pd 
from dash.dependencies import Input,Output
from dash import html as html
from dash import dcc as dcc
import plotly.offline as pyo
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import plotly.offline as pyo
pd.set_option('max_columns', None)
pd.set_option("max_rows", None)
data=pd.read_excel("GS_Encuesta_de_Salida.xlsx")
data.drop([132,142,182,208,240,272,274,276,300,320,327,401,336,347,354,362,361,369,421,434,499,506,614,626,646],inplace=True)
dataCuartel = data[['Selecciona el Cuartel al que pertenecías:',
              'Selecciona el Cuartel al que pertenecías:.1','Selecciona el Cuartel al que pertenecías:.2',
             'Selecciona el Cuartel al que pertenecías:.3','Selecciona el Cuartel al que pertenecías:.4',
             'Selecciona el Cuartel al que pertenecías:.5','Selecciona el Cuartel al que pertenecías:.6',
             'Selecciona el Cuartel al que pertenecías:.7','Selecciona el Cuartel al que pertenecías:.8',
            ]]
dataCuartel = dataCuartel.bfill(axis=1).iloc[:, 0]
dataRegion = data[['Selecciona la región a la que pertenecías:','Selecciona la Región a la que pertenecías:',
              'Selecciona la Región a la que pertenecías:.1','Selecciona la región a la que pertenecías:.1',
              'Selecciona la región a la que pertenecías:.2','Selecciona la región a la que pertenecías:.3',
              'Selecciona la región a la que pertenecías:.4','Selecciona la región a la que pertenecías:.5',
              'Selecciona la región a la que pertenecías:.6','Selecciona la región a la que pertenecías:.7',
              'Selecciona la región a la que pertenecías:.8','Selecciona la región a la que pertenecías:.9',
              'Selecciona la región a la que pertenecías:.10','Selecciona la región a la que pertenecías:.11',
              'Selecciona la región a la que pertenecías:.12','Selecciona la región a la que pertenecías:.13',
              'Selecciona la región a la que pertenecías:.14','Selecciona la región a la que pertenecías:.15',
              'Selecciona la región a la que pertenecías:.16','Selecciona la región a la que pertenecías:.17',
              'Selecciona la región a la que pertenecías:.18','Selecciona la región a la que pertenecías:.19',
              'Selecciona la región a la que pertenecías:.20','Selecciona la región a la que pertenecías:.21',
              'Selecciona la región a la que pertenecías:.22','Selecciona la región a la que pertenecías:.23',
              'Selecciona la región a la que pertenecías:.24','Selecciona la región a la que pertenecías:.25',
              'Selecciona la región a la que pertenecías:.26','Selecciona la región a la que pertenecías:.27',
              'Selecciona la región a la que pertenecías:.28','Selecciona la región a la que pertenecías:.29',
              'Selecciona la región a la que pertenecías:.30','Selecciona la región a la que pertenecías:.31',
              'Selecciona la región a la que pertenecías:.32','Selecciona la región a la que pertenecías:.33',
              'Selecciona la región a la que pertenecías:.34','Selecciona la región a la que pertenecías:.35',
              'Selecciona la región a la que pertenecías:.36','Selecciona la región a la que pertenecías:.37',
              'Selecciona la región a la que pertenecías:.38','Selecciona la región a la que pertenecías:.39',
              'Selecciona la región a la que pertenecías:.40','Selecciona la región a la que pertenecías:.41',
              'Selecciona la región a la que pertenecías:.42','Selecciona la región a la que pertenecías:.43',
              'Selecciona la región a la que pertenecías:.44'
            ]]
dataRegion = dataRegion.bfill(axis=1).iloc[:, 0]
data["Cuartel"]=dataCuartel
data["Region"]=dataRegion
data.drop(['Selecciona el Cuartel al que pertenecías:','Selecciona el Cuartel al que pertenecías:.1','Selecciona el Cuartel al que pertenecías:.2',
           'Selecciona el Cuartel al que pertenecías:.3','Selecciona el Cuartel al que pertenecías:.4','Selecciona el Cuartel al que pertenecías:.5','Selecciona el Cuartel al que pertenecías:.6',
           'Selecciona el Cuartel al que pertenecías:.7','Selecciona el Cuartel al que pertenecías:.8','Selecciona la región a la que pertenecías:','Selecciona la Región a la que pertenecías:',
           'Selecciona la Región a la que pertenecías:.1','Selecciona la región a la que pertenecías:.1','Selecciona la región a la que pertenecías:.2','Selecciona la región a la que pertenecías:.3',
           'Selecciona la región a la que pertenecías:.4','Selecciona la región a la que pertenecías:.5','Selecciona la región a la que pertenecías:.6','Selecciona la región a la que pertenecías:.7',
           'Selecciona la región a la que pertenecías:.8','Selecciona la región a la que pertenecías:.9','Selecciona la región a la que pertenecías:.10','Selecciona la región a la que pertenecías:.11',
           'Selecciona la región a la que pertenecías:.12','Selecciona la región a la que pertenecías:.13','Selecciona la región a la que pertenecías:.14','Selecciona la región a la que pertenecías:.15',
           'Selecciona la región a la que pertenecías:.16','Selecciona la región a la que pertenecías:.17','Selecciona la región a la que pertenecías:.18','Selecciona la región a la que pertenecías:.19',
           'Selecciona la región a la que pertenecías:.20','Selecciona la región a la que pertenecías:.21','Selecciona la región a la que pertenecías:.22','Selecciona la región a la que pertenecías:.23',
           'Selecciona la región a la que pertenecías:.24','Selecciona la región a la que pertenecías:.25','Selecciona la región a la que pertenecías:.26','Selecciona la región a la que pertenecías:.27',
           'Selecciona la región a la que pertenecías:.28','Selecciona la región a la que pertenecías:.29','Selecciona la región a la que pertenecías:.30','Selecciona la región a la que pertenecías:.31',
           'Selecciona la región a la que pertenecías:.32','Selecciona la región a la que pertenecías:.33','Selecciona la región a la que pertenecías:.34','Selecciona la región a la que pertenecías:.35',
           'Selecciona la región a la que pertenecías:.36','Selecciona la región a la que pertenecías:.37','Selecciona la región a la que pertenecías:.38','Selecciona la región a la que pertenecías:.39',
           'Selecciona la región a la que pertenecías:.40','Selecciona la región a la que pertenecías:.41','Selecciona la región a la que pertenecías:.42','Selecciona la región a la que pertenecías:.43',
           'Selecciona la región a la que pertenecías:.44','email_address', 'first_name', 'last_name','custom_1',"respondent_id","collector_id","ip_address","Unnamed: 147"], axis='columns', inplace=True)
first_column = data.pop('Cuartel')
data.insert(6, 'Cuartel', first_column)
first_column = data.pop('Region')
data.insert(7, 'Region', first_column)
data = data.rename(columns = {"Ayúdanos a ingresar los siguientes datos:":"Nombre completo",'Unnamed: 10': 'Número de empleado:', 
                              "Unnamed: 82":"Otro1 (especifique)",
                              "Unnamed: 86" : "Otro2 (especifique)","En el último año, ¿con qué frecuencia experimentaste alguna de las siguientes situaciones?":"Robo o asalto en transporte público.",
                              'Unnamed: 90':'Acoso en transporte público.', 'Unnamed: 91': "Robo total o parcial de vehículo propio(automóvil, motocicleta, bicicleta, etc).", 
                              "Unnamed: 92":'Agresión física por personas ajenas a la organización.', "Unnamed: 93":"Extorsión.",
                              "Unnamed: 96" : "Prestaciones", "Unnamed: 97":"Ubicación",
                              "¿Qué elementos mejoraron para realizar el cambio de empleo? Selecciona las necesarias:":"Sueldo",
                              "Unnamed: 98":"Desarrollo profesional1", "Unnamed: 99":"Ambiente laboral",
                              "Unnamed: 100" : "Cultura", "Unnamed: 101" : "Cambio de Liderazgo", "Unnamed: 102" : "Actividades de Puesto", "Unnamed: 103" : "Costos de traslado a lugar de trabajo",
                              "Unnamed: 104" : "Otro3 (especifique)",
                              "Selecciona los tres mejores momentos de tu estancia:":"Información sobre sueldo y prestaciones",
                              "Unnamed: 121" : "Proceso de reclutamiento1", "Unnamed: 122" : "Sesión de bienvenida1", "Unnamed: 123" : "Recibimiento a tu puesto1",
                              "Unnamed: 124" : "Capacitación1", "Unnamed: 125" : "Seguimiento a tu desempeño1", "Unnamed: 126" : "Evaluación1",
                              "Unnamed: 127" : "Convivencia con compañeros1", "Unnamed: 128" : "Convivencia con Formador1", "Unnamed: 129" : "Eventos de temporada (Fiesta de fin de año, entre otros)1",
                              "Unnamed: 130" : "Participación en acciones sociales1", "Unnamed: 131" : "Desarrollo profesional2", "Unnamed: 132":"Elite Azteca1","Unnamed: 133" : "Otro4 (especifique)",
                              "Unnamed: 134":"Información sobre sueldo y prestaciones","Unnamed: 135" : "Proceso de reclutamiento2",
                              "Unnamed: 136" : "Sesión de bienvenida2", "Unnamed: 137" : "Recibimiento a tu puesto2" ,"Unnamed: 138" : "Capacitación2", "Unnamed: 139" : "Seguimiento a tu desempeño2",
                              "Unnamed: 140": "Evaluación2", "Unnamed: 141" : "Convivencia con compañeros2", "Unnamed: 142" : "Convivencia con Formador2", "Unnamed: 143" : "Eventos de temporada (Fiesta de fin de año, entre otros)2",
                              "Unnamed: 144": "Participación en acciones sociales2", "Unnamed: 145" : "Desarrollo profesional3", "Unnamed: 146" : "Elite Azteca2", "Unnamed: 148":"Otro5 (especifique)",
                              "Selecciona el Territorio al que pertenecías":"Territorio","¿A que área pertenecías?":"Area"
                             })
data.drop([0],inplace=True)
data["Otro1 (especifique)"]=data["Otro1 (especifique)"].apply(lambda x: 1 if not pd.isnull(x) else 0)
data["Otro2 (especifique)"]=data["Otro2 (especifique)"].apply(lambda x: 1 if not pd.isnull(x) else 0)
data["Otro3 (especifique)"]=data["Otro3 (especifique)"].apply(lambda x: 1 if not pd.isnull(x) else 0)
data["Otro4 (especifique)"]=data["Otro4 (especifique)"].apply(lambda x: 1 if not pd.isnull(x) else 0)
data["Otro5 (especifique)"]=data["Otro5 (especifique)"].apply(lambda x: 1 if not pd.isnull(x) else 0)
data["Si tienes algún comentario adicional, nos lo puedes compartir."]=data["Si tienes algún comentario adicional, nos lo puedes compartir."].apply(lambda x: 1 if not pd.isnull(x) else 0)
data["En caso de presenciar un hecho en contra de los valores o del Código de Ética favor de compartirnos el detalle."]=data["En caso de presenciar un hecho en contra de los valores o del Código de Ética favor de compartirnos el detalle."].apply(lambda x: 1 if not pd.isnull(x) else 0)
dnumeric=data.drop(['Género:', 'Edad:', 'Estado civil:',
       'Selecciona el nivel de tu puesto:',
       '¿Cuánto tiempo laboraste en Grupo Salinas? (Considerando desde tu primer puesto)',
       '¿Cuánto tiempo laboraste en tu último puesto?',
       'Visión y Misión de Grupo Salinas.',
       'Visión y Misión de tu Unidad de Negocio', 'Código de Ética.',
       'Valores y Comportamientos.', 'Prosperidad Incluyente.',
       'Modelo de Gestión de Alto desempeño.', 'Honestel.',
        'Ideas.', 'Cuéntanos.',
       'Selecciona la opción por la cuál concluyes en Grupo Salinas:',
       '¿Cuánto tiempo en promedio haces de tu casa al trabajo?',
       '¿Cuántos medios de transporte utilizas de tu casa al trabajo?',
       'Robo o asalto en transporte público.',
       'Acoso en transporte público.',
       'Robo total o parcial de vehículo propio(automóvil, motocicleta, bicicleta, etc).',
       'Agresión física por personas ajenas a la organización.',
       'Extorsión.', '¿Cómo encontraste tu nuevo empleo?', 'Sueldo',
       'Prestaciones', 'Ubicación', 'Desarrollo profesional1',
       'Ambiente laboral', 'Cultura', 'Cambio de Liderazgo',
       'Actividades de Puesto', 'Costos de traslado a lugar de trabajo',
       'Existía un ambiente de compañerismo.',
       'Tus pares cumplían con los compromisos acordados.',
       'Ofrecías apoyo para cumplir los objetivos.',
       'Honestidad.', 'Lealtad a la empresa.',
       'Confianza y respeto mutuo.', 'Pasión por el Cliente.',
       'Trabajo en equipo.', 'Ejecución impecable.', 'Mejora Continua.',
       '¿Qué tan satisfecho estás con las actividades que realizaste?',
       '¿Qué tan satisfecho estás con tu crecimiento profesional al colaborar en GS?',
       'Tu horario laboral y descansos fueron respetados.',
       'Estás satisfecho con el balance entre tus actividades laborales y personales.',
       'Información sobre sueldo y prestaciones',
       'Proceso de reclutamiento1', 'Sesión de bienvenida1',
       'Recibimiento a tu puesto1', 'Capacitación1',
       'Seguimiento a tu desempeño1', 'Evaluación1',
       'Convivencia con compañeros1', 'Convivencia con Formador1',
       'Eventos de temporada (Fiesta de fin de año, entre otros)1',
       'Participación en acciones sociales1', 'Desarrollo profesional2',
       'Elite Azteca1',
       'Selecciona los tres momentos menos agradables',
       'Proceso de reclutamiento2', 'Sesión de bienvenida2',
       'Recibimiento a tu puesto2', 'Capacitación2',
       'Seguimiento a tu desempeño2', 'Evaluación2',
       'Convivencia con compañeros2', 'Convivencia con Formador2',
       'Eventos de temporada (Fiesta de fin de año, entre otros)2',
       'Participación en acciones sociales2', 'Desarrollo profesional3',
       'Elite Azteca2', 
       'Tu experiencia en el último puesto fue: ',
        ' ¿Qué tan probable es que recomiendes a Grupo Salinas a tus amigos o familiares?'],axis=1)
dnumeric.columns = dnumeric.columns.str.replace('_',' ',)
dnumeric.fillna('na', inplace=True)
dcategorica=data[['Género:', 'Edad:', 'Estado civil:',
       'Selecciona el nivel de tu puesto:',
       '¿Cuánto tiempo laboraste en Grupo Salinas? (Considerando desde tu primer puesto)',
       '¿Cuánto tiempo laboraste en tu último puesto?',
       'Visión y Misión de Grupo Salinas.',
       'Visión y Misión de tu Unidad de Negocio', 'Código de Ética.',
       'Valores y Comportamientos.', 'Prosperidad Incluyente.',
       'Modelo de Gestión de Alto desempeño.', 'Honestel.',
        'Ideas.', 'Cuéntanos.',
       'Selecciona la opción por la cuál concluyes en Grupo Salinas:',
       '¿Cuánto tiempo en promedio haces de tu casa al trabajo?',
       '¿Cuántos medios de transporte utilizas de tu casa al trabajo?',
       'Robo o asalto en transporte público.',
       'Acoso en transporte público.',
       'Robo total o parcial de vehículo propio(automóvil, motocicleta, bicicleta, etc).',
       'Agresión física por personas ajenas a la organización.',
       'Extorsión.', '¿Cómo encontraste tu nuevo empleo?', 'Sueldo',
       'Prestaciones', 'Ubicación', 'Desarrollo profesional1',
       'Ambiente laboral', 'Cultura', 'Cambio de Liderazgo',
       'Actividades de Puesto', 'Costos de traslado a lugar de trabajo',
       'Existía un ambiente de compañerismo.',
       'Tus pares cumplían con los compromisos acordados.',
       'Ofrecías apoyo para cumplir los objetivos.',
       'Honestidad.', 'Lealtad a la empresa.',
       'Confianza y respeto mutuo.', 'Pasión por el Cliente.',
       'Trabajo en equipo.', 'Ejecución impecable.', 'Mejora Continua.',
       '¿Qué tan satisfecho estás con las actividades que realizaste?',
       '¿Qué tan satisfecho estás con tu crecimiento profesional al colaborar en GS?',
       'Tu horario laboral y descansos fueron respetados.',
       'Estás satisfecho con el balance entre tus actividades laborales y personales.',
       'Información sobre sueldo y prestaciones',
       'Proceso de reclutamiento1', 'Sesión de bienvenida1',
       'Recibimiento a tu puesto1', 'Capacitación1',
       'Seguimiento a tu desempeño1', 'Evaluación1',
       'Convivencia con compañeros1', 'Convivencia con Formador1',
       'Eventos de temporada (Fiesta de fin de año, entre otros)1',
       'Participación en acciones sociales1', 'Desarrollo profesional2',
       'Elite Azteca1',
       'Selecciona los tres momentos menos agradables',
       'Proceso de reclutamiento2', 'Sesión de bienvenida2',
       'Recibimiento a tu puesto2', 'Capacitación2',
       'Seguimiento a tu desempeño2', 'Evaluación2',
       'Convivencia con compañeros2', 'Convivencia con Formador2',
       'Eventos de temporada (Fiesta de fin de año, entre otros)2',
       'Participación en acciones sociales2', 'Desarrollo profesional3',
       'Elite Azteca2', 
       'Tu experiencia en el último puesto fue: ',
        ' ¿Qué tan probable es que recomiendes a Grupo Salinas a tus amigos o familiares?']]
dcategorica.columns = dcategorica.columns.str.replace('_',' ',)
datacategrica=pd.get_dummies(dcategorica,drop_first=False)
datacategrica.rename(columns={
    '¿Cuánto tiempo laboraste en Grupo Salinas? (Considerando desde tu primer puesto)_0 a 3 meses':"0 a 3 meses tgs",
    '¿Cuánto tiempo laboraste en Grupo Salinas? (Considerando desde tu primer puesto)_1 a 3 años':"1 a 3 años tgs",
    '¿Cuánto tiempo laboraste en Grupo Salinas? (Considerando desde tu primer puesto)_10 a 15 años':"10 a 15 años tgs",
    '¿Cuánto tiempo laboraste en Grupo Salinas? (Considerando desde tu primer puesto)_15 a 20 años':"15 a 20 años tgs",
    '¿Cuánto tiempo laboraste en Grupo Salinas? (Considerando desde tu primer puesto)_3 a 5 años':"3 a 5 años tgs",
    '¿Cuánto tiempo laboraste en Grupo Salinas? (Considerando desde tu primer puesto)_3 a 6 meses':"3 a 6 meses tgs",
    '¿Cuánto tiempo laboraste en Grupo Salinas? (Considerando desde tu primer puesto)_5 a 10 años':"5 a 10 años tgs",
    '¿Cuánto tiempo laboraste en Grupo Salinas? (Considerando desde tu primer puesto)_6 a 12 meses':"6 a 12 meses tgs",
    '¿Cuánto tiempo laboraste en Grupo Salinas? (Considerando desde tu primer puesto)_más de 20 años':"más de 20 años tgs",
    '¿Cuánto tiempo laboraste en tu último puesto?_0 a 3 meses':"0 a 3 meses tup",
    '¿Cuánto tiempo laboraste en tu último puesto?_1 a 3 años':"1 a 3 años tup",
    '¿Cuánto tiempo laboraste en tu último puesto?_10 a 15 años':"10 a 15 año tup",
    '¿Cuánto tiempo laboraste en tu último puesto?_3 a 5 años':"3 a 5 años tup",
    '¿Cuánto tiempo laboraste en tu último puesto?_3 a 6 meses':"3 a 6 meses tup",
    '¿Cuánto tiempo laboraste en tu último puesto?_5 a 10 años':"5 a 10 añostup",
    '¿Cuánto tiempo laboraste en tu último puesto?_6 a 12 meses':"6 a 12 meses tup",
    'Visión y Misión de Grupo Salinas._Moderado':"Moderado vmgs",
    'Visión y Misión de Grupo Salinas._Mucho':"Mucho vmgs",
    'Visión y Misión de Grupo Salinas._Nada':"Nada vmgs",
    'Visión y Misión de Grupo Salinas._Poco':"Poco vmgs",
    'Visión y Misión de Grupo Salinas._Suficiente':"Suficiente vmgs",
    'Visión y Misión de tu Unidad de Negocio_Moderado':"Moderado vmun",
    'Visión y Misión de tu Unidad de Negocio_Mucho':"Mucho vmun",
    'Visión y Misión de tu Unidad de Negocio_Nada':"Nada vmun",
    'Visión y Misión de tu Unidad de Negocio_Poco':"Poco vmun",
    'Visión y Misión de tu Unidad de Negocio_Suficiente':"Suficiente vmun",
    'Código de Ética._Moderado':"Moderado ce", 
    'Código de Ética._Mucho':"Mucho ce",
    'Código de Ética._Nada':"Nada ce", 
    'Código de Ética._Poco':"Poco ce",
    'Código de Ética._Suficiente':"Suficiente ce",
    'Valores y Comportamientos._Moderado':"Moderado vc",
    'Valores y Comportamientos._Mucho':"Mucho vc",
    'Valores y Comportamientos._Nada':"Nada vc",
    'Valores y Comportamientos._Poco':"Poco vc",
    'Valores y Comportamientos._Suficiente':"Suficiente vc",
    'Prosperidad Incluyente._Moderado':"Moderado pi",
    'Prosperidad Incluyente._Mucho':"Mucho pi", 
    'Prosperidad Incluyente._Nada':"Nada pi",
    'Prosperidad Incluyente._Poco':"Poco pi",
    'Prosperidad Incluyente._Suficiente':"Suficiente pi",
    'Modelo de Gestión de Alto desempeño._Moderado':"Moderado mg",
    'Modelo de Gestión de Alto desempeño._Mucho':"Mucho mg",
    'Modelo de Gestión de Alto desempeño._Nada':"Nada mg",
    'Modelo de Gestión de Alto desempeño._Poco':"Poco mg",
    'Modelo de Gestión de Alto desempeño._Suficiente':"Suficiente mg",
    'Honestel._Moderado':"Moderado h", 
    'Honestel._Mucho':"Mucho h", 
    'Honestel._Nada':"Nada h",
    'Honestel._Poco':"Poco h", 
    'Honestel._Suficiente':"Suficiente h", 
    'Ideas._Moderado':"Moderado i",
    'Ideas._Mucho':"Mucho i", 
    'Ideas._Nada':"Nada i", 
    'Ideas._Poco':"Poco i", 
    'Ideas._Suficiente':"Suficiente i",
    'Cuéntanos._Moderado':"Moderado c", 
    'Cuéntanos._Mucho':"Mucho c", 
    'Cuéntanos._Nada':"Nada c",
    'Cuéntanos._Poco':"Poco c", 
    'Cuéntanos._Suficiente':"Suficiente c",
    'Selecciona la opción por la cuál concluyes en Grupo Salinas:_Ambiente laboral.':"Ambiente laboral cgs",
    'Selecciona la opción por la cuál concluyes en Grupo Salinas:_Asunto familiar.':"Asunto familiar cgs",
    'Selecciona la opción por la cuál concluyes en Grupo Salinas:_Desacuerdos con mi Formador.':"Desacuerdos con mi Formador cgs",
    'Selecciona la opción por la cuál concluyes en Grupo Salinas:_El tiempo/costo de traslado es alto.':"El tiempo/costo de traslado es alto cgs",
    'Selecciona la opción por la cuál concluyes en Grupo Salinas:_Encontré otro empleo.':"Encontré otro empleo cgs",
    'Selecciona la opción por la cuál concluyes en Grupo Salinas:_Inicio mi propio negocio.':"Inicio mi propio negocio cgs",
    'Selecciona la opción por la cuál concluyes en Grupo Salinas:_La zona del trabajo me exponía a situaciones de peligro.':"La zona del trabajo me exponía a situaciones de peligro cgs",
    'Selecciona la opción por la cuál concluyes en Grupo Salinas:_Maternidad.':"Maternidad cgs",
    'Selecciona la opción por la cuál concluyes en Grupo Salinas:_Me cambio de residencia.':"Me cambio de residencia cgs",
    'Selecciona la opción por la cuál concluyes en Grupo Salinas:_Otro (especifique)':"Otro (especifique) cgs",
    'Selecciona la opción por la cuál concluyes en Grupo Salinas:_Puesto no coincidió con sueldo y/o prestaciones indicadas.':"Puesto no coincidió con sueldo y/o prestaciones indicadas cgs",
    'Selecciona la opción por la cuál concluyes en Grupo Salinas:_Sufrí un accidente o una enfermedad.':"Sufrí un accidente o una enfermedad cgs",
    'Selecciona la opción por la cuál concluyes en Grupo Salinas:_Voy a seguir estudiando.':"Voy a seguir estudiando cgs",
    '¿Cuánto tiempo en promedio haces de tu casa al trabajo?_De 01 hora a 02 horas':"De 01 hora a 02 horas tcs",
    '¿Cuánto tiempo en promedio haces de tu casa al trabajo?_De 30 minutos a 01 hora':"De 30 minutos a 01 hora tcs",
    '¿Cuánto tiempo en promedio haces de tu casa al trabajo?_Menos de 30 minutos':"Menos de 30 minutos tcs",
    '¿Cuánto tiempo en promedio haces de tu casa al trabajo?_Más de 02 horas':"Más de 02 horas tcs",
    '¿Cuántos medios de transporte utilizas de tu casa al trabajo?_De 1 a 2':"De 1 a 2 tcs",
    '¿Cuántos medios de transporte utilizas de tu casa al trabajo?_De 3 a 4':"De 3 a 4 tcs",
    '¿Cuántos medios de transporte utilizas de tu casa al trabajo?_Ninguno':"Ninguno tcs",
    'Robo o asalto en transporte público._0 veces':"0 veces roa",
    'Robo o asalto en transporte público._1 a 2 veces':"1 a 2 veces roa",
    'Robo o asalto en transporte público._3 a 4 veces':"3 a 4 veces roa",
    'Acoso en transporte público._0 veces':"0 veces atp",
    'Acoso en transporte público._1 a 2 veces':"1 a 2 veces atp",
    'Acoso en transporte público._3 a 4 veces':"3 a 4 veces atp",
    'Acoso en transporte público._Mas de 5 veces':"Mas de 5 veces atp",
    'Robo total o parcial de vehículo propio(automóvil, motocicleta, bicicleta, etc)._0 veces':"0 veces rtp",
    'Robo total o parcial de vehículo propio(automóvil, motocicleta, bicicleta, etc)._1 a 2 veces':"1 a 2 veces rtp",
    'Robo total o parcial de vehículo propio(automóvil, motocicleta, bicicleta, etc)._3 a 4 veces':"3 a 4 veces rtp",
    'Agresión física por personas ajenas a la organización._0 veces':"0 veces afpe",
    'Agresión física por personas ajenas a la organización._1 a 2 veces':"1 a 2 veces afpe",
    'Agresión física por personas ajenas a la organización._3 a 4 veces':"3 a 4 veces afpe",
    'Agresión física por personas ajenas a la organización._Mas de 5 veces':"Mas de 5 veces afpe",
    'Extorsión._0 veces':"0 veces e", 
    'Extorsión._1 a 2 veces':"1 a 2 veces e",
    'Extorsión._3 a 4 veces':"3 a 4 veces e", 
    'Extorsión._Mas de 5 veces':"Mas de 5 veces e",
    '¿Cómo encontraste tu nuevo empleo?_Lo busqué por iniciativa propia.':"Lo busqué por iniciativa propia ne",
    '¿Cómo encontraste tu nuevo empleo?_Me buscaron de otra empresa.':"Me buscaron de otra empresa ne",
    'Sueldo_Sueldo':"Sueldo", 
    'Prestaciones_Prestaciones':"Prestaciones",
    'Ubicación_Ubicación':"Ubicación",
    'Desarrollo profesional1_Desarrollo profesional':"Desarrollo profesional",
    'Ambiente laboral_Ambiente laboral':"Ambiente laboral", 
    'Cultura_Cultura':"Cultura",
    'Cambio de Liderazgo_Cambio de Liderazgo':"Cambio de Liderazgo",
    'Actividades de Puesto_Actividades de Puesto':"Actividades de Puesto",
    'Costos de traslado a lugar de trabajo_Costos de traslado a lugar de trabajo':"Costos de traslado a lugar de trabajo",
    'Existía un ambiente de compañerismo._Ni en desacuerdo, ni de acuerdo':"Ni en desacuerdo, ni de acuerdo eac",
    'Existía un ambiente de compañerismo._Parcialmente de acuerdo':"Parcialmente de acuerdo eac",
    'Existía un ambiente de compañerismo._Parcialmente en desacuerdo':"Parcialmente en desacuerdo eac",
    'Existía un ambiente de compañerismo._Totalmente de acuerdo':"Totalmente de acuerdo eac",
    'Existía un ambiente de compañerismo._Totalmente en desacuerdo':"Totalmente en desacuerdo eac",
    'Tus pares cumplían con los compromisos acordados._Ni en desacuerdo, ni de acuerdo':"Ni en desacuerdo, ni de acuerdo tpc",
    'Tus pares cumplían con los compromisos acordados._Parcialmente de acuerdo':"Parcialmente de acuerdo tpc",
    'Tus pares cumplían con los compromisos acordados._Parcialmente en desacuerdo':"Parcialmente en desacuerdo tpc",
    'Tus pares cumplían con los compromisos acordados._Totalmente de acuerdo':"Totalmente de acuerdo tpc",
    'Tus pares cumplían con los compromisos acordados._Totalmente en desacuerdo':"Totalmente en desacuerdo tpc",
    'Ofrecías apoyo para cumplir los objetivos._Ni en desacuerdo, ni de acuerdo':"Ni en desacuerdo, ni de acuerdo oaco",
    'Ofrecías apoyo para cumplir los objetivos._Parcialmente de acuerdo':"Parcialmente de acuerdo oaco",
    'Ofrecías apoyo para cumplir los objetivos._Parcialmente en desacuerdo':"Parcialmente en desacuerdo oaco",
    'Ofrecías apoyo para cumplir los objetivos._Totalmente de acuerdo':"Totalmente de acuerdo oaco",
    'Ofrecías apoyo para cumplir los objetivos._Totalmente en desacuerdo':"Totalmente en desacuerdo oaco",
    'Honestidad._Ni en desacuerdo, ni de acuerdo':"Ni en desacuerdo, ni de acuerdo Honestidad",
    'Honestidad._Parcialmente de acuerdo':"Parcialmente de acuerdo Honestidad",
    'Honestidad._Parcialmente en desacuerdo':"Parcialmente en desacuerdo Honestidad",
    'Honestidad._Totalmente de acuerdo':"Totalmente de acuerdo Honestidad",
    'Honestidad._Totalmente en desacuerdo':"Totalmente en desacuerd Honestidad",
    'Lealtad a la empresa._Ni en desacuerdo, ni de acuerdo':"Ni en desacuerdo, ni de acuerdo Lealtad",
    'Lealtad a la empresa._Parcialmente de acuerdo':"Parcialmente de acuerdo Lealtad",
    'Lealtad a la empresa._Parcialmente en desacuerdo':"Parcialmente en desacuerdo Lealtad",
    'Lealtad a la empresa._Totalmente de acuerdo':"Totalmente de acuerdo Lealtad",
    'Lealtad a la empresa._Totalmente en desacuerdo':"Totalmente en desacuerdo Lealtad",
    'Confianza y respeto mutuo._Ni en desacuerdo, ni de acuerdo':"Ni en desacuerdo, ni de acuerdo cyrm",
    'Confianza y respeto mutuo._Parcialmente de acuerdo':"Parcialmente de acuerdo cyrm",
    'Confianza y respeto mutuo._Parcialmente en desacuerdo':"Parcialmente en desacuerdo cyrm",
    'Confianza y respeto mutuo._Totalmente de acuerdo':"Totalmente de acuerdo cyrm",
    'Confianza y respeto mutuo._Totalmente en desacuerdo':"Totalmente en desacuerdo cyrm",
    'Pasión por el Cliente._Ni en desacuerdo, ni de acuerdo':"Ni en desacuerdo, ni de acuerdo ppc",
    'Pasión por el Cliente._Parcialmente de acuerdo':"Parcialmente de acuerdo ppc",
    'Pasión por el Cliente._Parcialmente en desacuerdo':"Parcialmente en desacuerdo ppc",
    'Pasión por el Cliente._Totalmente de acuerdo':"Totalmente de acuerdo ppc",
    'Pasión por el Cliente._Totalmente en desacuerdo':"Totalmente en desacuerdo ppc",
    'Trabajo en equipo._Ni en desacuerdo, ni de acuerdo':"Ni en desacuerdo, ni de acuerdo te",
    'Trabajo en equipo._Parcialmente de acuerdo':"Parcialmente de acuerdo te",
    'Trabajo en equipo._Parcialmente en desacuerdo':"Parcialmente en desacuerdo te",
    'Trabajo en equipo._Totalmente de acuerdo':"Totalmente de acuerdo te",
    'Trabajo en equipo._Totalmente en desacuerdo':"Totalmente en desacuerdo te",
    'Ejecución impecable._Ni en desacuerdo, ni de acuerdo':"Ni en desacuerdo, ni de acuerdo ei",
    'Ejecución impecable._Parcialmente de acuerdo':"Parcialmente de acuerdo ei",
    'Ejecución impecable._Parcialmente en desacuerdo':"Parcialmente en desacuerdo ei",
    'Ejecución impecable._Totalmente de acuerdo':"Totalmente de acuerdo ei",
    'Ejecución impecable._Totalmente en desacuerdo':"Totalmente en desacuerdo ei",
    'Mejora Continua._Ni en desacuerdo, ni de acuerdo':"Ni en desacuerdo, ni de acuerdo Mc",
    'Mejora Continua._Parcialmente de acuerdo':"Parcialmente de acuerdo Mc",
    'Mejora Continua._Parcialmente en desacuerdo':"Parcialmente en desacuerdo Mc",
    'Mejora Continua._Totalmente de acuerdo':"Totalmente de acuerdo Mc",
    'Mejora Continua._Totalmente en desacuerdo':"Totalmente en desacuerdo Mc",
    '¿Qué tan satisfecho estás con las actividades que realizaste?_Moderado':"Moderado sar",
    '¿Qué tan satisfecho estás con las actividades que realizaste?_Mucho':"Mucho sar",
    '¿Qué tan satisfecho estás con las actividades que realizaste?_Nada':"Nada sar",
    '¿Qué tan satisfecho estás con las actividades que realizaste?_Poco':"Poco sar",
    '¿Qué tan satisfecho estás con las actividades que realizaste?_Suficiente':"Suficiente sar",
    '¿Qué tan satisfecho estás con tu crecimiento profesional al colaborar en GS?_Moderado':"Moderado stp",
    '¿Qué tan satisfecho estás con tu crecimiento profesional al colaborar en GS?_Mucho':"Mucho stp",
    '¿Qué tan satisfecho estás con tu crecimiento profesional al colaborar en GS?_Nada':"Nada stp",
    '¿Qué tan satisfecho estás con tu crecimiento profesional al colaborar en GS?_Poco':"Poco stp",
    '¿Qué tan satisfecho estás con tu crecimiento profesional al colaborar en GS?_Suficiente':"Suficiente stp",
    'Tu horario laboral y descansos fueron respetados._Ni en desacuerdo, ni de acuerdo':"Ni en desacuerdo, ni de acuerdo hlyd",
    'Tu horario laboral y descansos fueron respetados._Parcialmente de acuerdo':"Parcialmente de acuerdo hlyd",
    'Tu horario laboral y descansos fueron respetados._Parcialmente en desacuerdo':"Parcialmente en desacuerdo hlyd",
    'Tu horario laboral y descansos fueron respetados._Totalmente de acuerdo':"Totalmente de acuerdo hlyd",
    'Tu horario laboral y descansos fueron respetados._Totalmente en desacuerdo':"Totalmente en desacuerdo hlyd",
    'Estás satisfecho con el balance entre tus actividades laborales y personales._Ni en desacuerdo, ni de acuerdo':"Ni en desacuerdo, ni de acuerdo balyp",
    'Estás satisfecho con el balance entre tus actividades laborales y personales._Parcialmente de acuerdo':"Parcialmente de acuerdo balyp",
    'Estás satisfecho con el balance entre tus actividades laborales y personales._Parcialmente en desacuerdo':"Parcialmente en desacuerdo balyp",
    'Estás satisfecho con el balance entre tus actividades laborales y personales._Totalmente de acuerdo':"Totalmente de acuerdo balyp",
    'Estás satisfecho con el balance entre tus actividades laborales y personales._Totalmente en desacuerdo':"Totalmente en desacuerdo balyp",
    'Información sobre sueldo y prestaciones_Información sobre sueldo y prestaciones':"Información sobre sueldo y prestaciones1",
    'Proceso de reclutamiento1_Proceso de reclutamiento':"Proceso de reclutamiento1",
    'Sesión de bienvenida1_Sesión de bienvenida':"Sesión de bienvenida1",
    'Recibimiento a tu puesto1_Recibimiento a tu puesto':"Recibimiento a tu puesto1",
    'Capacitación1_Capacitación':"Capacitación1",
    'Seguimiento a tu desempeño1_Seguimiento a tu desempeño':"Seguimiento a tu desempeño1",
    'Evaluación1_Evaluación':"Evaluación1",
    'Convivencia con compañeros1_Convivencia con compañeros':"Convivencia con compañeros1",
    'Convivencia con Formador1_Convivencia con Formador':"Convivencia con Formador1",
    'Eventos de temporada (Fiesta de fin de año, entre otros)1_Eventos de temporada (Fiesta de fin de año, entre otros)':"Eventos de temporada (Fiesta de fin de año, entre otros)1",
    'Participación en acciones sociales1_Participación en acciones sociales':"Participación en acciones sociales1",
    'Desarrollo profesional2_Desarrollo profesional':"Desarrollo profesional2",
    'Elite Azteca1_Elite Azteca':"Elite Azteca1",
    'Selecciona los tres momentos menos agradables_Información sobre sueldo y prestaciones':"Información sobre sueldo y prestaciones2",
    'Proceso de reclutamiento2_Proceso de reclutamiento':"Proceso de reclutamiento2",
    'Sesión de bienvenida2_Sesión de bienvenida':"Sesión de bienvenida2",
    'Recibimiento a tu puesto2_Recibimiento a tu puesto':"Recibimiento a tu puesto2",
    'Capacitación2_Capacitación':"Capacitación2",
    'Seguimiento a tu desempeño2_Seguimiento a tu desempeño':"Seguimiento a tu desempeño2",
    'Evaluación2_Evaluación':"Evaluación2",
    'Convivencia con compañeros2_Convivencia con compañeros':"Convivencia con compañeros2",
    'Convivencia con Formador2_Convivencia con Formador':"Convivencia con Formador2",
    'Eventos de temporada (Fiesta de fin de año, entre otros)2_Eventos de temporada (Fiesta de fin de año, entre otros)':"Eventos de temporada (Fiesta de fin de año, entre otros)2",
    'Participación en acciones sociales2_Participación en acciones sociales':"Participación en acciones sociales2",
    'Desarrollo profesional3_Desarrollo profesional':"Desarrollo profesional3",
    'Elite Azteca2_Elite Azteca':"Elite Azteca2",
    'Tu experiencia en el último puesto fue: _Buena':"Buena expup",
    'Tu experiencia en el último puesto fue: _Excelente':"Excelente expup",
    'Tu experiencia en el último puesto fue: _Mala':"Mala expup",
    'Tu experiencia en el último puesto fue: _Muy mala':"Muy mala expup",
    'Tu experiencia en el último puesto fue: _Regular':"Regular expup",
    ' ¿Qué tan probable es que recomiendes a Grupo Salinas a tus amigos o familiares?_0':"0 prgsaf",
    ' ¿Qué tan probable es que recomiendes a Grupo Salinas a tus amigos o familiares?_1':"1 prgsaf",
    ' ¿Qué tan probable es que recomiendes a Grupo Salinas a tus amigos o familiares?_2':"2 prgsaf",
    ' ¿Qué tan probable es que recomiendes a Grupo Salinas a tus amigos o familiares?_3':"3 prgsaf",
    ' ¿Qué tan probable es que recomiendes a Grupo Salinas a tus amigos o familiares?_4':"4 prgsaf",
    ' ¿Qué tan probable es que recomiendes a Grupo Salinas a tus amigos o familiares?_5':"5 prgsaf",
    ' ¿Qué tan probable es que recomiendes a Grupo Salinas a tus amigos o familiares?_6':"6 prgsaf",
    ' ¿Qué tan probable es que recomiendes a Grupo Salinas a tus amigos o familiares?_7':"7 prgsaf",
    ' ¿Qué tan probable es que recomiendes a Grupo Salinas a tus amigos o familiares?_8':"8 prgsaf",
    ' ¿Qué tan probable es que recomiendes a Grupo Salinas a tus amigos o familiares?_9':"9 prgsaf",
    ' ¿Qué tan probable es que recomiendes a Grupo Salinas a tus amigos o familiares?_10':"10 prgsaf"},inplace=True)
datacategrica.columns.str.split('_').str[-1]
datacategrica = datacategrica.rename(columns=lambda x: x.split("_")[-1])
dcomplete = pd.concat([dnumeric,datacategrica],axis=1)
first_column = dcomplete.pop('Otro1 (especifique)')
dcomplete.insert(82, 'Otro1', first_column)
first_column = dcomplete.pop('Otro2 (especifique)')
dcomplete.insert(105, 'Otro2', first_column)
first_column = dcomplete.pop('Otro3 (especifique)')
dcomplete.insert(141, 'Otro3', first_column)
first_column = dcomplete.pop('En caso de presenciar un hecho en contra de los valores o del Código de Ética favor de compartirnos el detalle.')
dcomplete.insert(156, 'En caso de presenciar un hecho en contra de los valores o del Código de Ética favor de compartirnos el detalle.', first_column)
first_column = dcomplete.pop('Otro4 (especifique)')
dcomplete.insert(224, 'Otro4', first_column)
first_column = dcomplete.pop('Otro5 (especifique)')
dcomplete.insert(237, 'Otro5', first_column)
first_column = dcomplete.pop('Si tienes algún comentario adicional, nos lo puedes compartir.')
dcomplete.insert(253, 'Si tienes algún comentario adicional, nos lo puedes compartir.', first_column)
dcomplete.drop(["Nombre completo","date created","date modified"],axis='columns', inplace=True)
dcomplete.rename(columns={"Selecciona el Territorio al que pertenecías:":"Territorio"},inplace=True)
dcomplete.Territorio.replace("na","Corporativo",inplace=True)
dcomplete.Cuartel.replace("na","Corporativo",inplace=True)
dcomplete.Region.replace("na","Corporativo",inplace=True)
dcomplete.columns = dcomplete.columns.str.replace(' ','_',)
dcomplete.columns = dcomplete.columns.str.replace('/','_',)
dcomplete.columns = dcomplete.columns.str.replace(',','_',)
dcomplete.columns = dcomplete.columns.str.replace('(','_',)
dcomplete.columns = dcomplete.columns.str.replace(')','_',)
datagraph=dcomplete.groupby(["Area","Territorio","Cuartel","Region"]).agg(Femenino=('Femenino',sum),Masculino=('Masculino',sum),
                                                                          Prefiero_no_contestar=('Prefiero_no_contestar',sum),
                                                                          _18_a_25_años=('18_a_25_años',sum),
                                                                          _26_a_30_años=('26_a_30_años',sum),
                                                                          _31_a_40_años=('31_a_40_años',sum),
                                                                          _41_a_50_años=('41_a_50_años',sum),
                                                                          _51_a_60_años=('51_a_60_años',sum),
                                                                          Casado=("Casado",sum),
                                                                          Divorciado=('Divorciado',sum),
                                                                          Soltero=('Soltero',sum),
                                                                          Unión_libre=('Unión_libre',sum),
                                                                          Viudo=('Viudo',sum),
                                                                          Directivo=('Directivo',sum),
                                                                          Formador_de_equipo=('Formador_de_equipo',sum),
                                                                          Mando_medio=('Mando_medio',sum),
                                                                          Primera_línea=('Primera_línea',sum),
                                                                          _0_a_3_meses_tgs=('0_a_3_meses_tgs',sum),
                                                                          _1_a_3_años_tgs=('1_a_3_años_tgs',sum),
                                                                          _10_a_15_años_tg=('10_a_15_años_tgs',sum),
                                                                          _15_a_20_años_tgs=('15_a_20_años_tgs',sum),
                                                                          _3_a_5_años_tgs=('3_a_5_años_tgs',sum),
                                                                          _3_a_6_meses_tgs=('3_a_6_meses_tgs',sum),
                                                                          _5_a_10_años_tgs=('5_a_10_años_tgs',sum),
                                                                          _6_a_12_meses_tgs=('6_a_12_meses_tgs',sum),
                                                                          más_de_20_años_tgs=('más_de_20_años_tgs',sum),
                                                                          _0_a_3_meses_tup=('0_a_3_meses_tup',sum),
                                                                          _1_a_3_años_tup=('1_a_3_años_tup',sum),
                                                                          _10_a_15_año_tup=('10_a_15_año_tup',sum),
                                                                          _3_a_5_años_tup=('3_a_5_años_tup',sum),
                                                                          _3_a_6_meses_tup=('3_a_6_meses_tup',sum),
                                                                          _5_a_10_añostup=('5_a_10_añostup',sum),
                                                                          _6_a_12_meses_tup=('6_a_12_meses_tup',sum),
                                                                          Moderado_vmgs=('Moderado_vmgs',sum),
                                                                          Mucho_vmgs=('Mucho_vmgs',sum),
                                                                          Nada_vmgs=('Nada_vmgs',sum),
                                                                          Poco_vmgs=('Poco_vmgs',sum),
                                                                          Suficiente_vmgs=('Suficiente_vmgs',sum),
                                                                          Moderado_vmun=('Moderado_vmun',sum),
                                                                          Mucho_vmun=('Mucho_vmun',sum),
                                                                          Nada_vmun=('Nada_vmun',sum),
                                                                          Poco_vmun=('Poco_vmun',sum),
                                                                          Suficiente_vmun=('Suficiente_vmun',sum),
                                                                          Moderado_ce=('Moderado_ce',sum),
                                                                          Mucho_ce=('Mucho_ce',sum),
                                                                          Nada_ce=('Nada_ce',sum),
                                                                          Poco_ce=('Poco_ce',sum),
                                                                          Suficiente_ce=('Suficiente_ce',sum),
                                                                          Moderado_vc=('Moderado_vc',sum),
                                                                          Mucho_vc=('Mucho_vc',sum),
                                                                          Nada_vc=('Nada_vc',sum),
                                                                          Poco_vc=('Poco_vc',sum),
                                                                          Suficiente_vc=('Suficiente_vc',sum),
                                                                          Moderado_pi=('Moderado_pi',sum),
                                                                          Mucho_pi=('Mucho_pi',sum),
                                                                          Nada_pi=('Nada_pi',sum),
                                                                          Poco_pi=('Poco_pi',sum),
                                                                          Suficiente_pi=('Suficiente_pi',sum),
                                                                          Moderado_mg=('Moderado_mg',sum),
                                                                          Mucho_mg=('Mucho_mg',sum),
                                                                          Nada_mg=('Nada_mg',sum),
                                                                          Poco_mg=('Poco_mg',sum),
                                                                          Suficiente_mg=('Suficiente_mg',sum),
                                                                          Moderado_h=('Moderado_h',sum),
                                                                          Mucho_h=('Mucho_h',sum),
                                                                          Nada_h=('Nada_h',sum),
                                                                          Poco_h=('Poco_h',sum),
                                                                          Suficiente_h=('Suficiente_h',sum),
                                                                          Otro1=('Otro1',sum),
                                                                          Moderado_i=('Moderado_i',sum),
                                                                          Mucho_i=('Mucho_i',sum),
                                                                          Nada_i=('Nada_i',sum),
                                                                          Poco_i=('Poco_i',sum),
                                                                          Suficiente_i=('Suficiente_i',sum),
                                                                          Moderado_c=('Moderado_c',sum),
                                                                          Mucho_c=('Mucho_c',sum),
                                                                          Nada_c=('Nada_c',sum),
                                                                          Poco_c=('Poco_c',sum),
                                                                          Suficiente_c=('Suficiente_c',sum),
                                                                          Ambiente_laboral_cgs=("Ambiente_laboral_cgs",sum),
                                                                          Asunto_familiar_cgs=('Asunto_familiar_cgs',sum),
                                                                          Desacuerdos_con_mi_Formador_cgs=('Desacuerdos_con_mi_Formador_cgs',sum),
                                                                          El_tiempo_costo_de_traslado_es_alto_cgs=('El_tiempo_costo_de_traslado_es_alto_cgs',sum),
                                                                          Encontré_otro_empleo_cgs=('Encontré_otro_empleo_cgs',sum),
                                                                          Inicio_mi_propio_negocio_cgs=('Inicio_mi_propio_negocio_cgs',sum),
                                                                          La_zona_del_trabajo_me_exponía_a_situaciones_de_peligro_cgs=('La_zona_del_trabajo_me_exponía_a_situaciones_de_peligro_cgs',sum),
                                                                          Maternidad_cgs=('Maternidad_cgs',sum),
                                                                          Me_cambio_de_residencia_cgs=('Me_cambio_de_residencia_cgs',sum),
                                                                          Otro_especifique_cgs=('Otro__especifique__cgs',sum),
                                                                          Puesto_no_coincidió_con_sueldo_y_o_prestaciones_indicadas_cgs=('Puesto_no_coincidió_con_sueldo_y_o_prestaciones_indicadas_cgs',sum),
                                                                          Sufrí_un_accidente_o_una_enfermedad_cgs=('Sufrí_un_accidente_o_una_enfermedad_cgs',sum),
                                                                          Voy_a_seguir_estudiando_cgs=('Voy_a_seguir_estudiando_cgs',sum),
                                                                          Otro2=('Otro2',sum),
                                                                          De_01_hora_a_02_horas_tcs=('De_01_hora_a_02_horas_tcs',sum),
                                                                          De_30_minutos_a_01_hora_tcs=('De_30_minutos_a_01_hora_tcs',sum),
                                                                          Menos_de_30_minutos_tcs=('Menos_de_30_minutos_tcs',sum),
                                                                          Más_de_02_horas_tcs=('Más_de_02_horas_tcs',sum),
                                                                          De_1_a_2_tcs=('De_1_a_2_tcs',sum),
                                                                          De_3_a_4_tcs=('De_3_a_4_tcs',sum),
                                                                          Ninguno_tcs=('Ninguno_tcs',sum),
                                                                          _0_veces_roa=('0_veces_roa',sum),
                                                                          _1_a_2_veces_roa=('1_a_2_veces_roa',sum),
                                                                          _3_a_4_veces_roa=('3_a_4_veces_roa',sum),
                                                                          _0_veces_atp=('0_veces_atp',sum),
                                                                          _1_a_2_veces_atp=('1_a_2_veces_atp',sum),
                                                                          _3_a_4_veces_atp=('3_a_4_veces_atp',sum),
                                                                          Mas_de_5_veces_atp=('Mas_de_5_veces_atp',sum),
                                                                          _0_veces_rtp=('0_veces_rtp',sum),
                                                                          _1_a_2_veces_rtp=('1_a_2_veces_rtp',sum),
                                                                          _3_a_4_veces_rtp=('3_a_4_veces_rtp',sum),
                                                                          _0_veces_afpe=('0_veces_afpe',sum),
                                                                          _1_a_2_veces_afpe=('1_a_2_veces_afpe',sum),
                                                                          _3_a_4_veces_afpe=('3_a_4_veces_afpe',sum),
                                                                          Mas_de_5_veces_afpe=('Mas_de_5_veces_afpe',sum),
                                                                          _0_veces_e=('0_veces_e',sum),
                                                                          _1_a_2_veces_e=('1_a_2_veces_e',sum),
                                                                          _3_a_4_veces_e=('3_a_4_veces_e',sum),
                                                                          Mas_de_5_veces_e=('Mas_de_5_veces_e',sum),
                                                                          Lo_busqué_por_iniciativa_propia_ne=('Lo_busqué_por_iniciativa_propia_ne',sum),
                                                                          Me_buscaron_de_otra_empresa_ne=('Me_buscaron_de_otra_empresa_ne',sum),
                                                                          Sueldo=('Sueldo',sum),
                                                                          Prestaciones=('Prestaciones',sum),
                                                                          Ubicación=('Ubicación',sum),
                                                                          Desarrollo_profesional=('Desarrollo_profesional',sum),
                                                                          Ambiente_laboral=('Ambiente_laboral',sum),
                                                                          Cultura=('Cultura',sum),
                                                                          Cambio_de_Liderazgo=('Cambio_de_Liderazgo',sum),
                                                                          Actividades_de_Puesto=('Actividades_de_Puesto',sum),
                                                                          Costos_de_traslado_a_lugar_de_trabajo=('Costos_de_traslado_a_lugar_de_trabajo',sum),
                                                                          Otro3=('Otro3',sum),
                                                                          Ni_en_desacuerdo__ni_de_acuerdo_eac=('Ni_en_desacuerdo__ni_de_acuerdo_eac',sum),
                                                                          Parcialmente_de_acuerdo_eac=('Parcialmente_de_acuerdo_eac',sum),
                                                                          Parcialmente_en_desacuerdo_eac=('Parcialmente_en_desacuerdo_eac',sum),
                                                                          Totalmente_de_acuerdo_eac=('Totalmente_de_acuerdo_eac',sum),
                                                                          Totalmente_en_desacuerdo_eac=('Totalmente_en_desacuerdo_eac',sum),
                                                                          Ni_en_desacuerdo__ni_de_acuerdo_tpc=('Ni_en_desacuerdo__ni_de_acuerdo_tpc',sum),
                                                                          Parcialmente_de_acuerdo_tpc=('Parcialmente_de_acuerdo_tpc',sum),
                                                                          Parcialmente_en_desacuerdo_tpc=('Parcialmente_en_desacuerdo_tpc',sum),
                                                                          Totalmente_de_acuerdo_tpc=('Totalmente_de_acuerdo_tpc',sum),
                                                                          Totalmente_en_desacuerdo_tpc=('Totalmente_en_desacuerdo_tpc',sum),
                                                                          Ni_en_desacuerdo__ni_de_acuerdo_oaco=('Ni_en_desacuerdo__ni_de_acuerdo_oaco',sum),
                                                                          Parcialmente_de_acuerdo_oaco=('Parcialmente_de_acuerdo_oaco',sum),
                                                                          Parcialmente_en_desacuerdo_oaco=('Parcialmente_en_desacuerdo_oaco',sum),
                                                                          Totalmente_de_acuerdo_oaco=('Totalmente_de_acuerdo_oaco',sum),
                                                                          Totalmente_en_desacuerdo_oaco=('Totalmente_en_desacuerdo_oaco',sum),
                                                                          En_caso_de_presenciar_un_hecho_en_contra_de_los_valores_o_del_Código_de_Ética_favor_de_compartirnos_el_detalle=('En_caso_de_presenciar_un_hecho_en_contra_de_los_valores_o_del_Código_de_Ética_favor_de_compartirnos_el_detalle.',sum),
                                                                          Ni_en_desacuerdo__ni_de_acuerdo_Honestidad=('Ni_en_desacuerdo__ni_de_acuerdo_Honestidad',sum),
                                                                          Parcialmente_de_acuerdo_Honestidad=('Parcialmente_de_acuerdo_Honestidad',sum),
                                                                          Parcialmente_en_desacuerdo_Honestidad=('Parcialmente_en_desacuerdo_Honestidad',sum),
                                                                          Totalmente_de_acuerdo_Honestidad=('Totalmente_de_acuerdo_Honestidad',sum),
                                                                          Totalmente_en_desacuerd_Honestidad=('Totalmente_en_desacuerd_Honestidad',sum),
                                                                          Ni_en_desacuerdo__ni_de_acuerdo_Lealtad=('Ni_en_desacuerdo__ni_de_acuerdo_Lealtad',sum),
                                                                          Parcialmente_de_acuerdo_Lealtad=('Parcialmente_de_acuerdo_Lealtad',sum),
                                                                          Parcialmente_en_desacuerdo_Lealtad=('Parcialmente_en_desacuerdo_Lealtad',sum),
                                                                          Totalmente_de_acuerdo_Lealtad=('Totalmente_de_acuerdo_Lealtad',sum),
                                                                          Totalmente_en_desacuerdo_Lealtad=('Totalmente_en_desacuerdo_Lealtad',sum),
                                                                          Ni_en_desacuerdo__ni_de_acuerdo_cyrm=('Ni_en_desacuerdo__ni_de_acuerdo_cyrm',sum),
                                                                          Parcialmente_de_acuerdo_cyrm=('Parcialmente_de_acuerdo_cyrm',sum),
                                                                          Parcialmente_en_desacuerdo_cyrm=('Parcialmente_en_desacuerdo_cyrm',sum),
                                                                          Totalmente_de_acuerdo_cyrm=('Totalmente_de_acuerdo_cyrm',sum),
                                                                          Totalmente_en_desacuerdo_cyrm=('Totalmente_en_desacuerdo_cyrm',sum),
                                                                          Ni_en_desacuerdo__ni_de_acuerdo_ppc=('Ni_en_desacuerdo__ni_de_acuerdo_ppc',sum),
                                                                          Parcialmente_de_acuerdo_ppc=('Parcialmente_de_acuerdo_ppc',sum),
                                                                          Parcialmente_en_desacuerdo_ppc=('Parcialmente_en_desacuerdo_ppc',sum),
                                                                          Totalmente_de_acuerdo_ppc=('Totalmente_de_acuerdo_ppc',sum),
                                                                          Totalmente_en_desacuerdo_ppc=('Totalmente_en_desacuerdo_ppc',sum),
                                                                          Ni_en_desacuerdo__ni_de_acuerdo_te=('Ni_en_desacuerdo__ni_de_acuerdo_te',sum),
                                                                          Parcialmente_de_acuerdo_te=('Parcialmente_de_acuerdo_te',sum),
                                                                          Parcialmente_en_desacuerdo_te=('Parcialmente_en_desacuerdo_te',sum),
                                                                          Totalmente_de_acuerdo_te=('Totalmente_de_acuerdo_te',sum),
                                                                          Totalmente_en_desacuerdo_te=('Totalmente_en_desacuerdo_te',sum),
                                                                          Ni_en_desacuerdo__ni_de_acuerdo_ei=('Ni_en_desacuerdo__ni_de_acuerdo_ei',sum),
                                                                          Parcialmente_de_acuerdo_ei=('Parcialmente_de_acuerdo_ei',sum),
                                                                          Parcialmente_en_desacuerdo_ei=('Parcialmente_en_desacuerdo_ei',sum),
                                                                          Totalmente_de_acuerdo_ei=('Totalmente_de_acuerdo_ei',sum),
                                                                          Totalmente_en_desacuerdo_ei=('Totalmente_en_desacuerdo_ei',sum),
                                                                          Ni_en_desacuerdo__ni_de_acuerdo_Mc=('Ni_en_desacuerdo__ni_de_acuerdo_Mc',sum),
                                                                          Parcialmente_de_acuerdo_Mc=('Parcialmente_de_acuerdo_Mc',sum),
                                                                          Parcialmente_en_desacuerdo_Mc=('Parcialmente_en_desacuerdo_Mc',sum),
                                                                          Totalmente_de_acuerdo_Mc=('Totalmente_de_acuerdo_Mc',sum),
                                                                          Totalmente_en_desacuerdo_Mc=('Totalmente_en_desacuerdo_Mc',sum),
                                                                          Moderado_=('Moderado_sar',sum),
                                                                          Mucho_=('Mucho_sar',sum),
                                                                          Nada_=('Nada_sar',sum),
                                                                          Poco_=('Poco_sar',sum),
                                                                          Suficiente_=('Suficiente_sar',sum),
                                                                          Moderado__=('Moderado_stp',sum),
                                                                          Mucho__=('Mucho_stp',sum),
                                                                          Nada__=('Nada_stp',sum),
                                                                          Poco__=('Poco_stp',sum),
                                                                          Suficiente__=('Suficiente_stp',sum),
                                                                          Ni_en_desacuerdo__ni_de_acuerdo_hlyd=('Ni_en_desacuerdo__ni_de_acuerdo_hlyd',sum),
                                                                          Parcialmente_de_acuerdo_hlyd=('Parcialmente_de_acuerdo_hlyd',sum),
                                                                          Parcialmente_en_desacuerdo_hlyd=('Parcialmente_en_desacuerdo_hlyd',sum),
                                                                          Totalmente_de_acuerdo_hlyd=('Totalmente_de_acuerdo_hlyd',sum),
                                                                          Totalmente_en_desacuerdo_hlyd=('Totalmente_en_desacuerdo_hlyd',sum),
                                                                          Ni_en_desacuerdo__ni_de_acuerdo_balyp=('Ni_en_desacuerdo__ni_de_acuerdo_balyp',sum),
                                                                          Parcialmente_de_acuerdo_balyp=('Parcialmente_de_acuerdo_balyp',sum),
                                                                          Parcialmente_en_desacuerdo_balyp=('Parcialmente_en_desacuerdo_balyp',sum),
                                                                          Totalmente_de_acuerdo_balyp=('Totalmente_de_acuerdo_balyp',sum),
                                                                          Totalmente_en_desacuerdo_balyp=('Totalmente_en_desacuerdo_balyp',sum),
                                                                          Información_sobre_sueldo_y_prestaciones1=('Información_sobre_sueldo_y_prestaciones1',sum),
                                                                          Proceso_de_reclutamiento1=('Proceso_de_reclutamiento1',sum),
                                                                          Sesión_de_bienvenida1=('Sesión_de_bienvenida1',sum),
                                                                          Recibimiento_a_tu_puesto1=('Recibimiento_a_tu_puesto1',sum),
                                                                          Capacitación1=('Capacitación1',sum),
                                                                          Seguimiento_a_tu_desempeño1=('Seguimiento_a_tu_desempeño1',sum),
                                                                          Evaluación1=('Evaluación1',sum),
                                                                          Convivencia_con_compañeros1=('Convivencia_con_compañeros1',sum),
                                                                          Convivencia_con_Formador1=('Convivencia_con_Formador1',sum),
                                                                          Eventos_de_temporada_Fiesta_de_fin_de_año__entre_otros=('Eventos_de_temporada__Fiesta_de_fin_de_año__entre_otros_1',sum),
                                                                          Participación_en_acciones_sociales1=('Participación_en_acciones_sociales1',sum),
                                                                          Desarrollo_profesional2=('Desarrollo_profesional2',sum),
                                                                          Elite_Azteca1=('Elite_Azteca1',sum),
                                                                          Otro4=('Otro4',sum),
                                                                          Información_sobre_sueldo_y_prestaciones2=('Información_sobre_sueldo_y_prestaciones2',sum),
                                                                          Proceso_de_reclutamiento2=('Proceso_de_reclutamiento2',sum),
                                                                          Sesión_de_bienvenida2=('Sesión_de_bienvenida2',sum),
                                                                          Recibimiento_a_tu_puesto2=('Recibimiento_a_tu_puesto2',sum),
                                                                          Capacitación2=('Capacitación2',sum),
                                                                          Seguimiento_a_tu_desempeño2=('Seguimiento_a_tu_desempeño2',sum),
                                                                          Evaluación2=('Evaluación2',sum),
                                                                          Convivencia_con_compañeros2=('Convivencia_con_compañeros2',sum),
                                                                          Convivencia_con_Formador2=('Convivencia_con_Formador2',sum),
                                                                          Eventos_de_temporada__Fiesta_de_fin_de_año__entre_otros_2=('Eventos_de_temporada__Fiesta_de_fin_de_año__entre_otros_2',sum),
                                                                          Participación_en_acciones_sociales2=('Participación_en_acciones_sociales2',sum),
                                                                          Desarrollo_profesional3=('Desarrollo_profesional3',sum),
                                                                          Elite_Azteca2=('Elite_Azteca2',sum),
                                                                          Otro5=('Otro5',sum),
                                                                          Buena_expup=('Buena_expup',sum),
                                                                          Excelente_expup=('Excelente_expup',sum),
                                                                          Mala_expup=('Mala_expup',sum),
                                                                          Muy_mala_expup=('Muy_mala_expup',sum),
                                                                          Regular_expup=('Regular_expup',sum),
                                                                          _0_prgsaf=('0_prgsaf',sum),
                                                                          _1_prgsaf=('1_prgsaf',sum),
                                                                          _2_prgsaf=('2_prgsaf',sum),
                                                                          _3_prgsaf=('3_prgsaf',sum),
                                                                          _4_prgsaf=('4_prgsaf',sum),
                                                                          _5_prgsaf=('5_prgsaf',sum),
                                                                          _6_prgsaf=('6_prgsaf',sum),
                                                                          _7_prgsaf=('7_prgsaf',sum),
                                                                          _8_prgsaf=('8_prgsaf',sum),
                                                                          _9_prgsaf=('9_prgsaf',sum),
                                                                          _10_prgsaf=('10_prgsaf',sum),
                                                                          Si_tienes_algún_comentario_adicional__nos_lo_puedes_compartir=('Si_tienes_algún_comentario_adicional__nos_lo_puedes_compartir.',sum))

datagraph.sort_index(inplace=True)
datagraph.columns = datagraph.columns.str.replace('_',' ',)
dataArea=datagraph.reset_index()
dataArea.head(10)
dcuartel=dataArea.groupby(["Cuartel"]).sum()
dterritorio=dataArea.groupby(["Territorio"]).sum()
dregion=dataArea.groupby(["Region"]).sum()
dataAreapie=dcomplete.groupby("Area").agg({"Area":"count"})
dataAreapie=dataAreapie.rename(columns={"Area":"Area","Area":"Areavalues"})
dcomplete.rename(columns=({'Número_de_empleado:':"ID"}),inplace=True)


# In[3]:


dialogus="https://www.gruposalinas.com/images/home/empresa-dialogus.png"
app = dash.Dash(__name__,)
app.title="Cobranza y Crédito"
app.layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.Img(src=dialogus,height="150px",id=dialogus),
            ],style={'width': '40%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                html.H1("Dashboard Cobranza y Crédito",
                       style = {"textAlign":"left"}
                       ),
            ],style={'width': '60%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                html.H5("Datos representativos de la encuesta de salida",
                       style = {"textAlign":"left", 
                                "fontSize":20,
                               }),
            ],style = {'width': '60%',"textAlign":"left", "fontSize":20,"margin-bottom":"0px"}),
            
        ],className="one-half column", id="title"),
        
        html.Div([
            html.Div([
                html.H6(children = "Usuarios totales",
                        style = {"textAlign":"center", 
                                 "fontSize":20,"margin-bottom":"0px",}),
                html.P(f"{dcomplete.ID.value_counts().sum():,.0f}", 
                       style = {"textAlign":"center", "fontSize":20,"margin-bottom":"0px",})
                
                
            ], className="card_container three columns")
            
        ], className="row flex display", style={'width': '100%', 'float': 'center', 'display': 'inline-block'} ),
        

        html.Div([
            dcc.Graph(id='lineplot', #Creación componente Graph 1
                    figure=px.pie(dataAreapie,values="Areavalues",names=dataAreapie.index,title="Areas encuestadas",color=dataAreapie.index,
                                  color_discrete_map={"Geografía":"#0F6040","Corporativo":"#BE3233"}))
            
        ]),
        
#####################################################Territorio
        
        html.Div([
                html.H6(children = "Seleccion de usuarios",
                        style = {"textAlign":"center", 
                                 "fontSize":20}),
            html.P('Selecciona el Territorio:', className='fix_label', style={'color': 'black'}),
            dcc.Dropdown(id = 'STerritorio',
                         multi = False,
                         searchable= True,
                         placeholder= 'Territorio',
                         options= [{'label': c, 'value': c}
                                   for c in (datagraph.index.unique("Territorio"))], className='dcc_compon'),
            
]),
#         html.Div([
#             dcc.DatePickerRange(id='selector_fecha',start_date=dcomplete['Fecha'].min(),end_date=dcomplete['Fecha'].max()) #Seleccionamos todo el rango de fechas de nuestro dataframe
            
#         ],style={'width': '40%', 'float': 'left', 'display': 'inline-block'}),
 
################################################# Graficos
        
        
            html.Div([
                dcc.Graph(id="Territorioprgsaf")
            ],style={'width': '100%', 'float': 'center', 'display': 'inline-block'}),
        

#             html.Div([
            html.H6(children = "                    Demografia",
                        style = {'width': '100%','float': 'left', 'display': 'inline-block', 
                                 "fontSize":32}),
            html.Div([
                dcc.Graph(id="Territoriogenero")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territorioedad")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territorioedocivil")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Territoriolvlpuesto")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="TerritorioExperiencia_en_su_último_puesto")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
# ],),
        
        
#             html.Div([
            html.H6(children = "                    Antigüedad",
                    style = {'width': '100%','float': 'left', 'display': 'inline-block',"fontSize":32}),         
            html.Div([
                dcc.Graph(id="Territoriotgs")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territoriotup")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
# ],),    
             
#         html.Div([
            html.H6(children = "                    Cultura",
                    style = {'width': '100%','float': 'left', 'display': 'inline-block',"fontSize":32}),  
            html.Div([
                dcc.Graph(id="Territoriomvgs")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territoriomvun")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territorioce")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Territoriovyc1")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territoriopi")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territoriomgad")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territorioh")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Territorioi")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territorioc")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
# ],),

#         html.Div([
            html.H6(children = "                    Opciones de salida",
                        style = {'width': '100%','float': 'left', 'display': 'inline-block', 
                                 "fontSize":32}),            
            html.Div([
                dcc.Graph(id="Territoriorcgs")
            ],style={'width': '100%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territoriotpct")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territoriomtu")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Territorioratp")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territorioatp")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territoriorpvp")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territorioaspao")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Territorioeua")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territoriocene")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territoriocmce")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territoriotec")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Territoriopcc")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territoriohonestidad")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territoriolealtad")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territoriocyrm")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Territorioppc")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territorioei")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territoriomc")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
# ],),
                
#         html.Div([
            html.H6(children = "                    Bienestar",
                        style = {'width': '100%','float': 'left', 'display': 'inline-block', 
                                 "fontSize":32}), 
            html.Div([
                dcc.Graph(id="Territoriosargs")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Territorioscpgs")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territoriohdr")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territorioesbalp")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
# ],),
                 
#         html.Div([
            html.H6(children = "                    Momentos de verdad",
                        style = {'width': '100%','float': 'left', 'display': 'inline-block', 
                                 "fontSize":32}),
            html.Div([
                dcc.Graph(id="Territoriomme")
            ],style={'width': '100%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Territoriommae")
            ],style={'width': '100%', 'float': 'left', 'display': 'inline-block'}),
# ],),

        html.Div([
            html.P('Seleccione Cuartel:', className='fix_label', style={'color': 'black'}),
            dcc.Dropdown(id = 'SCuartel',
                         multi = False,
                         searchable= True,
                         placeholder= 'Cuartel',
                         options= [], className='dcc_compon'),
            html.Div([
                dcc.Graph(id="Cuartelprgsaf")
            ],style={'width': '100%', 'float': 'center', 'display': 'inline-block'}),
        
#         html.Div([
#             dcc.DatePickerRange(id='fechacuartel',start_date=dcomplete['Fecha'].min(),end_date=dcomplete['Fecha'].max()) #Seleccionamos todo el rango de fechas de nuestro dataframe
            
#         ],style={'width': '40%', 'float': 'left', 'display': 'inline-block'}),            
        

        html.Div([
            html.H6(children = "   Demografia",
                    style = {'width': '100%','float': 'left', 'display': 'inline-block',"fontSize":32}),
            html.Div([
                dcc.Graph(id="Cuartelgenero")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuarteledad")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuarteledocivil")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Cuartellvlpuesto")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="CuartelExperiencia_en_su_último_puesto")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
],),
        html.Div([
            html.H6(children = "   Antigüedad",
                        style = {'width': '100%','float': 'left', 'display': 'inline-block', 
                                 "fontSize":20}),       
            html.Div([
                dcc.Graph(id="Cuarteltgs")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuarteltup")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
],),
            
        html.Div([
            html.H6(children = "   Cultura",
                    style = {'width': '100%','float': 'left', 'display': 'inline-block',"fontSize":32}),
            html.Div([
                dcc.Graph(id="Cuartelmvgs")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelmvun")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelce")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Cuartelvyc")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelpi")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelmgad")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelh")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Cuarteli")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelc")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'})
,],),           

        html.Div([
            html.H6(children = "   Opciones de salida",
                    style = {'width': '100%','float': 'left', 'display': 'inline-block',"fontSize":32}),          
            html.Div([
                dcc.Graph(id="Cuartelrcgs")
            ],style={'width': '100%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuarteltpct")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelmtu")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Cuartelratp")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelatp")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelrpvp")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelaspao")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Cuarteleua")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelcene")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelcmce")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuarteltec")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Cuartelpcc")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelhonestidad")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartellealtad")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelcyrm")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Cuartelppc")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelei")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelmc")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
],),

                
        html.Div([
            html.H6(children = "   Bienestar",
                    style = {'width': '100%','float': 'left', 'display': 'inline-block',"fontSize":32}),
            html.Div([
                dcc.Graph(id="Cuartelsargs")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Cuartelscpgs")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelhdr")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelesbalp")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),

],),                 
        html.Div([
            html.H6(children = "   Momentos de verdad",
                    style = {'width': '100%','float': 'left', 'display': 'inline-block',"fontSize":32}),
            html.Div([
                dcc.Graph(id="Cuartelmme")
            ],style={'width': '100%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Cuartelmmae")
            ],style={'width': '100%', 'float': 'left', 'display': 'inline-block'}),
],),

        html.Div([
            html.P('Select Region:', className='fix_label', style={'color': 'black'}),
            dcc.Dropdown(id = 'SRegion',
                         multi = False,
                         searchable= True,
                         placeholder= 'Region',
                         options= [], className='dcc_compon'),        
],),
#         html.Div([
#             dcc.DatePickerRange(id='fechaRegion',start_date=dcomplete['Fecha'].min(),end_date=dcomplete['Fecha'].max()) #Seleccionamos todo el rango de fechas de nuestro dataframe
            
#         ],style={'width': '40%', 'float': 'left', 'display': 'inline-block'}),      
            
        html.Div([
            dcc.Graph(id="Regionprgsaf")
        ],style={'width': '100%', 'float': 'center', 'display': 'inline-block'}),
        

        html.Div([
            html.H6(children = "   Demografia",
                        style = {'width': '100%','float': 'left', 'display': 'inline-block',"fontSize":32}), 
                                 
            html.Div([
                dcc.Graph(id="Regiongenero")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionedad")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionedocivil")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Regionlvlpuesto")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="RegionExperiencia_en_su_último_puesto")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
],),
        
        
        html.Div([
            html.H6(children = "   Antigüedad",
                       style = {'width': '100%','float': 'left', 'display': 'inline-block',"fontSize":32}),       
            html.Div([
                dcc.Graph(id="Regiontgs")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regiontup")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
],),
        
        html.Div([
            html.H6(children = "   Cultura",
                        style = {'width': '100%','float': 'left', 'display': 'inline-block',"fontSize":32}),  
            html.Div([
                dcc.Graph(id="Regionmvgs")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionmvun")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionce")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Regionvyc")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionpi")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionmgad")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionh")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Regioni")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionc")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'})
,],),


        html.Div([
            html.H6(children = "Opciones de salida",
                        style = {'width': '100%','float': 'left', 'display': 'inline-block',"fontSize":32}),           
            html.Div([
                dcc.Graph(id="Regionrcgs")
            ],style={'width': '100%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regiontpct")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionmtu")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Regionratp")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionatp")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionrpvp")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionaspao")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Regioneua")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regioncene")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regioncmce")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regiontec")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Regionpcc")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionhonestidad")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionlealtad")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regioncyrm")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Regionppc")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionei")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionmc")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
],),

                
        html.Div([
            html.H6(children = "Bienestar",
                        style = {'width': '100%','float': 'left', 'display': 'inline-block',"fontSize":32}),
            html.Div([
                dcc.Graph(id="Regionsargs")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
             html.Div([
                dcc.Graph(id="Regionscpgs")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionhdr")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionesbalp")
            ],style={'width': '33%', 'float': 'left', 'display': 'inline-block'}),

],),                 
        html.Div([
            html.H6(children = "Momentos de verdad",
                        style = {'width': '100%','float': 'left', 'display': 'inline-block',"fontSize":32}), 
            html.Div([
                dcc.Graph(id="Regionmme")
            ],style={'width': '100%', 'float': 'left', 'display': 'inline-block'}),
            html.Div([
                dcc.Graph(id="Regionmmae")
            ],style={'width': '100%', 'float': 'left', 'display': 'inline-block'}),
],),          
            
],style={'width': '100%', 'float': 'left', 'display': 'inline-block'}),
            
    ],id="header", className = "row flex-display", style = {"margin-bottom":"25px","margin-left":"50px","margin-right":"15px" })
], id = "maincontainer", style = {"display" : "flex", "flex-direction" : "column"})


################################################Graficos
@app.callback(
    Output("Territorioprgsaf", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a= round((((dterritoriosentimental[" 10 prgsaf"][0]+dterritoriosentimental[" 9 prgsaf"][0])-
        (dterritoriosentimental[" 0 prgsaf"][0]+dterritoriosentimental[" 1 prgsaf"][0] +
       dterritoriosentimental[" 2 prgsaf"][0]+dterritoriosentimental[" 3 prgsaf"][0] +
       dterritoriosentimental[" 4 prgsaf"][0]+dterritoriosentimental[" 5 prgsaf"][0] + 
       dterritoriosentimental[" 6 prgsaf"][0]))/((dterritoriosentimental[" 0 prgsaf"][0]+dterritoriosentimental[" 1 prgsaf"][0] +
       dterritoriosentimental[" 2 prgsaf"][0]+dterritoriosentimental[" 3 prgsaf"][0] +
       dterritoriosentimental[" 4 prgsaf"][0]+dterritoriosentimental[" 5 prgsaf"][0] + 
       dterritoriosentimental[" 6 prgsaf"][0])+dterritoriosentimental[" 7 prgsaf"][0]+dterritoriosentimental[" 8 prgsaf"][0] +
       dterritoriosentimental[" 9 prgsaf"][0]+dterritoriosentimental[" 10 prgsaf"][0]))*100)
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = a,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Recomendarian grupo salinas", 'font': {'size': 24}},
        delta = {'reference': 30, 'increasing': {'color': "RebeccaPurple"}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 10], 'color': 'orange'},
                {'range': [10, 30], 'color': 'green'},
                {'range': [30, 100], 'color': 'blue'}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': a}}))

    fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})
    return fig

@app.callback(
    Output("Territoriogenero", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    datagraphTerritoriopie=dterritorio.loc[[STerritorio]]
    datagraphTerritoriopie=datagraphTerritoriopie[["Femenino","Masculino","Prefiero no contestar"]]
    color_discrete_map = {'Femenino':'#BE3233',
                          'Masculino':'#0F6040', 
                          'Prefiero no contestar':'#696C71'
                          }
    figpiet=px.pie(datagraphTerritoriopie,values=datagraphTerritoriopie.iloc[0].values,names=datagraphTerritoriopie.columns,
                   color=datagraphTerritoriopie.columns,color_discrete_map=color_discrete_map,title="Genero por Territorio")
    return figpiet

@app.callback(
    Output("Territorioedad", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriographedad=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriographedad[" 18 a 25 años"], x = dterritoriographedad.index, name = "18 a 25 años", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriographedad[" 26 a 30 años"], x = dterritoriographedad.index, name = "26 a 30 años", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriographedad[" 31 a 40 años"], x =dterritoriographedad.index, name = "31 a 40 años", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriographedad[" 41 a 50 años"], x = dterritoriographedad.index, name = "41 a 50 años", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriographedad[" 51 a 60 años"], x = dterritoriographedad.index, name = "51 a 60 años", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Rango de edad de los encuestados", 
                       xaxis =dict(title="Rango de edad"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Territorioedocivil", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Casado'], x = dterritoriosentimental.index, name = "Casado", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Divorciado'], x = dterritoriosentimental.index, name = "Divorciado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Soltero'], x =dterritoriosentimental.index, name = "Soltero", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Unión libre'], x = dterritoriosentimental.index, name = "Unión libre", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Viudo'], x = dterritoriosentimental.index, name = "Viudo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Estado civil", 
                       xaxis =dict(title="Estado civil"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig


@app.callback(
    Output("Territoriolvlpuesto", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    datagraphTerritoriopie=dterritorio.loc[[STerritorio]]
    datagraphTerritoriopie=datagraphTerritoriopie[["Directivo","Formador de equipo",'Mando medio','Primera línea']]
    color_discrete_map = {'Directivo':'#696C71',
                          'Formador de equipo':'#2BA739',
                          'Mando medio':'#BE3233', 
                          'Primera línea':'#0F6040'
                          }
    figpiet=px.pie(datagraphTerritoriopie,values=datagraphTerritoriopie.iloc[0].values,names=datagraphTerritoriopie.columns,
                   color=datagraphTerritoriopie.columns,
                   color_discrete_map=color_discrete_map,title="Nivel de puestos")
    return figpiet

@app.callback(
    Output("TerritorioExperiencia_en_su_último_puesto", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Excelente expup'], x = dterritoriosentimental.index, name = "Excelente", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Buena expup'], x = dterritoriosentimental.index, name = "Buena", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Regular expup'], x = dterritoriosentimental.index, name = "Regular", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Mala expup'], x =dterritoriosentimental.index, name = "Mala", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Muy mala expup'], x = dterritoriosentimental.index, name = "Muy mala", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Experiencia en su último puesto", 
                       xaxis =dict(title="Experiencias"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
@app.callback(
    Output("Territoriotgs", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental[' 0 a 3 meses tgs'], x = dterritoriosentimental.index, name = "0 a 3 meses", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 3 a 6 meses tgs'], x =dterritoriosentimental.index, name = "3 a 6 meses", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental[' 6 a 12 meses tgs'], x = dterritoriosentimental.index, name = "6 a 12 meses", marker = {"color" : "#008040"})
    d = go.Bar(y = dterritoriosentimental[' 1 a 3 años tgs'], x = dterritoriosentimental.index, name = "1 a 3 años", marker = {"color" : "#BE3233"})
    e = go.Bar(y = dterritoriosentimental[' 3 a 5 años tgs'], x = dterritoriosentimental.index, name = "3 a 5 años", marker = {"color" : "#992828"})
    f = go.Bar(y = dterritoriosentimental[' 5 a 10 años tgs'], x = dterritoriosentimental.index, name = "5 a 10 años", marker = {"color" : "#8E001D"})
    g = go.Bar(y = dterritoriosentimental[' 10 a 15 años tg'], x =dterritoriosentimental.index, name = "10 a 15 años", marker = {"color" : "#E00245"})
    h = go.Bar(y = dterritoriosentimental[' 15 a 20 años tgs'], x = dterritoriosentimental.index, name = "15 a 20 años", marker = {"color" : "#696C71"})
    i = go.Bar(y = dterritoriosentimental['más de 20 años tgs'], x = dterritoriosentimental.index, name = "más de 20 años", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "Tiempo en GS", 
                       xaxis =dict(title="Tiempo"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e,f,g,h,i]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Territoriotup", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental[' 0 a 3 meses tup'], x = dterritoriosentimental.index, name = "0 a 3 meses", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 3 a 6 meses tup'], x =dterritoriosentimental.index, name = "3 a 6 meses", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental[' 6 a 12 meses tup'], x = dterritoriosentimental.index, name = "6 a 12 meses", marker = {"color" : "#008040"})
    d = go.Bar(y = dterritoriosentimental[' 1 a 3 años tup'], x = dterritoriosentimental.index, name = "1 a 3 años", marker = {"color" : "#BE3233"})
    e = go.Bar(y = dterritoriosentimental[' 3 a 5 años tup'], x = dterritoriosentimental.index, name = "3 a 5 años", marker = {"color" : "#992828"})
    f = go.Bar(y = dterritoriosentimental[' 5 a 10 añostup'], x = dterritoriosentimental.index, name = "5 a 10 años", marker = {"color" : "#696C71"})
    g = go.Bar(y = dterritoriosentimental[' 10 a 15 año tup'], x =dterritoriosentimental.index, name = "10 a 15 año", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "Tiempo en su último puesto", 
                       xaxis =dict(title="Tiempo"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e,f,g]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
    
@app.callback(
    Output("Territoriomvgs", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Mucho vmgs'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Suficiente vmgs'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Moderado vmgs'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco vmgs'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada vmgs'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Misión y visión en GS", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Territoriomvun", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Mucho vmun'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Suficiente vmun'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Moderado vmun'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco vmun'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada vmun'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Misión y visión de tu Unidad de negocios", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Territorioce", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Mucho ce'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado ce'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente ce'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco ce'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada ce'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Código de ética", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Territoriovyc1", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Mucho vc'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado vc'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente vc'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco vc'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada vc'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Valores y comportamiento", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Territoriopi", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Mucho pi'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado pi'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente pi'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco pi'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada pi'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Prosperidad incluyente", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Territoriomgad", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Mucho mg'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado mg'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente mg'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco mg'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada mg'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Modelo de gestión de alto desempeño", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Territorioh", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Mucho h'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado h'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente h'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco h'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada h'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Honestel", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Territorioi", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Mucho i'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado i'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente i'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco i'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada i'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Ideas", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Territorioc", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Mucho c'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado c'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente c'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco c'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada c'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Cuéntanos", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Territoriorcgs", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Ambiente laboral cgs'], x = dterritoriosentimental.index, name = "Ambiente laboral", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Asunto familiar cgs'], x = dterritoriosentimental.index, name = "Asunto familiar", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Desacuerdos con mi Formador cgs'], x =dterritoriosentimental.index, name = "Desacuerdos con mi Formador", marker = {"color" : "#008040"})
    d = go.Bar(y = dterritoriosentimental['El tiempo costo de traslado es alto cgs'], x = dterritoriosentimental.index, name = "El tiempo costo de traslado es alto", marker = {"color" : "#00D068"})
    e = go.Bar(y = dterritoriosentimental['Encontré otro empleo cgs'], x =dterritoriosentimental.index, name = "Encontré otro empleo", marker = {"color" : "#009975"})
    f = go.Bar(y = dterritoriosentimental['Inicio mi propio negocio cgs'], x = dterritoriosentimental.index, name = "Inicio mi propio negocio", marker = {"color" : "#33B28C"})
    g = go.Bar(y = dterritoriosentimental['La zona del trabajo me exponía a situaciones de peligro cgs'], x = dterritoriosentimental.index, name = "La zona del trabajo me exponía a situaciones de peligro", marker = {"color" : "#BE3233"})
    h = go.Bar(y = dterritoriosentimental['Maternidad cgs'], x = dterritoriosentimental.index, name = "Maternidad", marker = {"color" : "#992828"})
    i = go.Bar(y = dterritoriosentimental['Me cambio de residencia cgs'], x = dterritoriosentimental.index, name = "Me cambio de residencia", marker = {"color" : "#8E001D"})
    j = go.Bar(y = dterritoriosentimental['Otro especifique cgs'], x =dterritoriosentimental.index, name = "Otro", marker = {"color" : "#E00245"})
    k = go.Bar(y = dterritoriosentimental['Puesto no coincidió con sueldo y o prestaciones indicadas cgs'], x = dterritoriosentimental.index, name = "Puesto no coincidió con sueldo y/o prestaciones indicadas", marker = {"color" : "#E32020"})
    l = go.Bar(y = dterritoriosentimental['Sufrí un accidente o una enfermedad cgs'], x =dterritoriosentimental.index, name = "Sufrí un accidente o una enfermedad", marker = {"color" : "#696C71"})
    m = go.Bar(y = dterritoriosentimental['Voy a seguir estudiando cgs'], x = dterritoriosentimental.index, name = "Voy a seguir estudiando", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "Razón por la cuál concluyes en GS", 
                       xaxis =dict(title="razón"), 
                       yaxis= dict(title="cantidad"),
                       autosize=True,
#                        width="autosize",
                       height=700,) 
    data=[a,b,c,d,e,f,g,h,i,j,k,l,m]
    fig = go.Figure(data = data,layout = layout)
    return fig

@app.callback(
    Output("Territoriotpct", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Menos de 30 minutos tcs'], x =dterritoriosentimental.index, name = "Menos de 30 minutos", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['De 30 minutos a 01 hora tcs'], x = dterritoriosentimental.index, name = "De 30 minutos a 1 hora", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['De 01 hora a 02 horas tcs'], x = dterritoriosentimental.index, name = "De 1 hora a 2 horas", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Más de 02 horas tcs'], x = dterritoriosentimental.index, name = "Más de 2 horas", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Tiempo promedio de casa a Trabajo", 
                       xaxis =dict(title="Tiempo"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Territoriomtu", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['De 1 a 2 tcs'], x = dterritoriosentimental.index, name = "De 1 a 2", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['De 3 a 4 tcs'], x = dterritoriosentimental.index, name = "De 3 a 4", marker = {"color" : "#BE3233"})
    c = go.Bar(y = dterritoriosentimental['Ninguno tcs'], x =dterritoriosentimental.index, name = "Ninguno", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Medios de transporte que utilizaban", 
                       xaxis =dict(title="Medio"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Territorioratp", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental[' 0 veces roa'], x = dterritoriosentimental.index, name = "0 veces", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 1 a 2 veces roa'], x = dterritoriosentimental.index, name = "1 a 2 veces", marker = {"color" : "#BE3233"})
    c = go.Bar(y = dterritoriosentimental[' 3 a 4 veces roa'], x =dterritoriosentimental.index, name = "3 a 4 veces", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Robo o asalto en transporte público en el último año", 
                       xaxis =dict(title="Veces"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Territorioatp", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental[' 0 veces atp'], x = dterritoriosentimental.index, name = "0 veces", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 1 a 2 veces atp'], x = dterritoriosentimental.index, name = "1 a 2 veces", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental[' 3 a 4 veces atp'], x =dterritoriosentimental.index, name = "3 a 4 veces", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Mas de 5 veces atp'], x =dterritoriosentimental.index, name = "Mas de 5", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Acoso en transporte público en el último año", 
                       xaxis =dict(title="Veces"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Territoriorpvp", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental[' 0 veces rtp'], x = dterritoriosentimental.index, name = "0 veces", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 1 a 2 veces rtp'], x = dterritoriosentimental.index, name = "1 a 2 veces", marker = {"color" : "#BE3233"})
    c = go.Bar(y = dterritoriosentimental[' 3 a 4 veces rtp'], x =dterritoriosentimental.index, name = "3 a 4 veces", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Robo total o parcial del vehículo propio en el último año", 
                       xaxis =dict(title="Veces"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c]
    fig = go.Figure(data = data, layout = layout)
    return fig


@app.callback(
    Output("Territorioaspao", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental[' 0 veces afpe'], x = dterritoriosentimental.index, name = "0 veces", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 1 a 2 veces afpe'], x = dterritoriosentimental.index, name = "1 a 2 veces", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental[' 3 a 4 veces afpe'], x =dterritoriosentimental.index, name = "3 a 4 veces", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Mas de 5 veces afpe'], x =dterritoriosentimental.index, name = "Mas de 5 veces", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Agresión física por personas ajenas a la organización", 
                       xaxis =dict(title="Veces"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Territorioeua", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental[' 0 veces e'], x = dterritoriosentimental.index, name = "0 veces", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 1 a 2 veces e'], x = dterritoriosentimental.index, name = "1 a 2 veces", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental[' 3 a 4 veces e'], x =dterritoriosentimental.index, name = "3 a 4 veces", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Mas de 5 veces e'], x =dterritoriosentimental.index, name = "Más de 5 veces", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Extorsión en el último año", 
                       xaxis =dict(title="Veces"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Territoriocene", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Lo busqué por iniciativa propia ne'], x = dterritoriosentimental.index, name = "Lo busqué por iniciativa propia", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Me buscaron de otra empresa ne'], x = dterritoriosentimental.index, name = "Me buscaron de otra empresa", marker = {"color" : "#BE3233"})
    layout = go.Layout(title = "Cómo encontraron su nuevo empleo", 
                       xaxis =dict(title="opciones"), 
                       yaxis= dict(title="Cantidas")) 
    data=[a,b]
    fig = go.Figure(data = data,layout = layout)
    return fig 
    
@app.callback(
    Output("Territoriocmce", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    c = go.Bar(y = dterritoriosentimental['Sueldo'], x =dterritoriosentimental.index, name = "Sueldo", marker = {"color" : "#0F6040"})
    d = go.Bar(y = dterritoriosentimental['Prestaciones'], x = dterritoriosentimental.index, name = "Prestaciones", marker = {"color" : "#2BA739"})
    e = go.Bar(y = dterritoriosentimental['Ubicación'], x =dterritoriosentimental.index, name = "Ubicación", marker = {"color" : "#008040"})
    f = go.Bar(y = dterritoriosentimental['Desarrollo profesional'], x = dterritoriosentimental.index, name = "Desarrollo profesional", marker = {"color" : "#00D068"})
    g = go.Bar(y = dterritoriosentimental['Ambiente laboral'], x = dterritoriosentimental.index, name = "Ambiente laboral", marker = {"color" : "#BE3233"})
    h = go.Bar(y = dterritoriosentimental['Cultura'], x = dterritoriosentimental.index, name = "Cultura", marker = {"color" : "#992828"})
    i = go.Bar(y = dterritoriosentimental['Cambio de Liderazgo'], x = dterritoriosentimental.index, name = "Cambio de Liderazgo", marker = {"color" : "#8E001D"})
    j = go.Bar(y = dterritoriosentimental['Actividades de Puesto'], x =dterritoriosentimental.index, name = "Actividades de Puesto", marker = {"color" : "#E00245"})
    k = go.Bar(y = dterritoriosentimental['Costos de traslado a lugar de trabajo'], x = dterritoriosentimental.index, name = "Costos de traslado a lugar de trabajo", marker = {"color" : "#696C71"})
    l = go.Bar(y = dterritoriosentimental['Otro3'], x =dterritoriosentimental.index, name = "Otro", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "Características  que mejoraron para el cambio del empleo", 
                       xaxis =dict(title="Carcaterísticas"), 
                       yaxis= dict(title="Cantidas")) 
    data=[c,d,e,f,g,h,i,j,k,l]
    fig = go.Figure(data = data,layout = layout)
    return fig
    
@app.callback(
    Output("Territoriotec", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo eac'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo eac'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo eac'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo eac'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo eac'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "En su equipo de trabajo existía compañerismo", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Territoriopcc", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo tpc'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo tpc'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo tpc'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo tpc'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo tpc'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "En su equipo de trabajo los pares cumplian con sus compromisos", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Territoriohonestidad", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo oaco'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo oaco'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo oaco'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo oaco'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo oaco'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Honestidad", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Territoriolealtad", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo Lealtad'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo Lealtad'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo Lealtad'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo Lealtad'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo Lealtad'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Lealtad", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Territoriocyrm", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo cyrm'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo cyrm'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo cyrm'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo cyrm'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo cyrm'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Confianza y respeto mutuo", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    

@app.callback(
    Output("Territorioppc", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo ppc'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo ppc'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo ppc'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo ppc'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo ppc'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Pasión por el cliente", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
@app.callback(
    Output("Territorioei", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo ei'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo ei'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo ei'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo ei'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo ei'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Ejecución impecable", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
@app.callback(
    Output("Territoriomc", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo Mc'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo Mc'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo Mc'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo Mc'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo Mc'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Mejora continua", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
@app.callback(
    Output("Territoriosargs", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    datagraphTerritoriopie=dterritorio.loc[[STerritorio]]
    datagraphTerritoriopie=datagraphTerritoriopie[['Mucho ','Suficiente ','Moderado ','Poco ','Nada ']]
    color_discrete_map = {'Mucho ':'#0F6040',
                          'Suficiente ':'#2BA739',
                          'Moderado ':'#BE3233', 
                          'Poco ':'#992828',
                          'Nada ':'#696C71'
                          }
    figpiet=px.pie(datagraphTerritoriopie,values=datagraphTerritoriopie.iloc[0].values,names=datagraphTerritoriopie.columns,
                   color=datagraphTerritoriopie.columns,
                   color_discrete_map=color_discrete_map,title="Satisfacción con actividades realizadas en GS")
    return figpiet
    
    
    
@app.callback(
    Output("Territorioscpgs", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    datagraphTerritoriopie=dterritorio.loc[[STerritorio]]
    datagraphTerritoriopie=datagraphTerritoriopie[['Mucho  ','Suficiente  ','Moderado  ','Poco  ','Nada  ']]
    color_discrete_map = {'Mucho  ':'#0F6040',
                          'Suficiente  ':'#2BA739',
                          'Moderado  ':'#BE3233', 
                          'Poco  ':'#992828',
                          'Nada  ':'#696C71'
                          }
    figpiet=px.pie(datagraphTerritoriopie,values=datagraphTerritoriopie.iloc[0].values,names=datagraphTerritoriopie.columns,
                   color=datagraphTerritoriopie.columns,
                   color_discrete_map=color_discrete_map,title="Satisfacción con crecimiento profesional en GS",)
    return figpiet
    
    
@app.callback(
    Output("Territoriohdr", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo hlyd'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo hlyd'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo hlyd'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo hlyd'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo hlyd'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Su horario laboral y descansos fueron respetados", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
    
@app.callback(
    Output("Territorioesbalp", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo balyp'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo balyp'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo balyp'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo balyp'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo balyp'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Está satisfecho con el balance entre tus actividades laborales y personales.", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
    
@app.callback(
    Output("Territoriomme", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Información sobre sueldo y prestaciones1'], x = dterritoriosentimental.index, name = "Información sobre sueldo y prestaciones", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Proceso de reclutamiento1'], x = dterritoriosentimental.index, name = "Proceso de reclutamiento", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Sesión de bienvenida1'], x =dterritoriosentimental.index, name = "Sesión de bienvenida", marker = {"color" : "#008040"})
    d = go.Bar(y = dterritoriosentimental['Recibimiento a tu puesto1'], x = dterritoriosentimental.index, name = "Recibimiento a tu puesto", marker = {"color" : "#00D068"})
    e = go.Bar(y = dterritoriosentimental['Capacitación1'], x =dterritoriosentimental.index, name = "Capacitación", marker = {"color" : "#006B68"})
    f = go.Bar(y = dterritoriosentimental['Seguimiento a tu desempeño1'], x = dterritoriosentimental.index, name = "Seguimiento a tu desempeño", marker = {"color" : "#009975"})
    g = go.Bar(y = dterritoriosentimental['Evaluación1'], x = dterritoriosentimental.index, name = "Evaluación", marker = {"color" : "#33B28C"})
    h = go.Bar(y = dterritoriosentimental['Convivencia con compañeros1'], x = dterritoriosentimental.index, name = "Convivencia con compañeros", marker = {"color" : "#BE3233"})
    i = go.Bar(y = dterritoriosentimental['Convivencia con Formador1'], x = dterritoriosentimental.index, name = "Convivencia con Formador", marker = {"color" : "#992828"})
    j = go.Bar(y = dterritoriosentimental['Eventos de temporada Fiesta de fin de año  entre otros'], x =dterritoriosentimental.index, name = "Eventos de temporada/Fiesta de fin de año entre otros", marker = {"color" : "#8E001D"})
    k = go.Bar(y = dterritoriosentimental['Participación en acciones sociales1'], x = dterritoriosentimental.index, name = "Participación en acciones sociales", marker = {"color" : "#E00245"})
    l = go.Bar(y = dterritoriosentimental['Desarrollo profesional2'], x =dterritoriosentimental.index, name = "Desarrollo profesional", marker = {"color" : "#E32020"})
    m = go.Bar(y = dterritoriosentimental['Elite Azteca1'], x = dterritoriosentimental.index, name = "Elite Azteca", marker = {"color" : "#696C71"})
    n = go.Bar(y = dterritoriosentimental['Otro4'], x = dterritoriosentimental.index, name = "Otro", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "3 mejores momentos en su estancia", 
                       xaxis =dict(title="Momentos"), 
                       autosize=True,
#                        width="autosize",
                       height=700,) 
    data=[a,b,c,d,e,f,g,h,i,j,k,l,m,n]
    fig = go.Figure(data = data,layout = layout)
    return fig
    
    
    
@app.callback(
    Output("Territoriommae", "figure"),
    [Input("STerritorio","value")]
)
def actualizar(STerritorio):
    dterritoriosentimental=dterritorio.loc[[STerritorio]]
    a = go.Bar(y = dterritoriosentimental['Información sobre sueldo y prestaciones2'], x = dterritoriosentimental.index, name = "Información sobre sueldo y prestaciones", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Proceso de reclutamiento2'], x = dterritoriosentimental.index, name = "Proceso de reclutamiento", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Sesión de bienvenida2'], x =dterritoriosentimental.index, name = "Sesión de bienvenida", marker = {"color" : "#008040"})
    d = go.Bar(y = dterritoriosentimental['Recibimiento a tu puesto2'], x = dterritoriosentimental.index, name = "Recibimiento a tu puesto", marker = {"color" : "#00D068"})
    e = go.Bar(y = dterritoriosentimental['Capacitación2'], x =dterritoriosentimental.index, name = "Capacitación", marker = {"color" : "#006B68"})
    f = go.Bar(y = dterritoriosentimental['Seguimiento a tu desempeño2'], x = dterritoriosentimental.index, name = "Seguimiento a tu desempeño", marker = {"color" : "#009975"})
    g = go.Bar(y = dterritoriosentimental['Evaluación2'], x = dterritoriosentimental.index, name = "Evaluación", marker = {"color" : "#33B28C"})
    h = go.Bar(y = dterritoriosentimental['Convivencia con compañeros2'], x = dterritoriosentimental.index, name = "Convivencia con compañeros", marker = {"color" : "#BE3233"})
    i = go.Bar(y = dterritoriosentimental['Convivencia con Formador2'], x = dterritoriosentimental.index, name = "Convivencia con Formador", marker = {"color" : "#992828"})
    j = go.Bar(y = dterritoriosentimental['Eventos de temporada  Fiesta de fin de año  entre otros 2'], x =dterritoriosentimental.index, name = "Eventos de temporada/Fiesta de fin de año entre otros", marker = {"color" : "#8E001D"})
    k = go.Bar(y = dterritoriosentimental['Participación en acciones sociales2'], x = dterritoriosentimental.index, name = "Participación en acciones sociales", marker = {"color" : "#E00245"})
    l = go.Bar(y = dterritoriosentimental['Desarrollo profesional2'], x =dterritoriosentimental.index, name = "Desarrollo profesional", marker = {"color" : "#E32020"})
    m = go.Bar(y = dterritoriosentimental['Elite Azteca2'], x = dterritoriosentimental.index, name = "Elite Azteca", marker = {"color" : "#696C71"})
    n = go.Bar(y = dterritoriosentimental['Otro5'], x = dterritoriosentimental.index, name = "Otro5", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "3 Momentos menos agradables en su estancia", 
                       xaxis =dict(title="Momentos"), 
                       yaxis= dict(title="Cantidad"),
                       autosize=True,
#                        width="autosize",
                       height=700,) 
    data=[a,b,c,d,e,f,g,h,i,j,k,l,m,n]
    fig = go.Figure(data = data,layout = layout)
    return fig
####################################################### Cuartel

@app.callback(
    Output("SCuartel", "options"),
    [Input("STerritorio","value")]
)
def actualizarcuartel(STerritorio):
    UPSRegionUPD=dataArea[dataArea["Territorio"]==STerritorio]
    return [{"label": i, "value": i} for i in UPSRegionUPD["Cuartel"].unique()]

@app.callback(
    Output("Cuartelprgsaf", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a= round((((dterritoriosentimental[" 10 prgsaf"][0]+dterritoriosentimental[" 9 prgsaf"][0])-
        (dterritoriosentimental[" 0 prgsaf"][0]+dterritoriosentimental[" 1 prgsaf"][0] +
       dterritoriosentimental[" 2 prgsaf"][0]+dterritoriosentimental[" 3 prgsaf"][0] +
       dterritoriosentimental[" 4 prgsaf"][0]+dterritoriosentimental[" 5 prgsaf"][0] + 
       dterritoriosentimental[" 6 prgsaf"][0]))/((dterritoriosentimental[" 0 prgsaf"][0]+dterritoriosentimental[" 1 prgsaf"][0] +
       dterritoriosentimental[" 2 prgsaf"][0]+dterritoriosentimental[" 3 prgsaf"][0] +
       dterritoriosentimental[" 4 prgsaf"][0]+dterritoriosentimental[" 5 prgsaf"][0] + 
       dterritoriosentimental[" 6 prgsaf"][0])+dterritoriosentimental[" 7 prgsaf"][0]+dterritoriosentimental[" 8 prgsaf"][0] +
       dterritoriosentimental[" 9 prgsaf"][0]+dterritoriosentimental[" 10 prgsaf"][0]))*100)
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = a,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Recomendarian grupo salinas", 'font': {'size': 24}},
        delta = {'reference': 30, 'increasing': {'color': "RebeccaPurple"}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 10], 'color': 'orange'},
                {'range': [10, 30], 'color': 'green'},
                {'range': [30, 100], 'color': 'blue'}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': a}}))

    fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})
    return fig
@app.callback(
    Output("Cuartelgenero", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    datagraphTerritoriopie=dcuartel.loc[[SCuartel]]
    datagraphTerritoriopie=datagraphTerritoriopie[["Femenino","Masculino","Prefiero no contestar"]]
    color_discrete_map = {'Femenino':'#BE3233',
                          'Masculino':'#0F6040', 
                          'Prefiero no contestar':'#696C71'
                          }
    figpiet=px.pie(datagraphTerritoriopie,values=datagraphTerritoriopie.iloc[0].values,names=datagraphTerritoriopie.columns,
                   color=datagraphTerritoriopie.columns,color_discrete_map=color_discrete_map,title="Genero por Territorio")
    return figpiet

@app.callback(
    Output("Cuarteledad", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriographedad=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriographedad[" 18 a 25 años"], x = dterritoriographedad.index, name = "18 a 25 años", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriographedad[" 26 a 30 años"], x = dterritoriographedad.index, name = "26 a 30 años", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriographedad[" 31 a 40 años"], x =dterritoriographedad.index, name = "31 a 40 años", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriographedad[" 41 a 50 años"], x = dterritoriographedad.index, name = "41 a 50 años", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriographedad[" 51 a 60 años"], x = dterritoriographedad.index, name = "51 a 60 años", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Rango de edad de los encuestados", 
                       xaxis =dict(title="Rango de edad"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Cuarteledocivil", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Casado'], x = dterritoriosentimental.index, name = "Casado", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Divorciado'], x = dterritoriosentimental.index, name = "Divorciado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Soltero'], x =dterritoriosentimental.index, name = "Soltero", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Unión libre'], x = dterritoriosentimental.index, name = "Unión libre", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Viudo'], x = dterritoriosentimental.index, name = "Viudo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Estado civil", 
                       xaxis =dict(title="Estado civil"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig


@app.callback(
    Output("Cuartellvlpuesto", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    datagraphTerritoriopie=dcuartel.loc[[SCuartel]]
    datagraphTerritoriopie=datagraphTerritoriopie[["Directivo","Formador de equipo",'Mando medio','Primera línea']]
    color_discrete_map = {'Directivo':'#696C71',
                          'Formador de equipo':'#2BA739',
                          'Mando medio':'#BE3233', 
                          'Primera línea':'#0F6040'
                          }
    figpiet=px.pie(datagraphTerritoriopie,values=datagraphTerritoriopie.iloc[0].values,names=datagraphTerritoriopie.columns,
                   color=datagraphTerritoriopie.columns,
                   color_discrete_map=color_discrete_map,title="Nivel de puestos")
    return figpiet

@app.callback(
    Output("CuartelExperiencia_en_su_último_puesto", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Excelente expup'], x = dterritoriosentimental.index, name = "Excelente", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Buena expup'], x = dterritoriosentimental.index, name = "Buena", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Regular expup'], x = dterritoriosentimental.index, name = "Regular", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Mala expup'], x =dterritoriosentimental.index, name = "Mala", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Muy mala expup'], x = dterritoriosentimental.index, name = "Muy mala", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Experiencia en su último puesto", 
                       xaxis =dict(title="Experiencias"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
@app.callback(
    Output("Cuarteltgs", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental[' 0 a 3 meses tgs'], x = dterritoriosentimental.index, name = "0 a 3 meses", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 3 a 6 meses tgs'], x =dterritoriosentimental.index, name = "3 a 6 meses", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental[' 6 a 12 meses tgs'], x = dterritoriosentimental.index, name = "6 a 12 meses", marker = {"color" : "#008040"})
    d = go.Bar(y = dterritoriosentimental[' 1 a 3 años tgs'], x = dterritoriosentimental.index, name = "1 a 3 años", marker = {"color" : "#BE3233"})
    e = go.Bar(y = dterritoriosentimental[' 3 a 5 años tgs'], x = dterritoriosentimental.index, name = "3 a 5 años", marker = {"color" : "#992828"})
    f = go.Bar(y = dterritoriosentimental[' 5 a 10 años tgs'], x = dterritoriosentimental.index, name = "5 a 10 años", marker = {"color" : "#8E001D"})
    g = go.Bar(y = dterritoriosentimental[' 10 a 15 años tg'], x =dterritoriosentimental.index, name = "10 a 15 años", marker = {"color" : "#E00245"})
    h = go.Bar(y = dterritoriosentimental[' 15 a 20 años tgs'], x = dterritoriosentimental.index, name = "15 a 20 años", marker = {"color" : "#696C71"})
    i = go.Bar(y = dterritoriosentimental['más de 20 años tgs'], x = dterritoriosentimental.index, name = "más de 20 años", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "Tiempo en GS", 
                       xaxis =dict(title="Tiempo"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e,f,g,h,i]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Cuarteltup", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental[' 0 a 3 meses tup'], x = dterritoriosentimental.index, name = "0 a 3 meses", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 3 a 6 meses tup'], x =dterritoriosentimental.index, name = "3 a 6 meses", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental[' 6 a 12 meses tup'], x = dterritoriosentimental.index, name = "6 a 12 meses", marker = {"color" : "#008040"})
    d = go.Bar(y = dterritoriosentimental[' 1 a 3 años tup'], x = dterritoriosentimental.index, name = "1 a 3 años", marker = {"color" : "#BE3233"})
    e = go.Bar(y = dterritoriosentimental[' 3 a 5 años tup'], x = dterritoriosentimental.index, name = "3 a 5 años", marker = {"color" : "#992828"})
    f = go.Bar(y = dterritoriosentimental[' 5 a 10 añostup'], x = dterritoriosentimental.index, name = "5 a 10 años", marker = {"color" : "#696C71"})
    g = go.Bar(y = dterritoriosentimental[' 10 a 15 año tup'], x =dterritoriosentimental.index, name = "10 a 15 año", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "Tiempo en su último puesto", 
                       xaxis =dict(title="Tiempo"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e,f,g]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
    
@app.callback(
    Output("Cuartelmvgs", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Mucho vmgs'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Suficiente vmgs'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Moderado vmgs'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco vmgs'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada vmgs'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Misión y visión en GS", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Cuartelmvun", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Mucho vmun'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Suficiente vmun'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Moderado vmun'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco vmun'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada vmun'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Misión y visión de tu Unidad de negocios", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Cuartelce", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Mucho ce'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado ce'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente ce'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco ce'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada ce'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Código de ética", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Cuartelvyc", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Mucho vc'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado vc'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente vc'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco vc'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada vc'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Valores y comportamiento", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Cuartelpi", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Mucho pi'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado pi'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente pi'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco pi'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada pi'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Prosperidad incluyente", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Cuartelmgad", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Mucho mg'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado mg'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente mg'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco mg'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada mg'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Modelo de gestión de alto desempeño", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Cuartelh", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Mucho h'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado h'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente h'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco h'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada h'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Honestel", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Cuarteli", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Mucho i'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado i'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente i'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco i'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada i'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Ideas", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Cuartelc", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Mucho c'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado c'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente c'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco c'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada c'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Cuéntanos", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Cuartelrcgs", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Ambiente laboral cgs'], x = dterritoriosentimental.index, name = "Ambiente laboral", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Asunto familiar cgs'], x = dterritoriosentimental.index, name = "Asunto familiar", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Desacuerdos con mi Formador cgs'], x =dterritoriosentimental.index, name = "Desacuerdos con mi Formador", marker = {"color" : "#008040"})
    d = go.Bar(y = dterritoriosentimental['El tiempo costo de traslado es alto cgs'], x = dterritoriosentimental.index, name = "El tiempo costo de traslado es alto", marker = {"color" : "#00D068"})
    e = go.Bar(y = dterritoriosentimental['Encontré otro empleo cgs'], x =dterritoriosentimental.index, name = "Encontré otro empleo", marker = {"color" : "#009975"})
    f = go.Bar(y = dterritoriosentimental['Inicio mi propio negocio cgs'], x = dterritoriosentimental.index, name = "Inicio mi propio negocio", marker = {"color" : "#33B28C"})
    g = go.Bar(y = dterritoriosentimental['La zona del trabajo me exponía a situaciones de peligro cgs'], x = dterritoriosentimental.index, name = "La zona del trabajo me exponía a situaciones de peligro", marker = {"color" : "#BE3233"})
    h = go.Bar(y = dterritoriosentimental['Maternidad cgs'], x = dterritoriosentimental.index, name = "Maternidad", marker = {"color" : "#992828"})
    i = go.Bar(y = dterritoriosentimental['Me cambio de residencia cgs'], x = dterritoriosentimental.index, name = "Me cambio de residencia", marker = {"color" : "#8E001D"})
    j = go.Bar(y = dterritoriosentimental['Otro especifique cgs'], x =dterritoriosentimental.index, name = "Otro", marker = {"color" : "#E00245"})
    k = go.Bar(y = dterritoriosentimental['Puesto no coincidió con sueldo y o prestaciones indicadas cgs'], x = dterritoriosentimental.index, name = "Puesto no coincidió con sueldo y/o prestaciones indicadas", marker = {"color" : "#E32020"})
    l = go.Bar(y = dterritoriosentimental['Sufrí un accidente o una enfermedad cgs'], x =dterritoriosentimental.index, name = "Sufrí un accidente o una enfermedad", marker = {"color" : "#696C71"})
    m = go.Bar(y = dterritoriosentimental['Voy a seguir estudiando cgs'], x = dterritoriosentimental.index, name = "Voy a seguir estudiando", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "Razón por la cuál concluyes en GS", 
                       xaxis =dict(title="razón"), 
                       yaxis= dict(title="cantidad"),
                       autosize=True,
#                        width="autosize",
                       height=700,) 
    data=[a,b,c,d,e,f,g,h,i,j,k,l,m]
    fig = go.Figure(data = data,layout = layout)
    return fig

@app.callback(
    Output("Cuarteltpct", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Menos de 30 minutos tcs'], x =dterritoriosentimental.index, name = "Menos de 30 minutos", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['De 30 minutos a 01 hora tcs'], x = dterritoriosentimental.index, name = "De 30 minutos a 1 hora", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['De 01 hora a 02 horas tcs'], x = dterritoriosentimental.index, name = "De 1 hora a 2 horas", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Más de 02 horas tcs'], x = dterritoriosentimental.index, name = "Más de 2 horas", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Tiempo promedio de casa a Trabajo", 
                       xaxis =dict(title="Tiempo"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Cuartelmtu", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['De 1 a 2 tcs'], x = dterritoriosentimental.index, name = "De 1 a 2", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['De 3 a 4 tcs'], x = dterritoriosentimental.index, name = "De 3 a 4", marker = {"color" : "#BE3233"})
    c = go.Bar(y = dterritoriosentimental['Ninguno tcs'], x =dterritoriosentimental.index, name = "Ninguno", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Medios de transporte que utilizaban", 
                       xaxis =dict(title="Medio"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Cuartelratp", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental[' 0 veces roa'], x = dterritoriosentimental.index, name = "0 veces", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 1 a 2 veces roa'], x = dterritoriosentimental.index, name = "1 a 2 veces", marker = {"color" : "#BE3233"})
    c = go.Bar(y = dterritoriosentimental[' 3 a 4 veces roa'], x =dterritoriosentimental.index, name = "3 a 4 veces", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Robo o asalto en transporte público en el último año", 
                       xaxis =dict(title="Veces"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Cuartelatp", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental[' 0 veces atp'], x = dterritoriosentimental.index, name = "0 veces", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 1 a 2 veces atp'], x = dterritoriosentimental.index, name = "1 a 2 veces", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental[' 3 a 4 veces atp'], x =dterritoriosentimental.index, name = "3 a 4 veces", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Mas de 5 veces atp'], x =dterritoriosentimental.index, name = "Mas de 5", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Acoso en transporte público en el último año", 
                       xaxis =dict(title="Veces"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Cuartelrpvp", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental[' 0 veces rtp'], x = dterritoriosentimental.index, name = "0 veces", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 1 a 2 veces rtp'], x = dterritoriosentimental.index, name = "1 a 2 veces", marker = {"color" : "#BE3233"})
    c = go.Bar(y = dterritoriosentimental[' 3 a 4 veces rtp'], x =dterritoriosentimental.index, name = "3 a 4 veces", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Robo total o parcial del vehículo propio en el último año", 
                       xaxis =dict(title="Veces"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c]
    fig = go.Figure(data = data, layout = layout)
    return fig


@app.callback(
    Output("Cuartelaspao", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental[' 0 veces afpe'], x = dterritoriosentimental.index, name = "0 veces", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 1 a 2 veces afpe'], x = dterritoriosentimental.index, name = "1 a 2 veces", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental[' 3 a 4 veces afpe'], x =dterritoriosentimental.index, name = "3 a 4 veces", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Mas de 5 veces afpe'], x =dterritoriosentimental.index, name = "Mas de 5 veces", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Agresión física por personas ajenas a la organización", 
                       xaxis =dict(title="Veces"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Cuarteleua", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental[' 0 veces e'], x = dterritoriosentimental.index, name = "0 veces", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 1 a 2 veces e'], x = dterritoriosentimental.index, name = "1 a 2 veces", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental[' 3 a 4 veces e'], x =dterritoriosentimental.index, name = "3 a 4 veces", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Mas de 5 veces e'], x =dterritoriosentimental.index, name = "Más de 5 veces", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Extorsión en el último año", 
                       xaxis =dict(title="Veces"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Cuartelcene", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Lo busqué por iniciativa propia ne'], x = dterritoriosentimental.index, name = "Lo busqué por iniciativa propia", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Me buscaron de otra empresa ne'], x = dterritoriosentimental.index, name = "Me buscaron de otra empresa", marker = {"color" : "#BE3233"})
    layout = go.Layout(title = "Cómo encontraron su nuevo empleo", 
                       xaxis =dict(title="opciones"), 
                       yaxis= dict(title="Cantidas")) 
    data=[a,b]
    fig = go.Figure(data = data,layout = layout)
    return fig 
    
@app.callback(
    Output("Cuartelcmce", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    c = go.Bar(y = dterritoriosentimental['Sueldo'], x =dterritoriosentimental.index, name = "Sueldo", marker = {"color" : "#0F6040"})
    d = go.Bar(y = dterritoriosentimental['Prestaciones'], x = dterritoriosentimental.index, name = "Prestaciones", marker = {"color" : "#2BA739"})
    e = go.Bar(y = dterritoriosentimental['Ubicación'], x =dterritoriosentimental.index, name = "Ubicación", marker = {"color" : "#008040"})
    f = go.Bar(y = dterritoriosentimental['Desarrollo profesional'], x = dterritoriosentimental.index, name = "Desarrollo profesional", marker = {"color" : "#00D068"})
    g = go.Bar(y = dterritoriosentimental['Ambiente laboral'], x = dterritoriosentimental.index, name = "Ambiente laboral", marker = {"color" : "#BE3233"})
    h = go.Bar(y = dterritoriosentimental['Cultura'], x = dterritoriosentimental.index, name = "Cultura", marker = {"color" : "#992828"})
    i = go.Bar(y = dterritoriosentimental['Cambio de Liderazgo'], x = dterritoriosentimental.index, name = "Cambio de Liderazgo", marker = {"color" : "#8E001D"})
    j = go.Bar(y = dterritoriosentimental['Actividades de Puesto'], x =dterritoriosentimental.index, name = "Actividades de Puesto", marker = {"color" : "#E00245"})
    k = go.Bar(y = dterritoriosentimental['Costos de traslado a lugar de trabajo'], x = dterritoriosentimental.index, name = "Costos de traslado a lugar de trabajo", marker = {"color" : "#696C71"})
    l = go.Bar(y = dterritoriosentimental['Otro3'], x =dterritoriosentimental.index, name = "Otro", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "Características  que mejoraron para el cambio del empleo", 
                       xaxis =dict(title="Carcaterísticas"), 
                       yaxis= dict(title="Cantidas")) 
    data=[c,d,e,f,g,h,i,j,k,l]
    fig = go.Figure(data = data,layout = layout)
    return fig
    
@app.callback(
    Output("Cuarteltec", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo eac'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo eac'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo eac'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo eac'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo eac'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "En su equipo de trabajo existia compañerismo", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Cuartelpcc", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo tpc'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo tpc'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo tpc'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo tpc'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo tpc'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "En su equipo de trabajo los pares cumplían con sus compromisos", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Cuartelhonestidad", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo oaco'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo oaco'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo oaco'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo oaco'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo oaco'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Honestidad", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Cuartellealtad", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo Lealtad'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo Lealtad'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo Lealtad'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo Lealtad'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo Lealtad'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Lealtad", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Cuartelcyrm", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo cyrm'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo cyrm'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo cyrm'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo cyrm'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo cyrm'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Confianza y respeto mutuo", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    

@app.callback(
    Output("Cuartelppc", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo ppc'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo ppc'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo ppc'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo ppc'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo ppc'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Pasión por el cliente", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
@app.callback(
    Output("Cuartelei", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo ei'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo ei'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo ei'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo ei'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo ei'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Ejecución impecable", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
@app.callback(
    Output("Cuartelmc", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo Mc'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo Mc'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo Mc'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo Mc'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo Mc'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Mejora continua", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
@app.callback(
    Output("Cuartelsargs", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    datagraphTerritoriopie=dcuartel.loc[[SCuartel]]
    datagraphTerritoriopie=datagraphTerritoriopie[['Mucho ','Suficiente ','Moderado ','Poco ','Nada ']]
    color_discrete_map = {'Mucho ':'#0F6040',
                          'Suficiente ':'#2BA739',
                          'Moderado ':'#BE3233', 
                          'Poco ':'#992828',
                          'Nada ':'#696C71'
                          }
    figpiet=px.pie(datagraphTerritoriopie,values=datagraphTerritoriopie.iloc[0].values,names=datagraphTerritoriopie.columns,
                   color=datagraphTerritoriopie.columns,
                   color_discrete_map=color_discrete_map,title="Satisfacción con actividades realizadas en GS")
    return figpiet
    
    
    
@app.callback(
    Output("Cuartelscpgs", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    datagraphTerritoriopie=dcuartel.loc[[SCuartel]]
    datagraphTerritoriopie=datagraphTerritoriopie[['Mucho  ','Suficiente  ','Moderado  ','Poco  ','Nada  ']]
    color_discrete_map = {'Mucho  ':'#0F6040',
                          'Suficiente  ':'#2BA739',
                          'Moderado  ':'#BE3233', 
                          'Poco  ':'#992828',
                          'Nada  ':'#696C71'
                          }
    figpiet=px.pie(datagraphTerritoriopie,values=datagraphTerritoriopie.iloc[0].values,names=datagraphTerritoriopie.columns,
                   color=datagraphTerritoriopie.columns,
                   color_discrete_map=color_discrete_map,title="Satisfacción con crecimiento profesional en GS",)
    return figpiet
    
    
@app.callback(
    Output("Cuartelhdr", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo hlyd'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo hlyd'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo hlyd'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo hlyd'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo hlyd'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Su horario laboral y descansos fueron respetados", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
    
@app.callback(
    Output("Cuartelesbalp", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo balyp'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo balyp'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo balyp'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo balyp'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo balyp'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Está satisfecho con el balance entre tus actividades laborales y personales.", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
    
@app.callback(
    Output("Cuartelmme", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Información sobre sueldo y prestaciones1'], x = dterritoriosentimental.index, name = "Información sobre sueldo y prestaciones", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Proceso de reclutamiento1'], x = dterritoriosentimental.index, name = "Proceso de reclutamiento", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Sesión de bienvenida1'], x =dterritoriosentimental.index, name = "Sesión de bienvenida", marker = {"color" : "#008040"})
    d = go.Bar(y = dterritoriosentimental['Recibimiento a tu puesto1'], x = dterritoriosentimental.index, name = "Recibimiento a tu puesto", marker = {"color" : "#00D068"})
    e = go.Bar(y = dterritoriosentimental['Capacitación1'], x =dterritoriosentimental.index, name = "Capacitación", marker = {"color" : "#006B68"})
    f = go.Bar(y = dterritoriosentimental['Seguimiento a tu desempeño1'], x = dterritoriosentimental.index, name = "Seguimiento a tu desempeño", marker = {"color" : "#009975"})
    g = go.Bar(y = dterritoriosentimental['Evaluación1'], x = dterritoriosentimental.index, name = "Evaluación", marker = {"color" : "#33B28C"})
    h = go.Bar(y = dterritoriosentimental['Convivencia con compañeros1'], x = dterritoriosentimental.index, name = "Convivencia con compañeros", marker = {"color" : "#BE3233"})
    i = go.Bar(y = dterritoriosentimental['Convivencia con Formador1'], x = dterritoriosentimental.index, name = "Convivencia con Formador", marker = {"color" : "#992828"})
    j = go.Bar(y = dterritoriosentimental['Eventos de temporada Fiesta de fin de año  entre otros'], x =dterritoriosentimental.index, name = "Eventos de temporada/Fiesta de fin de año entre otros", marker = {"color" : "#8E001D"})
    k = go.Bar(y = dterritoriosentimental['Participación en acciones sociales1'], x = dterritoriosentimental.index, name = "Participación en acciones sociales", marker = {"color" : "#E00245"})
    l = go.Bar(y = dterritoriosentimental['Desarrollo profesional2'], x =dterritoriosentimental.index, name = "Desarrollo profesional", marker = {"color" : "#E32020"})
    m = go.Bar(y = dterritoriosentimental['Elite Azteca1'], x = dterritoriosentimental.index, name = "Elite Azteca", marker = {"color" : "#696C71"})
    n = go.Bar(y = dterritoriosentimental['Otro4'], x = dterritoriosentimental.index, name = "Otro", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "3 mejores momentos en su estancia", 
                       xaxis =dict(title="Momentos"), 
                       yaxis= dict(title="Cantidas"),
                       autosize=True,
#                        width="autosize",
                       height=700,) 
    data=[a,b,c,d,e,f,g,h,i,j,k,l,m,n]
    fig = go.Figure(data = data,layout = layout)
    return fig
    
    
    
@app.callback(
    Output("Cuartelmmae", "figure"),
    [Input("SCuartel","value")]
)
def actualizar(SCuartel):
    dterritoriosentimental=dcuartel.loc[[SCuartel]]
    a = go.Bar(y = dterritoriosentimental['Información sobre sueldo y prestaciones2'], x = dterritoriosentimental.index, name = "Información sobre sueldo y prestaciones", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Proceso de reclutamiento2'], x = dterritoriosentimental.index, name = "Proceso de reclutamiento", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Sesión de bienvenida2'], x =dterritoriosentimental.index, name = "Sesión de bienvenida", marker = {"color" : "#008040"})
    d = go.Bar(y = dterritoriosentimental['Recibimiento a tu puesto2'], x = dterritoriosentimental.index, name = "Recibimiento a tu puesto", marker = {"color" : "#00D068"})
    e = go.Bar(y = dterritoriosentimental['Capacitación2'], x =dterritoriosentimental.index, name = "Capacitación", marker = {"color" : "#006B68"})
    f = go.Bar(y = dterritoriosentimental['Seguimiento a tu desempeño2'], x = dterritoriosentimental.index, name = "Seguimiento a tu desempeño", marker = {"color" : "#009975"})
    g = go.Bar(y = dterritoriosentimental['Evaluación2'], x = dterritoriosentimental.index, name = "Evaluación", marker = {"color" : "#33B28C"})
    h = go.Bar(y = dterritoriosentimental['Convivencia con compañeros2'], x = dterritoriosentimental.index, name = "Convivencia con compañeros", marker = {"color" : "#BE3233"})
    i = go.Bar(y = dterritoriosentimental['Convivencia con Formador2'], x = dterritoriosentimental.index, name = "Convivencia con Formador", marker = {"color" : "#992828"})
    j = go.Bar(y = dterritoriosentimental['Eventos de temporada  Fiesta de fin de año  entre otros 2'], x =dterritoriosentimental.index, name = "Eventos de temporada/Fiesta de fin de año entre otros", marker = {"color" : "#8E001D"})
    k = go.Bar(y = dterritoriosentimental['Participación en acciones sociales2'], x = dterritoriosentimental.index, name = "Participación en acciones sociales", marker = {"color" : "#E00245"})
    l = go.Bar(y = dterritoriosentimental['Desarrollo profesional2'], x =dterritoriosentimental.index, name = "Desarrollo profesional", marker = {"color" : "#E32020"})
    m = go.Bar(y = dterritoriosentimental['Elite Azteca2'], x = dterritoriosentimental.index, name = "Elite Azteca", marker = {"color" : "#696C71"})
    n = go.Bar(y = dterritoriosentimental['Otro5'], x = dterritoriosentimental.index, name = "Otro5", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "3 Momentos menos agradables en su estancia", 
                       xaxis =dict(title="Momentos"), 
                       yaxis= dict(title="Cantidad"),
                       autosize=True,
#                        width="autosize",
                       height=700,) 
    data=[a,b,c,d,e,f,g,h,i,j,k,l,m,n]
    fig = go.Figure(data = data,layout = layout)
    return fig
################################################## dropdowns
@app.callback(
    Output("SRegion", "options"),
    [Input("SCuartel","value")]
)
def actualizarregion(SCuartel):
    UPSCuartelUP=dataArea[dataArea["Cuartel"]==SCuartel]
    return [{"label": i, "value": i} for i in UPSCuartelUP["Region"].unique()]
################################################## dropdowns
# @app.callback(
#     Output("SCuartel", "options"),
#     [Input("STerritorio","value")]
# )
# def actualizarcuartel(STerritorio):
#     UPSRegionUPD=dataArea[dataArea["Territorio"]==STerritorio]
#     return [{"label": i, "value": i} for i in UPSRegionUPD["Cuartel"].unique()]

@app.callback(
    Output("Regionprgsaf", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a= round((((dterritoriosentimental[" 10 prgsaf"][0]+dterritoriosentimental[" 9 prgsaf"][0])-
        (dterritoriosentimental[" 0 prgsaf"][0]+dterritoriosentimental[" 1 prgsaf"][0] +
       dterritoriosentimental[" 2 prgsaf"][0]+dterritoriosentimental[" 3 prgsaf"][0] +
       dterritoriosentimental[" 4 prgsaf"][0]+dterritoriosentimental[" 5 prgsaf"][0] + 
       dterritoriosentimental[" 6 prgsaf"][0]))/((dterritoriosentimental[" 0 prgsaf"][0]+dterritoriosentimental[" 1 prgsaf"][0] +
       dterritoriosentimental[" 2 prgsaf"][0]+dterritoriosentimental[" 3 prgsaf"][0] +
       dterritoriosentimental[" 4 prgsaf"][0]+dterritoriosentimental[" 5 prgsaf"][0] + 
       dterritoriosentimental[" 6 prgsaf"][0])+dterritoriosentimental[" 7 prgsaf"][0]+dterritoriosentimental[" 8 prgsaf"][0] +
       dterritoriosentimental[" 9 prgsaf"][0]+dterritoriosentimental[" 10 prgsaf"][0]))*100)
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = a,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Recomendarian grupo salinas", 'font': {'size': 24}},
        delta = {'reference': 30, 'increasing': {'color': "RebeccaPurple"}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 10], 'color': 'orange'},
                {'range': [10, 30], 'color': 'green'},
                {'range': [30, 100], 'color': 'blue'}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': a}}))

    fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})
    return fig

@app.callback(
    Output("Regiongenero", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    datagraphTerritoriopie=dregion.loc[[SRegion]]
    datagraphTerritoriopie=datagraphTerritoriopie[["Femenino","Masculino","Prefiero no contestar"]]
    color_discrete_map = {'Femenino':'#BE3233',
                          'Masculino':'#0F6040', 
                          'Prefiero no contestar':'#696C71'
                          }
    figpiet=px.pie(datagraphTerritoriopie,values=datagraphTerritoriopie.iloc[0].values,names=datagraphTerritoriopie.columns,
                   color=datagraphTerritoriopie.columns,color_discrete_map=color_discrete_map,title="Genero por Territorio")
    return figpiet

@app.callback(
    Output("Regionedad", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriographedad=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriographedad[" 18 a 25 años"], x = dterritoriographedad.index, name = "18 a 25 años", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriographedad[" 26 a 30 años"], x = dterritoriographedad.index, name = "26 a 30 años", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriographedad[" 31 a 40 años"], x =dterritoriographedad.index, name = "31 a 40 años", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriographedad[" 41 a 50 años"], x = dterritoriographedad.index, name = "41 a 50 años", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriographedad[" 51 a 60 años"], x = dterritoriographedad.index, name = "51 a 60 años", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Rango de edad de los encuestados", 
                       xaxis =dict(title="Rango de edad"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Regionedocivil", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Casado'], x = dterritoriosentimental.index, name = "Casado", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Divorciado'], x = dterritoriosentimental.index, name = "Divorciado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Soltero'], x =dterritoriosentimental.index, name = "Soltero", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Unión libre'], x = dterritoriosentimental.index, name = "Unión libre", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Viudo'], x = dterritoriosentimental.index, name = "Viudo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Estado civil", 
                       xaxis =dict(title="Estado civil"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig


@app.callback(
    Output("Regionlvlpuesto", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    datagraphTerritoriopie=dregion.loc[[SRegion]]
    datagraphTerritoriopie=datagraphTerritoriopie[["Directivo","Formador de equipo",'Mando medio','Primera línea']]
    color_discrete_map = {'Directivo':'#696C71',
                          'Formador de equipo':'#2BA739',
                          'Mando medio':'#BE3233', 
                          'Primera línea':'#0F6040'
                          }
    figpiet=px.pie(datagraphTerritoriopie,values=datagraphTerritoriopie.iloc[0].values,names=datagraphTerritoriopie.columns,
                   color=datagraphTerritoriopie.columns,
                   color_discrete_map=color_discrete_map,title="Nivel de puestos")
    return figpiet

@app.callback(
    Output("RegionExperiencia_en_su_último_puesto", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Excelente expup'], x = dterritoriosentimental.index, name = "Excelente", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Buena expup'], x = dterritoriosentimental.index, name = "Buena", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Regular expup'], x = dterritoriosentimental.index, name = "Regular", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Mala expup'], x =dterritoriosentimental.index, name = "Mala", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Muy mala expup'], x = dterritoriosentimental.index, name = "Muy mala", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Experiencia en su último puesto", 
                       xaxis =dict(title="Experiencias"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
@app.callback(
    Output("Regiontgs", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental[' 0 a 3 meses tgs'], x = dterritoriosentimental.index, name = "0 a 3 meses", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 3 a 6 meses tgs'], x =dterritoriosentimental.index, name = "3 a 6 meses", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental[' 6 a 12 meses tgs'], x = dterritoriosentimental.index, name = "6 a 12 meses", marker = {"color" : "#008040"})
    d = go.Bar(y = dterritoriosentimental[' 1 a 3 años tgs'], x = dterritoriosentimental.index, name = "1 a 3 años", marker = {"color" : "#BE3233"})
    e = go.Bar(y = dterritoriosentimental[' 3 a 5 años tgs'], x = dterritoriosentimental.index, name = "3 a 5 años", marker = {"color" : "#992828"})
    f = go.Bar(y = dterritoriosentimental[' 5 a 10 años tgs'], x = dterritoriosentimental.index, name = "5 a 10 años", marker = {"color" : "#8E001D"})
    g = go.Bar(y = dterritoriosentimental[' 10 a 15 años tg'], x =dterritoriosentimental.index, name = "10 a 15 años", marker = {"color" : "#E00245"})
    h = go.Bar(y = dterritoriosentimental[' 15 a 20 años tgs'], x = dterritoriosentimental.index, name = "15 a 20 años", marker = {"color" : "#696C71"})
    i = go.Bar(y = dterritoriosentimental['más de 20 años tgs'], x = dterritoriosentimental.index, name = "más de 20 años", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "Tiempo en GS", 
                       xaxis =dict(title="Tiempo"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e,f,g,h,i]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Regiontup", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental[' 0 a 3 meses tup'], x = dterritoriosentimental.index, name = "0 a 3 meses", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 3 a 6 meses tup'], x =dterritoriosentimental.index, name = "3 a 6 meses", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental[' 6 a 12 meses tup'], x = dterritoriosentimental.index, name = "6 a 12 meses", marker = {"color" : "#008040"})
    d = go.Bar(y = dterritoriosentimental[' 1 a 3 años tup'], x = dterritoriosentimental.index, name = "1 a 3 años", marker = {"color" : "#BE3233"})
    e = go.Bar(y = dterritoriosentimental[' 3 a 5 años tup'], x = dterritoriosentimental.index, name = "3 a 5 años", marker = {"color" : "#992828"})
    f = go.Bar(y = dterritoriosentimental[' 5 a 10 añostup'], x = dterritoriosentimental.index, name = "5 a 10 años", marker = {"color" : "#696C71"})
    g = go.Bar(y = dterritoriosentimental[' 10 a 15 año tup'], x =dterritoriosentimental.index, name = "10 a 15 año", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "Tiempo en su último puesto", 
                       xaxis =dict(title="Tiempo"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e,f,g]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
    
@app.callback(
    Output("Regionmvgs", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Mucho vmgs'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Suficiente vmgs'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Moderado vmgs'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco vmgs'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada vmgs'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Misión y visión en GS", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Regionmvun", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Mucho vmun'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Suficiente vmun'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Moderado vmun'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco vmun'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada vmun'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Misión y visión de tu Unidad de negocios", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig


@app.callback(
    Output("Regionce", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Mucho ce'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado ce'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente ce'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco ce'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada ce'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Código de ética", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Regionvyc", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Mucho vc'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado vc'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente vc'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco vc'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada vc'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Valores y comportamiento", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Regionpi", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Mucho pi'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado pi'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente pi'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco pi'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada pi'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Prosperidad incluyente", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Regionmgad", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Mucho mg'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado mg'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente mg'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco mg'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada mg'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Modelo de gestión de alto desempeño", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Regionh", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Mucho h'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado h'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente h'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco h'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada h'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Honestel", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Regioni", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Mucho i'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado i'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente i'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco i'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada i'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Ideas", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Regionc", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Mucho c'], x = dterritoriosentimental.index, name = "Mucho", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Moderado c'], x = dterritoriosentimental.index, name = "Moderado", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Suficiente c'], x =dterritoriosentimental.index, name = "Suficiente", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Poco c'], x = dterritoriosentimental.index, name = "Poco", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental['Nada c'], x =dterritoriosentimental.index, name = "Nada", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Cuéntanos", 
                       xaxis =dict(title="Conocimiento que se tenia"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Regionrcgs", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Ambiente laboral cgs'], x = dterritoriosentimental.index, name = "Ambiente laboral", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Asunto familiar cgs'], x = dterritoriosentimental.index, name = "Asunto familiar", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Desacuerdos con mi Formador cgs'], x =dterritoriosentimental.index, name = "Desacuerdos con mi Formador", marker = {"color" : "#008040"})
    d = go.Bar(y = dterritoriosentimental['El tiempo costo de traslado es alto cgs'], x = dterritoriosentimental.index, name = "El tiempo costo de traslado es alto", marker = {"color" : "#00D068"})
    e = go.Bar(y = dterritoriosentimental['Encontré otro empleo cgs'], x =dterritoriosentimental.index, name = "Encontré otro empleo", marker = {"color" : "#009975"})
    f = go.Bar(y = dterritoriosentimental['Inicio mi propio negocio cgs'], x = dterritoriosentimental.index, name = "Inicio mi propio negocio", marker = {"color" : "#33B28C"})
    g = go.Bar(y = dterritoriosentimental['La zona del trabajo me exponía a situaciones de peligro cgs'], x = dterritoriosentimental.index, name = "La zona del trabajo me exponía a situaciones de peligro", marker = {"color" : "#BE3233"})
    h = go.Bar(y = dterritoriosentimental['Maternidad cgs'], x = dterritoriosentimental.index, name = "Maternidad", marker = {"color" : "#992828"})
    i = go.Bar(y = dterritoriosentimental['Me cambio de residencia cgs'], x = dterritoriosentimental.index, name = "Me cambio de residencia", marker = {"color" : "#8E001D"})
    j = go.Bar(y = dterritoriosentimental['Otro especifique cgs'], x =dterritoriosentimental.index, name = "Otro", marker = {"color" : "#E00245"})
    k = go.Bar(y = dterritoriosentimental['Puesto no coincidió con sueldo y o prestaciones indicadas cgs'], x = dterritoriosentimental.index, name = "Puesto no coincidió con sueldo y/o prestaciones indicadas", marker = {"color" : "#E32020"})
    l = go.Bar(y = dterritoriosentimental['Sufrí un accidente o una enfermedad cgs'], x =dterritoriosentimental.index, name = "Sufrí un accidente o una enfermedad", marker = {"color" : "#696C71"})
    m = go.Bar(y = dterritoriosentimental['Voy a seguir estudiando cgs'], x = dterritoriosentimental.index, name = "Voy a seguir estudiando", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "Razón por la cuál concluyes en GS", 
                       xaxis =dict(title="razón"), 
                       yaxis= dict(title="cantidad"),
                       autosize=True,
#                        width="autosize",
                       height=700,) 
    data=[a,b,c,d,e,f,g,h,i,j,k,l,m]
    fig = go.Figure(data = data,layout = layout)
    return fig

@app.callback(
    Output("Regiontpct", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Menos de 30 minutos tcs'], x =dterritoriosentimental.index, name = "Menos de 30 minutos", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['De 30 minutos a 01 hora tcs'], x = dterritoriosentimental.index, name = "De 30 minutos a 1 hora", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['De 01 hora a 02 horas tcs'], x = dterritoriosentimental.index, name = "De 1 hora a 2 horas", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Más de 02 horas tcs'], x = dterritoriosentimental.index, name = "Más de 2 horas", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Tiempo promedio de casa a Trabajo", 
                       xaxis =dict(title="Tiempo"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Regionmtu", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['De 1 a 2 tcs'], x = dterritoriosentimental.index, name = "De 1 a 2", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['De 3 a 4 tcs'], x = dterritoriosentimental.index, name = "De 3 a 4", marker = {"color" : "#BE3233"})
    c = go.Bar(y = dterritoriosentimental['Ninguno tcs'], x =dterritoriosentimental.index, name = "Ninguno", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Medios de transporte que utilizaban", 
                       xaxis =dict(title="Medio"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Regionratp", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegionl]]
    a = go.Bar(y = dterritoriosentimental[' 0 veces roa'], x = dterritoriosentimental.index, name = "0 veces", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 1 a 2 veces roa'], x = dterritoriosentimental.index, name = "1 a 2 veces", marker = {"color" : "#BE3233"})
    c = go.Bar(y = dterritoriosentimental[' 3 a 4 veces roa'], x =dterritoriosentimental.index, name = "3 a 4 veces", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Robo o asalto en transporte público en el último año", 
                       xaxis =dict(title="Veces"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Regionatp", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental[' 0 veces atp'], x = dterritoriosentimental.index, name = "0 veces", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 1 a 2 veces atp'], x = dterritoriosentimental.index, name = "1 a 2 veces", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental[' 3 a 4 veces atp'], x =dterritoriosentimental.index, name = "3 a 4 veces", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Mas de 5 veces atp'], x =dterritoriosentimental.index, name = "Mas de 5", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Acoso en transporte público en el último año", 
                       xaxis =dict(title="Veces"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Regionrpvp", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental[' 0 veces rtp'], x = dterritoriosentimental.index, name = "0 veces", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 1 a 2 veces rtp'], x = dterritoriosentimental.index, name = "1 a 2 veces", marker = {"color" : "#BE3233"})
    c = go.Bar(y = dterritoriosentimental[' 3 a 4 veces rtp'], x =dterritoriosentimental.index, name = "3 a 4 veces", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Robo total o parcial del vehículo propio en el último año", 
                       xaxis =dict(title="Veces"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c]
    fig = go.Figure(data = data, layout = layout)
    return fig


@app.callback(
    Output("Regionaspao", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental[' 0 veces afpe'], x = dterritoriosentimental.index, name = "0 veces", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 1 a 2 veces afpe'], x = dterritoriosentimental.index, name = "1 a 2 veces", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental[' 3 a 4 veces afpe'], x =dterritoriosentimental.index, name = "3 a 4 veces", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Mas de 5 veces afpe'], x =dterritoriosentimental.index, name = "Mas de 5 veces", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Agresión física por personas ajenas a la organización", 
                       xaxis =dict(title="Veces"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d]
    fig = go.Figure(data = data, layout = layout)
    return fig

@app.callback(
    Output("Regioneua", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental[' 0 veces e'], x = dterritoriosentimental.index, name = "0 veces", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental[' 1 a 2 veces e'], x = dterritoriosentimental.index, name = "1 a 2 veces", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental[' 3 a 4 veces e'], x =dterritoriosentimental.index, name = "3 a 4 veces", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Mas de 5 veces e'], x =dterritoriosentimental.index, name = "Más de 5 veces", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Extorsión en el último año", 
                       xaxis =dict(title="Veces"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Regioncene", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Lo busqué por iniciativa propia ne'], x = dterritoriosentimental.index, name = "Lo busqué por iniciativa propia", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Me buscaron de otra empresa ne'], x = dterritoriosentimental.index, name = "Me buscaron de otra empresa", marker = {"color" : "#BE3233"})
    layout = go.Layout(title = "Cómo encontraron su nuevo empleo", 
                       xaxis =dict(title="opciones"), 
                       yaxis= dict(title="Cantidas")) 
    data=[a,b]
    fig = go.Figure(data = data,layout = layout)
    return fig 
    
@app.callback(
    Output("Regioncmce", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    c = go.Bar(y = dterritoriosentimental['Sueldo'], x =dterritoriosentimental.index, name = "Sueldo", marker = {"color" : "#0F6040"})
    d = go.Bar(y = dterritoriosentimental['Prestaciones'], x = dterritoriosentimental.index, name = "Prestaciones", marker = {"color" : "#2BA739"})
    e = go.Bar(y = dterritoriosentimental['Ubicación'], x =dterritoriosentimental.index, name = "Ubicación", marker = {"color" : "#008040"})
    f = go.Bar(y = dterritoriosentimental['Desarrollo profesional'], x = dterritoriosentimental.index, name = "Desarrollo profesional", marker = {"color" : "#00D068"})
    g = go.Bar(y = dterritoriosentimental['Ambiente laboral'], x = dterritoriosentimental.index, name = "Ambiente laboral", marker = {"color" : "#BE3233"})
    h = go.Bar(y = dterritoriosentimental['Cultura'], x = dterritoriosentimental.index, name = "Cultura", marker = {"color" : "#992828"})
    i = go.Bar(y = dterritoriosentimental['Cambio de Liderazgo'], x = dterritoriosentimental.index, name = "Cambio de Liderazgo", marker = {"color" : "#8E001D"})
    j = go.Bar(y = dterritoriosentimental['Actividades de Puesto'], x =dterritoriosentimental.index, name = "Actividades de Puesto", marker = {"color" : "#E00245"})
    k = go.Bar(y = dterritoriosentimental['Costos de traslado a lugar de trabajo'], x = dterritoriosentimental.index, name = "Costos de traslado a lugar de trabajo", marker = {"color" : "#696C71"})
    l = go.Bar(y = dterritoriosentimental['Otro3'], x =dterritoriosentimental.index, name = "Otro", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "Características  que mejoraron para el cambio del empleo", 
                       xaxis =dict(title="Carcaterísticas"), 
                       yaxis= dict(title="Cantidas")) 
    data=[c,d,e,f,g,h,i,j,k,l]
    fig = go.Figure(data = data,layout = layout)
    return fig
    
    
@app.callback(
    Output("Regiontec", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo eac'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo eac'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo eac'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo eac'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo eac'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "En su equipo de trabajo existia compañerismo", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
                                        
    
@app.callback(
    Output("Regionpcc", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo tpc'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo tpc'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo tpc'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo tpc'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo tpc'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "En su equipo de trabajo los pares cumplían con sus compromisos", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Regionhonestidad", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo oaco'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo oaco'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo oaco'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo oaco'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo oaco'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Honestidad", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Regionlealtad", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo Lealtad'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo Lealtad'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo Lealtad'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo Lealtad'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo Lealtad'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Lealtad", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
@app.callback(
    Output("Regioncyrm", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo cyrm'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo cyrm'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo cyrm'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo cyrm'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo cyrm'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Confianza y respeto mutuo", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    

@app.callback(
    Output("Regionppc", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo ppc'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo ppc'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo ppc'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo ppc'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo ppc'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Pasión por el cliente", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
@app.callback(
    Output("Regionei", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo ei'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo ei'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo ei'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo ei'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo ei'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Ejecución impecable", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
@app.callback(
    Output("Regionmc", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo Mc'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo Mc'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo Mc'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo Mc'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo Mc'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Mejora continua", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig

    
    
@app.callback(
    Output("Regionsargs", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    datagraphTerritoriopie=dregion.loc[[SRegion]]
    datagraphTerritoriopie=datagraphTerritoriopie[['Mucho ','Suficiente ','Moderado ','Poco ','Nada ']]
    color_discrete_map = {'Mucho ':'#0F6040',
                          'Suficiente ':'#2BA739',
                          'Moderado ':'#BE3233', 
                          'Poco ':'#992828',
                          'Nada ':'#696C71'
                          }
    figpiet=px.pie(datagraphTerritoriopie,values=datagraphTerritoriopie.iloc[0].values,names=datagraphTerritoriopie.columns,
                   color=datagraphTerritoriopie.columns,
                   color_discrete_map=color_discrete_map,title="Satisfacción con actividades realizadas en GS")
    return figpiet
    
    

@app.callback(
    Output("Regionscpgs", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    datagraphTerritoriopie=dregion.loc[[SRegion]]
    datagraphTerritoriopie=datagraphTerritoriopie[['Mucho  ','Suficiente  ','Moderado  ','Poco  ','Nada  ']]
    color_discrete_map = {'Mucho  ':'#0F6040',
                          'Suficiente  ':'#2BA739',
                          'Moderado  ':'#BE3233', 
                          'Poco  ':'#992828',
                          'Nada  ':'#696C71'
                          }
    figpiet=px.pie(datagraphTerritoriopie,values=datagraphTerritoriopie.iloc[0].values,names=datagraphTerritoriopie.columns,
                   color=datagraphTerritoriopie.columns,
                   color_discrete_map=color_discrete_map,title="Satisfacción con crecimiento profesional en GS",)
    return figpiet
    
    
@app.callback(
    Output("Regionhdr", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo hlyd'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo hlyd'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo hlyd'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo hlyd'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo hlyd'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Su horario laboral y descansos fueron respetados", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
    
@app.callback(
    Output("Regionesbalp", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Totalmente de acuerdo balyp'], x = dterritoriosentimental.index, name = "Totalmente de acuerdo", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Parcialmente de acuerdo balyp'], x = dterritoriosentimental.index, name = "Parcialmente de acuerdo", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Ni en desacuerdo  ni de acuerdo balyp'], x = dterritoriosentimental.index, name = "Ni en desacuerdo  ni de acuerdo", marker = {"color" : "#BE3233"})
    d = go.Bar(y = dterritoriosentimental['Parcialmente en desacuerdo balyp'], x =dterritoriosentimental.index, name = "Parcialmente en desacuerdo", marker = {"color" : "#992828"})
    e = go.Bar(y = dterritoriosentimental[ 'Totalmente en desacuerdo balyp'], x =dterritoriosentimental.index, name = "Totalmente en desacuerdo", marker = {"color" : "#696C71"})
    layout = go.Layout(title = "Está satisfecho con el balance entre tus actividades laborales y personales.", 
                       xaxis =dict(title="nivel"), 
                       yaxis= dict(title="Cantidad")) 
    data=[a,b,c,d,e]
    fig = go.Figure(data = data, layout = layout)
    return fig
    
    
    
@app.callback(
    Output("Regionmme", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Información sobre sueldo y prestaciones1'], x = dterritoriosentimental.index, name = "Información sobre sueldo y prestaciones", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Proceso de reclutamiento1'], x = dterritoriosentimental.index, name = "Proceso de reclutamiento", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Sesión de bienvenida1'], x =dterritoriosentimental.index, name = "Sesión de bienvenida", marker = {"color" : "#008040"})
    d = go.Bar(y = dterritoriosentimental['Recibimiento a tu puesto1'], x = dterritoriosentimental.index, name = "Recibimiento a tu puesto", marker = {"color" : "#00D068"})
    e = go.Bar(y = dterritoriosentimental['Capacitación1'], x =dterritoriosentimental.index, name = "Capacitación", marker = {"color" : "#006B68"})
    f = go.Bar(y = dterritoriosentimental['Seguimiento a tu desempeño1'], x = dterritoriosentimental.index, name = "Seguimiento a tu desempeño", marker = {"color" : "#009975"})
    g = go.Bar(y = dterritoriosentimental['Evaluación1'], x = dterritoriosentimental.index, name = "Evaluación", marker = {"color" : "#33B28C"})
    h = go.Bar(y = dterritoriosentimental['Convivencia con compañeros1'], x = dterritoriosentimental.index, name = "Convivencia con compañeros", marker = {"color" : "#BE3233"})
    i = go.Bar(y = dterritoriosentimental['Convivencia con Formador1'], x = dterritoriosentimental.index, name = "Convivencia con Formador", marker = {"color" : "#992828"})
    j = go.Bar(y = dterritoriosentimental['Eventos de temporada Fiesta de fin de año  entre otros'], x =dterritoriosentimental.index, name = "Eventos de temporada/Fiesta de fin de año entre otros", marker = {"color" : "#8E001D"})
    k = go.Bar(y = dterritoriosentimental['Participación en acciones sociales1'], x = dterritoriosentimental.index, name = "Participación en acciones sociales", marker = {"color" : "#E00245"})
    l = go.Bar(y = dterritoriosentimental['Desarrollo profesional2'], x =dterritoriosentimental.index, name = "Desarrollo profesional", marker = {"color" : "#E32020"})
    m = go.Bar(y = dterritoriosentimental['Elite Azteca1'], x = dterritoriosentimental.index, name = "Elite Azteca", marker = {"color" : "#696C71"})
    n = go.Bar(y = dterritoriosentimental['Otro4'], x = dterritoriosentimental.index, name = "Otro", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "3 mejores momentos en su estancia", 
                       xaxis =dict(title="Momentos"), 
                       yaxis= dict(title="Cantidas"),
                       autosize=True,
#                        width="autosize",
                       height=700,) 
    data=[a,b,c,d,e,f,g,h,i,j,k,l,m,n]
    fig = go.Figure(data = data,layout = layout)
    return fig
    
    
    
@app.callback(
    Output("Regionmmae", "figure"),
    [Input("SRegion","value")]
)
def actualizar(SRegion):
    dterritoriosentimental=dregion.loc[[SRegion]]
    a = go.Bar(y = dterritoriosentimental['Información sobre sueldo y prestaciones2'], x = dterritoriosentimental.index, name = "Información sobre sueldo y prestaciones", marker = {"color" : "#0F6040"})
    b = go.Bar(y = dterritoriosentimental['Proceso de reclutamiento2'], x = dterritoriosentimental.index, name = "Proceso de reclutamiento", marker = {"color" : "#2BA739"})
    c = go.Bar(y = dterritoriosentimental['Sesión de bienvenida2'], x =dterritoriosentimental.index, name = "Sesión de bienvenida", marker = {"color" : "#008040"})
    d = go.Bar(y = dterritoriosentimental['Recibimiento a tu puesto2'], x = dterritoriosentimental.index, name = "Recibimiento a tu puesto", marker = {"color" : "#00D068"})
    e = go.Bar(y = dterritoriosentimental['Capacitación2'], x =dterritoriosentimental.index, name = "Capacitación", marker = {"color" : "#006B68"})
    f = go.Bar(y = dterritoriosentimental['Seguimiento a tu desempeño2'], x = dterritoriosentimental.index, name = "Seguimiento a tu desempeño", marker = {"color" : "#009975"})
    g = go.Bar(y = dterritoriosentimental['Evaluación2'], x = dterritoriosentimental.index, name = "Evaluación", marker = {"color" : "#33B28C"})
    h = go.Bar(y = dterritoriosentimental['Convivencia con compañeros2'], x = dterritoriosentimental.index, name = "Convivencia con compañeros", marker = {"color" : "#BE3233"})
    i = go.Bar(y = dterritoriosentimental['Convivencia con Formador2'], x = dterritoriosentimental.index, name = "Convivencia con Formador", marker = {"color" : "#992828"})
    j = go.Bar(y = dterritoriosentimental['Eventos de temporada  Fiesta de fin de año  entre otros 2'], x =dterritoriosentimental.index, name = "Eventos de temporada/Fiesta de fin de año entre otros", marker = {"color" : "#8E001D"})
    k = go.Bar(y = dterritoriosentimental['Participación en acciones sociales2'], x = dterritoriosentimental.index, name = "Participación en acciones sociales", marker = {"color" : "#E00245"})
    l = go.Bar(y = dterritoriosentimental['Desarrollo profesional2'], x =dterritoriosentimental.index, name = "Desarrollo profesional", marker = {"color" : "#E32020"})
    m = go.Bar(y = dterritoriosentimental['Elite Azteca2'], x = dterritoriosentimental.index, name = "Elite Azteca", marker = {"color" : "#696C71"})
    n = go.Bar(y = dterritoriosentimental['Otro5'], x = dterritoriosentimental.index, name = "Otro5", marker = {"color" : "#9A9CA0"})
    layout = go.Layout(title = "3 Momentos menos agradables en su estancia", 
                       xaxis =dict(title="Momentos"), 
                       yaxis= dict(title="Cantidad"),
                       autosize=True,
#                        width="autosize",
                       height=700,) 
    data=[a,b,c,d,e,f,g,h,i,j,k,l,m,n]
    fig = go.Figure(data = data,layout = layout)
    return fig

if __name__ =="__main__":
    app.run_server(debug=False,port=8080)


# In[ ]:




