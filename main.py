import flet as ft

def main(page:ft.Page):
    page.window.width = 500
    page.window.height = 750
    page.bgcolor = '#1e2428'
    page.title = 'MovieApp'
    page.padding = 0
    page.horizontal_alignment = 'center'

    def comecar_btn(e):
        from login import login_page
        page.clean()
        page.add(login_page(page))

    # Imagem main
    _main_img = ft.Container(
        alignment=ft.alignment.center,
        height=450,
        width=450,
        bgcolor='#272b30',
        border_radius=ft.border_radius.only(top_left=8,top_right=8),
        content=ft.Image(
            src='https://i.postimg.cc/GmbPxghG/Onboarding-1-4x.png',
            fit=ft.ImageFit.COVER,
            width=450,
        )

    )

    # Conteúdo principal
    _main_cont = ft.Container(
        bgcolor='#272b30',
        border_radius=8,
        width=500,
        height=350,
        padding=25,
        margin=ft.margin.only(top=-60),
        shadow=ft.BoxShadow(blur_radius=5,color='black'),
        content=ft.Column(
            spacing=20,
            horizontal_alignment='center',
            controls=[
                ft.Container(
                    content=ft.Text(
                        'Nunca perca \nséries e filmes!',
                        color='white',
                        size=38,
                        font_family='MontSerrat',
                        weight='w600',
                        text_align='center',
                    )
                ),
                ft.Container(
                    content=ft.Text(
                        'Assista filmes de onde quiser na palma da sua mão',
                        color='#8a8a8c',
                        size=18,
                        font_family='MontSerrat',
                        weight='w300',
                        text_align='center',
                    )
                ),
                ft.Container(
                    content=ft.ElevatedButton(
                        'Começar',
                        bgcolor='#ef233c',
                        color='white',
                        width='250',
                        height='50',
                        on_click=comecar_btn,
                    )
                )
            ]
        )
    )

    page.add(
        ft.Column(
            horizontal_alignment= 'center',
            controls=[
                _main_img,
                _main_cont,
            ]
        )
    )


ft.app(target=main)