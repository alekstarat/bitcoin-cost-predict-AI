import flet as ft
import requests
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from flet.plotly_chart import PlotlyChart

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    api_url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC&tsyms=USD"

    df = pd.read_csv('host/dataset.csv', sep=";")
    fig = px.line(df, x="updated", y="close")

    page.add(PlotlyChart(fig, expand=True))

    def get_price():
        response = requests.get(api_url)
        data = response.json()
        return data["BTC"]["USD"]
    
    t = ft.Text(value=f"{get_price()}", color="green")
    page.controls.append(t)
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)#, view=ft.WEB_BROWSER)