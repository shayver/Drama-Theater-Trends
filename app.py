#basics
import os
#shiny
import shinywidgets as sw
from shiny.express import ui, render, input
#math, plots
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
#extras
from faicons import icon_svg as icon
#data acquisition
from api_interactions import getData

ui.page_opts(fillable=False)
directory = os.getcwd()
ui.tags.style(
    "body {\
        font-family: Arial; \
        margin-top: 1em; \
        margin-right: 10em; \
        margin-left: 10em; \
        background-image: url('background.jpeg'); \
    }"
)

marker_color_html = "#077CCB"

with ui.layout_columns(col_widths=(12, 6, 6, 6, 6, 12)):
    with ui.card():
        ui.HTML("""
        <center>
            <h1 style="color: black;">
                Drama Theater Trends In Poland
            </h1>
        </center>
        """)
    with ui.card():
        with ui.value_box(showcase=icon("landmark")):
            result_theaters = getData('https://bdl.stat.gov.pl/api/v1/data/by-variable/194952?format=json&unit-level=0')
            "Number Of Theaters"
            str(result_theaters[1])
            "As Of Year " + str(result_theaters[2])
        @sw.render_widget
        def chart_theaters():
            fig = px.bar(result_theaters[0], x='year', y='val', height=200)
            fig.update_yaxes(visible=False, showticklabels=False)
            fig.update_xaxes(visible=False, showticklabels=False)
            fig.update_layout(
            plot_bgcolor='white'
            )
            fig.update_traces(marker_color = marker_color_html, hovertemplate='Year: %{x} <br>#Theaters: %{y}')
            return fig

    with ui.card():
        with ui.value_box(showcase=icon("masks-theater")):
            result_performances = getData('https://bdl.stat.gov.pl/api/v1/data/by-variable/194953?format=json&unit-level=0')
            "Total Number Of Performances"
            str(str(result_performances[1]))
            "As Of Year " + str(result_performances[2])
        @sw.render_widget
        def chart_performances():
            fig = px.bar(result_performances[0], x='year', y='val', height=200)
            fig.update_yaxes(visible=False, showticklabels=False)
            fig.update_xaxes(visible=False, showticklabels=False)
            fig.update_layout(
            plot_bgcolor='white'
            )
            fig.update_traces(marker_color = marker_color_html, hovertemplate='Year: %{x} <br>#Performances: %{y:.3s}')
            return fig
    
    with ui.card():
        with ui.value_box(showcase=icon("user-group")):
            result_audience = getData('https://bdl.stat.gov.pl/api/v1/data/by-variable/194954?format=json&unit-level=0')
            "Total Audience"
            str(result_audience[1])
            "As Of Year " + str(result_audience[2])
        @sw.render_widget
        def chart_audience():
            fig = px.bar(result_audience[0], x='year', y='val', height=200)
            fig.update_yaxes(visible=False, showticklabels=False)
            fig.update_xaxes(visible=False, showticklabels=False)
            fig.update_layout(
            plot_bgcolor='white'
            )
            fig.update_traces(marker_color = marker_color_html, hovertemplate='Year: %{x} <br>Total Audience: %{y:.3s}')
            return fig

    with ui.card():
        with ui.value_box(showcase=icon("ticket")):
            result_tickets = getData('https://bdl.stat.gov.pl/api/v1/data/by-variable/5083?format=json&unit-level=0')
            "Average Ticket Price"
            str(result_tickets[1]) + " PLN"
            "As Of Year " + str(result_tickets[2])
        @sw.render_widget
        def chart_tickets():

            fig_all = make_subplots(specs=[[{"secondary_y": True}]])
            fig1 = px.line(result_tickets[0], x='year', y='val', height=200)
            fig1.update_traces(line_color='orange', hovertemplate='Year: %{x} <br>Average Price: %{y} PLN')

            #result_2 = getData('')
            #fig2 = px.line(placeholder[0], x='year', y='val', height=200)
            #fig2.update_traces(yaxis="y2")

            fig_all.add_traces(fig1.data) #+ fig2.data)

            fig_all.layout.yaxis.title="Price"
            #fig_all.layout.yaxis2.title=""
            fig_all.update_layout(
                plot_bgcolor='white',
                yaxis=dict(
                    tickfont=dict(
                        color="#000000"
                    )
                ),
                title="Theater Ticket Prices",
                height = 200
            )
            return fig_all
    
    with ui.card():
        ui.HTML("""
        <p style="font-size: smaller; display: inline-block;">
            The data used in this dashboard has been provided by the <a href='https://stat.gov.pl/en/'>Statistics Poland</a>
            under the terms of the <a href='https://creativecommons.org/licenses/by/4.0/'>Creative Commons BY 4.0 - Attribution</a> license. <br>
            The data has been provided through the <a href='https://bdl.stat.gov.pl/bdl/start'>BDL</a> API. Visible values has been rounded for chart purposes. <br>
            The rights to this data are reserved by the Statistics Poland. The data presented in this dashboard is provided "as is" without any warranties, expressed or implied.
        </p>
        """)