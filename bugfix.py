from nicegui import ui

ui.label('Hello NiceGUI!')
ui.button('BUTTON', on_click=lambda: ui.notify('button was pressed'))

# When chip is clicked, the options panel is displayed normally
select1 = ui.select(list("ab"), value="a")
with select1.add_slot("selected"):
    with ui.element("q-chip"):
        ui.label("a")


#  need to click on the chip twice for the options panel to appear
select2 = ui.select(list("ab"))

select2.add_slot(
    "selected",
    r"""
<q-chip>
  <div>{{ 'a' }}</div>
  </q-chip>
""",
)


ui.run()