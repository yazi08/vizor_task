import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px









class BaseGraph:




    def get_main_df(self):
        df_install_main = pd.read_csv(r'D:\WORK FOLDER\Yaroslav\scripts_python\vizor_task\installs_main.csv')
        df_install_s_2 = pd.read_csv(r'D:\WORK FOLDER\Yaroslav\scripts_python\vizor_task\installs_s2.csv')

        df_install_main['install_time'] = pd.to_datetime(df_install_main['install_time'])
        df_install_main['contributor_1_touch_time'] = pd.to_datetime(df_install_main['contributor_1_touch_time'])
        df_install_main['contributor_2_touch_time'] = pd.to_datetime(df_install_main['contributor_2_touch_time'])
        df_install_main['contributor_1_date'] = pd.to_datetime(df_install_main['contributor_1_touch_time'].dt.date)
        df_install_main['contributor_2_date'] = pd.to_datetime(df_install_main['contributor_2_touch_time'].dt.date)
        df_install_main['install_date'] = pd.to_datetime(df_install_main['install_time'].dt.date)
        df_install_main['install_year'] = pd.to_datetime(df_install_main['install_time']).dt.year
        df_install_main['install_hour'] = pd.to_datetime(df_install_main['install_time']).dt.hour
        df_install_main['contributor_1_hour'] = pd.to_datetime(df_install_main['contributor_1_touch_time']).dt.hour
        df_install_main['contributor_2_hour'] = pd.to_datetime(df_install_main['contributor_2_touch_time']).dt.hour
        df_install_main['install_day'] = pd.to_datetime(df_install_main['install_time']).dt.day
        df_install_s_2['install_date'] = pd.to_datetime(df_install_s_2['install_date'])

        return df_install_main, df_install_s_2







    """Сравнительный график источников в зависимости от очереди """

    def get_plot_hist(self,df_2022,df_2023,value,title):

        fig, ax = plt.subplots()


        ax.hist(
            df_2022[value],
            bins=8,
            linewidth=0.7,
            edgecolor="white",
            alpha=0.5,
            color='red',
            label='2022'
        )

        ax.hist(
            df_2023[value],
            bins=8,
            linewidth=0.7,
            edgecolor="white",
            alpha=0.5,
            color='green',
            label='2023'
        )

        ax.set_xlabel(value)
        ax.set_ylabel('Count')
        ax.set_title(title)

        ax.legend()  # ← легенда здесь!

        return plt.show()


    def get_compar_contributor(self,df_sor_2_cont_1,df_sor_2_cont_2):
        fig, ax = plt.subplots(figsize=(25, 5))

        # Предположим, что все данные в df_compare
        ax.plot(df_sor_2_cont_1['contributor_1_date'], df_sor_2_cont_1['contributor_1'], marker='o', linestyle='-',
                label='contributor_1')
        ax.plot(df_sor_2_cont_2['contributor_2_date'], df_sor_2_cont_2['contributor_2'], marker='o', linestyle='-',
                label='contributor_2')

        ax.set_xlabel('Install Date')
        ax.set_ylabel('Installs')
        ax.set_title('Installs over time')
        ax.legend()  # добавляем легенду
        # plt.xticks(rotation=20)
        plt.tight_layout()
        return plt.show()



    def get_compar_contributor_plotly(self,df_sor_2_cont_1,df_sor_2_cont_2):
        fig = go.Figure()

        # contributor_1
        fig.add_trace(go.Scatter(
            x=df_sor_2_cont_1['contributor_1_date'],
            y=df_sor_2_cont_1['contributor_1'],
            mode='lines+markers',
            name='contributor_1',
            hovertemplate='contributor_1: %{y}<br>Date: %{x}<extra></extra>'
        ))

        # contributor_2
        fig.add_trace(go.Scatter(
            x=df_sor_2_cont_2['contributor_2_date'],
            y=df_sor_2_cont_2['contributor_2'],
            mode='lines+markers',
            name='contributor_2',
            hovertemplate='contributor_2: %{y}<br>Date: %{x}<extra></extra>'
        ))

        # Настройки графика
        fig.update_layout(
            title='Installs over time by contributor',
            xaxis_title='Install Date',
            yaxis_title='Installs',
            xaxis=dict(tickangle=-30),
            width=1200,
            height=500,
            hovermode='x unified'  # показывает значения всех линий при наведении на одну дату
        )

        return fig.show()




    def get_installs_s_2(self,df_install_s_2):
        fig, ax = plt.subplots(figsize=(25, 5))  # можно задать размер графика

        ax.plot(df_install_s_2['install_date'], df_install_s_2['installs'], marker='o', linestyle='-')
        ax.set_xlabel('Install Date')
        ax.set_ylabel('Installs')
        ax.set_title('Installs over time')
        plt.xticks(rotation=45)  # чтобы даты не налезали
        plt.tight_layout()
        plt.xticks(rotation=30)
        return plt.show()



    def get_compare_s_2_main(self,df_compare):
        fig, ax = plt.subplots(figsize=(25, 5))

        # Предположим, что все данные в df_compare
        ax.plot(df_compare['install_date'], df_compare['installs'], marker='o', linestyle='-', label='admin_s2')
        ax.plot(df_compare['install_date'], df_compare['installs_main'], marker='o', linestyle='-', label='main')

        ax.set_xlabel('Install Date')
        ax.set_ylabel('Installs')
        ax.set_title('Installs over time')
        ax.legend()  # добавляем легенду
        # plt.xticks(rotation=20)
        plt.tight_layout()
        return plt.show()



    def get_compare_s_2_main_gap(self, df_compare):



        df_compare['gap'] = df_compare['installs'] - df_compare['installs_main']

        fig = go.Figure()

        # Source 2
        fig.add_trace(go.Scatter(
            x=df_compare['install_date'],
            y=df_compare['installs'],
            mode='lines+markers',
            name='installs_s2',
            hovertemplate='installs_s2: %{y}<br>Date: %{x}<extra></extra>'
        ))

        # Main
        fig.add_trace(go.Scatter(
            x=df_compare['install_date'],
            y=df_compare['installs_main'],
            mode='lines+markers',
            name='installs_main',
            hovertemplate='installs_main: %{y}<br>Date: %{x}<extra></extra>'
        ))

        # Gap (разница)
        fig.add_trace(go.Scatter(
            x=df_compare['install_date'],
            y=df_compare['gap'],
            mode='lines+markers',
            name='Gap (installs_s2 - installs_main)',
            hovertemplate='Gap: %{y}<br>Date: %{x}<extra></extra>'
        ))

        # Настройки графика
        fig.update_layout(
            title='Installs over time with comparison',
            xaxis_title='Install Date',
            yaxis_title='Installs',
            xaxis=dict(tickangle=-30),
            width=2000,
            height=500,
            hovermode='x unified'  # показывает все значения в одной полоске при наведении
        )

        return fig.show()


    def get_resurce_all(self,df_sor_2_cont_1,df_sor_2_cont_2,df_compare):
        fig = go.Figure()

        # contributor_1
        fig.add_trace(go.Scatter(
            x=df_sor_2_cont_1['contributor_1_date'],
            y=df_sor_2_cont_1['contributor_1'],
            mode='lines+markers',
            name='contributor_1',
            hovertemplate='contributor_1: %{y}<br>Date: %{x}<extra></extra>'
        ))

        # contributor_2
        fig.add_trace(go.Scatter(
            x=df_sor_2_cont_2['contributor_2_date'],
            y=df_sor_2_cont_2['contributor_2'],
            mode='lines+markers',
            name='contributor_2',
            hovertemplate='contributor_2: %{y}<br>Date: %{x}<extra></extra>'
        ))

        # Source 2 (общие установки)
        fig.add_trace(go.Scatter(
            x=df_compare['install_date'],
            y=df_compare['installs'],
            mode='lines+markers',
            name='installs_s2',
            hovertemplate='installs_s2: %{y}<br>Date: %{x}<extra></extra>'
        ))

        # installs_main
        fig.add_trace(go.Scatter(
            x=df_compare['install_date'],
            y=df_compare['installs_main'],
            mode='lines+markers',
            name='installs_main',
            hovertemplate='installs_main: %{y}<br>Date: %{x}<extra></extra>'
        ))


        # installs_main + contr 1
        fig.add_trace(go.Scatter(
            x=df_compare['install_date'],
            y=df_compare['installs_main_pl_comt_1'],
            mode='lines+markers',
            name='installs_main + contr 1',
            hovertemplate='installs_main + contr 1: %{y}<br>Date: %{x}<extra></extra>'
        ))

        # Gap
        fig.add_trace(go.Scatter(
            x=df_compare['install_date'],
            y=df_compare['gap'],
            mode='lines+markers',
            name='Gap (Source 2 - installs_main)',
            hovertemplate='Gap: %{y}<br>Date: %{x}<extra></extra>'
        ))

        # Настройки графика
        fig.update_layout(
            title='Installs over time: Contributors vs Source 2 & Installs_main',
            xaxis_title='Install Date',
            yaxis_title='Installs',
            xaxis=dict(tickangle=-30),
            width=2000,
            height=600,
            hovermode='x unified'  # показывает все значения при наведении на одну дату
        )

        return fig.show()



    def get_heat_map(self,df_compare):
        fig = px.imshow(df_compare.corr(), text_auto=True)
        return fig.show()


