import flet as ft

def login_page(page:ft.Page):
    return ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Column(
            horizontal_alignment='center',
            alignment='center',
            controls=[
                ft.Container(
                    ft.Text(
                        'Fazer login',
                        color='white',
                        size=38,
                        weight='bold',
                        font_family='MontSerrat'
                    )
                ),
                ft.Container(
                    width=250,
                    height=40,
                    padding=10,
                    bgcolor='#272b30',
                    alignment=ft.alignment.center_left,
                    border_radius=8,
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=ft.Icon(
                                    name=ft.icons.EMAIL,
                                    color='white',
                                )
                            ),
                            ft.VerticalDivider(
                                width=1,
                                color='#b9babb'
                            )
                        ]
                    )
                )
            ]
        )
    )