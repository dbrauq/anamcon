# -------------------------------
# This file is part of AnamCon
# by David Brau Queralt
# -------------------------------

from report.report_utils import *
from report.config_report import *
from db_models.report_models import *

from datetime import datetime
from os.path import dirname, abspath, join
import pandas as pd 
import numpy as np
import matplotlib.pyplot as mpl
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, 
                                Paragraph, 
                                Spacer,
                                Image,
                                Table,
                                TableStyle,
                                HRFlowable)
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.units import mm


def create_and_get_report_path(username, anamnesis_timestamp):
    report = Report(username,anamnesis_timestamp)
    report.create_and_save_report()
    report_path = report.get_report_path()
    return report_path


class Report():
    def __init__(self, username, anamnesis_timestamp, document=[]):
        self.username = username
        self.anamnesis_timestamp = anamnesis_timestamp
        self.file_path = None
        self.report_name = "AnamCon_report_" + self.get_username() + "_" + self.get_anamnesis_timestamp()
        self.document = document
        self.user_data = db_get_full_user_data(self.username)
        self.user_data_frame = pd.DataFrame([self.user_data])
        self.anamnesis_data = db_get_full_anamnesis_data(self.username, self.anamnesis_timestamp)
        self.anamnesis_data_frame = pd.DataFrame([self.anamnesis_data])
    def get_username(self):
        return self.username
    
    def get_anamnesis_timestamp(self):
        return self.anamnesis_timestamp
    
    def get_report_name(self):
        return self.report_name
    
    def get_report_path(self):
        if USE_START_MODE == "DOCKER":
            return join(dirname(dirname(abspath(__file__))) + "/report/generated_reports",self.get_report_name()) + ".pdf"
        else:
            return join(USE_WEB_APP_REPORTS_PATH,self.get_report_name()) + ".pdf"
    
    def get_user_data_frame(self):
        return self.user_data_frame
    
    def get_user_data(self):
        return self.user_data
    
    def get_anamnesis_data(self):
        return self.anamnesis_data

    def get_anamnesis_data_frame(self):
        return self.anamnesis_data_frame
    
    def get_document(self):
        return self.document
    
    def append_document(self,document):
        self.document.append(document)
        return
    
    def append_line(self, width=100):
        line = HRFlowable(width=f"{width}%", color=colors.black, thickness=1, spaceBefore=1)
        self.append_document(line)

    def append_spacer(self):
        self.append_document(Spacer(1,10))
    
    def set_document(self, document):
        self.document = document

    def create_and_save_report(self):

        ##### TITLE ##### 
        logo_icon_path = join(dirname(abspath(__file__)), "img/logo_text.png")
        logo_image = Image(logo_icon_path, 30*mm, 3*mm, hAlign="LEFT")
        main_title_text = "<b>INFORME DE ANAMNESIS</b>"
        anamnesis_creation_datetime=self.get_anamnesis_data()["creation_datetime"].strftime("%Y-%m-%d")
        normal_style = getSampleStyleSheet()['Normal']
        main_title_style = ParagraphStyle("main_title_style", 
                                           parent=normal_style, 
                                           fontSize = 12,
                                           alignment=1)
        data = [["",logo_image, Paragraph(main_title_text, main_title_style), Paragraph(anamnesis_creation_datetime, main_title_style)]]
        table_style = TableStyle([
                                  ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                                  ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                                  ("LINEABOVE", (0, 0), (-1,0), 1, colors.HexColor("#000000")),
                                  ("LINEBELOW", (0,-1), (-1,-1), 1, colors.HexColor("#000000")),
                                  ("ALIGMENT", (0, -1), (-1, -1), "CENTER"),
                                  ("VALIGN", (0, -1), (-1, -1), "MIDDLE"),
                                  ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                  ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                  ("TOPPADDING", (0, 0), (-1, -1), 0),
                                  ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                                  ("LEFTMARGIN", (0, 0), (-1, -1), 0),
                                  ("RIGHTMARGIN", (0, 0), (-1, -1), 0),
                                  ("TOPMARGIN", (0, 0), (-1, -1), 0),
                                  ("BOTTOMMARGIN", (0, 0), (-1, -1), 0),
                                  #('GRID', (0, 0), (-1, -1), 1, colors.black),
                                  #('BOX', (0, 0), (-1, -1), 1, colors.black),
                                  #('borderRadius', (0, 0), (-1, -1), 5),
                                ])
        col_widths = [10*mm, 40*mm,"*", 50*mm] 
        row_heights = [12*mm]
        table = Table(data, 
                      style=table_style, 
                      colWidths=col_widths, 
                      rowHeights=row_heights, 
                      hAlign="LEFT")
        self.append_document(table)
        self.append_spacer()
        self.append_spacer()

        ##### PERSONAL DATA ##### 
        personal_data_title_text = "&nbsp&nbsp<b>></b>&nbsp INFORMACIÓN DEL PACIENTE"
        username = self.get_user_data()["username"]
        if not username: username = ""
        name = self.get_user_data()["name"]
        if not name: name = ""
        surname = self.get_user_data()["surname"]
        if not surname: surname = ""
        id_type = self.get_user_data()["id_type"]
        if not id_type: id_type = ""
        id = self.get_user_data()["id"]
        if not id: id = ""
        if self.get_user_data()["birth_date"]:
            birth_date = self.get_user_data()["birth_date"].strftime("%d-%m-%Y") if self.get_user_data()["birth_date"] is not None else None
            age = (datetime.now()-self.get_user_data()["birth_date"]).days // 365
        else: 
            birth_date = ""
            age = ""
        sex = self.get_user_data()["sex"]
        if not sex: sex = ""
        telephone = self.get_user_data()["telephone_number"]
        if not telephone: telephone = ""
        email = self.get_user_data()["email"]
        if not email: email = ""
        adress = self.get_user_data()["adress"]
        if not adress: adress = ""
        zip = self.get_user_data()["zip"]
        if not zip: zip = ""
        country = self.get_user_data()["country"]
        if not country: country = ""
        health_provider = self.get_user_data()["health_provider"]
        if not health_provider: health_provider = ""
        health_number = self.get_user_data()["health_number"]
        if not health_number: health_number = ""
        personal_data = [["","","","","","",""],
                        ["","Usuario:",username,"",id_type+":", id,""],
                        ["","Nombre:", name, "","Teléfono:",telephone,""],
                        ["","Apellidos:", surname,"","Email:",email,""],
                        ["","Fecha nacimiento:", birth_date,"", "Aseguradora:" ,health_provider,""],
                        ["","Edad:" ,age,"","ID sanitario:",health_number,""],
                        ["","Sexo:",sex,"","","",""],
                        ["","Dirección:",adress,"","","",""],
                        ["","Código postal:", zip,"","", "",""],
                        ["","País:", country,"", "", "",""],
                        ["","","","","","",""]]

        personal_data_style = ParagraphStyle("personal_data_title_style", 
                                                    parent=normal_style, 
                                                    fontSize = 11,
                                                    alignment=0)
        table_personal_data_style = TableStyle([
                                  ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                                  ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                                  ("LINEABOVE", (0,0), (-1,0), 1, colors.HexColor("#212121")),
                                  ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
                                  ('FONTNAME', (4, 0), (4, -1), 'Helvetica-Bold'),
                                  ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                                  ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                                  ("LEFTPADDING", (0, 0), (-1, -1), 5),
                                  ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                                  ("TOPPADDING", (0, 0), (-1, -1), 0),
                                  ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                                  ("LEFTMARGIN", (0, 0), (-1, -1), 0),
                                  ("RIGHTMARGIN", (0, 0), (-1, -1), 0),
                                  ("TOPMARGIN", (0, 0), (-1, -1), 0),
                                  ("BOTTOMMARGIN", (0, 0), (-1, -1), 0),
                                ])
        internal_margin = 2*mm
        cell_height = 7*mm
        col_widths_personal_data = [internal_margin,35*mm,62*mm,"*",35*mm, 62*mm,internal_margin] 
        row_heights_personal_data = [internal_margin,cell_height,cell_height,cell_height,cell_height,cell_height,cell_height,cell_height,cell_height,cell_height,internal_margin]

        table_personal_data = Table(personal_data, 
                                    style=table_personal_data_style, 
                                    colWidths=col_widths_personal_data, 
                                    rowHeights=row_heights_personal_data, 
                                    hAlign="LEFT")
        self.append_document(Paragraph(personal_data_title_text, personal_data_style))
        self.append_spacer()
        self.append_document(table_personal_data)
        self.append_spacer()
        self.append_spacer()
        
        ##### ANAMNESIS SUMMARY #####
        anamnesis_summary_title_text = "&nbsp&nbsp<b>></b>&nbsp RESUMEN DE LA ANAMNESIS"
        anamnesis_type = self.get_anamnesis_data()["anamnesis_mode"]
        title = self.get_anamnesis_data()["title"]
        duration_seconds = self.get_anamnesis_data()["duration_seconds"]
        duration_hours = duration_seconds // 3600
        duration_minutes = (duration_seconds % 3600) // 60
        duration_seconds = duration_seconds % 60
        final_duration = "{:02}:{:02}:{:02}".format(int(duration_hours),int(duration_minutes),int(duration_seconds))
        creation_datetime = self.get_anamnesis_data()["creation_datetime"].strftime("%d-%m-%Y | %H:%M:%S")
        last_interaction_datetime = self.get_anamnesis_data()["last_interaction_datetime"].strftime("%d-%m-%Y | %H:%M:%S")
        number_interactions = self.get_anamnesis_data()["number_interactions"]
        symptoms_raw = self.get_anamnesis_data()["symptoms"]
        num_symptoms = len(symptoms_raw)
        symptoms = []
        for symptom in symptoms_raw:
            symptoms.append(symptom.get(list(symptom.keys())[0])["title"])
        symptoms_text = ""
        num_symptom = 1
        for symtom_title in symptoms:
            symptoms_text += "[" + str(num_symptom) +"]  "
            symptoms_text += symtom_title
            symptoms_text += "\n\n"
            num_symptom += 1
        sentiment_types=[]
        sentiment_intensities=[]
        dialog = self.get_anamnesis_data()["dialog"]
        for i in range(len(dialog)):
            if (dialog[i]["complete_intent"] == True) and\
               (dialog[i]["new_intent"]) == False and\
               (dialog[i]["interaction_meaning"]) == "symptom":
                for j in range(i):
                    if dialog[i-j-1]["intent"] == dialog[i]["intent"] and\
                        dialog[i-j-1]["interaction_meaning"] == "symptom" and\
                        dialog[i-j-1]["new_intent"] == True and\
                        dialog[i-j-1]["intent"] != dialog[i-j-2]["intent"]:
                        sentiment_types.append(dialog[i-j-1]["query_sentiment_type"])
                        sentiment_intensities.append(dialog[i-j-1]["query_sentiment_intensity"])
                        break
        mean_sentiment_type = np.mean(sentiment_types)
        std_sentiment_type = np.std(sentiment_types)
        mean_sentiment_intensitie = np.mean(sentiment_intensities)
        std_sentiment_intensities = np.std(sentiment_intensities)
        mean_sentiment_type_2dec = "{:.2f}".format(mean_sentiment_type)
        std_sentiment_type_2dec = "{:.2f}".format(std_sentiment_type)
        mean_sentiment_intensitie_2dec = "{:.2f}".format(mean_sentiment_intensitie)
        std_sentiment_intensities_2dec = "{:.2f}".format(std_sentiment_intensities)
        sentiment_index = np.array(sentiment_types) * np.array(sentiment_intensities)
        mean_sentiment_index = np.mean(sentiment_index)
        mean_sentiment_index_2dec = "{:.2f}".format(mean_sentiment_index)
        std_sentiment_index = np.std(sentiment_index)
        std_sentiment_index_2dec = "{:.2f}".format(std_sentiment_index)
        anamnesis_data = [["","","","","","",""],
                        ["","Título:", title, "","Síntomas guía:", symptoms_text,""],
                        ["","Tipo:",anamnesis_type,"","", ""],
                        ["","Duración:", final_duration],
                        ["","Creación:", creation_datetime,"", "" ,""],
                        ["","Finalización:" ,last_interaction_datetime,"","",""],
                        ["","Nº Síntomas:" ,num_symptoms,"","","",""],
                        ["","Nº Interacciones:" ,number_interactions,"","",""],
                        ["","Sentimiento medio:" ,str(mean_sentiment_type_2dec) + " ± " + str(std_sentiment_type_2dec) + " *","","",""],
                        ["","Intensidad media sent.:" ,str(mean_sentiment_intensitie_2dec) + " ± " + str(std_sentiment_intensities_2dec) + " **","","",""],
                        ["","Índice medio sent.:" ,str(mean_sentiment_index_2dec) + " ± " + str(std_sentiment_index_2dec) + " ***","","",""],                       
                        ["","","","","","",""]]

        anamnesis_data_style = ParagraphStyle("anamnesis_data_style", 
                                                    parent=normal_style, 
                                                    fontSize = 11,
                                                    alignment=0)
        table_anamnesis_data_style = TableStyle([
                                  ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                                  ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                                  ("LINEABOVE", (0,0), (-1,0), 1, colors.HexColor("#212121")),
                                  ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
                                  ('FONTNAME', (4, 0), (4, -1), 'Helvetica-Bold'),
                                  ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                                  ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                                  ("VALIGN", (5, 1), (5, -2), "TOP"),
                                  ('FONTNAME', (5, 1), (5, -2), 'Helvetica-Bold'),
                                  ("LEFTPADDING", (0, 0), (-1, -1), 5),
                                  ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                                  ("TOPPADDING", (0, 0), (-1, -1), 0),
                                  ("TOPPADDING", (5, 1), (5, -2), 4),
                                  ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                                  ("LEFTMARGIN", (0, 0), (-1, -1), 0),
                                  ("RIGHTMARGIN", (0, 0), (-1, -1), 0),
                                  ("TOPMARGIN", (0, 0), (-1, -1), 0),
                                  ("BOTTOMMARGIN", (0, 0), (-1, -1), 0),
                                  ("SPAN", (5, 1), (5, -2)),
                                  #('GRID', (0, 0), (-1, -1), 1, colors.black),
                                  #('BOX', (0, 0), (-1, -1), 1, colors.black),
                                ])
        internal_margin = 2*mm
        cell_height = 7*mm
        col_widths_anamnesis_data = [internal_margin,45*mm,52*mm,"*",35*mm, 62*mm,internal_margin] 
        row_heights_anamnesis_data = [internal_margin,cell_height,cell_height,cell_height,cell_height,cell_height,cell_height,cell_height,cell_height,cell_height,cell_height,internal_margin]

        table_anamnesis_data = Table(anamnesis_data, 
                                    style=table_anamnesis_data_style, 
                                    colWidths=col_widths_anamnesis_data, 
                                    rowHeights=row_heights_anamnesis_data, 
                                    hAlign="LEFT")
        self.append_document(Paragraph(anamnesis_summary_title_text, anamnesis_data_style))
        self.append_spacer()
        self.append_document(table_anamnesis_data)
        self.append_spacer()

        ##### ANAMNESIS SUMMARY GRAPHIC#####
        agent = self.get_anamnesis_data()["agent_id"]
        symptom_summary_data= []
        for i in range(len(dialog)):
            if (dialog[i]["complete_intent"] == True) and\
               (dialog[i]["new_intent"]) == False and\
               (dialog[i]["interaction_meaning"]) == "symptom":
                symptom_params_raw = dialog[i]["intent_parameters_and_values"]
                symptom_params={}
                for param in symptom_params_raw:
                    symptom_params[db_get_parameter_title_from_intent_param(agent, dialog[i]["intent"],param)["parameter_title"]] = symptom_params_raw[param]
                for j in range(i):
                    if dialog[i-j-1]["intent"] == dialog[i]["intent"] and\
                        dialog[i-j-1]["interaction_meaning"] == "symptom" and\
                        dialog[i-j-1]["new_intent"] == True and\
                        dialog[i-j-1]["intent"] != dialog[i-j-2]["intent"]:
                            sentiment_type = dialog[i-j-1]["query_sentiment_type"]
                            sentiment_intensity = dialog[i-j-1]["query_sentiment_intensity"]
                            sentiment_index = "{:.2f}".format(sentiment_type * sentiment_intensity)
                            break
                symptom_term_and_region = db_get_symptom_identifier_and_region_from_intent(agent, dialog[i]["intent"])
                symptom_summary_data.append({"symptom_title":symptom_term_and_region["symptom_title"],
                                            "region":symptom_term_and_region["region"],
                                            "inicio":dialog[i]["intent_parameters_and_values"]["inicio"],
                                            "sentiment_type": sentiment_type,
                                            "sentiment_intensity": sentiment_intensity,
                                            "sentiment_index" : sentiment_index,
                                            "identifier":symptom_term_and_region["identifier"],
                                            "symptom_params":symptom_params})        
        symptom_summary_data_frame = pd.DataFrame(symptom_summary_data)
        mpl.rc('font', size=18)
        mpl.rc('axes', titlesize=20)
        mpl.rc('axes', labelsize=20)
        mpl.rc('xtick', labelsize=18)
        mpl.rc('ytick', labelsize=18)
        mpl.rc('legend', fontsize=18) 
        symptom_summary_data_frame["inicio"] = pd.to_datetime(symptom_summary_data_frame["inicio"])
        symptom_summary_data_frame["inicio"] = symptom_summary_data_frame["inicio"].dt.strftime('%d/%m/%Y | %H:%M:%S')
        mpl.figure(figsize=(20, 5))
        sorted_data_frame = symptom_summary_data_frame.sort_values(by="inicio")
        for idx, row in sorted_data_frame.iterrows():
            mpl.scatter(row["inicio"], row["sentiment_index"], label=f"{row['symptom_title']} ({row['region']})", s=100, linewidths=3)
        mpl.xlabel("Tiempo")
        mpl.ylabel("Índice sentimiento")
        mpl.title("Síntomas en el tiempo según el análisis de sentimientos en su manifestación")
        mpl.legend()
        mpl.grid(True, linestyle='--', alpha=0.7)
        summary_plot_path = dirname(dirname(abspath(__file__))) +"/report/generated_reports/" +self.get_report_name()+"anamnesis_summary_plot.png"
        mpl.savefig(summary_plot_path, bbox_inches='tight')
        summary_plot = Image(summary_plot_path, 206*mm, 60*mm, hAlign="LEFT")
        summary_plot_data = [[summary_plot]]
        summary_plot_data_style = TableStyle([
                                  ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                                  ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                                  ("ALIGMENT", (0, -1), (-1, -1), "CENTER"),
                                  ("VALIGN", (0, -1), (-1, -1), "MIDDLE"),
                                  ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                  ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                  ("TOPPADDING", (0, 0), (-1, -1), 0),
                                  ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                                  ("LEFTMARGIN", (0, 0), (-1, -1), 0),
                                  ("RIGHTMARGIN", (0, 0), (-1, -1), 0),
                                  ("TOPMARGIN", (0, 0), (-1, -1), 0),
                                  ("BOTTOMMARGIN", (0, 0), (-1, -1), 0),
                                ])
        col_widths = [206*mm] 
        row_heights = [60*mm]
        summary_plot_data_table = Table(summary_plot_data, 
                                        style=summary_plot_data_style, 
                                        colWidths=col_widths, 
                                        rowHeights=row_heights, 
                                        hAlign="CENTER")
        self.append_document(summary_plot_data_table)

        ##### SENTIMENT_ANALYSIS_EXPLANATION #####
        extra_summary_info = TableStyle([
                                  ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                                  ("ALIGMENT", (0, -1), (-1, -1), "CENTER"),
                                  ("VALIGN", (0, -1), (-1, -1), "MIDDLE"),
                                  ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                  ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                  ("TOPPADDING", (0, 0), (-1, -1), 0),
                                  ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                                  ("LEFTMARGIN", (0, 0), (-1, -1), 0),
                                  ("RIGHTMARGIN", (0, 0), (-1, -1), 0),
                                  ("TOPMARGIN", (0, 0), (-1, -1), 0),
                                  ("BOTTOMMARGIN", (0, 0), (-1, -1), 0),
                                ])
        extra_summary_data_style = ParagraphStyle("extra_summary_data_style", 
                                                parent=normal_style,
                                                textColor=colors.grey,
                                                fontSize = 9,
                                                alignment=0)
        extra_summary_text_1 = "* Tipo medio de los sentimientos en que se han expresado los síntomas. Rango de -1 (Negativo) a 1 (positivo)."
        extra_summary_text_2 = "** Intensidad media de los sentimientos en que se ha expresado los síntomas. Rango de 0 a infinito."
        extra_summary_text_3 = "*** Índice promedio de los sentimiento. Se obtiene como producto cartesiano del tipo medio e intensidad media de los sentimientos."

        extra_summary_data = [[Paragraph(extra_summary_text_1, extra_summary_data_style)],
                              [Paragraph(extra_summary_text_2, extra_summary_data_style)],
                              [Paragraph(extra_summary_text_3, extra_summary_data_style)]]
        col_widths = [206*mm] 
        row_heights = [4*mm,4*mm,4*mm]
        extra_summary_data_table = Table(extra_summary_data, 
                                        style=extra_summary_info, 
                                        colWidths=col_widths, 
                                        rowHeights=row_heights, 
                                        hAlign="CENTER")
        self.append_spacer()
        self.append_spacer()
        self.append_document(extra_summary_data_table)
        self.append_spacer()

        ##### SYMPTOMS DATA ##### 
        symptoms_data_title_text = "&nbsp&nbsp<b>></b>&nbsp INFORMACIÓN DE LOS SÍNTOMAS"
        symptoms_data_title_style = ParagraphStyle("symptoms_data_title_style", 
                                                    parent=normal_style, 
                                                    fontSize = 11,
                                                    alignment=0)
        symptoms_data_upper_line_data = [[""]]
        symptoms_data_upper_line_table = Table(symptoms_data_upper_line_data, 
                                            style=table_anamnesis_data_style, 
                                            colWidths=["*"], 
                                            rowHeights=[2*mm], 
                                            hAlign="LEFT")
        self.append_document(Paragraph(symptoms_data_title_text, symptoms_data_title_style))
        self.append_spacer()
        self.append_document(symptoms_data_upper_line_table)
        
        for symptom in symptom_summary_data:
            symptoms_data_full_style =[
                                  ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                                  ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                                  ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
                                  ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                                  ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                                  ("LEFTPADDING", (0, 0), (-1, -1), 5),
                                  ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                                  ("TOPPADDING", (0, 0), (-1, -1), 0),
                                  ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                                  ("LEFTMARGIN", (0, 0), (-1, -1), 0),
                                  ("RIGHTMARGIN", (0, 0), (-1, -1), 0),
                                  ("TOPMARGIN", (0, 0), (-1, -1), 0),
                                  ("BOTTOMMARGIN", (0, 0), (-1, -1), 0),
                                  #('GRID', (0, 0), (-1, -1), 1, colors.black)
                                ]
            symptoms_data_full = []
            symtom_data_line = 0
            symptoms_data_full.append(["","SÍNTOMA",symptom["symptom_title"],"","SNOMED CT ID",symptom["identifier"][0]["SNOMED"],""])
            symtom_data_line +=1
            symptoms_data_full_style.append(('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'))
            symptoms_data_full_style.append(('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#d7dbe0")))
            symptoms_data_full_style.append(('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'))
            symptoms_data_full.append(["","Parámetros","","","","",""])
            symtom_data_line +=1
            symptom["symptom_params"]["Inicio"] = str(datetime.fromisoformat(symptom["symptom_params"]["Inicio"]).strftime("%d-%m-%Y | %H:%M:%S"))
            symptoms_data_full.append(["","","Inicio","",symptom["symptom_params"]["Inicio"],"",""])
            symtom_data_line +=1
            for param in symptom["symptom_params"].keys():
                if param == "Inicio":
                    continue
                symptoms_data_full.append(["","",param,"",symptom["symptom_params"][param],"",""])
                symtom_data_line +=1
            symptoms_data_full.append(["","Sentimientos","","","","",""])
            symtom_data_line +=1
            symptoms_data_full.append(["","","Tipo de sentimiento","",symptom["sentiment_type"],"",""])
            symtom_data_line +=1
            symptoms_data_full.append(["","","Intensidad del sentimiento","",symptom["sentiment_intensity"],"",""])
            symtom_data_line +=1
            symptoms_data_full.append(["","","Índice del sentimiento","",symptom["sentiment_index"],"",""])
            symtom_data_line +=1            
            symptoms_data_full.append(["","","","","","",""])
            symtom_data_line +=1
            internal_margin = 2*mm
            cell_height = 7*mm
            row_heights_symptom = []
            for i in range(symtom_data_line):
                row_heights_symptom.append(cell_height)
            col_widths_symptom = [internal_margin,35*mm,62*mm,"*",35*mm, 62*mm,internal_margin] 
            symptoms_data_full_style = TableStyle(symptoms_data_full_style)
            symptoms_data_table = Table(symptoms_data_full, 
                                    style=symptoms_data_full_style, 
                                    colWidths=col_widths_symptom, 
                                    rowHeights=row_heights_symptom, 
                                    hAlign="LEFT")
            
            self.append_document(symptoms_data_table)
        self.append_spacer()
        self.append_spacer()

        ##### ANAMNESIS POR APARATOS ##### 
        review_data_title_text = "&nbsp&nbsp<b>></b>&nbsp ANAMNESIS POR APARATOS"
        review_data_raw = self.get_anamnesis_data()["dialog"]
        for i in range(len(review_data_raw)):
            review_started = False
            if(dialog[i]["interaction_meaning"]) == "review" and\
                dialog[i]["complete_intent"] == True and\
                dialog[i]["complete_intent"]:
                review_data_params = dialog[i]["intent_parameters_and_values"]
                review_data_params_final = {}   
                for param in review_data_params.keys():
                    if param != "intro" and review_data_params[param] != "$__assisted":
                        review_data_params_final[db_get_parameter_title_from_intent_param(agent, dialog[i]["intent"], 
                                                                                          param)["parameter_title"]]\
                        = review_data_params[param]
        internal_margin = 2*mm
        cell_height = 7*mm
        col_widths_review_data = [internal_margin,35*mm,62*mm,"*",35*mm, 62*mm,internal_margin] 
        row_heights_review_data = []
        review_data = [["","","","","","",""]]
        row_heights_review_data.append(internal_margin)  
        for param in review_data_params_final.keys():
            review_data.append(["",param,review_data_params_final[param],"","","",""])
            row_heights_review_data.append(cell_height)        

        review_data_style = ParagraphStyle("personal_data_title_style", 
                                                    parent=normal_style, 
                                                    fontSize = 11,
                                                    alignment=0)
        table_review_data_style = TableStyle([
                                  ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                                  ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                                  ("LINEABOVE", (0,0), (-1,0), 1, colors.HexColor("#212121")),
                                  ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
                                  ('FONTNAME', (4, 0), (4, -1), 'Helvetica-Bold'),
                                  ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                                  ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                                  ("LEFTPADDING", (0, 0), (-1, -1), 5),
                                  ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                                  ("TOPPADDING", (0, 0), (-1, -1), 0),
                                  ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                                  ("LEFTMARGIN", (0, 0), (-1, -1), 0),
                                  ("RIGHTMARGIN", (0, 0), (-1, -1), 0),
                                  ("TOPMARGIN", (0, 0), (-1, -1), 0),
                                  ("BOTTOMMARGIN", (0, 0), (-1, -1), 0),
                                ])
       


        table_review_data = Table(review_data, 
                                    style=table_review_data_style, 
                                    colWidths=col_widths_review_data, 
                                    rowHeights=row_heights_review_data, 
                                    hAlign="LEFT")
        self.append_document(Paragraph(review_data_title_text, review_data_style))
        self.append_spacer()
        self.append_document(table_review_data)
        self.append_spacer()
        self.append_spacer()

        ##### CONSTRUCCIÓN DOCUMENTO ##### 
        report_template = SimpleDocTemplate(
                          self.get_report_path(), 
                          pagesize=letter, 
                          rightMargin=10, 
                          leftMargin=10, 
                          topMargin=10, 
                          bottomMargin=10)
 
        report_template.build(self.get_document())   