import flet as ft

class FormLayout(ft.Container):
    def __init__(
        self,
        init_form,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.animForm = ft.AnimatedSwitcher(
            content=init_form,
            transition=ft.AnimatedSwitcherTransition.FADE,
            duration=250,
            switch_in_curve=ft.AnimationCurve.EASE_IN_OUT,
            switch_out_curve=ft.AnimationCurve.EASE_OUT
        )

        self.expand = True
        self.alignment = ft.alignment.top_left
        self.content = self.animForm

    def get_current_form(self):
        return self.animForm.content

    def set_form(self, form):
        self.animForm.content = form
        self.animForm.update()