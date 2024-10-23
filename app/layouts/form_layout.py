import flet as ft
from pages.form_page import FormPage

class FormLayout(ft.Container):
    def __init__(
        self,
        forms : list[FormPage],
        end_event,
        init : int = 0,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.forms = forms
        self.current_form = init
        self.end_event = end_event

        self.animForm = ft.AnimatedSwitcher(
            content=self.forms[self.current_form],
            transition=ft.AnimatedSwitcherTransition.FADE,
            duration=550,
            switch_in_curve=ft.AnimationCurve.EASE_OUT_QUAD,
            switch_out_curve=ft.AnimationCurve.EASE_IN_QUAD,
            reverse_duration=500
        )

        if len(self.forms) > 1:
            self.forms[self.current_form].set_button_on_click(self.next_form)
        else:
            self.forms[self.current_form].set_button_on_click(self.end_event)

        self.expand = True
        self.alignment = ft.alignment.top_left
        self.content = self.animForm

    def get_current_form(self):
        return self.animForm.content

    def set_form(self, form):
        form.set_button_on_click(self.next_form)
        self.animForm.content = form
        self.animForm.update()

    def next_form(self, _):
        self.current_form = self.current_form + 1
        if self.current_form == len(self.forms):
            self.end_event()
            return
        self.set_form(self.forms[self.current_form])